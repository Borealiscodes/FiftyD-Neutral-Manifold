"""
math_tools.py
Neutral Math Utilities for 50‑Dimensional Geometry

Provides small, system‑agnostic mathematical helpers used across the
neutral 50D manifold. These functions support geometric operations
without introducing semantics or domain‑specific interpretation.
"""

from __future__ import annotations
import math
from typing import Iterable, List


# ---------------------------------------------------------------------
# Basic math helpers
# ---------------------------------------------------------------------

def safe_divide(a: float, b: float) -> float:
    """
    Divides a by b, returning 0.0 if b is zero.
    Neutral helper to avoid runtime errors in geometric calculations.
    """
    if b == 0:
        return 0.0
    return a / b


def mean(values: Iterable[float]) -> float:
    """
    Returns the arithmetic mean of a list of floats.
    """
    values = list(values)
    if not values:
        raise ValueError("Cannot compute mean of an empty iterable.")
    return sum(values) / len(values)


def variance(values: Iterable[float]) -> float:
    """
    Returns the variance of a list of floats.
    """
    values = list(values)
    if not values:
        raise ValueError("Cannot compute variance of an empty iterable.")
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


def stddev(values: Iterable[float]) -> float:
    """
    Returns the standard deviation of a list of floats.
    """
    return math.sqrt(variance(values))


# ---------------------------------------------------------------------
# Geometry‑adjacent helpers
# ---------------------------------------------------------------------

def l2_norm(values: Iterable[float]) -> float:
    """
    Computes the L2 norm of a list of floats.
    """
    return math.sqrt(sum(v * v for v in values))


def l1_norm(values: Iterable[float]) -> float:
    """
    Computes the L1 norm of a list of floats.
    """
    return sum(abs(v) for v in values)


def clamp_value(v: float, min_val: float, max_val: float) -> float:
    """
    Clamps a single float to a given range.
    """
    return max(min(v, max_val), min_val)
