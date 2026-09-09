# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — milestone gates
- `references.bib` — canonical bibliography
- `citation-map.md` — citation provenance map
- `cited-synthesis.md` — citation-audited synthesis

## Completed sequence

\[
\boxed{
\text{elliptic / ppav}
\to
\text{curved hyperbolic curves}
\to
\text{Quillen / analytic torsion}
\to
\text{differential cohomology}
\to
\text{transgression}
\to
\text{factorized-pushforward no-go}
\to
\widehat\kappa_1/\text{Quillen}
\to
\text{global Deligne--RR closure}.
}
\]

Completed milestones: **v0.2–v0.10**. No Lorentzian/gravitational closure is claimed.

## Models I–III — flat theta / abelian laboratories

The elliptic and ppav models establish exact theta-state counting, exact Gram determinants, Poisson-resummed Bergman lattice sectors, and finite Weil/metaplectic holonomy. In the ppav conventions,

\[
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H},
\]

while flat corrected determinant lines can retain nontrivial global holonomy.

Sources/verifiers include `elliptic-model.md`, `modular-holonomy.md`, `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md` and their Python checkers.

## Model IV — compact hyperbolic curves

- `hyperbolic-model.html`
- `hyperbolic-model.md`
- `hyperbolic-loop.py`

The exact curved model separates a nonzero local Bergman-curvature sector from an independent global geodesic/holonomy sector. The Mumford determinant relation

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

carrying topology, curvature and loop holonomy in one object.

## Model VII — response / transgression

- `response-transgression.html`
- `response-transgression.md`
- `response-transgression.py`

Loop transgression gives

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z),
\]

whose value is the determinant holonomy function. Positive-dimensional pushforward lowers degree.

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

on a connected base. Thus factorized degree restoration cannot create an independent degree-two response direction.

## Model IX — non-factorized \(\widehat\kappa_1\) / Quillen comparison

- `kappa1-quillen.html`
- `kappa1-quillen.md`
- `kappa1-quillen.py`

For \(\pi:X\to B\), \(\omega=K_{X/B}\),

\[
\widehat\kappa_1
:=
\pi_!\bigl(\widehat c_1(\omega)^2\bigr).
\]

GRR and the Quillen local-index theorem give

\[
I(\widehat\kappa_1)=12I(\widehat\lambda_Q),
\qquad
R(\widehat\kappa_1)=12R(\widehat\lambda_Q),
\]

so the possible difference is topologically trivial and flat.

## Model X — global Deligne--Riemann--Roch closure

- `global-deligne-rr.html`
- `global-deligne-rr.md`
- `global-deligne-rr.py`

Fix the metrized Deligne-pairing realization of differential fiber integration. Deligne's curve-family isomorphism specializes at \(L=\omega\) to

\[
\lambda^{\otimes12}
\simeq
\langle\omega,\omega\rangle_\pi.
\]

With the Quillen metric on \(\lambda\) and the canonical Deligne metric on the pairing, the established metrized Deligne--Riemann--Roch theorem makes this an isometry up to an overall base-independent/topological constant. Such a constant does not alter the Chern connection. Therefore, as differential characters,

\[
\boxed{
\widehat\kappa_1
=
12\widehat\lambda_Q
}
\]

globally in the fixed convention.

Equivalently, for every loop \(\gamma\subset B\),

\[
\boxed{
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
=
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}.
}
\]

Thus the flat residual isolated in Model IX vanishes once the global metrized Deligne-pairing model is included. Topology, local curvature and global holonomy are three evaluations of the same connection-level identity in this canonical curve-family determinant sector.

## Current controlled frontier

The determinant/intersection \(U(1)\) sector is now closed for this smooth canonical curve-family direction. The next meaningful test must change the **target geometric structure**, not derive another identity among determinant lines.

In particular, an actual spacetime/frame response would require explicit maps of base spaces and an explicit passage from abelian \(U(1)\) line-connection data to the relevant nonabelian tangent/frame structure. That bridge is not supplied by Deligne--RR, GRR, Quillen theory, or differential cohomology alone.
