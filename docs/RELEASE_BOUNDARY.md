# Release Boundary

## Purpose

This staging tree is limited to general, public-safe research documentation and data-free engineering support. Its boundary is intentionally conservative so that inclusion in version control does not imply authorization to release research materials.

## Permitted material

Permitted material includes a high-level project description, conceptual methods scope, contribution guidance, ignore rules, a read-only boundary scanner, and synthetic tests. Such material must avoid empirical statements, numerical outcomes, source-specific descriptions, personal contact information, and publication-oriented language.

## Excluded material

The tree must not contain raw, intermediate, or derived research artifacts; figures or figure specifications; downloaded files; archives; notebooks; third-party source material; external metadata; access or activity logs; internal indexes; data-dependent tests; or tests that write to repository data, result, figure, download, archive, or output locations.

## Boundary check

`tools/release_boundary_scan.py` obtains the tracked-file list from Git, checks only those paths, and reads only tracked text files. It does not enumerate untracked files, open local data, access the network, or create artifacts. The check is a safeguard rather than a substitute for owner review.

Run it from a Git working tree:

```bash
python3 tools/release_boundary_scan.py
```

A nonzero exit status identifies paths or text requiring review. Review changes manually as well, especially documentation changes that could introduce claims not recognized by simple patterns.
