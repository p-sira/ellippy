# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from __future__ import annotations
from importlib import metadata as _metadata

__all__ = ["__name__", "__version__", "__author__", "__license__", "__copyright__"]

__name__ = "ellippy"
__author__ = "Sira Pornsiriprasert"
__license__ = "BSD-3-Clause"
__copyright__ = f"2025 {__author__}"

try:
    __version__ = _metadata.version("ellippy")
except _metadata.PackageNotFoundError:
    # Fallback for editable installs or when metadata is unavailable
    __version__ = "0.0.0+unknown"
