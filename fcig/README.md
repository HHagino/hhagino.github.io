# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — milestone gates
- `references.bib` — general bibliography
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
\text{functional-response no-go}
\to
\text{semiclassical closure audit}.
}
\]

Completed milestones: **v0.2–v0.15**. No derivation of Einstein dynamics from FCIG alone is claimed.

## Models I–III — flat theta / abelian laboratories

Exact theta-state counting, determinant/Hodge response, Poisson-resummed Bergman lattice sectors, and finite Weil/metaplectic holonomy. Main files: `elliptic-model.md`, `modular-holonomy.md`, `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md`.

## Models IV–VI — curved Bergman / Quillen / differential cohomology

`hyperbolic-model.md`, `quillen-refinement.md`, `differential-holonomy.md`.

These models separate local curvature, global geodesic/holonomy data, Quillen versus elementary \(L^2\) determinant metrics, and package a unitary line with connection as

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z).
\]

## Models VII–X — transgression, pushforward, and Deligne--RR closure

`response-transgression.md`, `factorized-pushforward.md`, `kappa1-quillen.md`, `global-deligne-rr.md`.

Loop transgression is a genuine response operation; factorized degree restoration cannot generate a new degree-two direction; and for smooth curve families the fixed metrized Deligne-pairing convention gives

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}.
\]

## Model XI — structure-group bridge audit

`structure-group-bridge.md`

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

The determinant connection retains the trace/Ricci sector but cannot reconstruct a generic nonabelian frame connection for \(n>1\).

## Models XII–XIII — mixed anomaly polynomial and descent

`mixed-characteristic.md`, `descent-inflow.md`.

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z),
\]

and the line-twisted Dirac index has

\[
\boxed{
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1.
}
\]

Locally this admits the five-dimensional secondary form

\[
I_5^{(0)}=a\wedge\left(\frac16c^2-\frac1{24}p_1\right),
\qquad dI_5^{(0)}=I_6,
\]

with four-dimensional boundary descent under \(a\mapsto a+d\alpha\). Global fermionic quantization is controlled by the Dirac index / Dai--Freed anomaly theory.

## Model XIV — functional-response no-go

`functional-response.md`, `functional-response.py`, `functional-response.bib`.

For any globally defined invariant functional \(S_{\rm inv}\),

\[
W'=W+S_{\rm inv}
\]

has the same gauge/diffeomorphism anomaly while its first functional derivatives change. Hence

\[
\boxed{
\text{same anomaly class}
\not\Rightarrow
\text{same }W,J,T_{\mu\nu}.
}
\]

This closes the direct anomaly-to-dynamics route.

## Model XV — constitutive / semiclassical closure audit

- Web: `semiclassical-closure.html`
- Source: `semiclassical-closure.md`
- Checker: `semiclassical-closure.py`
- Milestone bibliography: `semiclassical-closure.bib`

### Semiclassical variational track

Supply independently

\[
S_{\rm grav}^{\rm ren}[g]
\quad\text{and}\quad
W_{\rm ren}[A,g].
\]

With

\[
\mathcal E^{\rm grav}_{\mu\nu}
:=\frac{2}{\sqrt{|g|}}\frac{\delta S_{\rm grav}^{\rm ren}}{\delta g^{\mu\nu}},
\qquad
T_{\mu\nu}^{\rm ren}
:=-\frac{2}{\sqrt{|g|}}\frac{\delta W_{\rm ren}}{\delta g^{\mu\nu}},
\]

stationarity gives

\[
\boxed{\mathcal E^{\rm grav}_{\mu\nu}=T_{\mu\nu}^{\rm ren}}.
\]

This is a valid **conditional bridge**, but the gravitational action and variational principle are additional input.

Finite local counterterms shift the renormalized stress tensor and gravitational couplings. A prediction is meaningful only after renormalization conditions/couplings are fixed.

The exact FCIG insertion point is therefore a derived spacetime functional

\[
\boxed{W_{\rm FCIG}^{\rm ren}[A,g]},
\]

not the anomaly class by itself.

### Local-horizon track

Jacobson's route independently requires Lorentzian local Rindler horizons, Unruh temperature, matter heat flux, an area-proportional entropy variation and the Clausius relation.

The current FCIG quantities

\[
S_k^{\rm cap}=\log h^0(X,L^k),
\qquad
s_k=\log B_k-d\log k
\]

do **not yet** supply a canonical Lorentz-covariant codimension-two horizon entropy density. A new horizon map/local limit would be required.

A legitimate positive horizon bridge remains available if FCIG first derives a local diffeomorphism-invariant spacetime term \(\Delta L_{\rm FCIG}\): metric variation gives its dynamical correction and Wald/Iyer--Wald Noether charge gives its stationary-horizon entropy correction.

References: Jacobson (1995); Wald (1993); Iyer--Wald (1994); Wald (1978); Hollands--Wald (2001, 2005); Birrell--Davies (1982).

## Current controlled frontier

The dynamical bottleneck is now sharply located at

\[
\boxed{
\text{FCIG geometric/determinant data}
\xrightarrow{\ ?\ }
W_{\rm FCIG}^{\rm ren}[A,g]
\text{ or }\Delta L_{\rm FCIG}.
}
\]

The next target is **v0.16 — local heat-kernel / effective-action bridge**: start from an explicit physical elliptic/Dirac-type operator, derive the local heat-kernel/Seeley--DeWitt contributions to the determinant effective action, separate scheme-dependent gravitational counterterms from controlled finite pieces, and then vary the resulting action.

The horizon/thermodynamic track remains inactive until such a spacetime realization exists.
