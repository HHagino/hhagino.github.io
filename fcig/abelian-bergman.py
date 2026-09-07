"""Numerical verifier for FCIG Explicit Model IIIb.

Checks the exact multidimensional Bergman lattice formula for a non-diagonal
genus-two period matrix by comparing:

1. direct evaluation from the orthonormal level-k theta basis;
2. the Poisson-resummed lattice Fourier formula.

It also estimates the normalized shortest-vector scale mu(Omega).

Dependency: numpy

The numerical check is not the proof. The analytic derivation is in
`abelian-bergman.md`.
"""

from __future__ import annotations

import cmath
import itertools
import math

import numpy as np


def validate_omega(omega: np.ndarray) -> None:
    if not np.allclose(omega, omega.T):
        raise ValueError("Omega must be symmetric")
    eig = np.linalg.eigvalsh(np.imag(omega))
    if np.min(eig) <= 0:
        raise ValueError("Im(Omega) must be positive definite")


def theta_section(
    z: np.ndarray,
    omega: np.ndarray,
    k: int,
    j: tuple[int, ...],
    cutoff: int = 5,
) -> complex:
    """Level-k theta section in the conventions of abelian-model.md."""
    g = len(j)
    jv = np.asarray(j, dtype=float)
    total = 0j
    for n_tuple in itertools.product(range(-cutoff, cutoff + 1), repeat=g):
        n = np.asarray(n_tuple, dtype=float)
        q = n + jv / k
        total += np.exp(
            1j * math.pi * k * (q @ omega @ q)
            + 2j * math.pi * k * (q @ z)
        )
    return complex(total)


def bergman_direct(
    omega: np.ndarray,
    k: int,
    x: np.ndarray,
    t: np.ndarray,
    cutoff: int = 5,
) -> float:
    """Direct Bergman density from the orthonormal theta basis."""
    g = len(x)
    y_matrix = np.imag(omega)
    z = x + omega @ t

    theta_sum = 0.0
    for j in itertools.product(range(k), repeat=g):
        s = theta_section(z, omega, k, j, cutoff=cutoff)
        theta_sum += abs(s) ** 2

    y = np.imag(z)
    metric_weight = math.exp(
        -2 * math.pi * k * (y @ np.linalg.solve(y_matrix, y))
    )
    normalization = math.sqrt(float(np.linalg.det(2 * k * y_matrix)))
    return normalization * metric_weight * theta_sum


def q_omega(
    omega: np.ndarray,
    p: np.ndarray,
    ell: np.ndarray,
) -> float:
    """Q_Omega(p,ell)=(ell-Omega p)^* Y^{-1} (ell-Omega p)."""
    y_matrix = np.imag(omega)
    v = ell - omega @ p
    return float(np.real(np.conjugate(v) @ np.linalg.solve(y_matrix, v)))


def bergman_poisson(
    omega: np.ndarray,
    k: int,
    x: np.ndarray,
    t: np.ndarray,
    cutoff: int = 3,
) -> complex:
    """Poisson-resummed exact formula truncated on [-cutoff,cutoff]^(2g)."""
    g = len(x)
    total = 0j

    for p_tuple in itertools.product(range(-cutoff, cutoff + 1), repeat=g):
        p = np.asarray(p_tuple, dtype=float)
        for ell_tuple in itertools.product(
            range(-cutoff, cutoff + 1), repeat=g
        ):
            ell = np.asarray(ell_tuple, dtype=float)
            amplitude = math.exp(-math.pi * k * q_omega(omega, p, ell) / 2)
            phase = cmath.exp(
                2j * math.pi * k * (p @ x + ell @ t)
                + 1j * math.pi * k * (p @ ell)
            )
            total += amplitude * phase

    return (k**g) * total


def normalized_systole(
    omega: np.ndarray,
    cutoff: int = 5,
) -> tuple[float, tuple[tuple[int, ...], tuple[int, ...]]]:
    """Finite-window estimate of mu(Omega)."""
    g = omega.shape[0]
    best = math.inf
    best_pair: tuple[tuple[int, ...], tuple[int, ...]] | None = None

    for p_tuple in itertools.product(range(-cutoff, cutoff + 1), repeat=g):
        for ell_tuple in itertools.product(
            range(-cutoff, cutoff + 1), repeat=g
        ):
            if all(v == 0 for v in p_tuple) and all(v == 0 for v in ell_tuple):
                continue
            p = np.asarray(p_tuple, dtype=float)
            ell = np.asarray(ell_tuple, dtype=float)
            value = q_omega(omega, p, ell)
            if value < best:
                best = value
                best_pair = (p_tuple, ell_tuple)

    assert best_pair is not None
    return best, best_pair


def run_demo() -> None:
    omega = np.array(
        [
            [0.2 + 1.3j, 0.15 + 0.2j],
            [0.15 + 0.2j, -0.1 + 1.1j],
        ],
        dtype=complex,
    )
    validate_omega(omega)

    x = np.array([0.13, 0.29], dtype=float)
    t = np.array([0.22, 0.37], dtype=float)

    theta_cutoff = 5
    poisson_cutoff = 3

    print("FCIG Explicit Model IIIb: non-diagonal genus-2 Bergman check")
    print("Omega =")
    print(omega)
    print(f"x={x}, t={t}")
    print(f"theta cutoff={theta_cutoff}, Poisson cutoff={poisson_cutoff}")
    print()
    print("k   direct               Poisson(real)        total error          B/k^g")
    print("-" * 86)

    for k in [1, 2, 3, 4]:
        direct = bergman_direct(omega, k, x, t, cutoff=theta_cutoff)
        poisson = bergman_poisson(omega, k, x, t, cutoff=poisson_cutoff)
        error = abs(direct - poisson.real) + abs(poisson.imag)
        print(
            f"{k:<3d} {direct: .12f}   {poisson.real: .12f}   "
            f"{error:.3e}   {direct/(k**2):.12f}"
        )

    mu, pair = normalized_systole(omega, cutoff=5)
    print()
    print(f"finite-window mu(Omega) estimate = {mu:.12f}")
    print(f"minimizing pair (p,ell) = {pair}")

    # Typical output with these cutoffs:
    # k=2,3,4 agree to ~1e-15; k=1 is limited by the Poisson cutoff.
    # Increase the cutoffs to tighten the k=1 comparison.


if __name__ == "__main__":
    run_demo()
