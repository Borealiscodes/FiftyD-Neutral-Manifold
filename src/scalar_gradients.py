"""
scalar_gradients.py
Neutral Scalar Fields for the 50‑Dimensional Manifold

Defines simple scalar fields and their gradients over the 50‑dimensional
coordinate space. These fields provide geometric structure only and do
not imply any domain‑specific meaning or interpretation.
"""

from __future__ import annotations
from typing import Callable, List

from .manifold_50d import Coordinate50D, DIMENSIONS


class ScalarField50D:
    """
    Represents a scalar field defined over the 50D manifold.

    field_fn: maps a 50D coordinate to a scalar value.
    """

    def __init__(self, field_fn: Callable[[Coordinate50D], float]):
        self.field_fn = field_fn

    def value(self, coord: Coordinate50D) -> float:
        """Returns the scalar field value at the given coordinate."""
        return self.field_fn(coord)

    def gradient(self, coord: Coordinate50D, epsilon: float = 1e-6) -> List[float]:
        """
        Computes the numerical gradient of the scalar field at the given
        coordinate using finite differences.
        """
        base_value = self.field_fn(coord)
        grad = []

        for i in range(DIMENSIONS):
            shifted_values = coord.values.copy()
            shifted_values[i] += epsilon
            shifted_coord = Coordinate50D(shifted_values)

            shifted_value = self.field_fn(shifted_coord)
            grad.append((shifted_value - base_value) / epsilon)

        return grad


# ---------------------------------------------------------------------
# Example neutral scalar fields
# ---------------------------------------------------------------------

def altitude_field(coord: Coordinate50D) -> float:
    """
    A simple altitude-like scalar field based on vector norm.
    """
    return coord.norm()


def density_field(coord: Coordinate50D) -> float:
    """
    A density-like scalar field based on squared norm.
    """
    return coord.norm() ** 2


def smoothness_field(coord: Coordinate50D) -> float:
    """
    A smoothness-like scalar field based on average absolute value.
    """
    return sum(abs(v) for v in coord.values) / DIMENSIONS


# Predefined field instances
AltitudeField = ScalarField50D(altitude_field)
DensityField = ScalarField50D(density_field)
SmoothnessField = ScalarField50D(smoothness_field)
