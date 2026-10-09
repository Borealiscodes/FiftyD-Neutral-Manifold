"""
random.py
Neutral Random Generators for 50‑Dimensional Geometry

Provides random coordinate and matrix utilities used across the neutral
50D manifold. All operations are purely geometric and contain no
domain-specific semantics or external system references.
"""

from __future__ import annotations
import numpy as np

from ..manifold_50d import Coordinate50D, DIMENSIONS


# ---------------------------------------------------------------------
# Random coordinates
# ---------------------------------------------------------------------

def random_coord(low: float = -1.0, high: float = 1.0) -> Coordinate50D:
    """
    Returns a random 50D coordinate with uniform values in [low, high].
    """
    values = np.random.uniform(low, high, DIMENSIONS).tolist()
    return Coordinate50D(values)


def random_unit_coord() -> Coordinate50D:
    """
    Returns a random 50D coordinate normalized to unit magnitude.
    """
    values = np.random.uniform(-1.0, 1.0, DIMENSIONS)
    mag = np.linalg.norm(values)
    if mag == 0:
        return Coordinate50D(values.tolist())
    return Coordinate50D((values / mag).tolist())


# ---------------------------------------------------------------------
# Random matrices
# ---------------------------------------------------------------------

def random_matrix(low: float = -1.0, high: float = 1.0) -> np.ndarray:
    """
    Returns a random 50x50 matrix with uniform values in [low, high].
    """
    return np.random.uniform(low, high, (DIMENSIONS, DIMENSIONS))


def random_orthogonal_matrix() -> np.ndarray:
    """
    Returns a random 50x50 orthogonal matrix using QR decomposition.
    """
    # Generate a random matrix
    A = np.random.normal(size=(DIMENSIONS, DIMENSIONS))
    # QR decomposition
    Q, _ = np.linalg.qr(A)
    return Q


def random_diagonal_matrix(low: float = 0.1, high: float = 1.0) -> np.ndarray:
    """
    Returns a random diagonal 50x50 matrix with values in [low, high].
    """
    diag = np.random.uniform(low, high, DIMENSIONS)
    return np.diag(diag)
