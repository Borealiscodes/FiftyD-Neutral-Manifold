"""
operators.py
Neutral Operators for 50‑Dimensional Coordinates

Defines simple geometric operators acting on Coordinate50D objects.
Operators are reversible when possible and contain no semantics or
domain‑specific interpretation.
"""

from __future__ import annotations
from typing import Callable, List
import numpy as np

from .manifold_50d import Coordinate50D, DIMENSIONS


# ---------------------------------------------------------------------
# Identity Operator
# ---------------------------------------------------------------------

def identity_operator(coord: Coordinate50D) -> Coordinate50D:
    """
    Returns the coordinate unchanged.
    """
    return coord.copy()


# ---------------------------------------------------------------------
# Scaling Operator
# ---------------------------------------------------------------------

def scaling_operator(coord: Coordinate50D, factor: float) -> Coordinate50D:
    """
    Scales all coordinate values by a constant factor.
    """
    return Coordinate50D([v * factor for v in coord.values])


def scaling_inverse(factor: float) -> float:
    """
    Returns the inverse scaling factor.
    """
    if factor == 0:
        raise ValueError("Scaling factor cannot be zero.")
    return 1.0 / factor


# ---------------------------------------------------------------------
# Shift Operator
# ---------------------------------------------------------------------

def shift_operator(coord: Coordinate50D, shift: Coordinate50D) -> Coordinate50D:
    """
    Adds a shift vector to the coordinate.
    """
    return Coordinate50D([v + s for v, s in zip(coord.values, shift.values)])


def shift_inverse(shift: Coordinate50D) -> Coordinate50D:
    """
    Returns the inverse shift vector.
    """
    return Coordinate50D([-s for s in shift.values])


# ---------------------------------------------------------------------
# Linear Operator
# ---------------------------------------------------------------------

def linear_operator(coord: Coordinate50D, matrix: np.ndarray) -> Coordinate50D:
    """
    Applies a linear transformation using a 50x50 matrix.
    """
    if matrix.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrix must be 50x50.")
    result = matrix @ np.array(coord.values)
    return Coordinate50D(result.tolist())


def linear_inverse(matrix: np.ndarray) -> np.ndarray:
    """
    Returns the inverse of a 50x50 matrix.
    """
    if matrix.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrix must be 50x50.")
    return np.linalg.inv(matrix)
