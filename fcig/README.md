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
\to\text{induced determinant metric}
\to\text{intrinsic elliptic spectral curvature}.
}
\]

Completed milestones: **v0.2–v0.19**. No derivation of Einstein dynamics from FCIG alone is claimed.

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

Sources: `realization-sigma.md`, `realization-sigma.py`, `realization-sigma.bib`.

## Model XVIII — induced realization-map metric from determinants

For independent heavy scalars with \(P_i=-\partial^2+V_i(\Phi)\), the constant-background one-loop 1PI \(p^2\) response gives

\[
\boxed{G^{\rm ind}_{AB}=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}.}
\]

Writing \(s_i=\sqrt{V_i}\),

\[
\boxed{G^{\rm ind}=\frac1{48\pi^2}s^*\delta_{\mathbb R^N}.}
\]

Hence one species has rank at most one; two species are degenerate or locally flat; three species can fit local negative-curvature patches but cannot give a complete regular immersion of all \(\mathbb H\) into \(\mathbb R^3\) by Hilbert's theorem. Arbitrary mass functions therefore turn metric matching into inverse design rather than prediction.

Sources: `induced-metric.md`, `induced-metric.py`, `induced-metric.bib`.

## Model XIX — intrinsic elliptic spectral metric

- Web: `intrinsic-spectral.html`
- Source: `intrinsic-spectral.md`
- Checker: `intrinsic-spectral.py`
- Milestone bibliography: `intrinsic-spectral.bib`

Model XIX removes the arbitrary mass-map freedom. On

\[
E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),
\qquad \tau=u+iY,
\]

use the area-one flat metric

\[
\boxed{ds^2_\tau=\frac{|dz|^2}{Y}}.
\]

With \(z=x+\tau t\), the Fourier modes \(e^{2\pi i(mx+nt)}\) have the exact spectrum

\[
\boxed{\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2.}
\]

The spectrum is modular invariant as a multiset by an integral lattice relabeling. Its zeta function is the nonholomorphic Epstein/Eisenstein lattice sum, and the Kronecker limit formula yields

\[
\boxed{\det{}'\Delta_\tau=Y|\eta(\tau)|^4.}
\]

Because \(\eta\) is holomorphic and nonvanishing on \(\mathbb H\),

\[
\partial\bar\partial\log|\eta|^4=0.
\]

Therefore

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=\frac1{4Y^2}d\tau\wedge d\bar\tau
=F_{\lambda_H}.
}
\]

This is an exact **intrinsic spectral--Hodge identity** in the same elliptic convention used by Model I. Unlike Model XVIII, the target curvature is regenerated from the fixed full torus spectrum with no adjustable \(V_i(\tau)\).

The statement is deliberately at the moduli-space Chern-curvature level. It does **not** yet derive a spacetime kinetic term for a slowly varying modulus \(\tau(x)\). The full real Hessian also contains harmonic trace-free information from \(\eta\); the canonical equality is the mixed \((1,1)\) curvature identity above.

References: Ray--Singer (1973); Quillen (1985); Osgood--Phillips--Sarnak (1988); Faulhuber (2020/2021); NIST DLMF Chapter 23.

## Current controlled frontier

The elliptic target geometry now has two independent realizations:

\[
\boxed{
\text{Hodge metric/line geometry}
\quad\leftrightarrow\quad
\text{intrinsic zeta-spectral curvature}.
}
\]

The remaining bottleneck is dynamical rather than purely moduli-geometric. The next target is **v0.20 — adiabatic elliptic family / Kaluza--Klein response**: let \(\tau=\tau(x)\) vary over a spacetime/base, construct the corresponding total-space/fibered operator, include mode-basis connection and off-diagonal mixing, and derive the genuine spacetime two-derivative coefficient instead of identifying it with the moduli Hessian by analogy.

No Lorentzian/horizon closure is claimed.