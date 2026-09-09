# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — milestone gates
- `references.bib` — canonical bibliography
- milestone `.bib` files — source sets for individual models
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
\text{transgression / pushforward}
\to
\text{Deligne--RR closure}
\to
\text{structure-group audit}
\to
\text{mixed anomaly polynomial}
\to
\text{descent / inflow}
\to
\text{functional-response no-go}.
}
\]

Completed milestones: **v0.2–v0.14**. No Lorentzian/gravitational closure is claimed.

## Models I–III — flat theta / abelian laboratories

The elliptic and ppav models establish exact theta-state counting, determinant/Hodge response, Poisson-resummed Bergman lattice sectors, and finite Weil/metaplectic holonomy. Main files: `elliptic-model.md`, `modular-holonomy.md`, `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md` and their Python checkers.

## Model IV — compact hyperbolic curves

`hyperbolic-model.md` / `hyperbolic-loop.py`

The curved model separates local Bergman-curvature data from global geodesic/holonomy data. The Mumford determinant relation blocks a universal extrapolation of the flat-ppav determinant coefficient.

## Model V — Quillen / analytic torsion

`quillen-refinement.md` / `quillen-refinement.py`

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

## Model VI — differential cohomology / determinant holonomy

`differential-holonomy.md` / `differential-holonomy.py`

A unitary line with connection defines

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

carrying topology, curvature, and loop holonomy in one object.

## Models VII–VIII — transgression and pushforward no-go

`response-transgression.md` / `factorized-pushforward.md`

Loop transgression is a genuine standard response operation, while factorized degree restoration satisfies

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)=n\widehat{\mathcal A}
}
\]

on connected components and therefore cannot create an independent degree-two response direction.

## Models IX–X — \(\widehat\kappa_1\), Quillen, and global Deligne--RR

`kappa1-quillen.md` / `global-deligne-rr.md`

For \(\omega=K_{X/B}\),

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(\omega)^2\bigr),
\qquad
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the fixed metrized Deligne-pairing convention. Topology, local curvature, and holonomy obey the same connection-level identity.

## Model XI — determinant trace / Spin\(^c\) / reconstruction no-go

`structure-group-bridge.md` / `structure-group-bridge.py`

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

Fixing the determinant connection leaves an affine space over \(\Omega^1(M;\mathfrak{su}(E))\). Thus determinant data fixes the trace/Ricci sector but not a generic nonabelian frame connection for \(n>1\). K3 and Spin\(^c\) provide explicit tests.

## Model XII — mixed characteristic classes / anomaly polynomial

`mixed-characteristic.md` / `mixed-characteristic.py` / `mixed-characteristic.bib`

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z)
\]

is a legitimate mixed invariant. The line-twisted Dirac index has degree-six piece

\[
\boxed{
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1.
}
\]

## Model XIII — five-dimensional descent / global anomaly inflow

`descent-inflow.md` / `descent-inflow.py` / `descent-inflow.bib`

Locally, with \(da=c\),

\[
I_5^{(0)}=a\wedge\left(\frac16c^2-\frac1{24}p_1\right),
\qquad
dI_5^{(0)}=I_6,
\]

and under \(a\mapsto a+d\alpha\),

\[
\delta I_5^{(0)}
=d\left[\alpha\left(\frac16c^2-\frac1{24}p_1\right)\right].
\]

The rational fermion polynomial is globally quantized through the Dirac index / Dai--Freed anomaly theory, not by treating each fractional term as an arbitrary integral differential character.

## Model XIV — background-field functional response no-go

- Web: `functional-response.html`
- Source: `functional-response.md`
- Checker: `functional-response.py`
- Milestone bibliography: `functional-response.bib`

Let \(\mathcal B\) be the background-field space, \((\mathscr L_{\rm an},\nabla^{\rm an})\to\mathcal B\) the anomaly line, and \(Z\) a section. In a local trivialization, \(Z=e^{-W}\).

For any globally defined gauge/diffeomorphism-invariant functional \(S_{\rm inv}\),

\[
W'=W+S_{\rm inv}
\]

has the same gauge/diffeomorphism anomaly, while

\[
\boxed{
J'^\mu-J^\mu
=\frac1{\sqrt{|g|}}\frac{\delta S_{\rm inv}}{\delta A_\mu},
\qquad
T'_{\mu\nu}-T_{\mu\nu}
=-\frac2{\sqrt{|g|}}\frac{\delta S_{\rm inv}}{\delta g^{\mu\nu}}.
}
\]

Hence

\[
\boxed{
\text{same anomaly class}
\not\Rightarrow
\text{same }W,\ J,\ T_{\mu\nu}.
}
\]

An explicit 4D witness is

\[
S_\beta=-\frac\beta4\int\sqrt{|g|}\,F_{\mu\nu}F^{\mu\nu},
\]

which preserves gauge/diffeomorphism invariance and classical Weyl invariance but shifts both current and stress tensor. In four dimensions the stress shift is traceless.

The model also separates the consistent current \(\delta W/\delta A\) from the Bardeen--Zumino covariant current and records that anomaly-line curvature/holonomy constrain obstruction/integrability data on background space but do not select a section or its first functional derivatives.

References: Wess--Zumino (1971); Bardeen--Zumino (1984); Osborn (1991); Freed (2014); Dai--Freed (1994); Birrell--Davies (1982).

## Current controlled frontier

The direct anomaly-to-dynamics route is now closed:

\[
\boxed{
\text{anomaly geometry}
\not\Rightarrow
\text{unique effective action}
\not\Rightarrow
\text{unique stress tensor or Einstein dynamics}.
}
\]

The next controlled target is **v0.15 — constitutive / semiclassical closure audit**. It must supply an additional dynamical principle explicitly — e.g. a gravitational functional plus variational principle, or a separately justified local horizon/thermodynamic closure — and then test exactly where FCIG state-count/anomaly data can enter.

No Lorentzian metric, causal structure, horizon entropy law, or Einstein equation has yet been derived from FCIG alone.
