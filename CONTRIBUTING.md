# Contributing

Contributions are welcome when they keep this repository useful as an independent-research scaffold and respect its public-release boundary.

## Suitable contributions

Suitable changes improve conceptual documentation, release-boundary safeguards, code quality, or synthetic and data-free tests. Keep changes narrow, explain their purpose, and update the relevant public documentation when the release boundary changes.

## Material that must remain out of tree

Do not add recordings, tabular measurements, images, videos, notebooks, downloaded materials, third-party source files, metadata captured from external resources, access records, derived artifacts, figure specifications, or outcome-bearing documentation. Do not add an empirical claim, numerical finding, source-specific statement, citation, contact detail, or publication-oriented assertion.

## Code and tests

New public callables should use Google-style docstrings that state their summary, arguments, return value, and raised exceptions where applicable. Use concise comments only where they clarify a non-obvious decision. Tests must be synthetic and data-free, must not rely on external access, and must not write to repository data, result, figure, download, archive, or output paths.

## Before proposing a change

Run the checks listed in the README and review [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md). If a proposed change needs material outside the documented boundary, leave that material out and identify the decision for the project owner instead of adding it.
