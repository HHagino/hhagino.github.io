#!/usr/bin/env python3
"""Sanity checks for FCIG Model XXV.

This script checks only the arithmetic/lattice identities derived in the note.
It is not a replacement for the cited six-dimensional anomaly theorems.
"""

from __future__ import annotations


def U_dot(x: tuple[int, int], y: tuple[int, int]) -> int:
    """Bilinear form for U = [[0,1],[1,0]]."""
    return x[0] * y[1] + x[1] * y[0]


def is_characteristic_on_box(a: tuple[int, int], radius: int = 8) -> bool:
    """Finite-box sanity check of a.x == x.x mod 2.

    For U the exact criterion is immediate algebraically; the finite box is only a
    machine sanity check against sign/index mistakes.
    """
    for m in range(-radius, radius + 1):
        for n in range(-radius, radius + 1):
            x = (m, n)
            if (U_dot(a, x) - U_dot(x, x)) % 2:
                return False
    return True


def threshold(v: int, h: int, t: int) -> int:
    return 2 * v - h + 2 * t


def h_from_gravitational_anomaly(v: int, t: int) -> int:
    return 273 + v - 29 * t


def threshold_reduced(v: int, t: int) -> int:
    return v + 31 * t - 273


def main() -> None:
    # U is unimodular with determinant -1 and signature (1,1).
    det_u = -1
    assert abs(det_u) == 1

    a_good = (2, 2)
    a_bad = (4, 1)

    # Both obey the same local norm condition for T=1.
    assert U_dot(a_good, a_good) == 8
    assert U_dot(a_bad, a_bad) == 8
    assert 8 == 9 - 1

    # But only the F0-type vector is characteristic.
    assert is_characteristic_on_box(a_good)
    assert not is_characteristic_on_box(a_bad)
    assert (U_dot(a_bad, (1, 0)) - U_dot((1, 0), (1, 0))) % 2 == 1

    # Same field counts -> same threshold regardless of lattice refinement.
    v, h, t = 0, 244, 1
    assert h - v + 29 * t == 273
    assert threshold(v, h, t) == -242
    assert threshold_reduced(v, t) == -242

    # Positive F-theory witness from the generalized dP9 U(1)^8 model.
    v2, t2 = 8, 9
    h2 = h_from_gravitational_anomaly(v2, t2)
    assert h2 == 20
    assert h2 - v2 + 29 * t2 == 273
    assert threshold(v2, h2, t2) == 14
    assert threshold_reduced(v2, t2) == 14

    # Algebraic reduction is exact on a grid of integer test values.
    for t_test in range(0, 10):
        for v_test in range(0, 30):
            h_test = h_from_gravitational_anomaly(v_test, t_test)
            assert threshold(v_test, h_test, t_test) == threshold_reduced(v_test, t_test)

    print("Model XXV checks passed")
    print("U determinant:", det_u)
    print("a_good^2 = a_bad^2 =", U_dot(a_good, a_good))
    print("characteristic(a_good):", is_characteristic_on_box(a_good))
    print("characteristic(a_bad):", is_characteristic_on_box(a_bad))
    print("F0 witness K:", threshold(0, 244, 1))
    print("gdP9 U(1)^8 witness K:", threshold(v2, h2, t2))


if __name__ == "__main__":
    main()
