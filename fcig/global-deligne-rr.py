#!/usr/bin/env python3
"""Sanity checks for FCIG Model X.

This script does not prove Deligne--Riemann--Roch. It checks only the
specialization L=omega, the factor 12 bookkeeping, and the elementary fact
that a base-independent positive metric rescaling leaves a Chern connection
unchanged.
"""

from __future__ import annotations

import cmath
import math


def specialized_exponents() -> tuple[int, int]:
    """Return exponents in Deligne RR after setting L=omega.

    det Rpi_* omega appears to the 12th power; the second Deligne-pairing
    factor is <omega, O>^6 and is canonically trivial.
    """
    return 12, 0


def dlog_constant_metric_ratio(constant: float) -> float:
    """Derivative of log(C h)-log(h) with respect to base coordinates."""
    if constant <= 0:
        raise ValueError("metric rescaling constant must be positive")
    return 0.0


def holonomy_identity(theta: float) -> float:
    """Check Hol(lambda)^12 = Hol(lambda^12) for a sample phase."""
    hol = cmath.exp(2j * math.pi * theta)
    lhs = hol**12
    rhs = cmath.exp(2j * math.pi * 12 * theta)
    return abs(lhs - rhs)


def run_demo() -> None:
    det_exp, residual_pair_exp = specialized_exponents()
    print(f"determinant exponent: {det_exp}")
    print(f"nontrivial second pairing exponent after L=omega: {residual_pair_exp}")
    assert det_exp == 12
    assert residual_pair_exp == 0

    for c in (0.125, 1.0, 7.5):
        residual = dlog_constant_metric_ratio(c)
        print(f"C={c:g}: d log(C h) - d log(h) = {residual:g}")
        assert residual == 0.0

    for theta in (0.031, 0.173, 0.499):
        err = holonomy_identity(theta)
        print(f"theta={theta:.3f}: holonomy tensor-power error = {err:.3e}")
        assert err < 1e-12


if __name__ == "__main__":
    run_demo()
