"""Numerical checks for the FCIG elliptic-curve model.

This script compares

1. the direct level-k theta-function formula for the Bergman density, and
2. the Poisson-resummed lattice Fourier formula

for E_tau = C/(Z + tau Z).

No external dependencies are required.
"""

from __future__ import annotations

import cmath
import math


def theta_char(a: float, z: complex, tau: complex, cutoff: int = 40) -> complex:
    """Theta with characteristic [a,0]."""
    total = 0j
    for n in range(-cutoff, cutoff + 1):
        total += cmath.exp(
            math.pi * 1j * tau * (n + a) ** 2
            + 2 * math.pi * 1j * (n + a) * z
        )
    return total


def bergman_direct(k: int, tau: complex, x: float, t: float, cutoff: int = 40) -> float:
    """Direct theta-basis evaluation of B_k at z = x + tau t."""
    if k <= 0:
        raise ValueError("k must be positive")
    Y = tau.imag
    if Y <= 0:
        raise ValueError("tau must lie in the upper half-plane")

    z = x + tau * t
    theta_sum = 0.0
    for j in range(k):
        s_j = theta_char(j / k, k * z, k * tau, cutoff=cutoff)
        theta_sum += abs(s_j) ** 2

    metric_weight = math.exp(-2 * math.pi * k * (z.imag**2) / Y)
    normalization = math.sqrt(2 * k * Y)
    return normalization * metric_weight * theta_sum


def bergman_poisson(k: int, tau: complex, x: float, t: float, cutoff: int = 8) -> complex:
    """Poisson-resummed exact Fourier formula, truncated symmetrically."""
    if k <= 0:
        raise ValueError("k must be positive")
    Y = tau.imag
    if Y <= 0:
        raise ValueError("tau must lie in the upper half-plane")

    total = 0j
    for p in range(-cutoff, cutoff + 1):
        for ell in range(-cutoff, cutoff + 1):
            gaussian = math.exp(
                -math.pi * k * abs(ell - p * tau) ** 2 / (2 * Y)
            )
            phase = cmath.exp(
                2 * math.pi * 1j * k * (p * x + ell * t)
                + math.pi * 1j * k * p * ell
            )
            total += gaussian * phase
    return k * total


def normalized_systole(tau: complex, cutoff: int = 12) -> float:
    """Approximate mu(tau)=min |ell-p tau|^2/Im(tau) over nonzero lattice vectors."""
    Y = tau.imag
    best = math.inf
    for p in range(-cutoff, cutoff + 1):
        for ell in range(-cutoff, cutoff + 1):
            if p == 0 and ell == 0:
                continue
            best = min(best, abs(ell - p * tau) ** 2 / Y)
    return best


def run_demo() -> None:
    test_data = [
        (1, 1j, 0.0, 0.0),
        (1, 1j, 0.5, 0.5),  # theta zero for the standard degree-one section
        (2, 1j, 0.2, 0.4),
        (3, 0.3 + 1.2j, 0.2, 0.4),
        (8, 0.3 + 1.2j, 0.2, 0.4),
    ]

    print("k   tau          (x,t)        direct              Poisson             abs error")
    print("-" * 93)
    for k, tau, x, t in test_data:
        direct = bergman_direct(k, tau, x, t)
        poisson = bergman_poisson(k, tau, x, t)
        err = abs(direct - poisson.real) + abs(poisson.imag)
        print(
            f"{k:<3d} {tau!s:<12} ({x:.2f},{t:.2f})  "
            f"{direct: .12f}   {poisson.real: .12f}   {err:.3e}"
        )

    print("\nNormalized systoles:")
    for tau in [1j, 0.3 + 1.2j, 5j, 10j]:
        mu = normalized_systole(tau)
        print(f"tau={tau!s:<10} mu≈{mu:.8f}")

    print("\nLarge-k approach to the local flat asymptotic B_k ~ k:")
    tau = 0.3 + 1.2j
    x, t = 0.2, 0.4
    for k in [1, 2, 4, 8, 16]:
        value = bergman_direct(k, tau, x, t)
        print(f"k={k:2d}  B_k/k={value/k:.12f}")


if __name__ == "__main__":
    run_demo()
