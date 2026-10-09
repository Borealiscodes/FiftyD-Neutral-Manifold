"""
manifold_50d.py
Neutral 50‑Dimensional Coordinate Manifold

Defines a simple 50‑dimensional coordinate structure and basic geometric
operations. This file contains no domain‑specific semantics or external
system references. It provides foundational geometry only.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List
import math


DIMENSIONS = 50


@dataclass
class Coordinate50D:
    """
    A 50‑dimensional coordinate vector.

    Stores raw coordinate values and provides basic vector operations.
    """
    values: List[float]

    def __post_init__(self):
        if len(self.values) != DIMENSIONS:
            raise ValueError(f"Coordinate50D requires {DIMENSIONS} values.")

    def copy(self) -> "Coordinate50D":
        return Coordinate50D(self.values.copy())

    def norm(self) -> float:
        """Euclidean norm of the vector."""
        return math.sqrt(sum(v * v for v in self.values))

    def normalized(self) -> "Coordinate50D":
        """Returns a normalized version of the vector."""
        n = self.norm()
        if n == 0:
            return self.copy()
        return Coordinate50D([v / n for v in self.values])


class Manifold50D:
    """
    Neutral 50‑dimensional manifold.

    Provides:
    - origin coordinate
    - distance metric
    - axis projection
    """

    def __init__(self):
        self.dimensions = DIMENSIONS

    def origin(self) -> Coordinate50D:
        """Returns the 50D origin."""
        return Coordinate50D([0.0] * DIMENSIONS)

    def distance(self, a: Coordinate50D, b: Coordinate50D) -> float:
        """Euclidean distance between two coordinates."""
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a.values, b.values)))

    def project(self, coord: Coordinate50D, axes: List[int]) -> List[float]:
        """Projects a coordinate onto a subset of axes."""
        return [coord.values[i] for i in axes]
