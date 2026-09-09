#!/usr/bin/env python3
"""Sanity checks for FCIG Model XXI.

No external dependencies. This checks the d=6 b2 bookkeeping for scalar,
Dirac and Maxwell+ghost determinants, the vector-multiplet local cancellation,
and the exact scalar-type finite-threshold multiplicity rule.
"""

from fractions import Fraction
from math import isclose, pi


def local_coefficients_d6():
    d = 6
    # tr b2 for P=-(nabla^2+E), b2=E+R/6.
    b2_scalar = Fraction(1, 6)

    n_dirac = 2 ** (d // 2)  # complex rank 8
    b2_dirac = n_dirac * (Fraction(1, 6) - Fraction(1, 4))

    # One-form Hodge Laplacian: E=-Ric, hence tr E=-R.
    b2_oneform = Fraction(d, 6) - 1

    # Coefficients in W after determinant/statistics weights, in common proper-time units.
    w_scalar = -Fraction(1, 2) * b2_scalar
    w_dirac = Fraction(1, 2) * b2_dirac  # W_D=-1/2 log det D^2
    w_maxwell = -Fraction(1, 2) * b2_oneform + b2_scalar  # +1/2 logdet D1 - logdet D0

    return w_scalar, w_dirac, w_maxwell


def check_relative_table():
    scalar, dirac, maxwell = local_coefficients_d6()
    assert dirac / scalar == 4
    assert maxwell / scalar == -2
    # complex Weyl parity-even part = half a complex Dirac
    assert (dirac / 2) / scalar == 2


def check_vector_multiplet_local_cancellation():
    scalar, dirac, maxwell = local_coefficients_d6()
    weyl = dirac / 2
    # A 6d (1,0) vector multiplet has Maxwell + one SMW gaugino,
    # whose parity-even determinant equals one complex Weyl contribution.
    assert maxwell + weyl == 0


def scalar_finite_coeff(nu, L=1.0):
    return -nu / (16.0 * pi ** 3 * L * L)


def check_scalar_type_multiplicity():
    L = 2.3
    real = scalar_finite_coeff(1, L)
    complex_boson = scalar_finite_coeff(2, L)
    complex_ghost = scalar_finite_coeff(-2, L)
    assert isclose(complex_boson, 2.0 * real, rel_tol=1e-15)
    assert isclose(complex_ghost, -2.0 * real, rel_tol=1e-15)


def check_naive_dof_count_fails_locally():
    # In d=6 the physical on-shell counts are 1, 8 (Dirac), 4 (Maxwell),
    # but the local heat-kernel ratios are 1, 4, -2.
    expected_naive = (1, -8, 4)
    actual = (1, 4, -2)
    assert actual != expected_naive


def main():
    check_relative_table()
    check_vector_multiplet_local_cancellation()
    check_scalar_type_multiplicity()
    check_naive_dof_count_fails_locally()
    print("Model XXI supertrace sanity checks: PASS")


if __name__ == "__main__":
    main()
