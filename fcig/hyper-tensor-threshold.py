#!/usr/bin/env python3
"""Sanity checks for FCIG Model XXIII hyper/tensor thresholds.

This checker verifies only algebra/combinatorics in the conventions documented in
hyper-tensor-threshold.md. It is not a substitute for the cited self-dual-field
partition-function literature.
"""

from fractions import Fraction
from math import comb

D = 6


def pform_data(p: int):
    """Return (rank, e_p, C_p, local_ratio, B_trace) for an ordinary p-form.

    Model-XXII normalization:
      C_p = 2 * binom(D-2,p-1)
      tr E = e_p R, e_p = binom(D-2,p-1)
      B_trace = (2 C_p - e_p)/16

    Model-XXI local convention gives local_ratio = rank - 6 e_p relative
    to one real minimal scalar.
    """
    rank = comb(D, p)
    e_p = comb(D - 2, p - 1) if 1 <= p <= D - 1 else 0
    C_p = 2 * e_p
    local_ratio = rank - 6 * e_p
    B_trace = Fraction(2 * C_p - e_p, 16)
    return rank, e_p, C_p, local_ratio, B_trace


# Ordinary form representations.
r0, e0, C0, local0, B0 = pform_data(0)
r1, e1, C1, local1, B1 = pform_data(1)
r2, e2, C2, local2, B2 = pform_data(2)

assert (r0, e0, C0, local0, B0) == (1, 0, 0, 1, Fraction(0))
assert (r1, e1, C1, local1, B1) == (6, 1, 2, 0, Fraction(3, 16))
assert (r2, e2, C2, local2, B2) == (15, 4, 8, -9, Fraction(3, 4))

# Non-chiral real 2-form gauge determinant:
# W = 1/2 log det D2 - log det D1 + 3/2 log det D0.
# Relative to one real scalar (1/2 log det D0), the signed multiplicities are
# +1 on 2-forms, -2 on 1-forms, +3 on scalars.
nu_nonch = r2 - 2 * r1 + 3 * r0
local_nonch = local2 - 2 * local1 + 3 * local0
A_nonch = -Fraction(nu_nonch, 16)
B_nonch = B2 - 2 * B1 + 3 * B0

assert nu_nonch == 6
assert local_nonch == -6
assert A_nonch == Fraction(-3, 8)
assert B_nonch == Fraction(3, 8)

# Restricted parity-even self-dual magnitude = half the non-chiral logarithmic response.
selfdual = (
    Fraction(local_nonch, 2),
    A_nonch / 2,
    B_nonch / 2,
)
assert selfdual == (Fraction(-3), Fraction(-3, 16), Fraction(3, 16))

# Model-XXII elementary entries.
scalar = (Fraction(1), Fraction(-1, 16), Fraction(0))
weyl_smw = (Fraction(2), Fraction(1, 4), Fraction(-1, 16))
vector_multiplet = (Fraction(0), Fraction(0), Fraction(1, 8))

# Hypermultiplet = 4 real scalars + SMW.
hyper = tuple(4 * scalar[i] + weyl_smw[i] for i in range(3))
assert hyper == (Fraction(6), Fraction(0), Fraction(-1, 16))

# Tensor multiplet = self-dual 2-form + one scalar + SMW.
tensor = tuple(selfdual[i] + scalar[i] + weyl_smw[i] for i in range(3))
assert tensor == (Fraction(0), Fraction(0), Fraction(1, 8))

# Vector and tensor finite thresholds coincide in this convention.
assert tensor == vector_multiplet

# All three supersymmetric multiplets have zero weight-four coefficient.
assert vector_multiplet[1] == hyper[1] == tensor[1] == 0

# General V/H/T finite trace coefficient.
def B_total(nv: int, nh: int, nt: int) -> Fraction:
    return nv * vector_multiplet[2] + nh * hyper[2] + nt * tensor[2]

for nv, nh, nt in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 4)]:
    expected = Fraction(2 * nv - nh + 2 * nt, 16)
    assert B_total(nv, nh, nt) == expected

print("Model XXIII checks passed")
print("nonchiral 2-form:", (local_nonch, A_nonch, B_nonch))
print("self-dual magnitude:", selfdual)
print("vector multiplet:", vector_multiplet)
print("hypermultiplet:", hyper)
print("tensor multiplet:", tensor)
