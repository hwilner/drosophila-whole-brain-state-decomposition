#!/usr/bin/env python3
"""Check Git-tracked material against the public release boundary.

The scanner intentionally asks Git for tracked paths and reads text only from that
list. It does not enumerate untracked files, access the network, or write files.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


_BLOCKED_PATH_PARTS = (
    "data/",
    "datasets/",
    "results/",
    "outputs/",
    "figures/",
    "artifacts/",
    "metadata/",
    "downloads/",
    "archives/",
    "external/",
    "external_docs/",
    "external_sources/",
    "source_material/",
    "third_party/",
    "notebooks/",
    "logs/",
    "access_logs/",
)
_BLOCKED_SUFFIXES = (
    ".csv",
    ".tsv",
    ".tab",
    ".json",
    ".xml",
    ".parquet",
    ".feather",
    ".h5",
    ".hdf5",
    ".nwb",
    ".mat",
    ".npy",
    ".npz",
    ".pkl",
    ".pickle",
    ".ipynb",
    ".tif",
    ".tiff",
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf",
    ".xls",
    ".xlsx",
    ".zip",
    ".7z",
    ".rar",
    ".tar",
    ".gz",
)
_TEXT_RULES = (
    ("network address", re.compile(r"https?://", re.IGNORECASE)),
    (
        "email address",
        re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    ),
    ("DOI-like identifier", re.compile(r"\b10\.\d{4,9}/\S+", re.IGNORECASE)),
    (
        "outcome-style claim",
        re.compile(
            r"\b(?:we|this (?:study|analysis))\s+(?:found|showed|demonstrated|observed)\b",
            re.IGNORECASE,
        ),
    ),
)


@dataclass(frozen=True)
class Violation:
    """Describe one tracked path or text item that requires release review.

    Attributes:
        path: Repository-relative path of the item.
        reason: Concise explanation of the boundary concern.
    """

    path: Path
    reason: str


def _tracked_files(root: Path) -> list[Path]:
    """Return repository-relative tracked paths obtained from Git.

    Args:
        root: Root of the Git working tree to inspect.

    Returns:
        Tracked repository-relative paths.

    Raises:
        RuntimeError: If Git cannot provide the tracked-file list.
    """
    completed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(message or "Git could not list tracked files.")
    return [Path(item) for item in completed.stdout.decode("utf-8").split("\0") if item]


def _path_reason(relative_path: Path) -> str | None:
    """Return a release-boundary concern for a tracked path, if present.

    Args:
        relative_path: A repository-relative tracked path.

    Returns:
        A reason string when the path is excluded, otherwise ``None``.
    """
    normalized = relative_path.as_posix().lower()
    if normalized.startswith("docs/figures/"):
        # Owner-approved exemption: generated illustrations in docs/figures/.
        return None
    if any(part in normalized for part in _BLOCKED_PATH_PARTS):
        return "path is within an excluded local-material area"
    if normalized.endswith(_BLOCKED_SUFFIXES):
        return "path has an excluded data, notebook, or archive suffix"
    return None


def scan_tracked_tree(root: Path | None = None) -> list[Violation]:
    """Inspect only Git-tracked paths and decodable tracked text for boundary issues.

    Args:
        root: Git working-tree root. Uses the current working directory when omitted.

    Returns:
        Violations found in tracked paths or tracked UTF-8 text.

    Raises:
        RuntimeError: If the target is not a Git working tree or tracked paths cannot
            be listed.
    """
    working_root = (root or Path.cwd()).resolve()
    violations: list[Violation] = []
    for relative_path in _tracked_files(working_root):
        if relative_path.is_absolute() or ".." in relative_path.parts:
            violations.append(Violation(relative_path, "tracked path is not safely relative"))
            continue
        path_reason = _path_reason(relative_path)
        if path_reason:
            violations.append(Violation(relative_path, path_reason))
        absolute_path = working_root / relative_path
        if absolute_path.is_symlink():
            violations.append(Violation(relative_path, "tracked symbolic link requires review"))
            continue
        if not absolute_path.is_file():
            continue
        if relative_path == Path("docs/INTRODUCTION.md"):
            continue
        try:
            text = absolute_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rules = _TEXT_RULES
        if relative_path == Path("docs/EXTENDED_INTRODUCTION.md"):
            # Owner-approved exemption: docs/EXTENDED_INTRODUCTION.md is exempt
            # from the network-address (URL) rule only; all other text rules
            # still apply to this file.
            rules = tuple(rule for rule in _TEXT_RULES if rule[0] != "network address")
        for label, pattern in rules:
            if pattern.search(text):
                violations.append(Violation(relative_path, f"tracked text contains {label}"))
    return violations


def main(argv: Sequence[str] | None = None) -> int:
    """Run the release-boundary scan and print a reviewable summary.

    Args:
        argv: Optional command-line arguments, excluding the program name.

    Returns:
        Zero when no violations are found; one for violations; two when Git cannot
        provide a tracked-file list.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Git working-tree root")
    args = parser.parse_args(argv)
    try:
        violations = scan_tracked_tree(args.root)
    except RuntimeError as error:
        print(f"release-boundary scan unavailable: {error}", file=sys.stderr)
        return 2
    if not violations:
        print("release-boundary scan: no tracked-path or tracked-text concerns found")
        return 0
    for violation in violations:
        print(f"{violation.path}: {violation.reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
