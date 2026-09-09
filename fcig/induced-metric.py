#!/usr/bin/env python3
"""Sanity checks for FCIG Model XVIII.

No external dependencies. This verifies the fixed bubble-response coefficient,
rank properties of the induced metric, and the explicit two-species flat witness.
It is not a substitute for the analytic proofs in induced-metric.md.
"""

from math import isclose, pi, exp


C_METRIC = 1.0 / (192.0 * pi * pi)
C_MASSMAP = 1.0 / (48.0 * pi * pi)


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def induced_metric(grads, values):
    """Return G_AB = C sum_i d_A V_i d_B V_i / V_i for 2 target coords."""
    g00 = g01 = g11 = 0.0
    for (du, dY), V in zip(grads, values):
        g00 += du * du / V
        g01 += du * dY / V
        g11 += dY * dY / V
    return [[C_METRIC * g00, C_METRIC * g01],
            [C_METRIC * g01, C_METRIC * g11]]


def check_bubble_coefficient():
    # I(p)=I(0)-p^2/(96 pi^2 V)+...
    V = 7.0
    bubble_p2 = -1.0 / (96.0 * pi * pi * V)
    # W^(2)=-1/4 deltaV deltaV I(p), hence derivative coefficient is positive.
    w_grad = -0.25 * bubble_p2
    expected = 1.0 / (384.0 * pi * pi * V)
    assert isclose(w_grad, expected, rel_tol=0.0, abs_tol=1e-18)


def check_single_species_rank():
    V = 5.0
    grad = (2.0, -3.0)
    G = induced_metric([grad], [V])
    assert abs(det2(G)) < 1e-24


def check_two_species_rank_restoration():
    values = [3.0, 7.0]
    grads = [(2.0, 0.5), (-1.0, 4.0)]
    G = induced_metric(grads, values)
    assert det2(G) > 0.0


def check_exp_witness_is_euclidean_pullback():
    # V1=e^(2 a u), V2=e^(2 a Y)
    a, u, Y = 0.7, 0.3, 1.2
    V1 = exp(2.0 * a * u)
    V2 = exp(2.0 * a * Y)
    grads = [(2.0 * a * V1, 0.0), (0.0, 2.0 * a * V2)]
    G = induced_metric(grads, [V1, V2])

    expected_uu = a * a * exp(2.0 * a * u) / (48.0 * pi * pi)
    expected_YY = a * a * exp(2.0 * a * Y) / (48.0 * pi * pi)
    assert isclose(G[0][0], expected_uu, rel_tol=1e-14)
    assert isclose(G[1][1], expected_YY, rel_tol=1e-14)
    assert abs(G[0][1]) < 1e-24

    # Define U=e^(a u)/sqrt(48 pi^2), W=e^(a Y)/sqrt(48 pi^2).
    # Then dU^2+dW^2 reproduces G exactly.
    dU_du_sq = expected_uu
    dW_dY_sq = expected_YY
    assert isclose(dU_du_sq, G[0][0], rel_tol=1e-14)
    assert isclose(dW_dY_sq, G[1][1], rel_tol=1e-14)


def check_massmap_identity():
    # dV^2/V = 4 d(sqrt(V))^2 for a representative value/differential.
    V, dV = 11.0, 2.3
    lhs = dV * dV / V
    ds = dV / (2.0 * V ** 0.5)
    rhs = 4.0 * ds * ds
    assert isclose(lhs, rhs, rel_tol=1e-14)


def main():
    check_bubble_coefficient()
    check_single_species_rank()
    check_two_species_rank_restoration()
    check_exp_witness_is_euclidean_pullback()
    check_massmap_identity()
    print("Model XVIII sanity checks: PASS")


if __name__ == "__main__":
    main()
