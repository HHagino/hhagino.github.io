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
\text{non-factorized MMM/Deligne--RR test}.
}
\]

Completed milestones: **v0.2–v0.8**. Gravity closure remains inactive.

## Main research-program note

- Web: `index.html`
- Source: `research-note.md`

## Model I — elliptic curves

- `elliptic-model.html`
- `elliptic-model.md`
- `elliptic-bergman.py`

For the level-\(k\) theta space,

\[
F_{\det\mathcal H_k}=-\frac{k}{2}F_{\lambda_H},
\]

while the exact Bergman density separates the constant local sector from exponentially small lattice corrections.

## Model II — modular holonomy / metaplectic anomaly

- `modular-holonomy.html`
- `modular-holonomy.md`
- `weil-holonomy.py`

Finite theta transport exhibits a projective/metaplectic phase. Local curvature can cancel while flat global holonomy remains.

## Model III — principally polarized abelian varieties

- `abelian-model.html`
- `abelian-model.md`
- `abelian-gram.py`

For

\[
A_\Omega=\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g),
\qquad N_k=k^g,
\]

one obtains

\[
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H}.
\]

### IIIb — exact multidimensional Bergman lattice sector

- `abelian-bergman.html`
- `abelian-bergman.md`
- `abelian-bergman.py`

\[
B_{g,k}
=
k^g\sum_{p,\ell\in\mathbf Z^g}
 e^{-\pi kQ_\Omega(p,\ell)/2}
 e^{2\pi ik(p^Tx+\ell^Tt)+\pi ikp^T\ell},
\]

with exponential shortest-vector suppression for fixed \(\Omega\).

### IIIc — higher-dimensional Weil / metaplectic descent

- `abelian-weil.html`
- `abelian-weil.md`
- `abelian-weil.py`

The finite matrices satisfy, in the fixed convention,

\[
U_k(S)^2=C,
\qquad
(U_k(S)U_k(T_{I_g}))^3=e^{\pi ig/4}C.
\]

The corrected determinant line may be locally flat but globally nontrivial.

## Model IV — compact hyperbolic curves

- `hyperbolic-model.html`
- `hyperbolic-model.md`
- `hyperbolic-loop.py`

The exact hyperbolic Bergman formula realizes simultaneously

\[
\text{nonzero local curvature sector}
\oplus
\text{global geodesic/holonomy sector}.
\]

The Mumford relation

\[
\lambda_k\simeq\lambda_1^{\otimes(6k^2-6k+1)}
\]

gives a no-go for a universal extrapolation of the flat-ppav rank/2 coefficient.

## Model V — Quillen / analytic torsion

- `quillen-refinement.html`
- `quillen-refinement.md`
- `quillen-refinement.py`

With the fixed holomorphic analytic-torsion convention,

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

The pointwise Bergman-loop correction and global analytic torsion share hyperbolic trace geometry but are not literally the same functional.

## Model VI — differential cohomology / determinant holonomy

- `differential-holonomy.html`
- `differential-holonomy.md`
- `differential-holonomy.py`

A line with unitary connection defines

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

carrying characteristic class, curvature and loop holonomy. The flat kernel

\[
0\to H^1(B;\mathbf R/\mathbf Z)
\to\widehat H^2(B;\mathbf Z)
\xrightarrow{R}\Omega^2_{\mathbf Z}(B)\to0
\]

makes precise why zero curvature need not imply trivial global anomaly data.

## Model VII — response / transgression bridge

- `response-transgression.html`
- `response-transgression.md`
- `response-transgression.py`

Loop-space transgression gives the genuine standard response

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z),
\]

whose value is the determinant holonomy function. Positive-dimensional pushforward lowers degree, so another degree-two line requires additional coupling data.

## Model VIII — canonical coupling / factorized-pushforward no-go

- `factorized-pushforward.html`
- `factorized-pushforward.md`
- `factorized-pushforward.py`

For a smooth proper oriented real \(d\)-dimensional family

\[
p:Z\to M,
\]

a base differential character \(\widehat{\mathcal A}\in\widehat H^2(M;\mathbf Z)\), and any degree-restoring class \(\widehat u\in\widehat H^d(Z;\mathbf Z)\), the standard projection formula gives

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
\widehat{\mathcal A}\cup p_!(\widehat u).
}
\]

Since

\[
p_!(\widehat u)\in\widehat H^0(M;\mathbf Z),
\]

on a connected base this is an integer \(n\). Therefore

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
n\widehat{\mathcal A}.
}
\]

Thus **every factorized degree-restored response is only integer multiplication of the original differential character**.

For a genus-\(g\) curve family and the canonical coupling

\[
\widehat u=\widehat c_1(K_{X/B}),
\]

one has

\[
\boxed{
\pi_!\left(
\pi^*\widehat{\mathcal A}
\cup
\widehat c_1(K_{X/B})
\right)
=
(2g-2)\widehat{\mathcal A}.
}
\]

This restores degree but creates no new independent response geometry.

## Current controlled frontier

To escape Model VIII, a new degree-two base class must come from something **non-factorized**, for example

\[
\widehat W\in\widehat H^{d+2}(Z;\mathbf Z),
\qquad
p_!\widehat W\in\widehat H^2(M;\mathbf Z),
\]

rather than \(p^*\widehat{\mathcal A}\cup\widehat u\).

For curve families the next canonical prototype is the differential refinement of

\[
c_1(K_{X/B})^2,
\]

whose ordinary pushforward leads to the first Mumford--Morita--Miller direction. The exact differential/Quillen normalization is the next literature-audited milestone.

No Lorentzian or gravitational closure is claimed.
