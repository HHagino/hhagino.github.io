# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository distinguishes **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research/citation policy
- `ROADMAP.md` — active gates and completed milestones
- `references.bib` — general bibliography
- milestone `.bib` files — source sets for individual models
- `citation-map.md` / `cited-synthesis.md` — citation provenance and audited synthesis

## Status

Completed milestones: **v0.2–v0.24**.

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
\to\text{spin/multiplet thresholds}
\to\text{threshold/anomaly coefficient-space audit}.
}
\]

No derivation of Einstein dynamics or horizon thermodynamics from FCIG alone is claimed.

## Models I–X — determinant / cohomological foundation

The elliptic, ppav and curved-curve laboratories establish theta-state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos and the metrized Deligne--Riemann--Roch identity

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the canonical smooth curve-family model.

## Models XI–XVIII — structure-group, anomaly and operator audits

The determinant line retains only the trace/Ricci sector of a generic \(U(n)\) connection,

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad F_{\det E}=\operatorname{Tr}F_E,
\]

and anomaly data alone do not fix the effective action or first response:

\[
\boxed{\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.}
\]

A realization map can put FCIG curvature into an ordinary Laplace-type operator, but arbitrary heavy masses turn target-metric matching into inverse design rather than prediction.

## Model XIX — intrinsic spectral--Hodge identity

For the area-one elliptic torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

and

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}.}
\]

This is the first no-fit spectral regeneration of the pre-existing elliptic Hodge curvature.

## Models XX–XXIII — adiabatic and multiplet thresholds

For one real scalar, the finite two-derivative threshold is trace-free,

\[
G^{\rm fin}_{\rm scalar}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2].
\]

True spin fields generate an additional finite Poincare-trace sector. After completing standard 6d \(\mathcal N=(1,0)\) vector, hyper and tensor multiplets, the restricted parity-even table is

\[
\boxed{
\begin{array}{c|ccc}
\text{multiplet}&C_{\rm local}&A_{\mathcal G_4}&B_{Z_2}\\ \hline
\text{vector}&0&0&\frac18\\
\text{hyper}&6&0&-\frac1{16}\\
\text{tensor}&0&0&\frac18
\end{array}}
\]

and therefore

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{2n_V-n_H+2n_T}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
}
\]

Self-dual zero modes, theta characteristics and global anomaly phases remain separate from this parity-even determinant magnitude.

## Model XXIV — threshold versus anomaly polynomial

- Web: `threshold-anomaly.html`
- Source: `threshold-anomaly.md`
- Checker: `threshold-anomaly.py`
- Milestone bibliography: `threshold-anomaly.bib`

Using the standard free-multiplet anomaly convention, define

\[
R=-n_V+n_T,
\quad
P_1=-7n_V+7n_H+23n_T,
\quad
P_2=4n_V-4n_H-116n_T.
\]

Then

\[
I_8^{VHT}
=\frac{R}{24}c_2(R)^2
+\frac{R}{48}c_2(R)p_1(T)
+\frac{P_1}{5760}p_1(T)^2
+\frac{P_2}{5760}p_2(T).
\]

The independent anomaly coefficient matrix is

\[
M_\mathcal A=
\begin{pmatrix}
-1&0&1\\
-7&7&23\\
4&-4&-116
\end{pmatrix},
\qquad
\boxed{\det M_\mathcal A=720}.
\]

Thus the full three-component one-loop anomaly coefficient vector reconstructs the three multiplet counts. The finite threshold functional

\[
K=2n_V-n_H+2n_T
\]

is consequently reconstructible as

\[
\boxed{
K=-R-\frac8{45}P_1-\frac{11}{180}P_2,
}
\]

but this is coefficient-space linear algebra, not a physical identification of anomaly and kinetic response.

Their natural cancellation conditions are different:

\[
(1,2,0):\quad K=0\ \text{but}\ I_8\neq0,
\]

while

\[
(1,1,0):\quad P_1=P_2=0\ \text{but}\ K=1.
\]

Hence

\[
\boxed{
\text{threshold cancellation}
\not\Longleftrightarrow
\text{anomaly cancellation}.
}
\]

## Current frontier

The active target is **v0.25 — Green--Schwarz factorization / anomaly-lattice response audit**.

The next question is whether adding genuinely new anomaly data — Green--Schwarz four-forms, the tensor charge lattice and factorization coefficients — imposes any nontrivial constraint on the finite automorphic threshold beyond reconstructing microscopic field counts.

The key rule remains:

\[
\boxed{
\text{anomaly polynomial}
\neq
\text{Green--Schwarz factorization data}
\neq
\text{finite kinetic threshold}.
}
\]

Lorentzian/horizon closure remains inactive.
