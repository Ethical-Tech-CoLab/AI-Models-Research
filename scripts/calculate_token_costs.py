#!/usr/bin/env python3
r"""Compute token costs from published prices and measured token volumes.

Advertised price per million tokens is not cost. The quantity a reader needs is
cost per accepted task, which depends on how many tokens a task consumes, how
many of those are cached, how many are reasoning tokens, and how often the
output is accepted. This script implements the five formulas defined in
``docs/appendices/formulas.md`` and used in ``docs/15-token-economics.md``.

Formulas implemented:

    Effective tokens per task
        T_eff = T_in_fresh + T_in_cached + T_out + T_reason + T_tool

    Total API cost
        C = (T_in_fresh * P_in + T_in_cached * P_cached
             + (T_out + T_reason) * P_out) / 1e6

    Cost per accepted task
        C_task = C / a,  0 < a <= 1, where a is the acceptance rate

    Cache savings
        S = T_in_cached * (P_in - P_cached) / 1e6

    Reasoning overhead
        R = T_reason / T_out, reported as a ratio and as a share of cost

Prices are USD per one million tokens. All token counts are per task.

Usage:
    python scripts/calculate_token_costs.py \\
        --input-tokens 12000 --cached-tokens 8000 --output-tokens 900 \\
        --reasoning-tokens 3400 --price-input 3.00 --price-cached 0.30 \\
        --price-output 15.00 --acceptance-rate 0.72

    python scripts/calculate_token_costs.py --model gpt-example --from-data \\
        --input-tokens 12000 --output-tokens 900

Exit status:
    0  computation completed
    2  invalid arguments, or the model has no pricing row
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from _common import DATASETS, DataError, fail, read_csv

MILLION = 1_000_000


@dataclass(frozen=True)
class Prices:
    """Prices in USD per one million tokens.

    Attributes:
        input_fresh: Price of an uncached input token.
        input_cached: Price of a cached input token.
        output: Price of an output token, including billed reasoning tokens.
        batch_discount: Fractional discount applied to a batch request, in
            the range 0 to 1.
    """

    input_fresh: float
    input_cached: float
    output: float
    batch_discount: float = 0.0


@dataclass(frozen=True)
class Usage:
    """Token volumes for a single task.

    Attributes:
        input_fresh: Uncached input tokens.
        input_cached: Cached input tokens.
        output: Visible output tokens.
        reasoning: Reasoning tokens, whether or not they are visible.
        tool: Tokens consumed by tool definitions and tool results.
        acceptance_rate: Fraction of attempts whose output is accepted,
            greater than 0 and at most 1.
    """

    input_fresh: int
    input_cached: int
    output: int
    reasoning: int = 0
    tool: int = 0
    acceptance_rate: float = 1.0


@dataclass(frozen=True)
class CostBreakdown:
    """Result of a cost computation.

    Attributes:
        effective_tokens: Total tokens attributable to one attempt.
        input_cost: USD spent on input tokens, fresh and cached.
        output_cost: USD spent on output and reasoning tokens.
        total_cost: USD for one attempt.
        cost_per_accepted_task: USD per accepted output.
        cache_savings: USD saved by caching, relative to paying the fresh
            input price for every input token.
        reasoning_overhead_ratio: Reasoning tokens divided by output tokens.
        reasoning_cost_share: Fraction of total cost attributable to
            reasoning tokens.
    """

    effective_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float
    cost_per_accepted_task: float
    cache_savings: float
    reasoning_overhead_ratio: float
    reasoning_cost_share: float


def effective_tokens(usage: Usage) -> int:
    """Compute effective tokens per task.

    Args:
        usage: Token volumes for one task.

    Returns:
        The sum of every token class attributable to one attempt.
    """
    return usage.input_fresh + usage.input_cached + usage.output + usage.reasoning + usage.tool


def compute(usage: Usage, prices: Prices, batch: bool = False) -> CostBreakdown:
    """Compute the full cost breakdown for one task.

    Tool tokens are billed at the input price, because tool definitions and
    tool results enter the context as input.

    Args:
        usage: Token volumes for one task.
        prices: Prices in USD per million tokens.
        batch: Apply the batch discount to every component.

    Returns:
        The computed breakdown.

    Raises:
        ValueError: If any token count is negative, if the acceptance rate is
            outside the interval (0, 1], or if any price is negative.
    """
    for name, value in (
        ("input_fresh", usage.input_fresh),
        ("input_cached", usage.input_cached),
        ("output", usage.output),
        ("reasoning", usage.reasoning),
        ("tool", usage.tool),
    ):
        if value < 0:
            raise ValueError(f"token count {name!r} is negative: {value}")
    if not 0.0 < usage.acceptance_rate <= 1.0:
        raise ValueError(
            f"acceptance_rate must be greater than 0 and at most 1, got {usage.acceptance_rate}"
        )
    for name, price in (
        ("price_input", prices.input_fresh),
        ("price_cached", prices.input_cached),
        ("price_output", prices.output),
    ):
        if price < 0:
            raise ValueError(f"{name} is negative: {price}")
    if prices.input_cached > prices.input_fresh:
        raise ValueError(
            "cached input price exceeds fresh input price; confirm the pricing row, because "
            "caching that costs more than recomputation is not a cache"
        )

    multiplier = (1.0 - prices.batch_discount) if batch else 1.0
    billable_input = usage.input_fresh + usage.tool

    input_cost = (
        (billable_input * prices.input_fresh + usage.input_cached * prices.input_cached)
        * multiplier
        / MILLION
    )
    output_cost = (usage.output + usage.reasoning) * prices.output * multiplier / MILLION
    total = input_cost + output_cost

    savings = usage.input_cached * (prices.input_fresh - prices.input_cached) / MILLION
    reasoning_cost = usage.reasoning * prices.output * multiplier / MILLION

    return CostBreakdown(
        effective_tokens=effective_tokens(usage),
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=total,
        cost_per_accepted_task=total / usage.acceptance_rate,
        cache_savings=savings,
        reasoning_overhead_ratio=(usage.reasoning / usage.output) if usage.output else 0.0,
        reasoning_cost_share=(reasoning_cost / total) if total else 0.0,
    )


def prices_from_data(model_id: str) -> Prices:
    """Load prices for a model from ``data/pricing.csv``.

    Args:
        model_id: Exact model identifier as recorded in the dataset.

    Returns:
        The prices from the most recent effective date for that model.

    Raises:
        DataError: If the model has no pricing row, or if a price cell is not
            numeric.
    """
    _, rows = read_csv(DATASETS["pricing"])
    matches = [row for row in rows if row.get("model_id", "").strip() == model_id]
    if not matches:
        raise DataError(
            f"data/pricing.csv: no pricing row for model_id {model_id!r}. Add the row with its "
            f"source_id and effective_date before computing a cost"
        )
    row = max(matches, key=lambda r: r.get("effective_date", ""))
    try:
        return Prices(
            input_fresh=float(row["input_price_per_1m"]),
            input_cached=float(row["cached_input_price_per_1m"]),
            output=float(row["output_price_per_1m"]),
            batch_discount=float(row.get("batch_discount_percent", "0") or 0) / 100.0,
        )
    except (KeyError, ValueError) as exc:
        raise DataError(
            f"data/pricing.csv: model {model_id!r} has a non-numeric or missing price cell: {exc}"
        ) from exc


def render(breakdown: CostBreakdown, usage: Usage, prices: Prices) -> str:
    """Format a breakdown for the terminal.

    Args:
        breakdown: Computed costs.
        usage: The usage that produced them.
        prices: The prices that produced them.

    Returns:
        A multi-line report.
    """
    lines = [
        "Token cost breakdown",
        "====================",
        "",
        "Inputs",
        f"  fresh input tokens      {usage.input_fresh:>12,}",
        f"  cached input tokens     {usage.input_cached:>12,}",
        f"  output tokens           {usage.output:>12,}",
        f"  reasoning tokens        {usage.reasoning:>12,}",
        f"  tool tokens             {usage.tool:>12,}",
        f"  acceptance rate         {usage.acceptance_rate:>12.3f}",
        "",
        "Prices, USD per 1M tokens",
        f"  input                   {prices.input_fresh:>12.4f}",
        f"  cached input            {prices.input_cached:>12.4f}",
        f"  output                  {prices.output:>12.4f}",
        "",
        "Results",
        f"  effective tokens/task   {breakdown.effective_tokens:>12,}",
        f"  input cost, USD         {breakdown.input_cost:>12.6f}",
        f"  output cost, USD        {breakdown.output_cost:>12.6f}",
        f"  total cost, USD         {breakdown.total_cost:>12.6f}",
        f"  cost per accepted, USD  {breakdown.cost_per_accepted_task:>12.6f}",
        f"  cache savings, USD      {breakdown.cache_savings:>12.6f}",
        f"  reasoning overhead      {breakdown.reasoning_overhead_ratio:>12.3f}",
        f"  reasoning cost share    {breakdown.reasoning_cost_share:>12.3f}",
        "",
        "Note: this is a computation over the inputs supplied, not a measurement.",
        "Cite the pricing row and the token measurement that produced these inputs.",
    ]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="calculate_token_costs.py",
        description="Compute total API cost, cost per accepted task, cache savings, "
        "and reasoning overhead.",
    )
    parser.add_argument("--input-tokens", type=int, required=True, help="fresh input tokens")
    parser.add_argument("--cached-tokens", type=int, default=0, help="cached input tokens")
    parser.add_argument("--output-tokens", type=int, required=True, help="visible output tokens")
    parser.add_argument("--reasoning-tokens", type=int, default=0, help="reasoning tokens")
    parser.add_argument(
        "--tool-tokens", type=int, default=0, help="tool definition and result tokens"
    )
    parser.add_argument(
        "--acceptance-rate",
        type=float,
        default=1.0,
        help="fraction of attempts accepted, in (0, 1]",
    )
    parser.add_argument("--model", help="model_id to read prices from data/pricing.csv")
    parser.add_argument(
        "--from-data", action="store_true", help="require prices from data/pricing.csv"
    )
    parser.add_argument("--price-input", type=float, help="USD per 1M fresh input tokens")
    parser.add_argument("--price-cached", type=float, help="USD per 1M cached input tokens")
    parser.add_argument("--price-output", type=float, help="USD per 1M output tokens")
    parser.add_argument("--batch", action="store_true", help="apply the batch discount")
    return parser


def main() -> int:
    """Parse arguments, compute the breakdown, and print it.

    Returns:
        0 on success.
    """
    args = build_parser().parse_args()

    if args.from_data or args.model:
        if not args.model:
            fail("--from-data requires --model")
        try:
            prices = prices_from_data(args.model)
        except DataError as exc:
            fail(str(exc))
    else:
        missing = [
            name
            for name, value in (
                ("--price-input", args.price_input),
                ("--price-cached", args.price_cached),
                ("--price-output", args.price_output),
            )
            if value is None
        ]
        if missing:
            fail(
                "supply all of --price-input, --price-cached, and --price-output, or use "
                f"--model with --from-data. Missing: {', '.join(missing)}"
            )
        prices = Prices(args.price_input, args.price_cached, args.price_output)

    usage = Usage(
        input_fresh=args.input_tokens,
        input_cached=args.cached_tokens,
        output=args.output_tokens,
        reasoning=args.reasoning_tokens,
        tool=args.tool_tokens,
        acceptance_rate=args.acceptance_rate,
    )
    try:
        breakdown = compute(usage, prices, batch=args.batch)
    except ValueError as exc:
        fail(str(exc))
    print(render(breakdown, usage, prices))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
