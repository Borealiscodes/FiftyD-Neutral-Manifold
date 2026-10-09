"""
matrix_ops.py
Neutral Matrix Operations for 50‑Dimensional Geometry

Provides basic matrix utilities used across the neutral 50D manifold.
All operations are purely geometric and contain no domain-specific
semantics or external system references.
"""

from __future__ import annotations
import numpy as np
from typing import List

from ..manifold_50d import Coordinate50D, DIMENSIONS


# ---------------------------------------------------------------------
# Matrix construction
# ---------------------------------------------------------------------

def zero_matrix() -> np.ndarray:
    """Returns a 50x50 zero matrix."""
    return np.zeros((DIMENSIONS, DIMENSIONS))


def identity_matrix() -> np.ndarray:
    """Returns the 50x50 identity matrix."""
    return np.eye(DIMENSIONS)


def random_matrix(low: float = -1.0, high: float = 1.0) -> np.ndarray:
    """Returns a random 50x50 matrix with uniform values in [low, high]."""
    return np.random.uniform(low, high, (DIMENSIONS, DIMENSIONS))


# ---------------------------------------------------------------------
# Matrix operations
# ---------------------------------------------------------------------

def matmul(matrix: np.ndarray, coord: Coordinate50D) -> Coordinate50D:
    """
    Applies a matrix-vector multiplication.
    """
    if matrix.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrix must be 50x50.")
    result = matrix @ np.array(coord.values)
    return Coordinate50D(result.tolist())


def add_matrices(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Elementwise addition of two 50x50 matrices."""
    if a.shape != (DIMENSIONS, DIMENSIONS) or b.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrices must be 50x50.")
    return a + b


def subtract_matrices(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Elementwise subtraction of two 50x50 matrices."""
    if a.shape != (DIMENSIONS, DIMENSIONS) or b.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrices must be 50x50.")
    return a - b


def scale_matrix(matrix: np.ndarray, factor: float) -> np.ndarray:
    """Scales all matrix entries by a constant factor."""
    if matrix.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrix must be 50x50.")
    return matrix * factor


def transpose(matrix: np.ndarray) -> np.ndarray:
    """Returns the transpose of a 50x50 matrix."""
    if matrix.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrix must be 50x50.")
    return matrix.T


def inverse(matrix: np.ndarray) -> np.ndarray:
    """Returns the inverse of a 50x50 matrix."""
    if matrix.shape != (DIMENSIONS, DIMENSIONS):
        raise ValueError("Matrix must be 50x50.")
    return np.linalg.inv(matrix)


# ---------------------------------------------------------------------
# Utility operations
# ---------------------------------------------------------------------

def is_square(matrix: np.ndarray) -> bool:
    """Checks if a matrix is square."""
    return matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]


def is_50x50(matrix: np.ndarray) -> bool:
    """Checks if a matrix is exactly 50x50."""
    return matrix.shape == (DIMENSIONS, DIMENSIONS)
