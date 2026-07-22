# Pending workflows

These three GitHub Actions workflows are finished and verified locally. They are
parked here rather than in `.github/workflows/` because the token used for the
initial push carries only the `gist`, `read:org`, and `repo` scopes. GitHub
refuses any push from an OAuth application that creates or updates a file under
`.github/workflows/` without the `workflow` scope, so committing them to their
real location would have blocked the entire push.

They are kept in the repository rather than left untracked so that the
continuous integration setup is visible and reviewable, rather than existing
only on one machine.

## Activating them

```bash
gh auth refresh -h github.com -s workflow
git mv .github/workflows-pending/build-docs.yml   .github/workflows/build-docs.yml
git mv .github/workflows-pending/links.yml        .github/workflows/links.yml
git mv .github/workflows-pending/markdown-lint.yml .github/workflows/markdown-lint.yml
git rm .github/workflows-pending/README.md
git commit -m "ci: activate the documentation, validation, and link workflows"
git push
```

The first command opens a browser once to add the missing scope. Nothing else
about the workflows needs to change.

## What each one does

| File | Trigger | Purpose |
|---|---|---|
| `markdown-lint.yml` | push to `main`, pull request | Runs the three validators, confirms every generated table is in sync with its dataset, then lints Markdown and Python. This is the workflow that enforces the evidence rules. |
| `build-docs.yml` | push to `main`, pull request | Runs `mkdocs build --strict`, so a file present in the navigation but missing from disk, or present on disk but missing from the navigation, blocks the merge. |
| `links.yml` | weekly schedule, and pull requests touching `data/sources.csv` or `references.bib` | The only workflow that makes network calls. Checks that external source URLs still resolve and opens an issue when one has rotted, because a dead source URL means a claim can no longer be verified. |

All three were verified locally before being parked: every command they run
passes on the current tree.
