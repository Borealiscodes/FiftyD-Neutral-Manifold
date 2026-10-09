"""
stability_surfaces.py
Neutral Stability Surfaces for the 50‑Dimensional Manifold

Defines simple geometric stability surfaces and evaluation functions
over the 50‑dimensional coordinate space. These surfaces provide
structure for analyzing coordinate behavior without introducing
semantics or domain‑specific interpretation.
"""

from __future__ import annotations
from typing import Callable

from .manifold_50d import Coordinate50D, DIMENSIONS
from .scalar_gradients import ScalarField50D


class StabilitySurface50D:
    """
    Represents a stability surface defined by a scalar field and a
    threshold. A coordinate is considered 'stable' if the scalar field
    value is below the threshold.
    """

    def __init__(self, field: ScalarField50D, threshold: float):
        self.field = field
        self.threshold = threshold

    def is_stable(self, coord: Coordinate50D) -> bool:
        """Returns True if the coordinate lies within the stability surface."""
        return self.field.value(coord) <= self.threshold

    def margin(self, coord: Coordinate50D) -> float:
        """
        Returns the difference between the threshold and the field value.
        Positive values indicate stability; negative values indicate
        instability.
        """
        return self.threshold - self.field.value(coord)


# ---------------------------------------------------------------------
# Example neutral stability surfaces
# ---------------------------------------------------------------------

def make_altitude_surface(threshold: float) -> StabilitySurface50D:
    """
    Stability surface based on altitude-like scalar field.
    """
    from .scalar_gradients import AltitudeField
    return StabilitySurface50D(AltitudeField, threshold)


def make_density_surface(threshold: float) -> StabilitySurface50D:
    """
    Stability surface based on density-like scalar field.
    """
    from .scalar_gradients import DensityField
    return StabilitySurface50D(DensityField, threshold)


def make_smoothness_surface(threshold: float) -> StabilitySurface50D:
    """
    Stability surface based on smoothness-like scalar field.
    """
    from .scalar_gradients import SmoothnessField
    return StabilitySurface50D(SmoothnessField, threshold)
