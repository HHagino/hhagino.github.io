#!/usr/bin/env python3
"""Numerical checks for the FCIG disk transported-Bergman identity.

Uses only the Python standard library.  The identity checked is

    rho(x) * sqrt((1-x^2)(1-|g(ix)|^2)) / (1-ix*conj(g(ix)))
      = 1 / (C - i S u),

with C=cosh(L/2), S=sinh(L/2), u=2x/(1-x^2), and
rho=|C+iSx|/(C-iSx).  Raising both sides to 2q gives the oriented
Sun/FCIG cylinder kernel.
"""

from __future__ import annotations

import cmath
import math


def check(L: float, r: float, q: int) -> float:
    C = math.cosh(L / 2.0)
    S = math.sinh(L / 2.0)
    x = math.tanh(r / 2.0)
    z = 1j * x
    w = (C * z + S) / (S * z + C)
    u = math.sinh(r)

    coherent_base = math.sqrt((1.0 - abs(z) ** 2) * (1.0 - abs(w) ** 2)) / (
        1.0 - z * w.conjugate()
    )
    rho = abs(C + 1j * S * x) / (C - 1j * S * x)

    lhs = (rho * coherent_base) ** (2 * q)
    rhs = (C - 1j * S * u) ** (-2 * q)
    return abs(lhs - rhs)


def main() -> None:
    samples = [
        (0.4, -1.1, 2),
        (0.7, -0.2, 3),
        (1.2, 0.0, 4),
        (1.7, 0.8, 5),
        (2.4, 1.4, 7),
    ]
    worst = 0.0
    for L, r, q in samples:
        err = check(L, r, q)
        worst = max(worst, err)
        print(f"L={L:4.1f} r={r:4.1f} q={q:2d} error={err:.3e}")
    print(f"max error={worst:.3e}")
    if worst > 1e-11:
        raise SystemExit("transported Bergman identity check failed")


if __name__ == "__main__":
    main()
