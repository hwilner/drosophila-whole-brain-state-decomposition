"""Synthetic tests for the generic fail-closed pickle reader."""

from __future__ import annotations

import io
import pickle
import unittest

from tools.restricted_pickle_reader import RestrictedUnpickler, load_restricted


class RestrictedPickleReaderTests(unittest.TestCase):
    """Verify that basic structures load and global references are rejected."""

    def test_loads_basic_structure_without_global_reference(self) -> None:
        """A synthetic basic structure can be reconstructed without globals."""
        payload = pickle.dumps({"items": [1, 2, 3]}, protocol=4)
        self.assertEqual(load_restricted(io.BytesIO(payload)), {"items": [1, 2, 3]})

    def test_rejects_unlisted_global(self) -> None:
        """A synthetic unsafe global is rejected and never invoked."""
        unsafe_payload = b"cos\nsystem\n."
        with self.assertRaisesRegex(pickle.UnpicklingError, "Blocked pickle global"):
            RestrictedUnpickler(io.BytesIO(unsafe_payload)).load()

    def test_rejects_builtins_global(self) -> None:
        """A synthetic builtins global is rejected and never invoked."""
        payload = b"cbuiltins\nlen\n."
        with self.assertRaisesRegex(pickle.UnpicklingError, "Blocked pickle global"):
            RestrictedUnpickler(io.BytesIO(payload)).load()


if __name__ == "__main__":
    unittest.main()
