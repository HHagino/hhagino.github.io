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
\to\text{intrinsic elliptic spectral curvature}
\to\text{adiabatic KK response}.
}
\]

Completed milestones: **v0.2–v0.20**. No derivation of Einstein dynamics from FCIG alone is claimed.

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
\qquad
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

## Model XVI — explicit operator / heat-kernel bridge

For a supplied realization map \(\Phi:M\to\mathcal B_{\rm FCIG}\), the pulled-back line curvature

\[
\Omega=\Phi^*F_{\rm FCIG}
\]

enters a physical Laplace-type operator. Standard heat-kernel geometry gives

\[
\boxed{b_4\supset\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}},
\]

so FCIG line curvature enters a one-loop spacetime effective action without being identified with Riemann curvature.

## Model XVII — realization-map dynamics

On the elliptic target

\[
\mathbb H=\{\tau=u+iY\mid Y>0\},
\qquad ds^2_{\mathbb H}=\frac{du^2+dY^2}{Y^2},
\]

promote \(\Phi=(u,Y)\) to a harmonic-map field. The Hodge-curvature pullback is four-derivative after squaring, so it does not determine the two-derivative sigma normalization.

Sources: `realization-sigma.md`, `realization-sigma.py`, `realization-sigma.bib`.

## Model XVIII — induced determinant metric no-gos

For diagonal heavy scalars,

\[
\boxed{G^{\rm ind}_{AB}=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N},
\qquad s_i=\sqrt{V_i}.
\]

One species has rank at most one; two species are degenerate or locally flat; unconstrained higher-dimensional mass maps turn target-metric matching into inverse design.

Sources: `induced-metric.md`, `induced-metric.py`, `induced-metric.bib`.

## Model XIX — intrinsic spectral--Hodge identity

For the area-one elliptic torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4.
\]

Therefore

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=\frac1{4Y^2}d\tau\wedge d\bar\tau
=F_{\lambda_H}.
}
\]

The actual full torus spectrum regenerates the pre-existing Hodge curvature with the same coefficient and no adjustable spectral map.

Sources: `intrinsic-spectral.md`, `intrinsic-spectral.py`, `intrinsic-spectral.bib`.

## Model XX — adiabatic elliptic / Kaluza--Klein response

- Web: `adiabatic-elliptic.html`
- Source: `adiabatic-elliptic.md`
- Checker: `adiabatic-elliptic.py`
- Milestone bibliography: `adiabatic-elliptic.bib`

Let \(\tau=\tau(x)\) vary over a four-dimensional base and take the locally trivial fixed-volume torus metric

\[
 ds_6^2=g_{\mu\nu}dx^\mu dx^\nu+L^2G_{ab}(\tau(x))dy^ady^b,
\qquad \det G=1.
\]

The coordinate Fourier basis is \(\tau\)-independent in this restricted scalar model, so there is no local Berry/off-diagonal mode mixing and

\[
\boxed{M_{m,n}^2=\frac{4\pi^2}{L^2Y}|m\tau-n|^2.}
\]

The total-space curvature contains

\[
\boxed{
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau,
}
\]

so the local two-derivative tensor shape is intrinsically Poincare. Its one-loop coefficient is UV-sensitive and renormalizes the local six-dimensional Einstein--Hilbert term.

For the finite nonlocal tower response, define

\[
Q_{m,n}=\frac{|m\tau-n|^2}{Y},
\qquad
Z_\tau(s)=\sum{}'Q_{m,n}^{-s}.
\]

Epstein analytic continuation and the self-dual functional equation give

\[
Z_\tau(-1)=0,
\qquad
Z_\tau'(-1)=-\frac1{\pi^3}Z_\tau(2).
\]

Using the exact hyperbolic identities

\[
\nabla^2Q=Qg_{\rm hyp},
\qquad
|dQ|_{g_{\rm hyp}}^2=Q^2,
\]

the analytically subtracted tower tensor is

\[
\boxed{
\mathcal T^{\rm fin}_{AB}
=\frac1{\pi^3}
\left(\nabla_A\nabla_BZ_\tau(2)-Z_\tau(2)g^{\rm hyp}_{AB}\right),
\qquad
\operatorname{tr}_{g_{\rm hyp}}\mathcal T^{\rm fin}=0.
}
\]

Equivalently, with

\[
\mathcal G_4(\tau)=\sum{}'(m\tau-n)^{-4},
\]

\[
\boxed{
G^{\rm fin}_{(2)}
=-\frac1{16\pi^3L^2}
\operatorname{Re}\left[\mathcal G_4(\tau)(d\tau)^2\right].
}
\]

This finite threshold is modular and trace-free. It is **not** a positive Poincare sigma metric by itself. The full renormalized kinetic tensor has the form

\[
\boxed{
G^{\rm ren}=Z_Rg_{\rm hyp}+G^{\rm fin}_{(2)}+\cdots,
}
\]

where \(Z_R\) remains a renormalized local coupling.

Thus Models XIX and XX are genuinely different spectral projections:

\[
\boxed{
\text{Model XIX: finite }(1,1)\text{ Chern curvature}\propto g_{\rm hyp},
\qquad
\text{Model XX: finite spacetime threshold is trace-free weight }4.
}
\]

References: Maharana--Schwarz (1993); Vassilevich (2003); von Gersdorff (2008); Terras (1980, 2013); Apostol (1990).

## Current controlled frontier

The single-scalar elliptic adiabatic problem is now closed at two derivatives in the stated analytic-subtraction convention. The next target is **v0.21 — field-content / supertrace completion audit**.

The question is whether the finite automorphic threshold

\[
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2]
\]

survives, cancels or changes tensor structure when the microscopic determinant contains a physically specified combination of scalars, fermions, vectors, ghosts and bundle connections. Species/statistics may not be chosen merely to obtain a desired metric.

No Lorentzian/horizon closure is claimed.
