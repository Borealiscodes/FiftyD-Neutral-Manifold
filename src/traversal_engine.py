"""
traversal_engine.py
Neutral 50‑Dimensional Traversal Engine

Provides simple, reversible update rules for moving through the
50‑dimensional coordinate manifold. Contains no semantics or domain‑
specific interpretation. All operations are purely geometric.
"""

from __future__ import annotations
from typing import Callable, List
from dataclasses import dataclass

from .manifold_50d import Coordinate50D, DIMENSIONS


@dataclass
class TraversalStep:
    """
    Represents a single traversal update applied to a coordinate.
    The update is a function that maps a 50D coordinate to another.
    """
    update_fn: Callable[[Coordinate50D], Coordinate50D]


class TraversalEngine50D:
    """
    Neutral traversal engine for the 50D manifold.

    Provides:
    - stepwise coordinate updates
    - reversible traversal sequences
    - bounded update enforcement
    """

    def __init__(self, bound: float = 1.0):
        """
        bound: maximum allowed change per coordinate axis.
        """
        self.bound = bound

    def apply_step(self, coord: Coordinate50D, step: TraversalStep) -> Coordinate50D:
        """
        Applies a traversal step and enforces per‑axis bounds.
        """
        updated = step.update_fn(coord)
        bounded_values = [
            max(min(v, self.bound), -self.bound)
            for v in updated.values
        ]
        return Coordinate50D(bounded_values)

    def apply_sequence(
        self,
        coord: Coordinate50D,
        steps: List[TraversalStep]
    ) -> Coordinate50D:
        """
        Applies a sequence of traversal steps in order.
        """
        current = coord
        for step in steps:
            current = self.apply_step(current, step)
        return current

    def reverse_sequence(
        self,
        coord: Coordinate50D,
        steps: List[TraversalStep]
    ) -> Coordinate50D:
        """
        Applies the inverse of a traversal sequence by reversing the
        order and applying each step's inverse update function.

        Assumes each step has an inverse update function attached.
        """
        current = coord
        for step in reversed(steps):
            if not hasattr(step, "inverse_fn"):
                raise ValueError("TraversalStep missing inverse_fn.")
            current = Coordinate50D(step.inverse_fn(current).values)
        return current
