# Drosophila Whole-Brain State Decomposition

This independent research repository records two completed, separate observational analyses of neural–behavioural encoding in *Drosophila* and provides data-free safety and release tools.

## Research status

| Completed work | Outcome |
|---|---|
| Component–motion encoding analysis | Held-out component–motion encoding was positive in the eligible animals under the fixed observational protocol. |
| Annotation-related and combined predictors | Annotation evidence was heterogeneous, and combined predictors were not uniformly better than motion-related predictors. |
| Separate observational prediction analysis | Non-supportive overall: held-out improvement relative to its fixed baseline was directionally mixed. |
| Cross-route or cross-project synthesis | Not performed; the two analyses remain separate and are not pooled. |

**Current conclusion:** one source-specific route supports a limited observational component–motion association. The second route is non-supportive for its own predictive question. Together they do **not** establish causality, a common neural state, learning, a shared mechanism, or a cross-system conclusion.

## What is included

| Path | Contents |
|---|---|
| `tools/restricted_pickle_reader.py` | Generic fail-closed deserialization utility. |
| `tools/release_boundary_scan.py` | Tracked-text and tracked-path release-boundary scanner. |
| `tests/` | Synthetic tests for retained safety and release tooling. |
| `docs/` | Research status, methods scope, deferred directions, and contribution guidance. |

## Validation

Any nonzero scanner exit requires review. Exit status 1 reports tracked paths or text that need attention; status 2 means Git could not provide the tracked-file list, so rerun the check from a Git checkout. The scanner is a safeguard, not a replacement for manual owner review.

```bash
python -m unittest discover -s tests -v
python tools/release_boundary_scan.py
```

## Keywords

*Drosophila*, neural–behavioural encoding, observational analysis, held-out prediction, computational neuroscience, reproducible research safeguards.

## Contributing

Contributions are welcome for data-free software quality, synthetic tests, documentation, accessibility, and release controls. Please read [Contributing](CONTRIBUTING.md) and the [research status](docs/STATUS_AND_PLAN.md) before opening a change.

## Documentation

- [Introduction for new readers](docs/INTRODUCTION.md)
- [Current results and discussion](docs/CURRENT_RESULTS_AND_DISCUSSION.md)
- [Research status and plan](docs/STATUS_AND_PLAN.md)
- [Methods scope](docs/METHODS_SCOPE.md)
- [Release boundary](docs/RELEASE_BOUNDARY.md)
- [Deferred and dropped directions](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md)
