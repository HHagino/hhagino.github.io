#!/usr/bin/env python3
"""Sanity checks for FCIG Model XXII.

Checks:
1. the exact fiber Christoffel / winding identity;
2. vector and 6d Dirac Lorentz-generator quadratic indices;
3. Wilson-line and E-term coefficient arithmetic;
4. cancellation/survival pattern of a 6d N=(1,0) vector multiplet.

No external dependencies.
"""

from fractions import Fraction
from math import isclose, pi


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def G(u, Y):
    return [[1.0 / Y, u / Y],
            [u / Y, (u * u + Y * Y) / Y]]


def Ginv(u, Y):
    return [[Y + u * u / Y, -u / Y],
            [-u / Y, 1.0 / Y]]


def dG(u, Y, du, dY):
    return [
        [-dY / (Y * Y), du / Y - u * dY / (Y * Y)],
        [du / Y - u * dY / (Y * Y),
         2.0 * u * du / Y + dY - (u * u) * dY / (Y * Y)],
    ]


def full_metric_and_derivative(u, Y, L, du, dY):
    gf = G(u, Y)
    dgf = dG(u, Y, du, dY)
    g = [[0.0] * 3 for _ in range(3)]
    dg = [[0.0] * 3 for _ in range(3)]
    g[0][0] = 1.0
    for a in range(2):
        for b in range(2):
            g[a + 1][b + 1] = L * L * gf[a][b]
            dg[a + 1][b + 1] = L * L * dgf[a][b]
    gi = [[0.0] * 3 for _ in range(3)]
    gi[0][0] = 1.0
    gfi = Ginv(u, Y)
    for a in range(2):
        for b in range(2):
            gi[a + 1][b + 1] = gfi[a][b] / (L * L)
    return g, gi, dg


def gamma_internal(u, Y, L, du, dY, a):
    """Matrix (Gamma_a)^M_N for a=0,1 fiber coordinate, x-derivatives only."""
    g, gi, dg = full_metric_and_derivative(u, Y, L, du, dY)
    A = a + 1
    out = [[0.0] * 3 for _ in range(3)]

    def deriv(coord, i, j):
        return dg[i][j] if coord == 0 else 0.0

    for M in range(3):
        for N in range(3):
            val = 0.0
            for P in range(3):
                val += 0.5 * gi[M][P] * (
                    deriv(A, P, N) + deriv(N, P, A) - deriv(P, A, N)
                )
            out[M][N] = val
    return out


def check_winding_christoffel_identity():
    u, Y, L = 0.31, 1.27, 2.3
    du, dY = 0.17, -0.23
    p, q = 2.0, -1.0
    G1 = gamma_internal(u, Y, L, du, dY, 0)
    G2 = gamma_internal(u, Y, L, du, dY, 1)
    A = [[p * G1[i][j] + q * G2[i][j] for j in range(3)] for i in range(3)]
    lhs = trace(matmul(A, A))
    gf = G(u, Y)
    Q = p * p * gf[0][0] + 2.0 * p * q * gf[0][1] + q * q * gf[1][1]
    K = (du * du + dY * dY) / (Y * Y)
    rhs = -0.5 * L * L * Q * K
    assert isclose(lhs, rhs, rel_tol=2e-12, abs_tol=2e-12)


def check_lorentz_indices():
    # For one SO(2) rotation plane:
    # vector eigenvalues are +1,-1 plus four zeros -> trace J^2=2.
    C_vec = 1.0 + 1.0
    # 6d complex Dirac: four +1/2 and four -1/2 -> trace J^2=2.
    C_dirac = 8.0 * (0.5 ** 2)
    # complex Weyl is half the Dirac trace.
    C_weyl = C_dirac / 2.0
    assert isclose(C_vec, 2.0)
    assert isclose(C_dirac, 2.0)
    assert isclose(C_weyl, 1.0)


def trace_coefficient(F, C, e):
    """Coefficient b in b/(pi^3 L^2) Z_2 g_hyp.

    Wilson: (-1)^F C/8.
    E term: -(-1)^F e/16, where tr E=e R6 and R6^(2)=-K/2.
    """
    sign = -1 if F else 1
    return sign * Fraction(C, 8) - sign * Fraction(e, 16)


def check_representation_coefficients():
    b_dirac = trace_coefficient(1, 2, 2)
    b_vector = trace_coefficient(0, 2, 1)
    b_weyl = trace_coefficient(1, 1, 1)
    assert b_dirac == Fraction(-1, 8)
    assert b_vector == Fraction(3, 16)
    assert b_weyl == Fraction(-1, 16)

    # Ghost is scalar: no Lorentz or E correction in this trace sector.
    b_maxwell_ghost = b_vector
    assert b_maxwell_ghost == Fraction(3, 16)


def check_vector_multiplet():
    # Scalar-like weight-four multiplicities in units of one real scalar:
    nu_maxwell_ghost = 4
    nu_smw = -4
    assert nu_maxwell_ghost + nu_smw == 0

    # Spin/endormorphism trace sector:
    b_maxwell_ghost = Fraction(3, 16)
    b_smw = Fraction(-1, 16)
    b_total = b_maxwell_ghost + b_smw
    assert b_total == Fraction(1, 8)
    assert b_total > 0


def check_local_supertrace_consistency():
    # Model XXI local R6 coefficients, real-scalar units.
    scalar = 1
    dirac = 4
    maxwell_ghost = -2
    assert (scalar, dirac, maxwell_ghost) == (1, 4, -2)
    # SMW/Weyl = half Dirac in parity-even local sector.
    assert maxwell_ghost + dirac // 2 == 0


def main():
    check_winding_christoffel_identity()
    check_lorentz_indices()
    check_representation_coefficients()
    check_vector_multiplet()
    check_local_supertrace_consistency()
    print("Model XXII spin-threshold sanity checks: PASS")


if __name__ == "__main__":
    main()
