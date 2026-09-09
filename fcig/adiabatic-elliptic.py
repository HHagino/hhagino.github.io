#!/usr/bin/env python3
"""Sanity checks for FCIG Model XX.

No external dependencies. The analytic proof is in adiabatic-elliptic.md.
This checker verifies:
  * the area-one elliptic shape matrix and Poincare trace identity,
  * intrinsic KK masses and the local proper-time coefficient,
  * Hess_g Q = Q g and |dQ|_g^2 = Q^2,
  * the convergent finite-threshold tensor,
  * its trace-free property and weight-four Eisenstein representation,
  * modular covariance under S: tau -> -1/tau.
"""

from math import isclose, pi


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


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


def q_data(m, n, u, Y):
    """Q, first derivatives, and ordinary second derivatives."""
    A = m * u - n
    Q = A * A / Y + m * m * Y
    Qu = 2.0 * m * A / Y
    QY = m * m - A * A / (Y * Y)
    Quu = 2.0 * m * m / Y
    QuY = -2.0 * m * A / (Y * Y)
    QYY = 2.0 * A * A / (Y ** 3)
    return Q, Qu, QY, Quu, QuY, QYY


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
        gi = Ginv(u, Y)
        quad = gi[0][0] * m * m + 2.0 * gi[0][1] * m * n + gi[1][1] * n * n
        matrix_value = 4.0 * pi * pi * quad / (L * L)
        assert isclose(direct, matrix_value, rel_tol=1e-13, abs_tol=1e-13)


def check_proper_time_coefficient():
    Lambda = 3.7
    coeff_R = -0.5 * (1.0 / 6.0) * (1.0 / (4.0 * pi) ** 3) * (Lambda ** 4 / 2.0)
    expected_R = -(Lambda ** 4) / (24.0 * (4.0 * pi) ** 3)
    assert isclose(coeff_R, expected_R, rel_tol=1e-14)
    coeff_tau = -0.5 * coeff_R
    expected_tau = (Lambda ** 4) / (48.0 * (4.0 * pi) ** 3)
    assert isclose(coeff_tau, expected_tau, rel_tol=1e-14)


def check_Q_hyperbolic_identities():
    u, Y = 0.29, 1.41
    for m, n in [(1, 0), (0, 1), (2, -1), (-3, 2)]:
        Q, Qu, QY, Quu, QuY, QYY = q_data(m, n, u, Y)
        # Hyperbolic Christoffels:
        # Gamma^Y_uu=1/Y, Gamma^u_uY=-1/Y, Gamma^Y_YY=-1/Y.
        Huu = Quu - QY / Y
        HuY = QuY + Qu / Y
        HYY = QYY + QY / Y
        expected_diag = Q / (Y * Y)
        assert isclose(Huu, expected_diag, rel_tol=1e-13, abs_tol=1e-13)
        assert abs(HuY) < 1e-13
        assert isclose(HYY, expected_diag, rel_tol=1e-13, abs_tol=1e-13)
        norm_sq = Y * Y * (Qu * Qu + QY * QY)
        assert isclose(norm_sq, Q * Q, rel_tol=1e-12, abs_tol=1e-12)


def finite_tensor_from_epstein(u, Y, cutoff=45):
    """Convergent form of T_fin=(1/pi^3)(Hess Z(2)-Z(2)g)."""
    guu = 1.0 / (Y * Y)
    pref = 3.0 / (pi ** 3)
    Tuu = TuY = TYY = 0.0
    for m in range(-cutoff, cutoff + 1):
        for n in range(-cutoff, cutoff + 1):
            if m == 0 and n == 0:
                continue
            Q, Qu, QY, *_ = q_data(m, n, u, Y)
            inv_q2 = 1.0 / (Q * Q)
            lu, lY = Qu / Q, QY / Q
            Tuu += inv_q2 * (2.0 * lu * lu - guu)
            TuY += inv_q2 * (2.0 * lu * lY)
            TYY += inv_q2 * (2.0 * lY * lY - guu)
    return [[pref * Tuu, pref * TuY], [pref * TuY, pref * TYY]]


def G4_lattice(u, Y, cutoff=45):
    tau = complex(u, Y)
    total = 0j
    for m in range(-cutoff, cutoff + 1):
        for n in range(-cutoff, cutoff + 1):
            if m == 0 and n == 0:
                continue
            total += 1.0 / (m * tau - n) ** 4
    return total


def finite_tensor_from_G4(u, Y, cutoff=45):
    e4 = G4_lattice(u, Y, cutoff)
    c = 3.0 / (pi ** 3)
    # -c Re[G4 (du+i dY)^2]
    a = -c * e4.real
    b = c * e4.imag
    return [[a, b], [b, -a]]


def check_finite_threshold_identity_and_trace():
    u, Y = 0.31, 1.23
    A = finite_tensor_from_epstein(u, Y)
    B = finite_tensor_from_G4(u, Y)
    for i in range(2):
        for j in range(2):
            assert isclose(A[i][j], B[i][j], rel_tol=2e-11, abs_tol=2e-11)
    hyp_trace = Y * Y * (A[0][0] + A[1][1])
    assert abs(hyp_trace) < 1e-11
    # Nonzero trace-free 2x2 symmetric tensor has determinant < 0.
    assert det2(A) < 0.0


def S_transform(u, Y):
    r2 = u * u + Y * Y
    return -u / r2, Y / r2


def S_jacobian(u, Y):
    r2 = u * u + Y * Y
    r4 = r2 * r2
    return [[(u * u - Y * Y) / r4, 2.0 * u * Y / r4],
            [-2.0 * u * Y / r4, (u * u - Y * Y) / r4]]


def check_modular_covariance_under_S():
    u, Y = 0.27, 1.31
    up, Yp = S_transform(u, Y)
    T = finite_tensor_from_G4(u, Y, cutoff=55)
    Tp = finite_tensor_from_G4(up, Yp, cutoff=55)
    J = S_jacobian(u, Y)
    pulled = matmul(matmul(transpose(J), Tp), J)
    for i in range(2):
        for j in range(2):
            assert isclose(T[i][j], pulled[i][j], rel_tol=3e-10, abs_tol=3e-10)


def main():
    check_shape_matrix()
    check_poincare_trace_identity()
    check_intrinsic_kk_mass()
    check_proper_time_coefficient()
    check_Q_hyperbolic_identities()
    check_finite_threshold_identity_and_trace()
    check_modular_covariance_under_S()
    print("Model XX local + finite-threshold sanity checks: PASS")


if __name__ == "__main__":
    main()
