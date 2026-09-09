# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository distinguishes **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research/citation policy
- `ROADMAP.md` — active gates and completed milestones
- `references.bib` — general bibliography
- milestone `.bib` files — source sets for individual models
- `citation-map.md` / `cited-synthesis.md` — citation provenance and audited synthesis

## Status

Completed milestones: **v0.2–v0.25**.

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
\to\text{threshold/anomaly audit}
\to\text{Green--Schwarz / anomaly-lattice audit}.
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

After completing standard 6d \(\mathcal N=(1,0)\) vector, hyper and tensor multiplets, the restricted parity-even table is

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
=\frac{K}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp},
\qquad
K:=2n_V-n_H+2n_T.
}
\]

Self-dual zero modes, theta characteristics and global anomaly phases remain separate from this parity-even determinant magnitude.

## Model XXIV — threshold versus anomaly polynomial

Using the standard free-multiplet anomaly convention, define

\[
R=-n_V+n_T,
\quad
P_1=-7n_V+7n_H+23n_T,
\quad
P_2=4n_V-4n_H-116n_T.
\]

The independent anomaly coefficient matrix has

\[
\boxed{\det M_\mathcal A=720},
\]

so the full one-loop coefficient vector reconstructs the three multiplet counts and hence

\[
\boxed{
K=-R-\frac8{45}P_1-\frac{11}{180}P_2.
}
\]

This is coefficient-space reconstruction only. The cancellation kernels are different:

\[
(1,2,0):\ K=0\text{ but }I_8\neq0,
\qquad
(1,1,0):\ P_1=P_2=0\text{ but }K=1.
\]

Sources: `threshold-anomaly.*`.

## Model XXV — Green--Schwarz / anomaly-lattice audit

- Web: `green-schwarz-lattice.html`
- Source: `green-schwarz-lattice.md`
- Checker: `green-schwarz-lattice.py`
- Milestone bibliography: `green-schwarz-lattice.bib`

The standard six-dimensional Green--Schwarz data contain a tensor charge lattice \(\Lambda_S\) of signature \((1,T)\), gravitational coefficient \(a\), gauge coefficients \(b_i\), and global quantization / characteristic conditions.

Imposing the irreducible gravitational-anomaly relation

\[
H-V+29T=273
\]

on the Model-XXIII threshold gives

\[
\boxed{
K=2V-H+2T=V+31T-273.
}
\]

Thus at fixed \((V,T)\), the threshold is blind to refinements of

\[
a,\quad b_i,\quad
\Lambda_S\text{ embedding},\quad
G_{\rm global},\quad
\text{quadratic / characteristic data}.
\]

This blindness is physical rather than merely formal. On the even unimodular lattice

\[
U=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

both

\[
a=(2,2),\qquad a=(4,1)
\]

have \(a^2=8\) for \(T=1\), but only \((2,2)\) is characteristic. The Monnier--Moore--Park \((4,1)\) candidate has the same

\[
(V,H,T)=(0,244,1),\qquad K=-242,
\]

as a standard elliptic \(\mathbb F_0\) model, yet fails the global characteristic test.

Green--Schwarz/F-theory consistency also does not fix the sign of \(K\):

\[
\boxed{
K_{\mathbb F_0}=-242<0,
\qquad
K_{gdP_9,U(1)^8}=14>0.
}
\]

Hence

\[
\boxed{
\text{GS/lattice consistency}
\not\Rightarrow
K\ge0,\ K\le0,\ \text{or }K=0.
}
\]

The new lattice data are nevertheless genuine quantum-consistency information; they can accept or reject theories without changing the finite gauge-blind elliptic threshold.

## Current frontier

The active target is **v0.26 — charged elliptic / Jacobi threshold**.

Model XXV explains why the current threshold cannot see \(b_i\): Models XX–XXIII switched off background gauge holonomies. The next controlled extension introduces an elliptic gauge variable

\[
z=\alpha\tau+\beta
\]

so charged KK modes see shifted lattices and the determinant becomes theta/Jacobi-like. Only then is there an explicit channel through which charge lattices, representation weights and Green--Schwarz gauge data might constrain a finite spectral response.

The rule remains

\[
\boxed{
\text{anomaly / lattice data}
\neq
\text{finite response}
}
\]

unless an explicit spectral map is constructed.

Lorentzian/horizon closure remains inactive.
