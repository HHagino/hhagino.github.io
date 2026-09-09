#!/usr/bin/env python3
"""Sanity checks for FCIG Model XIX.

No external dependencies. Checks the area-one metric, exact Fourier spectrum,
modular lattice relabeling, eta-determinant modular invariance, and the mixed
spectral curvature using a numerical real-Laplacian approximation.
"""

import cmath
from math import isclose, log, pi


def metric_and_inverse(tau: complex):
    u, Y = tau.real, tau.imag
    g = ((1.0 / Y, u / Y),
         (u / Y, (u * u + Y * Y) / Y))
    gi = (((u * u + Y * Y) / Y, -u / Y),
          (-u / Y, 1.0 / Y))
    return g, gi


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def eigenvalue(m: int, n: int, tau: complex) -> float:
    Y = tau.imag
    return 4.0 * pi * pi * abs(m * tau - n) ** 2 / Y


def eigenvalue_from_inverse_metric(m: int, n: int, tau: complex) -> float:
    _, gi = metric_and_inverse(tau)
    quad = gi[0][0] * m * m + 2.0 * gi[0][1] * m * n + gi[1][1] * n * n
    return 4.0 * pi * pi * quad


def gamma_tau(tau: complex, a: int, b: int, c: int, d: int) -> complex:
    return (a * tau + b) / (c * tau + d)


def relabel_pair(m: int, n: int, a: int, b: int, c: int, d: int):
    return a * m - c * n, d * n - b * m


def eta(tau: complex, terms: int = 100) -> complex:
    q = cmath.exp(2j * pi * tau)
    out = cmath.exp(1j * pi * tau / 12.0)
    qn = q
    for _ in range(1, terms + 1):
        out *= (1.0 - qn)
        qn *= q
    return out


def logdet(tau: complex) -> float:
    return log(tau.imag) + 4.0 * log(abs(eta(tau)))


def check_area_and_spectrum():
    tau = 0.31 + 1.27j
    g, _ = metric_and_inverse(tau)
    assert isclose(det2(g), 1.0, rel_tol=0.0, abs_tol=1e-14)
    for m, n in [(1, 0), (0, 1), (2, -1), (-3, 2)]:
        a = eigenvalue(m, n, tau)
        b = eigenvalue_from_inverse_metric(m, n, tau)
        assert isclose(a, b, rel_tol=1e-13, abs_tol=1e-13)


def check_modular_spectrum():
    tau = 0.23 + 1.11j
    generators = [
        (1, 1, 0, 1),   # T
        (0, -1, 1, 0),  # S
    ]
    pairs = [(1, 0), (0, 1), (2, -1), (-3, 2)]
    for a, b, c, d in generators:
        tp = gamma_tau(tau, a, b, c, d)
        for m, n in pairs:
            mp, np = relabel_pair(m, n, a, b, c, d)
            lhs = eigenvalue(m, n, tp)
            rhs = eigenvalue(mp, np, tau)
            assert isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)


def check_eta_determinant_modular_invariance():
    tau = 0.19 + 1.18j
    for a, b, c, d in [(1, 1, 0, 1), (0, -1, 1, 0)]:
        tp = gamma_tau(tau, a, b, c, d)
        lhs = tp.imag * abs(eta(tp)) ** 4
        rhs = tau.imag * abs(eta(tau)) ** 4
        assert isclose(lhs, rhs, rel_tol=2e-11, abs_tol=2e-11)


def check_spectral_curvature():
    # partial_tau partial_taubar f = (1/4)(d_u^2+d_Y^2)f.
    # For f=log det' Delta, -partial partialbar f = 1/(4 Y^2).
    tau = 0.27 + 1.21j
    u, Y = tau.real, tau.imag
    h = 2e-4

    f0 = logdet(tau)
    f_up = logdet((u + h) + 1j * Y)
    f_um = logdet((u - h) + 1j * Y)
    f_Yp = logdet(u + 1j * (Y + h))
    f_Ym = logdet(u + 1j * (Y - h))
    lap = (f_up - 2.0 * f0 + f_um) / (h * h) + (f_Yp - 2.0 * f0 + f_Ym) / (h * h)
    mixed_negative = -0.25 * lap
    expected = 1.0 / (4.0 * Y * Y)
    assert isclose(mixed_negative, expected, rel_tol=3e-6, abs_tol=3e-7)


def main():
    check_area_and_spectrum()
    check_modular_spectrum()
    check_eta_determinant_modular_invariance()
    check_spectral_curvature()
    print("Model XIX sanity checks: PASS")


if __name__ == "__main__":
    main()
