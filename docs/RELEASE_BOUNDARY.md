# Release Boundary

## Purpose

This public repository contains data-free engineering support and a concise qualitative account of two completed, separate observational analyses. The status record states their bounded supportive and non-supportive outcomes without exposing research artifacts, numerical outputs, or source-specific operational details.

## Permitted material

Permitted material includes a high-level project description, qualitative outcome statements with explicit limitations, conceptual methods scope, contribution guidance, ignore rules, a read-only boundary scanner, and synthetic tests. Outcome statements must avoid numerical values, source identifiers, access records, and causal, mechanistic, or cross-system interpretation.

## Excluded material

The tree must not contain raw, intermediate, or derived research artifacts; figures or figure specifications; downloaded files; archives; notebooks; third-party source material; external metadata; access or activity logs; internal indexes; data-dependent tests; or tests that write to repository data, result, figure, download, archive, or output locations.

## Boundary check

`tools/release_boundary_scan.py` obtains the tracked-file list from Git, checks only those paths, and reads only tracked text files. It does not enumerate untracked files, open local data, access the network, or create artifacts. The check is a safeguard rather than a substitute for owner review.

Run it from a Git working tree:

```bash
python3 tools/release_boundary_scan.py
```

A nonzero exit status identifies paths or text requiring review. Review changes manually as well, especially documentation changes that could introduce numerical results, source-specific records, or claims beyond the documented observational inference.
