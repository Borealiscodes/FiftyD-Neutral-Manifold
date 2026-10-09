"""
vector_ops.py
Neutral Vector Operations for 50‑Dimensional Coordinates

Provides basic vector utilities used across the neutral 50D manifold.
All operations are purely geometric and contain no domain-specific
semantics or external system references.
"""

from __future__ import annotations
from typing import List
import math

from ..manifold_50d import Coordinate50D, DIMENSIONS


# ---------------------------------------------------------------------
# Basic vector operations
# ---------------------------------------------------------------------

def add(a: Coordinate50D, b: Coordinate50D) -> Coordinate50D:
    """Elementwise addition of two 50D coordinates."""
    return Coordinate50D([x + y for x, y in zip(a.values, b.values)])


def subtract(a: Coordinate50D, b: Coordinate50D) -> Coordinate50D:
    """Elementwise subtraction of two 50D coordinates."""
    return Coordinate50D([x - y for x, y in zip(a.values, b.values)])


def scale(coord: Coordinate50D, factor: float) -> Coordinate50D:
    """Scales all coordinate values by a constant factor."""
    return Coordinate50D([v * factor for v in coord.values])


def dot(a: Coordinate50D, b: Coordinate50D) -> float:
    """Dot product of two 50D coordinates."""
    return sum(x * y for x, y in zip(a.values, b.values))


def magnitude(coord: Coordinate50D) -> float:
    """Returns the Euclidean magnitude of the coordinate."""
    return math.sqrt(sum(v * v for v in coord.values))


def normalize(coord: Coordinate50D) -> Coordinate50D:
    """Returns a normalized version of the coordinate."""
    mag = magnitude(coord)
    if mag == 0:
        return coord.copy()
    return Coordinate50D([v / mag for v in coord.values])


# ---------------------------------------------------------------------
# Utility operations
# ---------------------------------------------------------------------

def interpolate(a: Coordinate50D, b: Coordinate50D, t: float) -> Coordinate50D:
    """
    Linear interpolation between two coordinates.
    t = 0 → a
    t = 1 → b
    """
    return Coordinate50D([(1 - t) * x + t * y for x, y in zip(a.values, b.values)])


def clamp(coord: Coordinate50D, min_val: float, max_val: float) -> Coordinate50D:
    """Clamps each coordinate value to the given range."""
    return Coordinate50D([max(min(v, max_val), min_val) for v in coord.values])


def average(coords: List[Coordinate50D]) -> Coordinate50D:
    """Returns the elementwise average of a list of coordinates."""
    if not coords:
        raise ValueError("Cannot average an empty list of coordinates.")

    accum = [0.0] * DIMENSIONS
    for c in coords:
        for i, v in enumerate(c.values):
            accum[i] += v

    count = len(coords)
    return Coordinate50D([v / count for v in accum])
