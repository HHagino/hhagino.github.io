"""Sanity checks for FCIG Explicit Model VI.

This script illustrates elementary degree-two differential-character bookkeeping:
- a flat character can have zero curvature and nontrivial holonomy;
- curvature controls the holonomy of a boundary;
- tensor products add curvature and holonomy phases.

It is not a differential-cohomology implementation and does not compute a
Bismut--Freed eta invariant.

Dependency: Python standard library only.
"""

from __future__ import annotations

import cmath
import math

TAU = 2.0 * math.pi


def u1_from_character(value_mod_1: float) -> complex:
    """exp(2 pi i h) for h in R/Z."""
    return cmath.exp(1j * TAU * value_mod_1)


def character_from_angle(angle: float) -> float:
    """Convert a U(1) phase angle in radians to R/Z."""
    return (angle / TAU) % 1.0


def boundary_holonomy_from_flux(integral_curvature_over_2pi_i: float) -> complex:
    """Hol(boundary C) = exp(2 pi i * integral_C F/(2 pi i))."""
    return u1_from_character(integral_curvature_over_2pi_i)


def tensor_character(h1: float, h2: float) -> float:
    """Differential-character values add under tensor product."""
    return (h1 + h2) % 1.0


def run_demo() -> None:
    print("FCIG Explicit Model VI: differential-character sanity checks")
    print()

    # Flat example: the Model IIIc witness chi=-1 corresponds to 1/2 mod Z.
    h_flat = 0.5
    hol_flat = u1_from_character(h_flat)
    print("Flat character example")
    print(f"curvature class                         : 0")
    print(f"character value h(gamma)                : {h_flat:.6f} mod Z")
    print(f"holonomy exp(2 pi i h)                  : {hol_flat.real:+.6f}{hol_flat.imag:+.6f}i")
    print()

    # Curved boundary compatibility. Integral flux need not be integral for a
    # chain with boundary; only closed 2-cycles impose the integrality condition.
    flux = 0.375
    hol_boundary = boundary_holonomy_from_flux(flux)
    print("Boundary compatibility example")
    print(f"integral_C F/(2 pi i)                   : {flux:.6f}")
    print(f"Hol(boundary C)                         : {hol_boundary.real:+.6f}{hol_boundary.imag:+.6f}i")
    print()

    # On a closed 2-cycle an integral flux gives trivial boundary phase, as it must.
    closed_flux = 3.0
    closed_phase = boundary_holonomy_from_flux(closed_flux)
    print("Integral-period check")
    print(f"closed-cycle normalized flux            : {closed_flux:.1f}")
    print(f"exp(2 pi i * flux)                      : {closed_phase.real:+.6f}{closed_phase.imag:+.6f}i")
    print()

    # Tensor product: add characters, multiply holonomies.
    h1, h2 = 0.20, 0.35
    h12 = tensor_character(h1, h2)
    hol_product = u1_from_character(h1) * u1_from_character(h2)
    hol_sum = u1_from_character(h12)
    print("Tensor-product check")
    print(f"h1 + h2 mod Z                          : {h12:.6f}")
    print(f"|Hol1*Hol2 - Hol(h1+h2)|               : {abs(hol_product - hol_sum):.3e}")


if __name__ == "__main__":
    run_demo()
