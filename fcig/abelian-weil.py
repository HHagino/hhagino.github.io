"""Numerical checks for FCIG Explicit Model IIIc.

Checks the even-level finite Weil matrices for principally polarized abelian
varieties and independently compares the S and T_B transformations against
truncated theta sums on a non-diagonal genus-2 period matrix.

Dependency: numpy

The numerical checks are not proofs; the analytic derivations are in
`abelian-weil.md`.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def label_list(k: int, g: int) -> list[tuple[int, ...]]:
    return list(itertools.product(range(k), repeat=g))


def charge_conjugation(k: int, g: int) -> np.ndarray:
    labs = label_list(k, g)
    index = {lab: i for i, lab in enumerate(labs)}
    out = np.zeros((k**g, k**g), dtype=complex)
    for row, lab in enumerate(labs):
        neg = tuple((-np.asarray(lab, dtype=int)) % k)
        out[row, index[neg]] = 1.0
    return out


def weil_S(k: int, g: int) -> np.ndarray:
    """Normalized g-dimensional finite Fourier matrix."""
    labs = label_list(k, g)
    out = np.empty((k**g, k**g), dtype=complex)
    norm = k ** (-g / 2)
    for row, j in enumerate(labs):
        jv = np.asarray(j, dtype=int)
        for col, ell in enumerate(labs):
            lv = np.asarray(ell, dtype=int)
            out[row, col] = norm * np.exp(-2j * math.pi * (jv @ lv) / k)
    return out


def weil_T(k: int, B: np.ndarray) -> np.ndarray:
    """Upper symplectic shear for even k."""
    g = B.shape[0]
    if k % 2:
        raise ValueError("This fixed-characteristic formula is for even k")
    if not np.array_equal(B, B.T):
        raise ValueError("B must be symmetric")
    labs = label_list(k, g)
    phases = []
    for j in labs:
        jv = np.asarray(j, dtype=int)
        phases.append(np.exp(1j * math.pi * (jv @ B @ jv) / k))
    return np.diag(phases)


def weil_R(k: int, A: np.ndarray) -> np.ndarray:
    """Permutation matrix for R_A = diag(A, A^{-T})."""
    g = A.shape[0]
    det = round(float(np.linalg.det(A)))
    if abs(det) != 1:
        raise ValueError("A must be integral unimodular")
    labs = label_list(k, g)
    index = {lab: i for i, lab in enumerate(labs)}
    out = np.zeros((k**g, k**g), dtype=complex)
    for row, j in enumerate(labs):
        image = tuple((A.T @ np.asarray(j, dtype=int)) % k)
        out[row, index[image]] = 1.0
    return out


def determinant_T_closed(k: int, B: np.ndarray) -> complex:
    """Closed formula from Proposition 7.1 of abelian-weil.md."""
    g = B.shape[0]
    diagonal = ((k - 1) * (2 * k - 1) / 6.0) * np.trace(B)
    off_diag_sum = sum(B[a, b] for a in range(g) for b in range(a + 1, g))
    off_diagonal = ((k - 1) ** 2 / 2.0) * off_diag_sum
    exponent = math.pi * (k ** (g - 1)) * (diagonal + off_diagonal)
    return np.exp(1j * exponent)


def theta_vector(
    omega: np.ndarray,
    z: np.ndarray,
    k: int,
    cutoff: int = 4,
) -> np.ndarray:
    """Direct level-k theta vector in the conventions of abelian-weil.md."""
    g = omega.shape[0]
    values = []
    for j in label_list(k, g):
        jv = np.asarray(j, dtype=float)
        total = 0j
        for n in itertools.product(range(-cutoff, cutoff + 1), repeat=g):
            nv = np.asarray(n, dtype=float)
            q = nv + jv / k
            total += np.exp(
                1j * math.pi * k * (q @ omega @ q)
                + 2j * math.pi * k * (q @ z)
            )
        values.append(total)
    return np.asarray(values, dtype=complex)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def finite_matrix_checks() -> None:
    print("Finite Weil matrix checks")
    print("=" * 72)

    for g, k in [(1, 2), (2, 2), (2, 4), (3, 2)]:
        S = weil_S(k, g)
        T = weil_T(k, np.eye(g, dtype=int))
        C = charge_conjugation(k, g)
        I = np.eye(k**g, dtype=complex)

        unitary_S = max_abs(S.conj().T @ S - I)
        unitary_T = max_abs(T.conj().T @ T - I)
        s_squared = max_abs(S @ S - C)
        gauss = max_abs(
            np.linalg.matrix_power(S @ T, 3)
            - np.exp(1j * math.pi * g / 4) * C
        )

        print(
            f"g={g}, k={k}: "
            f"unitary(S)={unitary_S:.3e}, "
            f"unitary(T)={unitary_T:.3e}, "
            f"S^2-C={s_squared:.3e}, "
            f"(ST)^3-phase={gauss:.3e}"
        )

    g, k = 2, 2
    A = np.array([[1, 1], [0, 1]], dtype=int)
    B = np.array([[1, 0], [0, 0]], dtype=int)
    RA = weil_R(k, A)
    TB = weil_T(k, B)
    transformed_B = A @ B @ A.T
    covariance = max_abs(RA @ TB @ np.linalg.inv(RA) - weil_T(k, transformed_B))
    print(f"R_A T_B R_A^-1 covariance error: {covariance:.3e}")

    Bx = np.array([[0, 1], [1, 0]], dtype=int)
    direct_det = np.linalg.det(weil_T(2, Bx))
    closed_det = determinant_T_closed(2, Bx)
    print("\nExplicit flat-holonomy witness (g=2, k=2)")
    print(f"det U(T_Bx) direct : {direct_det.real:+.12f}{direct_det.imag:+.12f}i")
    print(f"det U(T_Bx) closed : {closed_det.real:+.12f}{closed_det.imag:+.12f}i")
    print("expected corrected-line multiplier: -1")


def direct_theta_checks() -> None:
    print("\nDirect theta transformation checks")
    print("=" * 72)

    omega = np.array(
        [
            [0.2 + 1.3j, 0.15 + 0.2j],
            [0.15 + 0.2j, -0.1 + 1.1j],
        ],
        dtype=complex,
    )
    z = np.array([0.13 + 0.2j, -0.07 + 0.1j], dtype=complex)
    k = 2
    g = 2
    cutoff = 4

    B = np.array([[1, 1], [1, 0]], dtype=int)
    lhs_T = theta_vector(omega + B, z, k, cutoff=cutoff)
    rhs_T = weil_T(k, B) @ theta_vector(omega, z, k, cutoff=cutoff)
    err_T = max_abs(lhs_T - rhs_T)

    omega_inv = np.linalg.inv(omega)
    lhs_S = theta_vector(-omega_inv, omega_inv @ z, k, cutoff=cutoff)
    prefactor = (
        np.sqrt(np.linalg.det(-1j * omega))
        * np.exp(1j * math.pi * k * (z @ omega_inv @ z))
    )
    rhs_S = prefactor * (weil_S(k, g) @ theta_vector(omega, z, k, cutoff=cutoff))
    err_S = max_abs(lhs_S - rhs_S)

    A = np.array([[1, 1], [0, 1]], dtype=int)
    lhs_R = theta_vector(A @ omega @ A.T, A @ z, k, cutoff=cutoff)
    rhs_R = weil_R(k, A) @ theta_vector(omega, z, k, cutoff=cutoff)
    err_R = max_abs(lhs_R - rhs_R)

    print("Omega =")
    print(omega)
    print(f"k={k}, theta cutoff={cutoff}")
    print(f"T_B direct transformation error : {err_T:.3e}")
    print(f"S direct transformation error   : {err_S:.3e}")
    print(f"R_A direct transformation error : {err_R:.3e}")


def run_demo() -> None:
    finite_matrix_checks()
    direct_theta_checks()


if __name__ == "__main__":
    run_demo()
