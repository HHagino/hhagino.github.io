#!/usr/bin/env python3
"""Sanity checks for FCIG Model XI.

This script is not a proof.  It provides small matrix witnesses for the two
algebraic facts used in the note:

1. traceless nonabelian curvature can vary while determinant/trace curvature
   is held fixed;
2. curvature induced from a single U(1) generator through a fixed homomorphism
   is confined to one abelian direction.

No third-party dependencies are required.
"""

from __future__ import annotations

from typing import Iterable

Matrix = tuple[tuple[complex, ...], ...]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(len(a)))
        for i in range(len(a))
    )


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * x for x in row) for row in a)


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return matsub(matmul(a, b), matmul(b, a))


def frobenius_norm(a: Matrix) -> float:
    return sum(abs(x) ** 2 for row in a for x in row) ** 0.5


def close(a: complex, b: complex, tol: float = 1e-12) -> bool:
    return abs(a - b) < tol


def pauli_witness() -> tuple[Matrix, Matrix, Matrix]:
    """Return anti-Hermitian i*sigma_x, i*sigma_y and identity generator."""
    ix: Matrix = ((0j, 1j), (1j, 0j))
    iy: Matrix = ((0j, 1 + 0j), (-1 + 0j, 0j))
    identity_i: Matrix = ((1j, 0j), (0j, 1j))
    return ix, iy, identity_i


def determinant_trace_witness() -> None:
    x, y, identity_i = pauli_witness()

    # Two curvature components with the same central trace data but with an
    # additional noncommuting SU(2) sector.
    central_12 = scale(0.35, identity_i)
    central_34 = scale(-0.20, identity_i)

    full_12 = tuple(
        tuple(central_12[i][j] + x[i][j] for j in range(2))
        for i in range(2)
    )
    full_34 = tuple(
        tuple(central_34[i][j] + y[i][j] for j in range(2))
        for i in range(2)
    )

    assert close(trace(full_12), trace(central_12))
    assert close(trace(full_34), trace(central_34))

    central_comm = commutator(central_12, central_34)
    full_comm = commutator(full_12, full_34)

    assert frobenius_norm(central_comm) < 1e-12
    assert frobenius_norm(full_comm) > 1e-6

    print("determinant trace preserved: PASS")
    print(f"  tr(F12) = {trace(full_12)}")
    print(f"  tr(F34) = {trace(full_34)}")
    print(f"  ||[central12, central34]|| = {frobenius_norm(central_comm):.3e}")
    print(f"  ||[full12, full34]||       = {frobenius_norm(full_comm):.3e}")


def fixed_u1_image_witness() -> None:
    _, _, generator = pauli_witness()

    # Any two curvature values induced from one fixed U(1) Lie-algebra
    # generator are scalar multiples of the same matrix and therefore commute.
    f1 = scale(1.7, generator)
    f2 = scale(-0.4, generator)
    c = commutator(f1, f2)
    assert frobenius_norm(c) < 1e-12

    print("fixed U(1) image is abelian: PASS")
    print(f"  ||[phi_*(F1), phi_*(F2)]|| = {frobenius_norm(c):.3e}")


def dimension_table(dimensions: Iterable[int] = range(1, 6)) -> None:
    print("\nstructure-group dimensions")
    print(" n | dim U(n) | dim SU(n) | determinant dimension")
    for n in dimensions:
        print(f" {n} | {n*n:8d} | {n*n-1:9d} | {1:21d}")


def main() -> None:
    determinant_trace_witness()
    fixed_u1_image_witness()
    dimension_table()


if __name__ == "__main__":
    main()
