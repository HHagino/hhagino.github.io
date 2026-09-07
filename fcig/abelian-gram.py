"""Numerical checks for FCIG Explicit Model III.

Checks the exact Gram-matrix prediction

    <s_j, s_m> = delta_{j,m} det(2 k Im(Omega))^(-1/2)

for a small principally polarized abelian variety using truncated theta sums
and midpoint integration over the normalized fundamental domain.

Dependency: numpy

The numerical check is not the proof; the analytic Gaussian proof is in
`abelian-model.md`.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def theta_section(
    z: np.ndarray,
    omega: np.ndarray,
    k: int,
    j: tuple[int, ...],
    cutoff: int = 2,
) -> complex:
    """Level-k theta section in the conventions of abelian-model.md."""
    g = len(j)
    jv = np.asarray(j, dtype=float)
    total = 0j

    for n_tuple in itertools.product(range(-cutoff, cutoff + 1), repeat=g):
        n = np.asarray(n_tuple, dtype=float)
        q = n + jv / k
        exponent = (
            1j * math.pi * k * (q @ omega @ q)
            + 2j * math.pi * k * (q @ z)
        )
        total += np.exp(exponent)

    return complex(total)


def hermitian_product(
    sj: complex,
    sm: complex,
    z: np.ndarray,
    omega: np.ndarray,
    k: int,
) -> complex:
    """Pointwise Hermitian product with the Gaussian metric."""
    y_matrix = np.imag(omega)
    y = np.imag(z)
    weight = math.exp(-2 * math.pi * k * (y @ np.linalg.solve(y_matrix, y)))
    return sj * np.conjugate(sm) * weight


def midpoint_inner_product(
    omega: np.ndarray,
    k: int,
    j: tuple[int, ...],
    m: tuple[int, ...],
    grid: int = 7,
    cutoff: int = 2,
) -> complex:
    """Midpoint integration over x,t in [0,1)^g with normalized volume."""
    g = len(j)
    points = (np.arange(grid, dtype=float) + 0.5) / grid
    total = 0j

    for x_tuple in itertools.product(points, repeat=g):
        x = np.asarray(x_tuple, dtype=float)
        for t_tuple in itertools.product(points, repeat=g):
            t = np.asarray(t_tuple, dtype=float)
            z = x + omega @ t
            sj = theta_section(z, omega, k, j, cutoff=cutoff)
            sm = theta_section(z, omega, k, m, cutoff=cutoff)
            total += hermitian_product(sj, sm, z, omega, k)

    return total / (grid ** (2 * g))


def predicted_norm(omega: np.ndarray, k: int) -> float:
    """det(2 k Im Omega)^(-1/2)."""
    y_matrix = np.imag(omega)
    return 1.0 / math.sqrt(float(np.linalg.det(2 * k * y_matrix)))


def validate_omega(omega: np.ndarray) -> None:
    if not np.allclose(omega, omega.T):
        raise ValueError("Omega must be symmetric")
    eigenvalues = np.linalg.eigvalsh(np.imag(omega))
    if np.min(eigenvalues) <= 0:
        raise ValueError("Im(Omega) must be positive definite")


def run_demo() -> None:
    # Non-diagonal genus-2 period matrix.
    omega = np.array(
        [
            [1.2j, 0.15 + 0.2j],
            [0.15 + 0.2j, 0.9j],
        ],
        dtype=complex,
    )
    validate_omega(omega)

    k = 2
    predicted = predicted_norm(omega, k)
    diagonal = midpoint_inner_product(omega, k, (0, 0), (0, 0))
    off_diagonal = midpoint_inner_product(omega, k, (0, 0), (1, 0))

    print("FCIG Explicit Model III: genus-2 Gram check")
    print("Omega =")
    print(omega)
    print(f"k = {k}")
    print(f"predicted diagonal norm : {predicted:.15f}")
    print(f"numerical diagonal norm : {diagonal.real:.15f}")
    print(f"diagonal abs error      : {abs(diagonal - predicted):.3e}")
    print(f"off-diagonal magnitude  : {abs(off_diagonal):.3e}")

    # With grid=7 and cutoff=2 this example typically reaches near
    # floating-point precision for the diagonal norm and orthogonality.


if __name__ == "__main__":
    run_demo()
