"""Synthetic, data-free tests for the tracked-tree release-boundary scanner."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.release_boundary_scan import scan_tracked_tree


class ReleaseBoundaryScanTests(unittest.TestCase):
    """Exercise scanner behavior using temporary documentation-only fixtures."""

    def test_accepts_safe_tracked_text(self) -> None:
        """A tracked documentation file without boundary indicators is accepted."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "README.md").write_text("Independent research scaffold.\n", encoding="utf-8")
            with patch(
                "tools.release_boundary_scan._tracked_files",
                return_value=[Path("README.md")],
            ):
                self.assertEqual(scan_tracked_tree(root), [])

    def test_reports_excluded_path_and_external_address(self) -> None:
        """Excluded paths and externally addressed tracked text are reported."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "NOTES.md").write_text(
                "Address: " + "http" + "s://example.invalid\n",
                encoding="utf-8",
            )
            with patch(
                "tools.release_boundary_scan._tracked_files",
                return_value=[Path("data/raw/example.npy"), Path("NOTES.md")],
            ):
                violations = scan_tracked_tree(root)
            reasons = [violation.reason for violation in violations]
            self.assertIn("path is within an excluded local-material area", reasons)
            self.assertIn("tracked text contains network address", reasons)

    def test_reports_source_identifier_and_outcome_style_language(self) -> None:
        """Synthetic prohibited text patterns are reported for owner review."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "NOTES.md").write_text(
                "Identifier " + "10" + ".1234/example and this " + "analysis " + "showed a pattern.\n",
                encoding="utf-8",
            )
            with patch(
                "tools.release_boundary_scan._tracked_files",
                return_value=[Path("NOTES.md")],
            ):
                violations = scan_tracked_tree(root)
            reasons = [violation.reason for violation in violations]
            self.assertIn("tracked text contains DOI-like identifier", reasons)
            self.assertIn("tracked text contains outcome-style claim", reasons)

    def test_raises_when_tracked_list_is_unavailable(self) -> None:
        """A Git listing failure is surfaced rather than scanning untracked files."""
        completed = subprocess.CompletedProcess(["git"], 1, stderr=b"not a repository")
        with patch("tools.release_boundary_scan.subprocess.run", return_value=completed):
            with self.assertRaisesRegex(RuntimeError, "not a repository"):
                scan_tracked_tree(Path("."))


if __name__ == "__main__":
    unittest.main()
