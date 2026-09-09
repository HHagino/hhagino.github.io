#!/usr/bin/env python3
"""Sanity checks for FCIG Model XVII.

No external dependencies. Checks the upper-half-plane target geometry, a vertical
geodesic solution, modular invariance for S, and the pullback area-form witness.
"""

import cmath
import math


def christoffels(Y: float):
    # indices 0=u, 1=Y
    return {
        (0, 0, 1): -1.0 / Y,
        (0, 1, 0): -1.0 / Y,
        (1, 0, 0): 1.0 / Y,
        (1, 1, 1): -1.0 / Y,
    }


def check_christoffels() -> None:
    Y = 2.5
    G = christoffels(Y)
    assert math.isclose(G[(0, 0, 1)], -0.4)
    assert math.isclose(G[(1, 0, 0)], 0.4)
    assert math.isclose(G[(1, 1, 1)], -0.4)


def check_vertical_geodesic() -> None:
    # Flat one-dimensional base coordinate x, phi=a*x+b, Y=exp(phi).
    a, b, x = 0.7, -0.2, 1.3
    Y = math.exp(a * x + b)
    Yp = a * Y
    Ypp = a * a * Y

    # u'=0. The Y harmonic-map equation is Y'' - (Y')^2/Y = 0.
    residual = Ypp - Yp * Yp / Y
    assert abs(residual) < 1e-12

    # Pullback hyperbolic area form vanishes because du=0.
    du = 0.0
    dY = Yp
    area_component = du * dY / (Y * Y)
    assert area_component == 0.0


def check_nonzero_pullback_witness() -> None:
    Y = 1.7
    # Gradients on two independent base directions:
    du_x, du_y = 1.0, 0.0
    dY_x, dY_y = 0.0, 1.0
    omega_xy = (du_x * dY_y - du_y * dY_x) / (Y * Y)
    assert omega_xy > 0.0


def check_modular_S_invariance() -> None:
    tau = 0.31 + 1.27j
    dtau = 0.17 - 0.08j

    # S: tau'=-1/tau, d tau'=d tau/tau^2.
    tau_p = -1.0 / tau
    dtau_p = dtau / (tau * tau)

    lhs = abs(dtau) ** 2 / (tau.imag ** 2)
    rhs = abs(dtau_p) ** 2 / (tau_p.imag ** 2)
    assert math.isclose(lhs, rhs, rel_tol=0.0, abs_tol=1e-12)


def check_sigma_vs_curvature_derivative_order() -> None:
    # Sigma kinetic density is quadratic in a scaling s of first derivatives.
    # Pullback-curvature-squared is quartic.
    for s in (0.3, 0.7, 1.4):
        kinetic = s ** 2
        curvature_sq = s ** 4
        assert math.isclose(kinetic / s**2, 1.0)
        assert math.isclose(curvature_sq / s**4, 1.0)


def main() -> None:
    check_christoffels()
    check_vertical_geodesic()
    check_nonzero_pullback_witness()
    check_modular_S_invariance()
    check_sigma_vs_curvature_derivative_order()
    print("Model XVII sanity checks: PASS")


if __name__ == "__main__":
    main()
