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
\text{semiclassical closure audit}
\to
\text{heat-kernel effective-action bridge}
\to
\text{realization-map dynamics}.
}
\]

Completed milestones: **v0.2–v0.17**. No derivation of Einstein dynamics from FCIG alone is claimed.

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
\boxed{
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1.
}
\]

Local descent gives a five-dimensional secondary/inflow form; global fermionic quantization is controlled by the Dirac index / Dai--Freed anomaly theory.

## Model XIV — functional-response no-go

For invariant \(S_{\rm inv}\), \(W'=W+S_{\rm inv}\) has the same anomaly while first functional derivatives may differ:

\[
\boxed{
\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.
}
\]

## Model XV — constitutive / semiclassical closure audit

Supplying independent renormalized gravitational and effective actions gives the conditional variational bridge

\[
\mathcal E^{\rm grav}_{\mu\nu}=T_{\mu\nu}^{\rm ren},
\]

but the action principle, renormalized couplings and any Jacobson-style Lorentzian horizon data are additional inputs.

## Model XVI — explicit operator / heat-kernel effective-action bridge

- `heat-kernel-bridge.md`
- `heat-kernel-bridge.py`
- `heat-kernel-bridge.bib`

Supply a four-dimensional Euclidean background and a realization map

\[
\Phi:M\to\mathcal B_{\rm FCIG}.
\]

Pulling back an FCIG line gives

\[
\Omega=\Phi^*F_{\rm FCIG}.
\]

For

\[
P=-\left(g^{\mu\nu}\nabla_\mu\nabla_\nu+E\right),
\]

standard heat-kernel geometry gives

\[
b_0=I,
\qquad
b_2=E+\frac16R,
\qquad
\boxed{b_4\supset\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}}.
\]

Thus

\[
\boxed{
b_4^{\rm FCIG}\supset
\frac1{12}(\Phi^*F_{\rm FCIG})_{\mu\nu}(\Phi^*F_{\rm FCIG})^{\mu\nu}.}
\]

This is an operator-level local spacetime effective-action invariant built from FCIG line curvature without identifying it with Riemann curvature. Divergent local coefficients renormalize couplings and are not parameter-free FCIG predictions.

References: Vassilevich (2003); Gilkey (1995); Birrell--Davies (1982); Wald (1993); Iyer--Wald (1994).

## Model XVII — realization-map / sigma-model dynamics

- Web: `realization-sigma.html`
- Source: `realization-sigma.md`
- Checker: `realization-sigma.py`
- Milestone bibliography: `realization-sigma.bib`

Use the pre-existing elliptic FCIG target

\[
\mathbb H=\{\tau=u+iY\mid Y>0\},
\qquad
 ds^2_{\mathbb H}=\frac{du^2+dY^2}{Y^2}.
\]

Promote

\[
\boxed{\Phi(x)=\tau(x)=u(x)+iY(x)}
\]

to a spacetime field with the standard harmonic-map action

\[
\boxed{
S_\Phi=\frac{Z_\Phi}{2}
\int_M\sqrt g\,
\frac{(\partial u)^2+(\partial Y)^2}{Y^2}.
}
\]

The explicit equations are

\[
\boxed{
\Box u-\frac2Y\partial u\cdot\partial Y=0,
\qquad
\Box Y+\frac{(\partial u)^2-(\partial Y)^2}{Y}=0.
}
\]

and the stress tensor is

\[
\boxed{
T^{(\Phi)}_{\mu\nu}
=\frac{Z_\Phi}{Y^2}
\left[
\partial_\mu u\partial_\nu u+
\partial_\mu Y\partial_\nu Y
-\frac12g_{\mu\nu}\big((\partial u)^2+(\partial Y)^2\big)
\right].
}
\]

The Hodge line supplies a second target-geometric structure. In the existing elliptic convention,

\[
\mathfrak f_H:=\frac{i}{2\pi}F_{\lambda_H}
=\frac{1}{4\pi}\omega_{\rm hyp},
\qquad
\omega_{\rm hyp}=\frac{du\wedge dY}{Y^2}.
\]

Therefore

\[
\boxed{
(\Phi^*\mathfrak f_H)_{\mu\nu}
=\frac{1}{4\pi Y^2}
(\partial_\mu u\partial_\nu Y-
\partial_\nu u\partial_\mu Y).
}
\]

This feeds the Model-XVI heat-kernel \(\Omega^2\) sector. Crucially, it is quartic in first derivatives after squaring, whereas \(S_\Phi\) is quadratic. Hence

\[
\boxed{
\Omega^2\text{ heat-kernel term}
\not\Rightarrow
\text{two-derivative sigma normalization }Z_\Phi.
}
\]

The normalization \(Z_\Phi\) remains constitutive input unless a further microscopic/determinant calculation derives it.

Two explicit witnesses sharpen the separation:

1. **Vertical geodesic:** \(u=u_0,\ Y=e^\varphi\) reduces to \(\Box\varphi=0\), but \(\Phi^*F_H=0\). Thus nonzero sigma stress can coexist with zero pulled-back line curvature.
2. **Hyperbolic identity-map sector:** an identity map on a hyperbolic two-dimensional factor is harmonic and has \(\Phi^*\omega_{\rm hyp}\neq0\), activating the curvature-squared determinant coupling.

On the true modular target \([\mathbb H/SL(2,\mathbf Z)]\), the local Poincare sigma density descends, while Hodge/theta lines can retain modular/metaplectic holonomy. Global nontrivial sectors require orbifold/stack patching.

References: Eells--Sampson (1964); Mumford (1983); Birkenhake--Lange (2004); Vassilevich (2003) for the heat-kernel insertion.

## Current controlled frontier

The realization map is now typed and dynamical, but its two-derivative normalization is not yet derived. The active target is **v0.18 — induced realization-map dynamics from determinants**.

The key question is whether an explicit slowly varying operator family \(P(\Phi)\) generates

\[
\frac12\int_M\sqrt g\,G^{\rm ind}_{AB}(\Phi)
\partial_\mu\Phi^A\partial^\mu\Phi^B
\]

inside \(\tfrac12\log\det P(\Phi)\), and whether the induced spectral metric \(G^{\rm ind}\) coincides with, is proportional to, or differs from the pre-existing Fisher/Hodge/Poincare metric.

Only such a calculation can turn \(Z_\Phi\) from external constitutive data into a derived quantity. Lorentzian/horizon closure remains separate.