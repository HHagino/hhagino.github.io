# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository distinguishes **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to stay readable and independently checkable.

- `RESEARCH_POLICY.md` — research/citation policy
- `ROADMAP.md` — active gates and completed milestones
- `references.bib` — general bibliography
- milestone `.bib` files — source sets for individual models
- `citation-map.md` / `cited-synthesis.md` — citation provenance and synthesis

## Status

Completed milestones: **v0.2–v0.22**.

The current controlled chain is

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
\to\text{spin-dependent automorphic thresholds}.
}
\]

No derivation of Einstein dynamics or horizon thermodynamics from FCIG alone is claimed.

## Geometric / determinant foundation — Models I–X

The elliptic, ppav and curved-curve laboratories establish exact theta-state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos and the metrized Deligne--Riemann--Roch closure

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the canonical smooth curve-family model.

## Structure-group and anomaly audits — Models XI–XV

The determinant line retains only the trace/Ricci part of a generic \(U(n)\) connection:

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

but anomaly data do not determine a unique effective action or first response:

\[
\boxed{\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.}
\]

A gravitational equation appears only after an independent renormalized variational principle is supplied.

## Operator and realization bridge — Models XVI–XVIII

A supplied realization map \(\Phi:M\to\mathcal B_{\rm FCIG}\) puts FCIG line curvature into an ordinary Laplace-type operator,

\[
b_4\supset\frac1{12}(\Phi^*F_{\rm FCIG})_{\mu\nu}(\Phi^*F_{\rm FCIG})^{\mu\nu}.
\]

For arbitrary heavy scalar masses, the one-loop two-derivative target metric is

\[
G^{\rm ind}_{AB}
=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N},
\]

so unconstrained masses turn metric matching into inverse design rather than prediction.

## Model XIX — intrinsic spectral--Hodge identity

For the area-one elliptic torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

and therefore

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

Thus Model XIX and Model XX are different spectral projections: finite \((1,1)\) moduli curvature versus finite trace-free spacetime threshold.

Sources: `adiabatic-elliptic.md`, `adiabatic-elliptic.py`, `adiabatic-elliptic.bib`.

## Model XXI — field-content audit

The six-dimensional local \(R_6\) response, normalized to one real minimal scalar, is

\[
\boxed{\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2.}
\]

Hence the local response is not a naive signed physical-polarization count. A 6d \(\mathcal N=(1,0)\) vector multiplet gives the parity-even local cancellation

\[
\boxed{-2+2=0.}
\]

True spinors/vectors nevertheless carry spin connections and curvature endomorphisms, so their finite threshold cannot be obtained from the scalar answer by component counting alone.

Sources: `field-content-supertrace.md`, `field-content-supertrace.py`, `field-content-supertrace.bib`.

## Model XXII — spin-connection automorphic thresholds

- Web: `spin-threshold.html`
- Source: `spin-threshold.md`
- Checker: `spin-threshold.py`
- Milestone bibliography: `spin-threshold.bib`

For winding \(\lambda=(p,q)\) with

\[
Q_\lambda=\lambda^TG(\tau)\lambda,
\]

the elliptic Levi-Civita connection obeys the exact vector-representation identity

\[
\boxed{
\operatorname{tr}_{\rm vec}[(\lambda\cdot\omega)^2]
=\frac{L^2}{2}Q_\lambda\,
\frac{(\partial u)^2+(\partial Y)^2}{Y^2}.
}
\]

With Lorentz Dynkin index \(C_R\) and \(\operatorname{tr}_R E=e_RR_6\), the finite representation-dependent Poincare-trace correction is

\[
\boxed{
\Delta G_{\rm tr}^{(R)}
=\frac{(-1)^F(2C_R-e_R)}{16\pi^3L^2}
Z_\tau(2)\,g_{\rm hyp}.
}
\]

In the fixed parity-even conventions:

\[
\boxed{
\begin{aligned}
G_D^{\rm fin}
&=\frac1{2\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2]
-\frac1{8\pi^3L^2}Z_\tau(2)g_{\rm hyp},\\[1mm]
G_{A+gh}^{\rm fin}
&=-\frac1{4\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2]
+\frac3{16\pi^3L^2}Z_\tau(2)g_{\rm hyp},\\[1mm]
G_{W}^{\rm fin}
&=\frac1{4\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2]
-\frac1{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
\end{aligned}}
\]

For a specified 6d \(\mathcal N=(1,0)\) vector multiplet, the weight-four trace-free terms cancel while the spin-transport trace term survives:

\[
\boxed{
G_{\rm vm}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}\,g_{\rm hyp}.
}
\]

Since \(Z_\tau(2)>0\), this finite parity-even threshold is positive definite in the controlled interior region. It does not imply chiral-anomaly cancellation or a supersymmetric completion of an arbitrary \(\tau(x)\) background.

## Current frontier

The active target is **v0.23 — multiplet completion beyond the vector multiplet**. The next controlled tests are the 6d \(\mathcal N=(1,0)\) hypermultiplet and tensor multiplet, with self-dual/chiral determinants treated carefully rather than inferred by degree counting.

The goal is to determine whether the surviving positive

\[
Z_\tau(2)g_{\rm hyp}
\]

sector is universal, multiplet-dependent, or canceled only in larger independently specified field contents.

Lorentzian/horizon closure remains separate.
