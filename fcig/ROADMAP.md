# FCIG Research Roadmap

**Current target:** v0.9 — non-factorized MMM / Deligne--Riemann--Roch test  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are kept as explicit no-go results.

---

## v0.3 — principally polarized abelian varieties — COMPLETE

The flat ppav laboratory established exact state counting, determinant/Hodge response, a Poisson-resummed Bergman lattice sector, and finite Weil/metaplectic holonomy.

Sources: `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md`.

---

## v0.4 — compact hyperbolic curves — COMPLETE

The curved model exhibits a nonzero local Bergman-curvature sector and an independent global geodesic/holonomy sector. The Mumford determinant relation gives a no-go for a universal flat-ppav rank/2 law.

Sources: `hyperbolic-model.md`, `hyperbolic-loop.py`.

---

## v0.5 — Quillen / analytic torsion — COMPLETE

On the same determinant line,

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

The Quillen/family-index curvature and the elementary \(L^2\) determinant curvature are therefore related by analytic torsion but are not interchangeable.

Sources: `quillen-refinement.md`, `quillen-refinement.py`.

---

## v0.6 — differential cohomology / determinant holonomy — COMPLETE

A line with unitary connection is encoded by

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

with topology, curvature and holonomy in one object. The flat kernel of the curvature map explains how nontrivial global holonomy can survive when local curvature vanishes.

Sources: `differential-holonomy.md`, `differential-holonomy.py`.

---

## v0.7 — response / transgression bridge — COMPLETE

Loop-space transgression gives

\[
\boxed{
\tau_{S^1}:\widehat H^2(B;\mathbf Z)
\to\widehat H^1(LB;\mathbf Z),
}
\]

whose value is the determinant holonomy function. More generally, real \(d\)-dimensional pushforward lowers degree by \(d\), so a degree-two line cannot be transported through a positive-dimensional fiber without additional degree-restoring data.

Sources: `response-transgression.md`, `response-transgression.py`.

---

## v0.8 — canonical coupling / factorized pushforward — COMPLETE

Let

\[
p:Z\to M
\]

be a smooth proper oriented real \(d\)-dimensional family, let

\[
\widehat{\mathcal A}\in\widehat H^2(M;\mathbf Z),
\qquad
\widehat u\in\widehat H^d(Z;\mathbf Z).
\]

### Gate V — projection formula — PASS

The standard differential-cohomology projection formula gives

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
\widehat{\mathcal A}\cup p_!(\widehat u).
}
\]

### Gate W — factorized-pushforward no-go — PASS

Since

\[
p_!(\widehat u)\in\widehat H^0(M;\mathbf Z),
\]

on a connected base it is an integer \(n\). Hence

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
n\widehat{\mathcal A}.
}
\]

Thus every factorized degree-restored response is only integer multiplication of the original differential character. It cannot generate an independent degree-two response direction.

### Gate X — canonical curve-family coupling — PASS WITH NO-GO

For a smooth genus-\(g\) curve family

\[
\pi:X\to B
\]

and

\[
\widehat u=\widehat c_1(K_{X/B}),
\]

standard curve theory gives

\[
\pi_!\widehat c_1(K_{X/B})=2g-2.
\]

Therefore

\[
\boxed{
\pi_!\left(
\pi^*\widehat{\mathcal A}\cup\widehat c_1(K_{X/B})
\right)
=
(2g-2)\widehat{\mathcal A}.
}
\]

The canonical line restores degree exactly but creates no new independent response geometry.

### Gate Y — flat/curved preservation — PASS

If \(R(\widehat{\mathcal A})=0\), the factorized response stays flat. If \(R(\widehat{\mathcal A})\neq0\), the curvature is only multiplied by \(n\). Likewise loop holonomy is raised to the \(n\)-th power. No new tensor type or structure group appears.

Sources: `factorized-pushforward.md`, `factorized-pushforward.py`.

### v0.8 conclusion

\[
\boxed{
\text{degree restoration by a factorized coupling}
\neq
\text{generation of new response geometry}.
}
\]

This rules out an entire class of FCIG response ansätze.

---

## v0.9 — non-factorized MMM / Deligne--Riemann--Roch test — ACTIVE

To escape v0.8, use a total-space class that is not of the form

\[
p^*\widehat{\mathcal A}\cup\widehat u.
\]

For a curve family the first canonical candidate is a differential refinement of

\[
\boxed{
c_1(K_{X/B})^2\in H^4(X;\mathbf Z),
}
\]

whose ordinary fiber integral gives the first Mumford--Morita--Miller direction.

### Gate Z1 — ordinary cohomology normalization

Fix the convention for

\[
\kappa_1=\pi_*\bigl(c_1(K_{X/B})^2\bigr)
\in H^2(B;\mathbf Z)
\]

and audit its relation to the Hodge class on the smooth moduli locus, including all normalization and boundary qualifications.

### Gate Z2 — differential refinement

Construct or cite a differential refinement

\[
\widehat\kappa_1
=
\pi_!\bigl(\widehat c_1(K_{X/B})^2\bigr)
\in\widehat H^2(B;\mathbf Z)
\]

with the required fiber-integration orientation and connection conventions.

### Gate Z3 — compare with Quillen / Deligne--RR

Determine whether \(\widehat\kappa_1\) agrees with a multiple of the Quillen determinant differential character, differs by a flat class, or requires an explicit secondary correction. No equality will be stated until the metric/connection normalization is fixed from the literature.

### Gate Z4 — response audit

Even if a genuinely new degree-two \(U(1)\) class is obtained, record that it still does not supply a Lorentzian frame connection without further structure.

---

## Gravity Closure gate — NOT ACTIVE

No derivation of gravity is claimed. A future closure would still need explicit base-space, tensor-type, structure-group, causal, entropy-functional and falsification maps.
