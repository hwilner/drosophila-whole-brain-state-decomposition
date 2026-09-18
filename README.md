# Drosophila Whole-Brain State Decomposition

This repository is a **public-safe staging scaffold** for independent research on conceptual and computational approaches to decomposing brain-wide activity into interpretable state descriptions in *Drosophila*. It contains documentation, a release-boundary check, and data-free tests only; it does not include research data, source material, derived outputs, figures, or empirical findings.

## Current status

The project is in a documentation-and-boundary-setting stage. **This current tree supersedes earlier working materials that may have contained unsupported empirical, or source-specific language.** No such statements are represented here and none should be inferred from the repository.

## Contents

| Path | Contents |
|---|---|
| [`docs/STATUS_AND_PLAN.md`](docs/STATUS_AND_PLAN.md) | Current status and conservative next steps. |
| [`docs/METHODS_SCOPE.md`](docs/METHODS_SCOPE.md) | Conceptual methods scope and non-claims. |
| [`docs/DEFERRED_AND_DROPPED_DIRECTIONS.md`](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md) | Work deliberately outside this public tree. |
| [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md) | Public-release inclusion rules and scanner use. |
| [`tools/release_boundary_scan.py`](tools/release_boundary_scan.py) | Read-only scanner for tracked paths and text. |
| [`tests/`](tests) | Synthetic, data-free checks for the scanner. |

## Keywords

*Drosophila*; whole-brain activity; state decomposition; computational neuroscience; reproducibility; research software; release boundaries.

## Contributing

Contributions that improve documentation clarity, boundary checks, synthetic test coverage, or maintainable data-free tooling are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [release boundary](docs/RELEASE_BOUNDARY.md) before proposing a change.

## Local checks

Run the data-free checks from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 tools/release_boundary_scan.py
```

The scanner reads only Git-tracked paths and text and does not access local data or generate outputs.
