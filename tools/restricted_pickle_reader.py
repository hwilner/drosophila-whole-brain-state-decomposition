"""Fail-closed pickle reader for data-free safety checks.

This module is deliberately generic and does not authorize repository data. It
rejects every pickle global reference rather than maintaining a source-specific
allowlist.
"""

from __future__ import annotations

import pickle
from typing import Any, BinaryIO


class RestrictedUnpickler(pickle.Unpickler):
    """Reject all global references while loading basic pickle structures.

    The class exists for synthetic safety tests only. It is not a general-purpose
    trust decision for serialized material.
    """

    def find_class(self, module: str, name: str) -> Any:
        """Reject a requested global reference.

        Args:
            module: Module requested by the serialized object.
            name: Attribute requested from the module.

        Raises:
            pickle.UnpicklingError: Always, because global references are excluded.
        """
        raise pickle.UnpicklingError(f"Blocked pickle global: {module}.{name}")


def load_restricted(handle: BinaryIO) -> Any:
    """Load a basic pickle structure with all global references disabled.

    Args:
        handle: Binary stream positioned at a pickle payload.

    Returns:
        The reconstructed basic pickle value.

    Raises:
        pickle.UnpicklingError: If the payload requests a global reference or is
            otherwise invalid.
    """
    return RestrictedUnpickler(handle).load()
