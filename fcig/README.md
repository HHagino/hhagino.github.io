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
\to\text{curved curves}
\to\text{Quillen / differential cohomology}
\to\text{Deligne--RR closure}
\to\text{anomaly / response audits}
\to\text{semiclassical closure audit}
\to\text{heat-kernel bridge}
\to\text{realization-map dynamics}
\to\text{induced determinant metric}.
}
\]

Completed milestones: **v0.2–v0.18**. No derivation of Einstein dynamics from FCIG alone is claimed.

## Models I–X — geometric / determinant foundation

The elliptic, ppav and curved-curve laboratories establish exact theta/state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos and the global metrized Deligne--Riemann--Roch closure

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the canonical smooth curve-family model.

## Model XI — structure-group bridge audit

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

The determinant connection retains trace/Ricci information but cannot reconstruct a generic nonabelian frame connection for \(n>1\).

## Models XII–XIII — mixed anomaly polynomial and descent

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z),
\]

and

\[
\boxed{[\widehat A(TM)\operatorname{ch}(L)]_{(6)}=\frac16c_1^3-\frac1{24}c_1p_1.}
\]

Local descent gives a five-dimensional secondary/inflow form; global fermionic quantization is controlled by the Dirac index / Dai--Freed anomaly theory.

## Model XIV — functional-response no-go

For invariant \(S_{\rm inv}\), \(W'=W+S_{\rm inv}\) has the same anomaly while first functional derivatives may differ:

\[
\boxed{\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.}
\]

## Model XV — constitutive / semiclassical closure audit

Supplying independent renormalized gravitational and effective actions gives the conditional variational bridge

\[
\mathcal E^{\rm grav}_{\mu\nu}=T_{\mu\nu}^{\rm ren},
\]

but the action principle, renormalized couplings and Jacobson-style Lorentzian horizon data remain additional inputs.

## Model XVI — explicit operator / heat-kernel effective-action bridge

For a supplied realization map \(\Phi:M\to\mathcal B_{\rm FCIG}\), the pulled-back line curvature

\[
\Omega=\Phi^*F_{\rm FCIG}
\]

enters a physical Laplace-type operator. Standard heat-kernel geometry gives

\[
\boxed{b_4\supset\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}},
\]

so the FCIG line curvature contributes to a one-loop spacetime effective action without being identified with Riemann curvature. Divergent local coefficients renormalize couplings and are not parameter-free predictions.

References: Vassilevich (2003); Gilkey (1995); Birrell--Davies (1982); Wald (1993); Iyer--Wald (1994).

## Model XVII — realization-map / sigma-model dynamics

- `realization-sigma.md`
- `realization-sigma.py`
- `realization-sigma.bib`

Use the pre-existing elliptic target

\[
\mathbb H=\{\tau=u+iY\mid Y>0\},
\qquad ds^2_{\mathbb H}=\frac{du^2+dY^2}{Y^2}.
\]

Promote \(\Phi=(u,Y)\) to a harmonic-map field,

\[
S_\Phi=\frac{Z_\Phi}{2}\int_M\sqrt g\,\frac{(\partial u)^2+(\partial Y)^2}{Y^2},
\]

with the standard equations and stress tensor. The Hodge curvature pullback is bilinear in first derivatives, so the Model-XVI \(\Omega^2\) term is four-derivative in \(\Phi\) and does not determine the two-derivative coefficient \(Z_\Phi\).

References: Eells--Sampson (1964); Mumford (1983); Birkenhake--Lange (2004); Vassilevich (2003).

## Model XVIII — induced realization-map metric from determinants

- Web: `induced-metric.html`
- Source: `induced-metric.md`
- Checker: `induced-metric.py`
- Milestone bibliography: `induced-metric.bib`

For independent heavy real scalars

\[
P_i(\Phi)=-\partial^2+V_i(\Phi),\qquad V_i>0,
\]

define the induced two-derivative response operationally by the \(p^2\) coefficient of the one-loop 1PI two-point function around a constant background. In the fixed Euclidean bubble convention,

\[
I(p)=I(0)-\frac{p^2}{96\pi^2V}+O(p^4),
\]

so

\[
\boxed{G^{\rm ind}_{AB}=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}.}
\]

Writing \(s_i=\sqrt{V_i}\) gives the structural identity

\[
\boxed{G^{\rm ind}=\frac1{48\pi^2}\sum_i ds_i^2=\frac1{48\pi^2}s^*\delta_{\mathbb R^N}.}
\]

This yields exact obstructions:

\[
\boxed{
\begin{aligned}
N=1&:\ \operatorname{rank}G^{\rm ind}\le1,\\
N=2&:\ G^{\rm ind}\text{ is degenerate or locally flat},\\
N=3&:\ \text{local hyperbolic fitting is possible, but complete }\mathbb H\to\mathbb R^3\text{ is forbidden by Hilbert.}
\end{aligned}}
\]

Hence two diagonal species can restore rank but can never reproduce the Poincare curvature \(K=-1\). This remains true under modular invariance. An explicit invariant witness uses Klein's modular invariant \(J\):

\[
V_1=M^2e^{2a\Re J(\tau)},\qquad V_2=M^2e^{2a\Im J(\tau)}.
\]

At regular points it has rank two, but the induced metric is still locally flat.

The main predictivity result is therefore:

\[
\boxed{
\text{a determinant induces a target metric only after a microscopic mass/operator map is supplied;}
\quad
\text{arbitrary spectral data can encode the desired metric by inverse design.}
}
\]

The one-loop coefficient above is intentionally tied to the constant-background 1PI two-point definition. Chan and modern covariant derivative-expansion methods provide the standard context, while Canevarolo--Prokopec document that off-shell gradient-expansion prescriptions require care.

References: Chan (1986); Henning--Lu--Murayama (2018); Canevarolo--Prokopec (2024); NIST DLMF Chapter 23; do Carmo (1976); Hilbert (1901).

## Current controlled frontier

The remaining bottleneck is no longer whether a determinant **can** make a metric. It can. The question is whether FCIG fixes the microscopic operator family without reverse-engineering the answer.

The next target is **v0.19 — intrinsic elliptic spectral metric**: use the actual modular-covariant spectrum already present in the elliptic FCIG laboratory (flat-torus Laplacian / theta / Quillen data), rather than arbitrary functions \(V_i(\tau)\), and compute its moduli response.

A particularly concrete test is the area-normalized torus spectrum

\[
\lambda_{m,n}(\tau)\propto\frac{|m\tau-n|^2}{\Im\tau},
\]

whose multiset is modular invariant. The goal is to determine whether its zeta/determinant or adiabatic two-point response produces the Poincare/Hodge metric with a fixed coefficient, or merely another scheme-dependent/constitutive structure.

Lorentzian/horizon closure remains separate.