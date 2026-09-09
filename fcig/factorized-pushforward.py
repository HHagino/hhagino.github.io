#!/usr/bin/env python3
"""Sanity checks for FCIG Model VIII.

This script does not prove the differential-cohomology projection formula.
It only checks the degree bookkeeping, the canonical multiplier 2g-2,
and the corresponding U(1) holonomy-power rule.
"""

from __future__ import annotations

import cmath
import math


def response_degree(base_degree: int, coupling_degree: int, fiber_dimension: int) -> int:
    """Degree of p_!(p^*A cup u)."""
    return base_degree + coupling_degree - fiber_dimension


def canonical_multiplier(genus: int) -> int:
    """Degree of the canonical bundle of a compact genus-g curve."""
    if genus < 0:
        raise ValueError("genus must be nonnegative")
    return 2 * genus - 2


def holonomy_power(theta: float, multiplier: int) -> complex:
    """Return exp(2 pi i theta)^multiplier."""
    return cmath.exp(2j * math.pi * theta) ** multiplier


def holonomy_scaled_character(theta: float, multiplier: int) -> complex:
    """Return exp(2 pi i multiplier*theta), the differential-character prediction."""
    return cmath.exp(2j * math.pi * multiplier * theta)


def run_demo() -> None:
    print("Degree checks")
    for d in (1, 2, 4):
        print(
            f"fiber d={d}: bare pushforward 2->{2-d}; "
            f"degree-restored with u in Hhat^{d}: "
            f"{response_degree(2, d, d)}"
        )

    print("\nCanonical curve multipliers")
    for genus in (2, 3, 5, 10):
        n = canonical_multiplier(genus)
        print(f"g={genus}: 2g-2={n}")

    print("\nHolonomy compatibility")
    theta = 0.173
    for genus in (2, 3, 5):
        n = canonical_multiplier(genus)
        lhs = holonomy_power(theta, n)
        rhs = holonomy_scaled_character(theta, n)
        err = abs(lhs - rhs)
        print(f"g={genus}: |Hol(A)^n - Hol(nA)| = {err:.3e}")
        assert err < 1e-12

    assert response_degree(2, 2, 2) == 2
    assert canonical_multiplier(2) == 2
    assert canonical_multiplier(3) == 4


if __name__ == "__main__":
    run_demo()
