"""
operator_placeholders.py
Neutral Operator Placeholders for the 50‑Dimensional Manifold

Defines simple placeholder operator structures that act on 50‑dimensional
coordinates. These operators provide a neutral scaffolding for future
geometric transformations without introducing semantics or domain-specific
interpretation.
"""

from __future__ import annotations
from typing import Callable
from dataclasses import dataclass

from .manifold_50d import Coordinate50D, DIMENSIONS


@dataclass
class Operator50D:
    """
    Represents a neutral operator acting on a 50D coordinate.

    op_fn: a function mapping a Coordinate50D to another Coordinate50D.
    """

    op_fn: Callable[[Coordinate50D], Coordinate50D]

    def apply(self, coord: Coordinate50D) -> Coordinate50D:
        """Applies the operator to a coordinate."""
        return self.op_fn(coord)


@dataclass
class LinearOperator50D(Operator50D):
    """
    A simple linear operator defined by a 50x50 matrix.

    The matrix is represented as a list of 50 rows, each containing 50 floats.
    """

    matrix: list[list[float]]

    def __post_init__(self):
        if len(self.matrix) != DIMENSIONS:
            raise ValueError("LinearOperator50D requires a 50x50 matrix.")
        for row in self.matrix:
            if len(row) != DIMENSIONS:
                raise ValueError("LinearOperator50D requires a 50x50 matrix.")

        # Wrap the matrix multiplication into op_fn
        def linear_fn(coord: Coordinate50D) -> Coordinate50D:
            new_values = []
            for row in self.matrix:
                new_values.append(sum(r * v for r, v in zip(row, coord.values)))
            return Coordinate50D(new_values)

        self.op_fn = linear_fn


# ---------------------------------------------------------------------
# Example neutral operators
# ---------------------------------------------------------------------

def identity_operator() -> Operator50D:
    """Returns an identity operator that leaves coordinates unchanged."""
    def op(coord: Coordinate50D) -> Coordinate50D:
        return coord.copy()
    return Operator50D(op)


def scale_operator(factor: float) -> Operator50D:
    """Returns a scaling operator that multiplies all coordinates by a factor."""
    def op(coord: Coordinate50D) -> Coordinate50D:
        return Coordinate50D([v * factor for v in coord.values])
    return Operator50D(op)


def shift_operator(offset: float) -> Operator50D:
    """Returns a shift operator that adds a constant offset to all coordinates."""
    def op(coord: Coordinate50D) -> Coordinate50D:
        return Coordinate50D([v + offset for v in coord.values])
    return Operator50D(op)
