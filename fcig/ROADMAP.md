# FCIG Research Roadmap

**Current target:** v0.7 — response / transgression bridge test  
**Updated:** 2026-09-09

The roadmap is ordered so that each mathematical mechanism is tested before it is used in a gravitational interpretation. A failed extrapolation is recorded as a no-go result rather than repaired by changing definitions after the fact.

---

## Milestone v0.3 — principally polarized abelian varieties — COMPLETE

The flat ppav laboratory established

\[
\dim H^0(A_\Omega,L^k)=k^g,
\qquad
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H},
\]

an exact Poisson-resummed Bergman lattice formula with exponential shortest-vector suppression, and finite Weil/metaplectic descent with explicit nontrivial flat holonomy.

Sources:

- `abelian-model.md`
- `abelian-bergman.md`
- `abelian-weil.md`

---

## Milestone v0.4 — compact hyperbolic genus-\(g\ge2\) curves — COMPLETE

For

\[
X=\Gamma\backslash\mathbb H,
\qquad
\mathcal H_k=H^0(X,K_X^k),
\]

the curved model exhibits a nonzero local Bergman-curvature sector and an independent global geodesic/holonomy sector. The determinant comparison gives

\[
\lambda_k\simeq\lambda_1^{\otimes(6k^2-6k+1)},
\]

which is a no-go for a universal flat-ppav rank/2 law.

Sources:

- `hyperbolic-model.md`
- `hyperbolic-loop.py`

---

## Milestone v0.5 — Quillen / analytic-torsion refinement — COMPLETE

On the same determinant line \(\lambda_k\), ordinary \(L^2\) and Quillen metrics are separated by holomorphic analytic torsion:

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

The Quillen curvature is fixed by the family local-index theorem, while the torsion factor is globally spectral and, on hyperbolic surfaces, related to Selberg-zeta / geodesic data. The pointwise Bergman-loop correction and analytic torsion are not literally the same functional.

Sources:

- `quillen-refinement.md`
- `quillen-refinement.py`

---

## Milestone v0.6 — differential-cohomology / determinant-holonomy synthesis — COMPLETE

A Hermitian line with unitary connection is represented by

\[
\boxed{
\widehat c_1(L,\nabla)
\in\widehat H^2(B;\mathbf Z).
}
\]

### Gate N — differential-cohomology object — PASS

The convention is fixed so that

\[
I(\widehat c_1)=c_1(L),
\qquad
R(\widehat c_1)=\frac{F_\nabla}{2\pi i},
\]

and the Cheeger--Simons character evaluates on one-cycles to give \(U(1)\) holonomy.

The curvature exact sequence is

\[
\boxed{
0\to H^1(B;\mathbf R/\mathbf Z)
\to\widehat H^2(B;\mathbf Z)
\xrightarrow{R}\Omega^2_{\mathbf Z}(B)\to0.
}
\]

Thus curvature-zero classes can retain nontrivial global holonomy.

### Gate O — Quillen/Bismut--Freed connection — PASS

The determinant line with its natural Quillen/Bismut--Freed connection defines a differential character. Its curvature is the family-index curvature, while loop holonomy is governed, in the Dirac-family setting, by the Bismut--Freed adiabatic eta-invariant holonomy theorem.

For the hyperbolic canonical family,

\[
R(\widehat c_1(\lambda_k,\nabla^Q))
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}.
\]

### Gate P — flat/curved anomaly comparison — PASS WITH NON-IDENTIFICATION

On the appropriate theta/metaplectic quotient or cover, the corrected ppav line is a flat differential character:

\[
R=0,
\qquad
\operatorname{Hol}\neq1
\]

in explicit examples. The curved Quillen determinant character instead has nonzero curvature and eta-invariant holonomy.

The two models share the same **category of line-with-connection data**, not the same base, class, or monodromy mechanism.

### Gate Q — pre-gravity no-go audit — PASS

Remaining mismatches are explicit:

1. parameter/moduli base \(B\) versus physical spacetime \(M\);
2. \(U(1)\) determinant connection versus tangent/frame connection;
3. Euclidean/Kähler geometry versus Lorentzian causal structure;
4. state-count/Bergman information versus horizon entropy;
5. forward family-index map versus the unproved inverse response to spacetime dynamics.

Sources:

- `differential-holonomy.md`
- `differential-holonomy.py`

The v0.6 conclusion is:

\[
\boxed{
\text{determinant anomaly data}
=
\text{one differential character carrying topology + curvature + holonomy}.
}
\]

This solves the curvature-only anomaly ambiguity, not the gravity closure.

---

## Milestone v0.7 — response / transgression bridge test — ACTIVE

The next question is whether the determinant differential character can participate in a **mathematically specified response map** to another geometric connection, rather than being verbally identified with one.

### Gate R — specify the correspondence of spaces

Any proposed response must begin with explicit maps, for example a correspondence

\[
M\xleftarrow{\;p\;}Z\xrightarrow{\;q\;}B
\]

or a family \(\pi:Z\to B\), instead of silently treating moduli space as spacetime.

**Pass condition:** source, target, and base of every differential class are explicit.

### Gate S — use a genuine differential-cohomology operation

Test a pullback, transgression, or differential-cohomology pushforward where its orientation hypotheses are satisfied.

**Pass condition:** the operation exists as a standard mathematical construction and its degree shift is correct. An analogy is not enough.

### Gate T — tensor/structure-group audit at the target

If the target remains \(U(1)\), record that it is still an abelian response line. If a tangent/frame connection is desired, construct an actual map of geometric structures rather than equating two curvature forms.

**Pass condition:** no equation identifies \(i\mathbf R\)-valued curvature with \(\mathfrak{so}(1,d-1)\)-valued curvature without an explicit homomorphism/coupling.

### Gate U — one explicit response example or a no-go

Produce one model in which a standard pullback/transgression/pushforward maps the determinant differential character to a new, well-defined geometric observable. If no nontrivial map with the desired type exists, record that as a no-go.

**Pass condition:** a checkable example with references and fixed conventions.

---

## Gravity Closure gate — NOT ACTIVE

No claim that FCIG derives gravity should be made until at least the v0.7 response bridge exists and the Lorentzian/causal mismatch is separately addressed.

The closure target remains

\[
\boxed{
\text{local state-density/index data}
+
\text{global holonomy/spectral data}
+
\text{causal thermodynamics}
\Longrightarrow ?
\text{Lorentzian field equation}.
}
\]

A successful closure must specify:

1. the physical spacetime object;
2. the map from parameter/moduli data to spacetime variables;
3. tensor-type and structure-group matching;
4. the entropy/information functional varied;
5. the limit reproducing established gravitational dynamics;
6. a falsification route.
