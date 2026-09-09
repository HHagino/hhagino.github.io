#!/usr/bin/env python3
"""Symbolic sanity checks for FCIG Model IX.

This script checks only the formal degree-two GRR coefficient and the
resulting factor 12. It does not prove GRR or the Quillen local-index theorem.
"""

from fractions import Fraction


def multiply_truncated(a: list[Fraction], b: list[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= degree:
                out[i + j] += ai * bj
    return out


def run_demo() -> None:
    # exp(x) = 1 + x + x^2/2 + O(x^3)
    ch_omega = [Fraction(1), Fraction(1), Fraction(1, 2)]

    # Td(omega^{-1}) = 1 - x/2 + x^2/12 + O(x^3)
    td_vertical = [Fraction(1), Fraction(-1, 2), Fraction(1, 12)]

    product = multiply_truncated(ch_omega, td_vertical, 2)
    expected = [Fraction(1), Fraction(1, 2), Fraction(1, 12)]

    print("ch(omega) Td(T_pi) coefficients through x^2:")
    print(product)
    assert product == expected

    grr_coefficient = product[2]
    factor = 1 / grr_coefficient
    print(f"degree-four coefficient = {grr_coefficient}")
    print(f"kappa_1 / c1(lambda) factor = {factor}")
    assert factor == 12

    # Differential-character consequence:
    # I(kappa_hat - 12 lambda_hat_Q) = 0
    # R(kappa_hat - 12 lambda_hat_Q) = 0
    characteristic_residual = Fraction(1) - 12 * grr_coefficient
    curvature_residual = Fraction(1) - 12 * grr_coefficient
    print(f"characteristic residual coefficient = {characteristic_residual}")
    print(f"curvature residual coefficient = {curvature_residual}")
    assert characteristic_residual == 0
    assert curvature_residual == 0


if __name__ == "__main__":
    run_demo()
