#!/usr/bin/env python3
"""Exact arithmetic checks for FCIG Model XXIV.

No floating point arithmetic is used.  The checker verifies the anomaly-map
rank/determinant, threshold/anomaly counterexamples, kernel intersections,
and the reconstruction of K from the three independent anomaly coefficients.
"""

from fractions import Fraction as F


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def dot(row, x):
    return sum(a * b for a, b in zip(row, x))


R = (-1, 0, 1)
P1 = (-7, 7, 23)
P2 = (4, -4, -116)
K = (2, -1, 2)
M = (R, P1, P2)

# Gate 1: anomaly map is invertible.
assert det3(M) == 720

# Gate 2: K=0 does not imply anomaly cancellation.
x = (1, 2, 0)
assert dot(K, x) == 0
assert (dot(R, x), dot(P1, x), dot(P2, x)) == (-1, 7, -4)

# Gate 3: pure gravitational one-loop cancellation does not imply K=0.
x = (1, 1, 0)
assert dot(P1, x) == 0
assert dot(P2, x) == 0
assert dot(K, x) == 1
assert dot(R, x) == -1

# Gate 4: matter-only p2 condition is H-V+29T=0.
for x in [(3, 32, 1), (29, 0, -1), (1, 1, 0)]:
    V, H, T = x
    assert dot(P2, x) == -4 * (H - V + 29 * T)

# Gate 5: standard supergravity arithmetic witnesses.
x = (0, 244, 1)
V, H, T = x
assert H - V + 29 * T == 273
assert dot(K, x) == -242

x = (25, 66, 8)
V, H, T = x
assert H - V + 29 * T == 273
assert dot(K, x) == 0

# Gate 6: exact reconstruction K = -R -(8/45)P1 -(11/180)P2.
for j in range(3):
    rhs = -F(R[j]) - F(8, 45) * P1[j] - F(11, 180) * P2[j]
    assert rhs == F(K[j])

# Gate 7: kernel intersection witnesses.
# ker(K) cap ker(P2) is span(-31,-60,1).
x = (-31, -60, 1)
assert dot(K, x) == 0
assert dot(P2, x) == 0

# ker(P1,P2) is span(1,1,0), and K is nonzero on it.
x = (1, 1, 0)
assert dot(P1, x) == dot(P2, x) == 0
assert dot(K, x) != 0

print("Model XXIV checks passed")
print("det anomaly map =", det3(M))
print("K=0 witness anomaly =", (-1, 7, -4))
print("pure-gravity kernel witness K =", 1)
print("K reconstruction coefficients =", (-1, F(-8, 45), F(-11, 180)))
