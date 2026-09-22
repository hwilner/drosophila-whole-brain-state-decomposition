# Contributing

Contributions are welcome when they keep this repository useful as an independent-research scaffold and respect its public-release boundary.

## Suitable contributions

Suitable changes improve conceptual documentation, release-boundary safeguards, code quality, or synthetic and data-free tests. Keep changes narrow, explain their purpose, and update the relevant public documentation when the release boundary changes.

## Material that must remain out of tree

Do not add recordings, tabular measurements, images, videos, notebooks, downloaded materials, third-party source files, metadata captured from external resources, access records, derived artifacts, figure specifications, or outcome-bearing documentation. Do not add an empirical claim, numerical finding, source-specific statement, citation, contact detail, or assertion beyond the documented repository scope.

## Code and tests

New public callables should use Google-style docstrings that state their summary, arguments, return value, and raised exceptions where applicable. Use concise comments only where they clarify a non-obvious decision. Tests must be synthetic and data-free, must not rely on external access, and must not write to repository data, result, figure, download, archive, or output paths.

## Future Testing Opportunities

The following **data-free software or documentation tests** can be worked on now. They must use only synthetic, non-research material and must remain within the public-release boundary:

- Propose a synthetic test case that checks the release-boundary guidance is understandable for a newly introduced prohibited path or phrase.
- Review the public documentation for plain-language consistency, especially the distinction between association, prediction, and causation, and propose a narrowly scoped wording improvement.
- Propose an accessibility review of heading structure, link text, or Markdown readability, without adding external source material or outcome-bearing content.
- Propose a synthetic edge-case test for the retained fail-closed deserialization utility or release-boundary scanner, with no research-like inputs or derived outputs.

The following **research-facing tests** require maintainer approval and an appropriate, separately governed data boundary. Do not add their data, outputs, implementation, or external material to this repository:

- Define in advance how a route-specific held-out evaluation would keep fitting, model selection, and final evaluation separate.
- Define a prospective comparison that asks whether annotation-related predictors add reliable held-out value beyond motion-related predictors within the component–motion route.
- Define a prospective evaluation of whether the separate prediction route shows a consistent held-out pattern relative to its fixed baseline under stated conditions.
- Define an approved experimental design that could distinguish an observational association from a causal question, with safeguards stated before outcomes are inspected.

## Before proposing a change

Run the checks listed in the README and review [`docs/RELEASE_BOUNDARY.md`](docs/RELEASE_BOUNDARY.md). If a proposed change needs material outside the documented boundary, leave that material out and identify the decision for the project owner instead of adding it.
