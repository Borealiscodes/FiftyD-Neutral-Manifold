"""
stability_surfaces.py
Neutral Stability Surfaces for the 50‑Dimensional Manifold

Defines simple geometric stability surfaces and evaluation functions
over the 50‑dimensional coordinate space. These surfaces provide
structure for analyzing coordinate behavior without introducing
semantics or domain‑specific interpretation.

Supports both:
- pure scalar field functions (scalar_fields.py)
- gradient-capable scalar field objects (scalar_gradients.py via .value)
"""

from __future__ import annotations
from typing import Callable

from .manifold_50d import Coordinate50D
from .scalar_fields import altitude_field, density_field, smoothness_field


class StabilitySurface:
    """
    Represents a stability surface defined by a scalar field function
    and a threshold. Accepts any callable that maps a coordinate to a float.

    This allows:
    - pure scalar functions: f(coord) -> float
    - gradient-capable objects: obj.value(coord) -> float
    """

    def __init__(self, field_fn: Callable[[Coordinate50D], float], threshold: float):
        self.field_fn = field_fn
        self.threshold = threshold

    def is_stable(self, coord: Coordinate50D) -> bool:
        """Returns True if the coordinate lies within the stability surface."""
        return self.field_fn(coord) <= self.threshold

    def margin(self, coord: Coordinate50D) -> float:
        """
        Returns the difference between the threshold and the field value.
        Positive values indicate stability; negative values indicate instability.
        """
        return self.threshold - self.field_fn(coord)


# ---------------------------------------------------------------------
# Pure-function stability surfaces
# ---------------------------------------------------------------------

def make_altitude_surface(threshold: float) -> StabilitySurface:
    return StabilitySurface(altitude_field, threshold)


def make_density_surface(threshold: float) -> StabilitySurface:
    return StabilitySurface(density_field, threshold)


def make_smoothness_surface(threshold: float) -> StabilitySurface:
    return StabilitySurface(smoothness_field, threshold)


# ---------------------------------------------------------------------
# Gradient-capable stability surfaces (optional)
# ---------------------------------------------------------------------

def make_altitude_surface_grad(threshold: float) -> StabilitySurface:
    from .scalar_gradients import AltitudeField
    return StabilitySurface(AltitudeField().value, threshold)


def make_density_surface_grad(threshold: float) -> StabilitySurface:
    from .scalar_gradients import DensityField
    return StabilitySurface(DensityField().value, threshold)


def make_smoothness_surface_grad(threshold: float) -> StabilitySurface:
    from .scalar_gradients import SmoothnessField
    return StabilitySurface(SmoothnessField().value, threshold)
