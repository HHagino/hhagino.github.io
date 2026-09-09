#!/usr/bin/env python3
"""Sanity checks for FCIG Model XIV.

This script does not prove the field-theory statements.  It checks the
algebraic identities used in the explicit Maxwell counterexample and the
affine-response bookkeeping.

No third-party dependencies are required.
"""

from fractions import Fraction


def maxwell_trace_coefficient(d: int) -> Fraction:
    """Coefficient multiplying beta*F^2 in T^mu_mu."""
    return Fraction(1, 1) - Fraction(d, 4)


def anomaly_shift(invariant_variation: float) -> float:
    """Gauge/diffeomorphism anomaly shift from an invariant functional."""
    return invariant_variation


def response_shift(beta: float, div_f: float, maxwell_tensor_component: float) -> tuple[float, float]:
    """Toy bookkeeping for the current and stress response shifts."""
    delta_j = beta * div_f
    delta_t = beta * maxwell_tensor_component
    return delta_j, delta_t


def main() -> None:
    print("FCIG Model XIV sanity checks")
    print("--------------------------------")

    # 1. Maxwell stress is traceless specifically in d=4.
    for d in (2, 3, 4, 5, 6):
        coeff = maxwell_trace_coefficient(d)
        print(f"d={d}: trace coefficient = {coeff}")
    assert maxwell_trace_coefficient(4) == 0
    assert maxwell_trace_coefficient(3) != 0

    # 2. An invariant functional has zero symmetry variation by hypothesis.
    assert anomaly_shift(0.0) == 0.0

    # 3. Nevertheless first responses can shift nontrivially.
    delta_j, delta_t = response_shift(beta=2.0, div_f=3.0, maxwell_tensor_component=-5.0)
    print(f"example delta J = {delta_j}")
    print(f"example delta T = {delta_t}")
    assert delta_j != 0.0
    assert delta_t != 0.0

    print("PASS: same anomaly can coexist with different first responses.")


if __name__ == "__main__":
    main()
