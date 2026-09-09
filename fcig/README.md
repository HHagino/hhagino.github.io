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
\text{theta / ppav}
\to
\text{curved curves}
\to
\text{Quillen / differential cohomology}
\to
\text{transgression}
\to
\text{pushforward no-go}
\to
\text{Deligne--RR closure}
\to
\text{structure-group no-go}
\to
\text{mixed anomaly polynomial}.
}
\]

Completed milestones: **v0.2–v0.12**. No Lorentzian/gravitational closure is claimed.

## Models I–III — flat theta / abelian laboratories

The elliptic and ppav models establish exact theta-state counting, exact Gram determinants, Poisson-resummed Bergman lattice sectors, and finite Weil/metaplectic holonomy. In the ppav conventions,

\[
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H},
\]

while flat corrected determinant lines can retain nontrivial global holonomy.

Main files: `elliptic-model.md`, `modular-holonomy.md`, `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md` and their Python checkers.

## Model IV — compact hyperbolic curves

`hyperbolic-model.md` / `hyperbolic-loop.py`

The curved model separates a nonzero local Bergman-curvature sector from an independent global geodesic/holonomy sector. The Mumford determinant relation is a no-go for a universal extrapolation of the flat-ppav rank/2 coefficient.

## Model V — Quillen / analytic torsion

`quillen-refinement.md` / `quillen-refinement.py`

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

The elementary \(L^2\) determinant metric and Quillen/family-index metric are related but not interchangeable.

## Model VI — differential cohomology / determinant holonomy

`differential-holonomy.md` / `differential-holonomy.py`

A unitary line with connection defines

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

carrying topology, curvature and loop holonomy in one object.

## Model VII — response / transgression

`response-transgression.md` / `response-transgression.py`

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z)
\]

is a genuine response map whose value is the determinant holonomy function. Positive-dimensional pushforward lowers degree.

## Model VIII — factorized-pushforward no-go

`factorized-pushforward.md` / `factorized-pushforward.py`

For a smooth proper oriented real \(d\)-dimensional family,

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=n\widehat{\mathcal A},
\qquad n\in\mathbf Z,
}
\]

on a connected base. Factorized degree restoration cannot create an independent degree-two response direction.

## Model IX — non-factorized \(\widehat\kappa_1\) / Quillen comparison

`kappa1-quillen.md` / `kappa1-quillen.py`

For \(\pi:X\to B\), \(\omega=K_{X/B}\),

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(\omega)^2\bigr),
\]

and GRR plus the Quillen local-index theorem give equality with \(12\widehat\lambda_Q\) at characteristic-class and curvature levels, leaving only a possible flat residual.

## Model X — global Deligne--Riemann--Roch closure

`global-deligne-rr.md` / `global-deligne-rr.py`

The metrized Deligne-pairing model closes the residual globally:

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q,
}
\]

hence

\[
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
=
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}.
\]

## Model XI — determinant trace / Spin\(^c\) / reconstruction no-go

`structure-group-bridge.md` / `structure-group-bridge.py`

The exact sequence

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1
\]

induces

\[
F_{\det E}=\operatorname{Tr}F_E.
\]

For fixed determinant connection, unitary lifts form an affine space over

\[
\Omega^1(M;\mathfrak{su}(E)).
\]

Thus determinant data fixes only the trace sector for \(n>1\). In Kähler tangent geometry it sees Ricci curvature; a Ricci-flat K3 is an explicit witness that determinant curvature may vanish while nonabelian tangent curvature remains. A Spin\(^c\) connection positively combines an independently supplied frame connection with determinant-line data, but the line alone does not reconstruct the frame connection.

## Model XII — mixed characteristic classes / degree-six anomaly bridge

- Web: `mixed-characteristic.html`
- Source: `mixed-characteristic.md`
- Checker: `mixed-characteristic.py`
- Milestone bibliography: `mixed-characteristic.bib`

Now treat the line and frame connections as **independent fields on the same base**. The first canonical mixed differential characteristic class is

\[
\boxed{
\widehat c_1(L)\cup\widehat p_1(TM)
\in\widehat H^6(M;\mathbf Z).
}
\]

For a line-twisted Dirac index, standard index theory gives

\[
\boxed{
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac16c_1(L)^3
-
\frac1{24}c_1(L)p_1(TM).
}
\]

This is a genuine mixed gauge/frame invariant without any structure-group identification. Classic gauge/gravitational anomaly theory uses precisely such higher-degree characteristic polynomials and descent.

The degree audit is equally important:

\[
\boxed{
\deg(c_1p_1)=6>4.
}
\]

Therefore this polynomial is **not** itself a local four-form action density in four dimensions; descent, transgression/inflow, an extension manifold, or additional non-topological structure is required.

For generic semisimple higher-rank orthogonal frame algebras there is also no nonzero invariant linear Chern--Weil polynomial analogous to \(c_1\). The first Pontryagin class is degree four. The abelian \(SO(2)\cong U(1)\) Euler/\(c_1\) exception is recorded explicitly.

References: Alvarez-Gaumé--Witten (1984), Zumino--Wu--Zee (1984), Bardeen--Zumino (1984), Alvarez-Gaumé--Ginsparg (1985), Freed (2014), Lawson--Michelsohn.

## Current controlled frontier

The program now has a mathematically valid way for FCIG line data and an independent frame connection to occur in one invariant:

\[
\boxed{
U(1)\text{ line}
+
\text{frame connection}
\longrightarrow
\text{mixed degree-six characteristic/anomaly class}.
}
\]

The next target is **v0.13: explicit descent / anomaly-inflow realization**. Starting from the degree-six polynomial, the task is to construct a five-dimensional secondary/Chern--Simons datum and its four-dimensional boundary variation, then keep that anomaly response sharply separated from stress-energy or Einstein dynamics.

No Lorentzian metric, causal structure, horizon entropy law, or gravitational field equation has yet been derived.