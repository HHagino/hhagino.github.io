# FCIG Research Roadmap

**Current target:** v0.8 — canonical-coupling / factorized-pushforward test  
**Updated:** 2026-09-09

The roadmap is ordered so that each mathematical mechanism is tested before it is used in a gravitational interpretation. Failed extrapolations are recorded as no-go results rather than repaired by changing definitions after the fact.

---

## Milestone v0.3 — principally polarized abelian varieties — COMPLETE

The flat ppav laboratory established

\[
\dim H^0(A_\Omega,L^k)=k^g,
\qquad
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H},
\]

an exact Poisson-resummed Bergman lattice formula with exponential shortest-vector suppression, and finite Weil/metaplectic descent with explicit nontrivial flat holonomy.

Sources: `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md`.

---

## Milestone v0.4 — compact hyperbolic curves — COMPLETE

For a compact hyperbolic curve

\[
X=\Gamma\backslash\mathbb H,
\qquad
\mathcal H_k=H^0(X,K_X^k),
\]

the model exhibits a nonzero local Bergman-curvature sector and an independent global geodesic/holonomy sector. The determinant comparison gives

\[
\lambda_k\simeq\lambda_1^{\otimes(6k^2-6k+1)},
\]

which is a no-go for a universal flat-ppav rank/2 law.

Sources: `hyperbolic-model.md`, `hyperbolic-loop.py`.

---

## Milestone v0.5 — Quillen / analytic torsion — COMPLETE

On the same determinant line \(\lambda_k\), ordinary \(L^2\) and Quillen metrics satisfy, in the fixed convention,

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

The Quillen curvature is fixed by the family local-index theorem, while the torsion factor is globally spectral and is related on hyperbolic surfaces to Selberg-zeta / closed-geodesic data. The pointwise Bergman-loop correction and analytic torsion are not literally the same functional.

Sources: `quillen-refinement.md`, `quillen-refinement.py`.

---

## Milestone v0.6 — differential cohomology / determinant holonomy — COMPLETE

A Hermitian line with unitary connection defines

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

with characteristic class, curvature and loop holonomy. The curvature exact sequence

\[
\boxed{
0\to H^1(B;\mathbf R/\mathbf Z)
\to\widehat H^2(B;\mathbf Z)
\xrightarrow{R}\Omega^2_{\mathbf Z}(B)\to0
}
\]

makes precise why curvature zero does not imply trivial global holonomy. The flat ppav corrected line and the curved Quillen determinant line lie in the same category of line-with-connection data but are not the same class or the same model.

Sources: `differential-holonomy.md`, `differential-holonomy.py`.

---

## Milestone v0.7 — response / transgression bridge — COMPLETE

### Gate R — spaces and maps — PASS

Every response operation is stated using explicit source and target spaces. In particular, for the free loop space

\[
LB=C^\infty(S^1,B),
\qquad
\operatorname{ev}:LB\times S^1\to B,
\]

there is no identification of the parameter base \(B\) with another geometric space by analogy.

### Gate S — genuine differential-cohomology operations — PASS

Differential-character transgression is

\[
\boxed{
\tau_{S^1}
=\widehat\pi_!\operatorname{ev}^*:
\widehat H^2(B;\mathbf Z)
\longrightarrow
\widehat H^1(LB;\mathbf Z).
}
\]

For a line bundle with connection,

\[
\boxed{
\tau_{S^1}(\widehat{\mathcal A})(\gamma)
=\operatorname{Hol}_{\widehat{\mathcal A}}(\gamma).
}
\]

This is a genuine response map: the determinant differential character produces the holonomy function on loop space. Standard fiber integration, product and transgression are cited to Bär--Becker; the determinant holonomy input is cited to Bismut--Freed / Dai--Freed.

### Gate T — degree and structure-group audit — PASS WITH NO-GO

For a correspondence

\[
M\xleftarrow{p}Z\xrightarrow{q}B
\]

with closed oriented real \(d\)-dimensional fibers,

\[
\boxed{
p_!q^*\widehat{\mathcal A}
\in\widehat H^{2-d}(M;\mathbf Z).
}
\]

Hence a positive-dimensional pushforward does **not** by itself produce another degree-two line-with-connection class. In particular, circle transgression lands in degree one, i.e. a \(U(1)\)-valued function rather than a new line bundle.

A degree-preserving template must contain an additional class

\[
\widehat u\in\widehat H^d(Z;\mathbf Z),
\]

so that

\[
\boxed{
\widehat{\mathcal R}_{p,q,\widehat u}
=p_!(q^*\widehat{\mathcal A}\cup\widehat u)
\in\widehat H^2(M;\mathbf Z).
}
\]

Even then the target is still an abelian \(U(1)\) line with connection; no tangent/frame connection has been produced.

### Gate U — explicit response example — PASS

For a loop \(c:S^1\to B\), the pullback \(c^*\widehat{\mathcal A}\in\widehat H^2(S^1;\mathbf Z)\) is necessarily flat because \(S^1\) has no nonzero 2-forms, while its holonomy is exactly the original determinant holonomy on \(c\). For a Bismut--Freed determinant connection, the latter is governed by the adiabatic eta-invariant holonomy theorem.

Source and degree checker: `response-transgression.md`, `response-transgression.py`.

### v0.7 conclusion

\[
\boxed{
\text{response maps exist, but differential-cohomology degree and structure group sharply constrain their targets.}
}
\]

---

## Milestone v0.8 — canonical coupling / factorized pushforward — ACTIVE

The next test asks whether the degree-restoring class can be chosen canonically from geometry already present in a family, instead of being introduced ad hoc.

For a smooth proper family of genus-\(g\ge2\) curves

\[
\pi:X\to B,
\]

the natural first candidate is

\[
\widehat u=\widehat c_1(K_{X/B})\in\widehat H^2(X;\mathbf Z).
\]

The first pass condition is to apply the standard projection formula to

\[
\pi_!\bigl(\pi^*\widehat{\mathcal A}\cup\widehat u\bigr)
\]

and determine whether this produces new response geometry or only a scalar multiple of the original differential character.

A stronger general test will treat arbitrary \(\widehat u\in\widehat H^2(X)\). If the projection formula forces every factorized ansatz of this type to be an integer multiple of \(\widehat{\mathcal A}\) on a connected base, that will be recorded as a structural no-go theorem.

---

## Gravity Closure gate — NOT ACTIVE

No claim that FCIG derives gravity should be made at this stage. A successful closure would still have to specify:

1. the physical spacetime object;
2. a mathematically defined map from parameter/moduli data to spacetime variables;
3. tensor-type and structure-group matching;
4. Lorentzian causal structure;
5. the entropy/information functional varied;
6. a limit reproducing established gravitational dynamics;
7. a falsification route.
