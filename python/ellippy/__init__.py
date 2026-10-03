# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from __future__ import annotations

from . import bulirsch, carlson, legendre, misc
from .__about__ import *
from .bulirsch import *
from .carlson import *
from .legendre import *
from .misc import *

__all__ = [  # noqa: RUF022
    # Submodules
    "bulirsch",
    "carlson",
    "legendre",
    "misc",
    # Legendre complete
    "ellipk",
    "ellipe",
    "ellipke",
    "ellippi",
    "ellipd",
    # Legendre incomplete
    "ellipf",
    "ellipeinc",
    "ellippiinc",
    "ellipdinc",
    "ellippiinc_bulirsch",
    # Bulirsch
    "cel",
    "cel1",
    "cel2",
    "cel3",
    "el1",
    "el2",
    "el3",
    # Carlson
    "elliprf",
    "elliprg",
    "elliprj",
    "elliprc",
    "elliprd",
    # Misc
    "jacobi_zeta",
    "heuman_lambda",
]
