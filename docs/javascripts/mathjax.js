// MathJax configuration for MkDocs Material.
//
// Formulas in this repository are analytical, not decorative: each one is
// defined once in docs/appendices/formulas.md and referenced elsewhere.
// See docs/appendices/formulas.md for the canonical definitions.

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
