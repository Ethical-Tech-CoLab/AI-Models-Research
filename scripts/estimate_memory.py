#!/usr/bin/env python3
"""Estimate accelerator memory for serving a model of known size.

The estimate is arithmetic over disclosed quantities. It is not a measurement,
and it is not a substitute for one: real memory use depends on the serving
framework, on attention kernel choice, on fragmentation, and on activation
memory that varies with batch composition. The purpose of this script is to
establish whether a configuration is plausible before hardware is committed,
and to make the assumptions behind any published figure explicit.

Formulas implemented, as defined in ``docs/appendices/formulas.md``:

    Weight memory
        M_w = N_params * bytes_per_param

    KV cache memory, per sequence
        M_kv = 2 * L * H_kv * d_head * S * bytes_per_element

      where L is layers, H_kv is key and value heads after any grouping,
      d_head is head dimension, and S is sequence length. The factor of 2
      counts keys and values.

    Total
        M = M_w + B * M_kv + M_overhead

      where B is concurrent sequences and overhead covers activations,
      framework allocations, and fragmentation, applied as a fraction.

Precision to bytes per element: fp32 4, bf16 and fp16 2, fp8 1, int8 1,
int4 0.5. Quantization applied to weights does not necessarily apply to the
KV cache, so the two precisions are set independently.

Usage:
    python scripts/estimate_memory.py --params 70 --layers 80 \\
        --kv-heads 8 --head-dim 128 --seq-len 32768 --batch 8 \\
        --weight-precision bf16 --kv-precision fp16

Exit status:
    0  computation completed
    2  invalid arguments
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from _common import fail

BYTES_PER_ELEMENT: dict[str, float] = {
    "fp32": 4.0,
    "tf32": 4.0,
    "bf16": 2.0,
    "fp16": 2.0,
    "fp8": 1.0,
    "int8": 1.0,
    "int4": 0.5,
}

GIB = 1024**3
BILLION = 1_000_000_000


@dataclass(frozen=True)
class MemoryEstimate:
    """Result of a memory estimate, in gibibytes.

    Attributes:
        weights_gib: Memory held by model weights.
        kv_per_sequence_gib: KV cache for one sequence at the stated length.
        kv_total_gib: KV cache for all concurrent sequences.
        overhead_gib: Activation and framework overhead.
        total_gib: Sum of the above.
        accelerators_required: Number of accelerators of the stated memory
            size needed to hold the total, or None when no size was given.
    """

    weights_gib: float
    kv_per_sequence_gib: float
    kv_total_gib: float
    overhead_gib: float
    total_gib: float
    accelerators_required: int | None


def bytes_per_element(precision: str) -> float:
    """Return bytes per element for a named numerical precision.

    Args:
        precision: Precision name, for example ``bf16``.

    Returns:
        Bytes per element.

    Raises:
        ValueError: If the precision is not recognised.
    """
    key = precision.lower()
    if key not in BYTES_PER_ELEMENT:
        raise ValueError(
            f"unknown precision {precision!r}; expected one of "
            f"{', '.join(sorted(BYTES_PER_ELEMENT))}"
        )
    return BYTES_PER_ELEMENT[key]


def weight_memory_gib(params_billions: float, precision: str) -> float:
    """Compute weight memory in gibibytes.

    Args:
        params_billions: Parameter count in billions. For a mixture-of-experts
            model use the total, not the active count: all experts must be
            resident even though only some are used per token.
        precision: Weight precision.

    Returns:
        Weight memory in gibibytes.

    Raises:
        ValueError: If the parameter count is not positive.
    """
    if params_billions <= 0:
        raise ValueError(f"parameter count must be positive, got {params_billions}")
    return params_billions * BILLION * bytes_per_element(precision) / GIB


def kv_cache_gib(
    layers: int, kv_heads: int, head_dim: int, seq_len: int, precision: str
) -> float:
    """Compute KV cache memory for a single sequence, in gibibytes.

    Args:
        layers: Number of transformer layers.
        kv_heads: Key and value heads per layer after grouping. For multi-head
            attention this equals the query head count; for grouped-query
            attention it is smaller; for multi-query attention it is 1.
        head_dim: Dimension of each head.
        seq_len: Sequence length in tokens.
        precision: KV cache precision.

    Returns:
        KV cache memory for one sequence, in gibibytes.

    Raises:
        ValueError: If any dimension is not positive.
    """
    for name, value in (
        ("layers", layers),
        ("kv_heads", kv_heads),
        ("head_dim", head_dim),
        ("seq_len", seq_len),
    ):
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")
    element = bytes_per_element(precision)
    return 2 * layers * kv_heads * head_dim * seq_len * element / GIB


def estimate(
    params_billions: float,
    layers: int,
    kv_heads: int,
    head_dim: int,
    seq_len: int,
    batch: int,
    weight_precision: str,
    kv_precision: str,
    overhead_fraction: float,
    accelerator_gib: float | None,
) -> MemoryEstimate:
    """Produce a full memory estimate.

    Args:
        params_billions: Total parameters in billions.
        layers: Transformer layers.
        kv_heads: Key and value heads per layer.
        head_dim: Head dimension.
        seq_len: Sequence length in tokens.
        batch: Concurrent sequences.
        weight_precision: Precision of resident weights.
        kv_precision: Precision of the KV cache.
        overhead_fraction: Activation and framework overhead as a fraction of
            weights plus KV cache.
        accelerator_gib: Memory per accelerator, used to report how many are
            required. None to skip that calculation.

    Returns:
        The estimate.

    Raises:
        ValueError: If batch or overhead are out of range, or if an inner
            computation rejects its arguments.
    """
    if batch <= 0:
        raise ValueError(f"batch must be positive, got {batch}")
    if overhead_fraction < 0:
        raise ValueError(f"overhead fraction must not be negative, got {overhead_fraction}")
    if accelerator_gib is not None and accelerator_gib <= 0:
        raise ValueError(f"accelerator memory must be positive, got {accelerator_gib}")

    weights = weight_memory_gib(params_billions, weight_precision)
    kv_one = kv_cache_gib(layers, kv_heads, head_dim, seq_len, kv_precision)
    kv_all = kv_one * batch
    overhead = (weights + kv_all) * overhead_fraction
    total = weights + kv_all + overhead
    required = None
    if accelerator_gib is not None:
        required = int(-(-total // accelerator_gib))
    return MemoryEstimate(weights, kv_one, kv_all, overhead, total, required)


def render(result: MemoryEstimate, args: argparse.Namespace) -> str:
    """Format an estimate for the terminal.

    Args:
        result: The computed estimate.
        args: The parsed arguments that produced it.

    Returns:
        A multi-line report.
    """
    lines = [
        "Memory estimate",
        "===============",
        "",
        "Configuration",
        f"  total parameters, B     {args.params:>12,.2f}",
        f"  layers                  {args.layers:>12,}",
        f"  key and value heads     {args.kv_heads:>12,}",
        f"  head dimension          {args.head_dim:>12,}",
        f"  sequence length         {args.seq_len:>12,}",
        f"  concurrent sequences    {args.batch:>12,}",
        f"  weight precision        {args.weight_precision:>12}",
        f"  KV cache precision      {args.kv_precision:>12}",
        f"  overhead fraction       {args.overhead:>12.3f}",
        "",
        "Results, GiB",
        f"  weights                 {result.weights_gib:>12.2f}",
        f"  KV cache per sequence   {result.kv_per_sequence_gib:>12.2f}",
        f"  KV cache total          {result.kv_total_gib:>12.2f}",
        f"  overhead                {result.overhead_gib:>12.2f}",
        f"  total                   {result.total_gib:>12.2f}",
    ]
    if result.accelerators_required is not None:
        lines.append(
            f"  accelerators at {args.accelerator_gib:g} GiB  {result.accelerators_required:>6,}"
        )
    lines += [
        "",
        "This is an estimate over disclosed quantities, not a measurement. Real memory use",
        "depends on the serving framework, the attention kernel, and fragmentation. Do not",
        "publish this figure as a measured hardware requirement.",
    ]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="estimate_memory.py",
        description="Estimate weight and KV cache memory for serving a model.",
    )
    parser.add_argument("--params", type=float, required=True, help="total parameters in billions")
    parser.add_argument("--layers", type=int, required=True, help="transformer layers")
    parser.add_argument(
        "--kv-heads", type=int, required=True, help="key and value heads per layer after grouping"
    )
    parser.add_argument("--head-dim", type=int, required=True, help="head dimension")
    parser.add_argument("--seq-len", type=int, required=True, help="sequence length in tokens")
    parser.add_argument("--batch", type=int, default=1, help="concurrent sequences")
    parser.add_argument(
        "--weight-precision", default="bf16", choices=sorted(BYTES_PER_ELEMENT), help="weights"
    )
    parser.add_argument(
        "--kv-precision", default="fp16", choices=sorted(BYTES_PER_ELEMENT), help="KV cache"
    )
    parser.add_argument(
        "--overhead",
        type=float,
        default=0.15,
        help="activation and framework overhead as a fraction of weights plus KV cache",
    )
    parser.add_argument(
        "--accelerator-gib", type=float, help="memory per accelerator, to report how many are needed"
    )
    return parser


def main() -> int:
    """Parse arguments, compute the estimate, and print it.

    Returns:
        0 on success.
    """
    args = build_parser().parse_args()
    try:
        result = estimate(
            params_billions=args.params,
            layers=args.layers,
            kv_heads=args.kv_heads,
            head_dim=args.head_dim,
            seq_len=args.seq_len,
            batch=args.batch,
            weight_precision=args.weight_precision,
            kv_precision=args.kv_precision,
            overhead_fraction=args.overhead,
            accelerator_gib=args.accelerator_gib,
        )
    except ValueError as exc:
        fail(str(exc))
    print(render(result, args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
