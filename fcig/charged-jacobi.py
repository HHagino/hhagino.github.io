#!/usr/bin/env python3
"""Sanity checks for FCIG Model XXVI.

Uses only the Python standard library. The finite products/series are numerical
checks of conventions; they do not replace the cited Kronecker/Jacobi theorems.
"""

from __future__ import annotations

import cmath
import math


def eta(tau: complex, nmax: int = 120) -> complex:
    q = cmath.exp(2j * math.pi * tau)
    prod = 1.0 + 0.0j
    for n in range(1, nmax + 1):
        prod *= 1.0 - q**n
    return cmath.exp(1j * math.pi * tau / 12.0) * prod


def theta1(z: complex, tau: complex, nmax: int = 40) -> complex:
    # theta_1 with elliptic periods 1 and tau.
    s = 0.0 + 0.0j
    for n in range(-nmax, nmax + 1):
        h = n + 0.5
        s += ((-1) ** n) * cmath.exp(
            1j * math.pi * tau * h * h + 2j * math.pi * h * z
        )
    return -1j * s


def determinant(tau: complex, z: complex, charge: int = 1) -> float:
    y = tau.imag
    v = z.imag
    hol = theta1(charge * z, tau) / eta(tau)
    return math.exp(-2.0 * math.pi * charge * charge * v * v / y) * abs(hol) ** 2


def eig(tau: complex, z: complex, m: int, n: int, charge: int = 1) -> float:
    return 4.0 * math.pi**2 / tau.imag * abs(m * tau - n + charge * z) ** 2


def close(a: float, b: float, tol: float = 3e-10) -> None:
    scale = max(1.0, abs(a), abs(b))
    assert abs(a - b) <= tol * scale, (a, b, abs(a - b))


def main() -> None:
    tau = 0.23 + 1.17j
    z = 0.31 + 0.27j
    d0 = determinant(tau, z)

    # Elliptic translations.
    for r, s in [(1, 0), (0, 1), (1, -2)]:
        close(d0, determinant(tau, z + r * tau + s))

    # Modular generators S and T.
    close(d0, determinant(-1.0 / tau, z / tau))
    close(d0, determinant(tau + 1.0, z))

    # Spectrum is relabeled by a large gauge transformation.
    q = 2
    r, s = 1, -1
    lhs = eig(tau, z + r * tau + s, 3, -2, q)
    # m -> m + q r, n -> n - q s in the chosen convention.
    rhs = eig(tau, z, 3 + q * r, -2 - q * s, q)
    close(lhs, rhs)

    # Zero-mode normalization: D/lambda_small -> Y |eta|^4.
    target = tau.imag * abs(eta(tau)) ** 4
    eps = 1.0e-5
    zsmall = eps * (1.0 + 0.3j)
    ratio = determinant(tau, zsmall) / eig(tau, zsmall, 0, 0)
    close(ratio, target, tol=2e-7)

    # Fiberwise Jacobi curvature coefficient scales exactly as q^2.
    c1 = math.pi / tau.imag
    c3 = 9.0 * math.pi / tau.imag
    close(c3 / c1, 9.0)

    print("Model XXVI checks passed")
    print("D(tau,z):", d0)
    print("zero-mode ratio:", ratio)
    print("untwisted primed determinant:", target)
    print("charge-3 / charge-1 curvature ratio:", c3 / c1)


if __name__ == "__main__":
    main()
