"""Numerical verifier for FCIG Explicit Model II.

Checks:
- even-k T transformation,
- S transformation by the finite Fourier matrix,
- projective relation (U_S U_T)^3 = exp(pi i/4) C,
- determinant formulas for U_S and U_T,
- odd-k T exchange of theta-characteristic sectors,
- odd-k closure under T^2.

No external dependencies are required.
"""

from __future__ import annotations

import cmath
import math


def theta_level(
    k: int,
    j: int,
    z: complex,
    tau: complex,
    cutoff: int = 60,
    sector: int = 0,
) -> complex:
    """Level-k theta state.

    sector=0 is the original theta characteristic.
    sector=1 inserts (-1)^n and is the companion odd-k T sector.
    """
    total = 0j
    for n in range(-cutoff, cutoff + 1):
        a = n + j / k
        sign = -1 if (sector and n % 2) else 1
        total += sign * cmath.exp(
            math.pi * 1j * k * tau * a * a
            + 2 * math.pi * 1j * k * a * z
        )
    return total


def eye(n: int) -> list[list[complex]]:
    return [[1 + 0j if i == j else 0j for j in range(n)] for i in range(n)]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][r] * b[r][j] for r in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def matpow(a: list[list[complex]], n: int) -> list[list[complex]]:
    result = eye(len(a))
    base = a
    while n:
        if n & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n //= 2
    return result


def matvec(a: list[list[complex]], v: list[complex]) -> list[complex]:
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def max_matrix_error(a: list[list[complex]], b: list[list[complex]]) -> float:
    return max(
        abs(a[i][j] - b[i][j])
        for i in range(len(a))
        for j in range(len(a[0]))
    )


def determinant(a: list[list[complex]]) -> complex:
    """Small dense determinant by Gaussian elimination."""
    m = [row[:] for row in a]
    n = len(m)
    det = 1 + 0j
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(m[r][i]))
        if abs(m[pivot][i]) < 1e-14:
            return 0j
        if pivot != i:
            m[i], m[pivot] = m[pivot], m[i]
            det *= -1
        piv = m[i][i]
        det *= piv
        for r in range(i + 1, n):
            factor = m[r][i] / piv
            for c in range(i + 1, n):
                m[r][c] -= factor * m[i][c]
    return det


def weil_matrices(k: int) -> tuple[list[list[complex]], list[list[complex]]]:
    s = [
        [cmath.exp(-2j * math.pi * j * ell / k) / math.sqrt(k) for ell in range(k)]
        for j in range(k)
    ]
    t = [[0j for _ in range(k)] for _ in range(k)]
    for j in range(k):
        t[j][j] = cmath.exp(1j * math.pi * j * j / k)
    return s, t


def check_even_level(k: int, z: complex, tau: complex) -> None:
    if k % 2:
        raise ValueError("even k required")

    s, t = weil_matrices(k)
    v = [theta_level(k, j, z, tau) for j in range(k)]

    # T
    actual_t = [theta_level(k, j, z, tau + 1) for j in range(k)]
    predicted_t = matvec(t, v)
    err_t = max(abs(a - b) for a, b in zip(actual_t, predicted_t))

    # S
    actual_s = [theta_level(k, j, z / tau, -1 / tau) for j in range(k)]
    scalar = cmath.sqrt(-1j * tau) * cmath.exp(1j * math.pi * k * z * z / tau)
    predicted_s = [scalar * value for value in matvec(s, v)]
    err_s = max(abs(a - b) for a, b in zip(actual_s, predicted_s))

    # Projective modular relation
    c = matmul(s, s)
    lhs = matpow(matmul(s, t), 3)
    phase = cmath.exp(1j * math.pi / 4)
    rhs = [[phase * c[i][j] for j in range(k)] for i in range(k)]
    err_relation = max_matrix_error(lhs, rhs)

    # Determinants
    det_s = determinant(s)
    det_t = determinant(t)
    det_s_formula = cmath.exp(-1j * math.pi * (k - 1) * (3 * k - 2) / 4)
    det_t_formula = cmath.exp(1j * math.pi * (k - 1) * (2 * k - 1) / 6)

    print(f"even k={k}")
    print(f"  T error                 {err_t:.3e}")
    print(f"  S error                 {err_s:.3e}")
    print(f"  projective relation     {err_relation:.3e}")
    print(f"  det(U_S) formula error  {abs(det_s-det_s_formula):.3e}")
    print(f"  det(U_T) formula error  {abs(det_t-det_t_formula):.3e}")


def check_odd_level(k: int, z: complex, tau: complex) -> None:
    if not k % 2:
        raise ValueError("odd k required")

    plus = [theta_level(k, j, z, tau, sector=0) for j in range(k)]
    minus = [theta_level(k, j, z, tau, sector=1) for j in range(k)]

    actual_t = [theta_level(k, j, z, tau + 1, sector=0) for j in range(k)]
    predicted_t = [
        cmath.exp(1j * math.pi * j * j / k) * minus[j]
        for j in range(k)
    ]
    err_swap = max(abs(a - b) for a, b in zip(actual_t, predicted_t))

    actual_t2 = [theta_level(k, j, z, tau + 2, sector=0) for j in range(k)]
    predicted_t2 = [
        cmath.exp(2j * math.pi * j * j / k) * plus[j]
        for j in range(k)
    ]
    err_t2 = max(abs(a - b) for a, b in zip(actual_t2, predicted_t2))

    print(f"odd k={k}")
    print(f"  T sector-swap error     {err_swap:.3e}")
    print(f"  T^2 closure error       {err_t2:.3e}")


def run_demo() -> None:
    tau = 0.3 + 1.2j
    z = 0.17 + 0.11j

    print("FCIG Explicit Model II numerical checks\n")
    for k in (2, 4, 6, 8):
        check_even_level(k, z, tau)
        print()

    for k in (1, 3, 5, 7):
        check_odd_level(k, z, tau)
        print()


if __name__ == "__main__":
    run_demo()
