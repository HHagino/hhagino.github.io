#!/usr/bin/env python3
"""Sanity checks for the local sector of FCIG Model XX.

No external dependencies. Checks the area-one elliptic shape matrix, the
Poincare trace identity, KK masses, and the proper-time UV coefficient used
in adiabatic-elliptic.md.
"""

from math import isclose, pi


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def trace(A):
    return A[0][0] + A[1][1]


def G(u, Y):
    return [[1.0 / Y, u / Y], [u / Y, (u * u + Y * Y) / Y]]


def Ginv(u, Y):
    return [[Y + u * u / Y, -u / Y], [-u / Y, 1.0 / Y]]


def dG_du(u, Y):
    return [[0.0, 1.0 / Y], [1.0 / Y, 2.0 * u / Y]]


def dG_dY(u, Y):
    return [[-1.0 / (Y * Y), -u / (Y * Y)],
            [-u / (Y * Y), 1.0 - u * u / (Y * Y)]]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def bilinear_trace(u, Y, A, B):
    gi = Ginv(u, Y)
    return trace(matmul(matmul(matmul(gi, A), gi), B))


def mass2(m, n, u, Y, L=1.0):
    return 4.0 * pi * pi * ((m * u - n) ** 2 + (m * Y) ** 2) / (L * L * Y)


def check_shape_matrix():
    u, Y = 0.31, 1.27
    assert isclose(det2(G(u, Y)), 1.0, rel_tol=0.0, abs_tol=1e-14)


def check_poincare_trace_identity():
    u, Y = 0.37, 1.19
    gu = dG_du(u, Y)
    gY = dG_dY(u, Y)
    uu = bilinear_trace(u, Y, gu, gu)
    YY = bilinear_trace(u, Y, gY, gY)
    uY = bilinear_trace(u, Y, gu, gY)
    expected = 2.0 / (Y * Y)
    assert isclose(uu, expected, rel_tol=1e-13, abs_tol=1e-13)
    assert isclose(YY, expected, rel_tol=1e-13, abs_tol=1e-13)
    assert abs(uY) < 1e-13


def check_intrinsic_kk_mass():
    u, Y, L = 0.28, 1.33, 2.4
    for m, n in [(1, 0), (0, 1), (2, -1), (-3, 2)]:
        direct = mass2(m, n, u, Y, L)
        # q^T G^{-1} q / L^2 with Fourier factor (2pi)^2
        gi = Ginv(u, Y)
        quad = gi[0][0] * m * m + 2.0 * gi[0][1] * m * n + gi[1][1] * n * n
        matrix_value = 4.0 * pi * pi * quad / (L * L)
        assert isclose(direct, matrix_value, rel_tol=1e-13, abs_tol=1e-13)


def check_proper_time_coefficient():
    # W = -1/2 int dt/t (4pi t)^-3 int sqrt(g) [1 + t R/6 + ...]
    # int_{Lambda^-2}^infty t^-3 dt = Lambda^4/2.
    Lambda = 3.7
    coeff_R = -0.5 * (1.0 / 6.0) * (1.0 / (4.0 * pi) ** 3) * (Lambda ** 4 / 2.0)
    expected_R = -(Lambda ** 4) / (24.0 * (4.0 * pi) ** 3)
    assert isclose(coeff_R, expected_R, rel_tol=1e-14)

    # R6 contains -1/2 * Poincare kinetic density, so the induced coefficient is positive.
    coeff_tau = -0.5 * coeff_R
    expected_tau = (Lambda ** 4) / (48.0 * (4.0 * pi) ** 3)
    assert isclose(coeff_tau, expected_tau, rel_tol=1e-14)


def main():
    check_shape_matrix()
    check_poincare_trace_identity()
    check_intrinsic_kk_mass()
    check_proper_time_coefficient()
    print("Model XX local-sector sanity checks: PASS")


if __name__ == "__main__":
    main()
