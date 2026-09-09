#!/usr/bin/env python3
"""Degree/convention checker for FCIG Model XII.

This script checks only formal characteristic-class algebra.  It is not a
calculation of a quantum anomaly coefficient in a chosen physics convention.
"""

from fractions import Fraction


def degree(*degrees: int) -> int:
    return sum(degrees)


def index_degree_six(charge: int = 1) -> tuple[Fraction, Fraction]:
    """Coefficients of c^3 and c*p1 in [Ahat ch(L^q)]_6.

    Ahat = 1 - p1/24 + ...
    ch(L^q) = exp(q c) = 1 + q c + q^2 c^2/2 + q^3 c^3/6 + ...
    """
    cubic = Fraction(charge**3, 6)
    mixed = -Fraction(charge, 24)
    return cubic, mixed


def main() -> None:
    assert degree(2, 4) == 6
    assert degree(2, 2, 2) == 6

    print("degree audit: PASS")
    print("  deg c1        = 2")
    print("  deg p1        = 4")
    print("  deg(c1*p1)    = 6")
    print("  deg(c1^3)     = 6")

    for q in (-2, -1, 1, 2, 3):
        cubic, mixed = index_degree_six(q)
        print(
            f"  q={q:+d}: [Ahat ch(L^q)]_6 = "
            f"({cubic}) c^3 + ({mixed}) c p1"
        )

    c3, cp1 = index_degree_six(1)
    assert c3 == Fraction(1, 6)
    assert cp1 == -Fraction(1, 24)

    # A six-form cannot be a top-degree differential form on a 4-manifold.
    spacetime_dimension = 4
    anomaly_degree = 6
    assert anomaly_degree > spacetime_dimension
    print("\n4D direct-action degree obstruction: PASS")
    print(f"  anomaly degree {anomaly_degree} > spacetime dimension {spacetime_dimension}")

    # The generic SO(n>=3) Chern-Weil hierarchy begins with quadratic
    # invariant polynomial data (Pontryagin degree 4), whereas SO(2) is an
    # abelian exception with Euler/c1 degree 2.
    print("\northogonal degree audit")
    print("  generic SO(n>=3): first Pontryagin degree = 4")
    print("  SO(2) exception: Euler/c1 degree = 2")


if __name__ == "__main__":
    main()
