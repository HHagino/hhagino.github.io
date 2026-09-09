# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims.

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — milestone gates
- `references.bib` — canonical bibliography
- `citation-map.md` — citation provenance map
- `cited-synthesis.md` — citation-audited synthesis

`main` is intended to remain readable and independently checkable. Exploratory work is developed on topic branches and merged through pull requests.

## Research sequence

\[
\boxed{
\text{elliptic}
\to
\text{flat ppav}
\to
\text{hyperbolic curves}
\to
\text{Quillen / torsion}
\to
\text{differential cohomology}
\to
\text{transgression}
\to
\text{factorized-pushforward no-go}
\to
\widehat\kappa_1/\text{Quillen comparison}
\to
\text{global Deligne--RR holonomy audit}.
}
\]

Completed milestones: **v0.2–v0.9**. Gravity closure remains inactive.

## Main research-program note

- Web: `index.html`
- Source: `research-note.md`

## Models I–III — elliptic and flat abelian laboratories

The elliptic and ppav models establish exact theta-state counting, explicit Gram determinants, Poisson-resummed Bergman lattice sectors, and finite Weil/metaplectic holonomy. In the ppav conventions,

\[
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H},
\]

while flat corrected determinant lines can retain nontrivial global holonomy.

Sources and verifiers:

- `elliptic-model.md`, `elliptic-bergman.py`
- `modular-holonomy.md`, `weil-holonomy.py`
- `abelian-model.md`, `abelian-gram.py`
- `abelian-bergman.md`, `abelian-bergman.py`
- `abelian-weil.md`, `abelian-weil.py`

## Model IV — compact hyperbolic curves

- `hyperbolic-model.html`
- `hyperbolic-model.md`
- `hyperbolic-loop.py`

The curved model realizes

\[
\text{nonzero local curvature sector}
\oplus
\text{global geodesic/holonomy sector}.
\]

The Mumford determinant relation

\[
\lambda_k\simeq\lambda_1^{\otimes(6k^2-6k+1)}
\]

is a no-go for a universal extrapolation of the flat-ppav rank/2 coefficient.

## Model V — Quillen / analytic torsion

- `quillen-refinement.html`
- `quillen-refinement.md`
- `quillen-refinement.py`

With the fixed convention,

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

The elementary \(L^2\) determinant metric and the Quillen/family-index metric are related but not interchangeable.

## Model VI — differential cohomology / determinant holonomy

- `differential-holonomy.html`
- `differential-holonomy.md`
- `differential-holonomy.py`

A unitary line with connection defines

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

carrying topology, curvature, and loop holonomy. The curvature exact sequence makes precise why zero local curvature can coexist with nontrivial global holonomy.

## Model VII — response / transgression bridge

- `response-transgression.html`
- `response-transgression.md`
- `response-transgression.py`

Loop transgression gives

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z),
\]

whose value is the determinant holonomy function. Positive-dimensional pushforward lowers degree, so another degree-two line requires additional degree-restoring data.

## Model VIII — factorized-pushforward no-go

- `factorized-pushforward.html`
- `factorized-pushforward.md`
- `factorized-pushforward.py`

For a smooth proper oriented real \(d\)-dimensional family \(p:Z\to M\),

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
n\widehat{\mathcal A},
\qquad n\in\mathbf Z
}
\]

on a connected base, for every degree-restoring \(\widehat u\in\widehat H^d(Z;\mathbf Z)\). Thus factorized degree restoration cannot create an independent response direction.

For a genus-\(g\) curve family and \(\widehat u=\widehat c_1(K_{X/B})\),

\[
\pi_!\left(\pi^*\widehat{\mathcal A}\cup\widehat c_1(K_{X/B})\right)
=(2g-2)\widehat{\mathcal A}.
\]

## Model IX — non-factorized \(\widehat\kappa_1\) and Quillen comparison

- `kappa1-quillen.html`
- `kappa1-quillen.md`
- `kappa1-quillen.py`

For a smooth family of curves \(\pi:X\to B\) with \(\omega=K_{X/B}\), define

\[
\boxed{
\widehat\kappa_1
:=
\pi_!\left(\widehat c_1(\omega)^2\right)
\in\widehat H^2(B;\mathbf Z).
}
\]

GRR fixes the smooth-locus characteristic-class normalization

\[
\boxed{
I(\widehat\kappa_1)
=
\kappa_1
=
12c_1(\lambda).
}
\]

Using the Bismut--Gillet--Soulé Quillen local-index formula with the same normalized Chern form gives

\[
\boxed{
R(\widehat\kappa_1)
=
12R(\widehat\lambda_Q).
}
\]

Therefore the residual

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

Thus the only remaining discrepancy is a **topologically trivial flat differential character**. If \(H^1(B;\mathbf R)=0\), in particular on a simply connected base,

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q.
}
\]

Globally on a non-simply-connected moduli quotient, the residual loop holonomy is deliberately left for the next metric-compatible Deligne--Riemann--Roch / Deligne-pairing audit.

## Current controlled frontier

The next exact question is no longer whether the local forms match: they do. It is whether the globally defined metric/connection-refined Deligne--Riemann--Roch identification forces

\[
\widehat\delta_{\mathrm{DR}}=0
\]

on the relevant quotient, or leaves a genuine flat secondary character.

Even a positive answer remains a statement about \(U(1)\) differential characters on a parameter/moduli base. No Lorentzian tangent/frame connection or gravitational field equation has been derived.
