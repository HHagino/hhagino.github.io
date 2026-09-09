# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository distinguishes **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research/citation policy
- `ROADMAP.md` — active gates and completed milestones
- `references.bib` — general bibliography
- milestone `.bib` files — source sets for individual models
- `citation-map.md` / `cited-synthesis.md` — citation provenance and audited synthesis

## Status

Completed milestones: **v0.2–v0.23**.

The controlled chain is

\[
\boxed{
\text{theta / ppav}
\to\text{curved curves}
\to\text{Quillen / differential cohomology}
\to\text{Deligne--RR}
\to\text{anomaly / response no-gos}
\to\text{operator / heat-kernel bridge}
\to\text{intrinsic elliptic spectrum}
\to\text{adiabatic KK response}
\to\text{spin/multiplet automorphic thresholds}.
}
\]

No derivation of Einstein dynamics or horizon thermodynamics from FCIG alone is claimed.

## Models I–X — determinant / cohomological foundation

The elliptic, ppav and curved-curve laboratories establish exact theta-state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos and the metrized Deligne--Riemann--Roch identity

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the canonical smooth curve-family model.

## Models XI–XV — structure-group, anomaly and response audits

The determinant line retains only the trace/Ricci sector of a generic \(U(n)\) connection,

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

Independent line and frame connections can enter the same index/anomaly polynomial,

\[
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1,
\]

but anomaly data alone do not fix the effective action or its first response:

\[
\boxed{\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.}
\]

A gravitational equation appears only after an independent renormalized variational principle is supplied.

## Models XVI–XVIII — operator / realization bridge

A supplied realization map \(\Phi:M\to\mathcal B_{\rm FCIG}\) puts pulled-back FCIG line curvature into an ordinary Laplace-type operator. Arbitrary heavy scalar masses induce

\[
G^{\rm ind}_{AB}
=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N},
\]

so freely chosen masses turn target-metric matching into inverse design rather than prediction.

## Model XIX — intrinsic spectral--Hodge identity

For the area-one elliptic torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

and

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=F_{\lambda_H}
=\frac1{4Y^2}d\tau\wedge d\bar\tau.
}
\]

This is the first no-fit spectral regeneration of the pre-existing elliptic Hodge curvature.

Sources: `intrinsic-spectral.md`, `intrinsic-spectral.py`, `intrinsic-spectral.bib`.

## Model XX — adiabatic elliptic / KK response

For the fixed-volume local torus family,

\[
M_{m,n}^2=\frac{4\pi^2}{L^2Y}|m\tau-n|^2,
\qquad
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau.
\]

The local Poincare-shaped kinetic normalization is UV/counterterm sensitive. Epstein analytic continuation gives the finite one-real-scalar threshold

\[
\boxed{
G^{\rm fin}_{\rm scalar}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
\qquad
\operatorname{tr}_{g_{\rm hyp}}G^{\rm fin}_{\rm scalar}=0.
}
\]

Sources: `adiabatic-elliptic.md`, `adiabatic-elliptic.py`, `adiabatic-elliptic.bib`.

## Models XXI–XXII — field-content and spin thresholds

The local six-dimensional \(R_6\) response, normalized to one real scalar, is

\[
\boxed{\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2.}
\]

True spin fields carry Lorentz connections and curvature endomorphisms. Model XXII derives

\[
\Delta G_{\rm tr}^{(R)}
=\frac{(-1)^F(2C_R-e_R)}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
\]

For a specified 6d \(\mathcal N=(1,0)\) vector multiplet, local and weight-four terms cancel while a positive finite trace term survives:

\[
\boxed{
G_{\rm vector}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp}.
}
\]

Sources: `field-content-supertrace.*`, `spin-threshold.*`.

## Model XXIII — hyper/tensor multiplet completion

- Web: `hyper-tensor-threshold.html`
- Source: `hyper-tensor-threshold.md`
- Checker: `hyper-tensor-threshold.py`
- Milestone bibliography: `hyper-tensor-threshold.bib`

For the parity-even nonzero-tower sector, a non-chiral real two-form has

\[
(C_{\rm local},A_{\mathcal G_4},B_{Z_2})_{B,\rm nonch}
=\left(-6,-\frac38,\frac38\right).
\]

Using the standard holomorphic-factorization / determinant-norm prescription for the self-dual field magnitude gives

\[
(C_{\rm local},A,B)_{B^+}
=\left(-3,-\frac3{16},\frac3{16}\right),
\]

with theta characteristics, zero modes and chiral/global phases kept separate.

The completed 6d \(\mathcal N=(1,0)\) multiplet table is

\[
\boxed{
\begin{array}{c|ccc}
\text{multiplet}&C_{\rm local}&A_{\mathcal G_4}&B_{Z_2}\\ \hline
\text{vector}&0&0&\frac18\\
\text{hyper}&6&0&-\frac1{16}\\
\text{tensor}&0&0&\frac18
\end{array}}
\]

so

\[
\boxed{
G_{\rm vector}^{\rm fin}=G_{\rm tensor}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp},
\qquad
G_{\rm hyper}^{\rm fin}
=-\frac{Z_\tau(2)}{16\pi^3L^2}g_{\rm hyp}.
}
\]

All three multiplets cancel the finite weight-four trace-free tensor in this restricted background. For independently fixed multiplicities,

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{2n_V-n_H+2n_T}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
}
\]

This coefficient is a kinetic threshold, not an anomaly coefficient. Multiplicities may not be chosen merely to engineer a desired sign or cancellation.

## Current frontier

The next controlled question is to compare the completed vector/hyper/tensor threshold table with **independently specified 6d multiplet combinations and their anomaly polynomials**, while retaining the strict distinction

\[
\boxed{
\text{anomaly polynomial}
\neq
\text{local counterterm}
\neq
\text{finite automorphic kinetic threshold}.
}
\]

Self-dual global phases, nontrivial torus bundles, background gauge fields and the cusp/EFT breakdown remain separate extensions. Lorentzian/horizon closure remains inactive.
