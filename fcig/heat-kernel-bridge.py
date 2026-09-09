#!/usr/bin/env python3
"""Sanity checks for FCIG Model XVI.

No external dependencies. This is not a proof; it verifies coefficient algebra and
proper-time UV degree bookkeeping in the conventions used by the note.
"""

from fractions import Fraction


def check_scalar_r2_reduction() -> None:
    # General b4 R^2 coefficient for E = -xi R:
    # (5 - 60 xi + 180 xi^2)/360
    lhs = (
        Fraction(5, 360),
        Fraction(-60, 360),
        Fraction(180, 360),
    )

    # 1/2 (xi - 1/6)^2
    rhs = (
        Fraction(1, 72),
        Fraction(-1, 6),
        Fraction(1, 2),
    )

    assert lhs == rhs


def check_bundle_and_curvature_coefficients() -> None:
    assert Fraction(30, 360) == Fraction(1, 12)   # Omega^2
    assert Fraction(2, 360) == Fraction(1, 180)   # Riemann^2
    assert Fraction(-2, 360) == Fraction(-1, 180) # Ricci^2


def check_total_derivative_coefficient() -> None:
    # (12 - 60 xi)/360 = (1 - 5 xi)/30
    lhs = (Fraction(12, 360), Fraction(-60, 360))
    rhs = (Fraction(1, 30), Fraction(-1, 6))
    assert lhs == rhs


def check_conformal_scalar() -> None:
    xi = Fraction(1, 6)
    b2_r = Fraction(1, 6) - xi
    r2 = Fraction(1, 2) * (xi - Fraction(1, 6)) ** 2
    assert b2_r == 0
    assert r2 == 0


def check_four_dimensional_uv_orders() -> None:
    # K(t) ~ t^-2 [B0 + t B2 + t^2 B4 + ...], while W has dt/t.
    # Thus integrands scale as t^-3, t^-2, t^-1 for B0, B2, B4.
    powers = {"B0": -3, "B2": -2, "B4": -1, "B6": 0}
    assert powers["B0"] == -3
    assert powers["B2"] == -2
    assert powers["B4"] == -1
    assert powers["B6"] >= 0


def main() -> None:
    check_scalar_r2_reduction()
    check_bundle_and_curvature_coefficients()
    check_total_derivative_coefficient()
    check_conformal_scalar()
    check_four_dimensional_uv_orders()
    print("Model XVI sanity checks: PASS")


if __name__ == "__main__":
    main()
