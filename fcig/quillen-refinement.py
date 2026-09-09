"""Sanity checks for FCIG Explicit Model V.

This script does NOT compute a determinant for a particular compact surface.
It checks algebraic coefficient relations and illustrates the different
length-spectrum dependence of a truncated Selberg product and a pointwise
Bergman-loop toy sum.

Dependency: Python standard library only.
"""

from __future__ import annotations

import cmath
import math


def mumford_coefficient(k: int) -> int:
    """c_k = 6 k^2 - 6 k + 1."""
    return 6 * k * k - 6 * k + 1


def state_rank(genus: int, k: int) -> int:
    """dim H^0(X, K_X^k) for genus >= 2, k >= 2."""
    if genus < 2 or k < 2:
        raise ValueError("require genus >= 2 and k >= 2")
    return (2 * k - 1) * (genus - 1)


def truncated_selberg_product(lengths: list[float], s: float, m_cutoff: int = 20) -> float:
    """Finite toy product prod_l prod_{m=0}^M (1-exp(-(s+m)l)).

    This mirrors the structure of the Selberg Euler product but is not a
    surface determinant unless a complete primitive length spectrum and the
    correct limiting/regularization procedure are supplied.
    """
    log_z = 0.0
    for ell in lengths:
        if ell <= 0:
            raise ValueError("lengths must be positive")
        for m in range(m_cutoff + 1):
            x = math.exp(-(s + m) * ell)
            log_z += math.log1p(-x)
    return math.exp(log_z)


def bergman_loop_toy(lengths: list[float], phases: list[float], k: int) -> float:
    """Finite toy version of the v0.4 pointwise loop weight."""
    if len(lengths) != len(phases):
        raise ValueError("lengths and phases must have equal length")
    return sum(
        math.cosh(ell / 2.0) ** (-2 * k) * math.cos(2 * math.pi * k * alpha)
        for ell, alpha in zip(lengths, phases)
    )


def run_demo() -> None:
    genus = 2
    print("FCIG Explicit Model V: determinant-metric sanity checks")
    print()

    print("k   rank H^0(K^k)   Mumford c_k   c_k / rank")
    for k in range(2, 7):
        rank = state_rank(genus, k)
        ck = mumford_coefficient(k)
        print(f"{k:<3d} {rank:<15d} {ck:<13d} {ck / rank:.6f}")

    # A finite length list used only to illustrate functional dependence.
    lengths = [1.15, 1.72, 2.31, 2.95]
    phases_a = [0.0, 0.12, 0.27, 0.41]
    phases_b = [0.18, 0.12, 0.27, 0.41]
    k = 3

    z0 = truncated_selberg_product(lengths, s=2.0, m_cutoff=24)
    berg_a = bergman_loop_toy(lengths, phases_a, k)
    berg_b = bergman_loop_toy(lengths, phases_b, k)

    perturbed = lengths.copy()
    perturbed[0] += 0.05
    z1 = truncated_selberg_product(perturbed, s=2.0, m_cutoff=24)

    print()
    print("Toy spectral/geodesic comparison")
    print(f"truncated Selberg product             : {z0:.15e}")
    print(f"after changing one closed length      : {z1:.15e}")
    print(f"relative product change               : {(z1 / z0 - 1):.6e}")
    print(f"pointwise Bergman toy (phase set A)   : {berg_a:.15e}")
    print(f"pointwise Bergman toy (phase set B)   : {berg_b:.15e}")
    print()
    print("The two objects use related geodesic data but different functionals.")
    print("Quillen convention in the note: h_Q = exp(T_hol) h_L2,")
    print("so F_Q - F_L2 = -ddbar(T_hol).")


if __name__ == "__main__":
    run_demo()
