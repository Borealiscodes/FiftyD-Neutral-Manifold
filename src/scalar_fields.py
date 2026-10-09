"""
scalar_fields.py
Neutral Scalar Field Definitions for the 50‑Dimensional Manifold

Provides simple scalar functions that map a 50D coordinate to a single
numeric value. Contains no semantics or domain‑specific interpretation.
All operations are purely geometric.
"""

from __future__ import annotations
from typing import Callable
from .manifold_50d import Coordinate50D


def altitude_field(coord: Coordinate50D) -> float:
    """
    Computes a magnitude‑style scalar value.
    """
    return sum(v * v for v in coord.values) ** 0.5


def density_field(coord: Coordinate50D) -> float:
    """
    Computes a sum‑style scalar value.
    """
    return sum(coord.values)


def smoothness_field(coord: Coordinate50D) -> float:
    """
    Computes a variation‑style scalar value.
    """
    diffs = [
        abs(coord.values[i] - coord.values[i - 1])
        for i in range(1, len(coord.values))
    ]
    return sum(diffs)
