"""Sanity checks for FCIG Explicit Model VII.

Checks only degree bookkeeping and elementary U(1) holonomy identities.
It does not implement differential cohomology or a Bismut--Freed eta invariant.

Dependency: Python standard library only.
"""

from __future__ import annotations

import cmath
import math

TAU = 2.0 * math.pi


def pushforward_degree(input_degree: int, fiber_dimension: int) -> int:
    """Ordinary differential-cohomology fiber integration lowers degree by d."""
    if fiber_dimension < 0:
        raise ValueError("fiber dimension must be nonnegative")
    return input_degree - fiber_dimension


def coupled_response_degree(anomaly_degree: int, coupling_degree: int, fiber_dimension: int) -> int:
    """Degree of p_!(q^*A cup u)."""
    return anomaly_degree + coupling_degree - fiber_dimension


def holonomy(character_value_mod_1: float) -> complex:
    return cmath.exp(1j * TAU * character_value_mod_1)


def run_demo() -> None:
    print("FCIG Explicit Model VII: response/transgression sanity checks")
    print()

    anomaly_degree = 2

    print("Degree bookkeeping")
    print(f"loop transgression: Hhat^{anomaly_degree} -> Hhat^{pushforward_degree(2, 1)}")
    print(f"curve-fiber pushforward: Hhat^{anomaly_degree} -> Hhat^{pushforward_degree(2, 2)}")
    print(
        "degree-preserving coupled response with d=2, deg(u)=2: "
        f"Hhat^{coupled_response_degree(2, 2, 2)}"
    )
    print()

    assert pushforward_degree(2, 1) == 1
    assert pushforward_degree(2, 2) == 0
    assert coupled_response_degree(2, 1, 1) == 2
    assert coupled_response_degree(2, 2, 2) == 2

    print("Flat holonomy witness")
    h = 0.5
    z = holonomy(h)
    print(f"h = {h} mod Z -> holonomy = {z.real:+.6f}{z.imag:+.6f}i")
    assert abs(z + 1) < 1e-12
    print()

    print("Conclusion")
    print("- ordinary S^1 transgression of a degree-2 line class has degree 1;")
    print("- a positive-dimensional pushforward does not preserve degree 2 by itself;")
    print("- adding a degree-d coupling class restores degree 2 algebraically,")
    print("  but the geometry must supply that coupling independently.")


if __name__ == "__main__":
    run_demo()
