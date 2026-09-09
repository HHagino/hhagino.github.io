# FCIG Research Roadmap

**Current target:** v0.10 — metric-compatible Deligne--Riemann--Roch / global holonomy audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are kept as explicit no-go results.

---

## v0.3 — principally polarized abelian varieties — COMPLETE

The flat ppav laboratory established exact state counting, determinant/Hodge response, a Poisson-resummed Bergman lattice sector, and finite Weil/metaplectic holonomy.

---

## v0.4 — compact hyperbolic curves — COMPLETE

The curved model exhibits a nonzero local Bergman-curvature sector and an independent global geodesic/holonomy sector. The Mumford determinant relation gives a no-go for a universal flat-ppav rank/2 law.

---

## v0.5 — Quillen / analytic torsion — COMPLETE

On the same determinant line,

\[
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
\]

---

## v0.6 — differential cohomology / determinant holonomy — COMPLETE

A unitary line with connection is encoded by a degree-two differential character carrying topology, curvature and loop holonomy.

---

## v0.7 — response / transgression bridge — COMPLETE

Loop transgression is a genuine standard response operation, while positive-dimensional pushforward exposes a degree obstruction.

---

## v0.8 — factorized pushforward — COMPLETE WITH NO-GO

For a smooth proper oriented real \(d\)-dimensional family \(p:Z\to M\), a base class \(\widehat{\mathcal A}\in\widehat H^2(M;\mathbf Z)\), and \(\widehat u\in\widehat H^d(Z;\mathbf Z)\),

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
n\widehat{\mathcal A}
}
\]

on each connected component. Factorized degree restoration cannot generate an independent degree-two response direction.

---

## v0.9 — non-factorized \(\widehat\kappa_1\) / Quillen comparison — COMPLETE

Let

\[
\pi:X\to B,
\qquad
\omega=K_{X/B},
\]

and define

\[
\boxed{
\widehat\kappa_1
:=
\pi_!\bigl(\widehat c_1(\omega)^2\bigr)
\in\widehat H^2(B;\mathbf Z).
}
\]

### Gate Z1 — ordinary cohomology normalization — PASS

GRR on the smooth locus gives

\[
\boxed{
\kappa_1
:=
\pi_*\bigl(c_1(\omega)^2\bigr)
=
12c_1(\lambda),
}
\]

where \(\lambda=\det R\pi_*\omega\). Boundary corrections on compactified moduli are not part of this statement.

### Gate Z2 — differential refinement — PASS

Standard differential-character product and fiber integration give the canonical class \(\widehat\kappa_1\), with

\[
I(\widehat\kappa_1)=\kappa_1,
\qquad
R(\widehat\kappa_1)
=
\pi_*\left(R(\widehat c_1(\omega))^2\right).
\]

### Gate Z3 — Quillen comparison — PASS UP TO A FLAT CLASS

Let

\[
\widehat\lambda_Q
=
\widehat c_1(\lambda,\nabla^Q).
\]

The Bismut--Gillet--Soulé local family index theorem, in the same normalized Chern-form convention, gives

\[
\boxed{
R(\widehat\kappa_1)
=
12R(\widehat\lambda_Q).
}
\]

Together with Gate Z1,

\[
\boxed{
\widehat\delta_{\mathrm{DR}}
:=
\widehat\kappa_1-12\widehat\lambda_Q
}
\]

satisfies

\[
\boxed{
I(\widehat\delta_{\mathrm{DR}})=0,
\qquad
R(\widehat\delta_{\mathrm{DR}})=0.
}
\]

Hence the only possible discrepancy is a topologically trivial flat differential character.

### Gate Z4 — local/global audit — PASS

If

\[
H^1(B;\mathbf R)=0,
\]

then the residual group vanishes and

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q.
}
\]

In particular this holds on simply connected parameter bases. On a non-simply-connected quotient, global equality is equivalent to triviality of the residual flat holonomy and is **not** asserted yet.

Sources and checker:

- `kappa1-quillen.md`
- `kappa1-quillen.py`
- Stacks GRR
- Bär--Becker
- Bismut--Gillet--Soulé
- Eriksson / Deligne--Riemann--Roch
- Harris--Morrison

### v0.9 conclusion

\[
\boxed{
\text{first canonical non-factorized class}
=
12\times\text{Quillen/Hodge class}
+
\text{possible flat global secondary class}.
}
\]

The local and topological ambiguity is closed; only global flat holonomy remains.

---

## v0.10 — metric-compatible Deligne--Riemann--Roch / global holonomy audit — ACTIVE

The remaining target is the flat residual

\[
\widehat\delta_{\mathrm{DR}}
=
\widehat\kappa_1-12\widehat\lambda_Q.
\]

### Gate AA — Deligne pairing identification

Fix the differential/metric convention identifying the differential pushforward of

\[
\widehat c_1(\omega)^2
\]

with the Chern class of the metrized Deligne self-pairing

\[
\langle\omega,\omega\rangle.
\]

### Gate AB — metric-compatible Deligne--RR

Audit the theorem relating

\[
\lambda^{\otimes12}
\]

and

\[
\langle\omega,\omega\rangle
\]

with Quillen and Deligne metrics. Track any genus-dependent constant and verify whether it affects the Chern connection.

### Gate AC — global holonomy

Determine whether the resulting connection-preserving isomorphism forces

\[
\widehat\delta_{\mathrm{DR}}=0
\]

globally, or whether a residual flat character survives on the quotient.

No global equality will be claimed until these connection/holonomy conventions are audited from the literature.

---

## Gravity Closure gate — NOT ACTIVE

Even a complete Deligne--RR equality remains an equality of \(U(1)\) differential characters on a parameter/moduli base. No Lorentzian tangent/frame connection or gravitational field equation has been derived.
