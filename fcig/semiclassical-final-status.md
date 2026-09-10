# FCIG Semiclassical Branch — Final Status Ledger

**Frozen status: 2026-09-10**

The current canonical source for the representation-side semiclassical branch is:

1. `semiclassical-preprint-v1.md` — frozen v1.0 synthesis;
2. `unrestricted-schwartz-closure.md` — UQ-A2/UQ-B2 closure;
3. `semiclassical-atlas-closure.md` — sharp proportional-K atlas;
4. the JA/RF/UR/BC notes — derivation notebooks and proof details.

Any earlier `OPEN`, `TARGET`, or `NEXT GATE` language in derivation notebooks is historical when it conflicts with this ledger.

## Closed gates

\[
\boxed{
\begin{array}{ll}
\mathrm{UQ\!\!-A1} & \mathrm{PASS},\\
\mathrm{UQ\!\!-B1} & \mathrm{PASS},\\
\mathrm{JA/RF/UR/BC} & \mathrm{PASS\ at\ leading\ canonical\ level},\\
\mathrm{SAC\!\!-A} & \mathrm{PASS},\\
\mathrm{UQ\!\!-B2} & \mathrm{PASS},\\
\mathrm{UQ\!\!-A2} & \mathrm{PASS}.
\end{array}}
\]

## Two complementary master statements

### Sharp local semiclassical atlas

For `m/q -> alpha`, `n/q -> beta`, the radial holomorphic-discrete-series coefficient is governed by:

- real-saddle forbidden rates outside the exact caustics;
- conjugate-saddle oscillation between the caustics;
- Airy functions at simple folds;
- Bessel functions when `q|alpha-beta| = O(1)`;
- Hermite--Gaussian / parabolic-cylinder functions when `q min(alpha,beta) = O(1)`.

### Global unrestricted Schwartz closure

For every Harish--Chandra Schwartz seminorm `p_{D,E,N}` there is a polynomial `P_{D,E,N}` such that

\[
\boxed{
p_{D,E,N}(M_{m,n}^{(q)})
\le C_{D,E,N}P_{D,E,N}(q,m,n)
}
\]

for all holomorphic discrete-series parameters and all K-type labels. The existence of a finite polynomial loss follows from the discrete-series Harish--Chandra Schwartz Fourier block; the zeroth-order uniform Xi majorant is supplied by Cowling--Haagerup--Howe, and explicit K-type derivative costs are polynomial from the derived representation.

## Not claimed

The branch does **not** claim:

- optimal polynomial exponents in the unrestricted Schwartz theorem;
- one closed-form WKB remainder valid uniformly over every unbounded parameter ratio;
- an identification of K-type labels, Cartan radius, transverse FCIG Fourier frequency, and Harish--Chandra spectral parameter;
- equality of matrix coefficients, characters, orbital integrals, or cyclic relative traces;
- literature novelty for Airy/Bessel/Hermite asymptotic machinery or Harish--Chandra Schwartz theory.

These are claim firewalls, not open structural gates.

## Current conclusion

\[
\boxed{
\textbf{Representation-side semiclassical closure: COMPLETE at structural theorem level.}
}
\]

Future work is quantitative refinement and the separate FCIG geometry/orbital/global-physics program, not completion of the radial discrete-series semiclassical atlas itself.
