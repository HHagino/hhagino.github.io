# FCIG Research Roadmap

**Current target:** v0.24 — multiplet threshold / anomaly-polynomial comparison audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations remain explicit no-go results.

---

## v0.3–v0.17 — geometric, determinant and response foundation — COMPLETE

Established milestones include theta/ppav state counting, curved-curve Bergman and Quillen sectors, differential cohomology, determinant holonomy, global metrized Deligne--Riemann--Roch, structure-group and pushforward no-gos, anomaly descent, functional-response ambiguity, the conditional semiclassical bridge, heat-kernel operators and elliptic realization-map dynamics.

No Einstein equation is derived from these data alone.

---

## v0.18 — arbitrary-mass induced metric — COMPLETE WITH NO-GO

\[
G^{\rm ind}_{AB}
=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N}.
\]

Unconstrained masses turn target-metric matching into inverse design; prediction requires an intrinsic operator/spectrum.

---

## v0.19 — intrinsic elliptic spectral metric — COMPLETE

\[
\lambda_{m,n}=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}.}
\]

This is a finite moduli-space Chern-curvature identity.

---

## v0.20 — adiabatic elliptic / KK response — COMPLETE

For the fixed-volume elliptic family,

\[
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau,
\qquad
M_{m,n}^2=\frac{4\pi^2}{L^2Y}|m\tau-n|^2.
\]

The local Poincare-shaped coefficient is UV/counterterm sensitive. The finite one-real-scalar threshold is

\[
\boxed{
G^{\rm fin}_{\rm scalar}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
\qquad
\operatorname{tr}_{g_{\rm hyp}}G^{\rm fin}_{\rm scalar}=0.
}
\]

---

## v0.21 — field-content audit — COMPLETE WITH SPIN-CONNECTION OBSTRUCTION

The local six-dimensional \(R_6\) sector obeys

\[
\boxed{\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2.}
\]

A 6d \(\mathcal N=(1,0)\) vector multiplet has local parity-even cancellation \(-2+2=0\), but finite spin responses cannot be obtained by signed component counting.

---

## v0.22 — spin-connection automorphic thresholds — COMPLETE

For Lorentz representation \(R\),

\[
\boxed{
\Delta G_{\rm tr}^{(R)}
=\frac{(-1)^F(2C_R-e_R)}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
}
\]

For a specified 6d \(\mathcal N=(1,0)\) vector multiplet, the local and finite weight-four terms cancel while

\[
\boxed{
G_{\rm vector}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp}>0
}
\]

in the controlled interior region.

Sources: `spin-threshold.md`, `spin-threshold.py`, `spin-threshold.bib`.

---

## v0.23 — hyper/tensor multiplet automorphic thresholds — COMPLETE

Sources:

- `hyper-tensor-threshold.md`
- `hyper-tensor-threshold.py`
- `hyper-tensor-threshold.bib`
- `hyper-tensor-threshold.html`

### Gate DC — hypermultiplet — PASS

A 6d \(\mathcal N=(1,0)\) hypermultiplet contains four real scalars and one SMW fermion. Therefore

\[
\boxed{
(C_{\rm local},A_{\mathcal G_4},B_{Z_2})_{\rm hyper}
=\left(6,0,-\frac1{16}\right)
}
\]

and

\[
\boxed{
G_{\rm hyper}^{\rm fin}
=-\frac{Z_\tau(2)}{16\pi^3L^2}g_{\rm hyp}.
}
\]

The isolated hypermultiplet contribution is negative definite in this parity-even one-loop convention.

### Gate DD — non-chiral two-form determinant — PASS

The standard reducible-gauge determinant is

\[
W_{B,\rm nonch}
=\frac12\log\det{}'\Delta_2
-\log\det{}'\Delta_1
+\frac32\log\det{}'\Delta_0.
\]

Using the Model-XXII \(p\)-form Lorentz-index reduction gives

\[
\boxed{
(C_{\rm local},A,B)_{B,\rm nonch}
=\left(-6,-\frac38,\frac38\right).
}
\]

### Gate DE — self-dual magnitude prescription — PASS WITH GLOBAL CAVEAT

Holomorphic factorization / self-dual determinant-line literature justifies taking one half of the non-chiral logarithmic response for the parity-even nonzero-mode magnitude, while zero modes, theta characteristics and chiral/global phases remain separate.

Thus

\[
\boxed{
(C_{\rm local},A,B)_{B^+}
=\left(-3,-\frac3{16},\frac3{16}\right).
}
\]

This is not a claim that the full global chiral partition function is a literal positive square root of the non-chiral function.

### Gate DF — tensor multiplet — PASS

A tensor multiplet contains one self-dual/anti-self-dual two-form, one real scalar and one SMW fermion. Hence

\[
\boxed{
(C_{\rm local},A,B)_{\rm tensor}
=\left(0,0,\frac18\right)
}
\]

and

\[
\boxed{
G_{\rm tensor}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp}.
}
\]

The parity-even tensor-multiplet threshold exactly equals the vector-multiplet threshold in the restricted model.

### Gate DG — completed multiplet table — PASS

\[
\boxed{
\begin{array}{c|ccc}
\text{multiplet}&C_{\rm local}&A_{\mathcal G_4}&B_{Z_2}\\ \hline
\text{vector}&0&0&\frac18\\
\text{hyper}&6&0&-\frac1{16}\\
\text{tensor}&0&0&\frac18
\end{array}}
\]

All three supersymmetric multiplets cancel the finite weight-four trace-free sector in this background.

For independently fixed multiplicities,

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{2n_V-n_H+2n_T}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
}
\]

This is bookkeeping only; multiplicities may not be chosen merely to engineer a desired sign.

### Gate DH — anomaly consistency — PASS WITH STRICT DISTINCTION

The multiplet anomaly polynomials are separate observables from the local and finite kinetic coefficients above:

\[
\boxed{
I_8
\neq
C_{\rm local}
\neq
(A_{\mathcal G_4},B_{Z_2}).
}
\]

No anomaly cancellation is inferred from the threshold table, and no threshold cancellation is inferred from an anomaly-free field content.

### Scope

The result is restricted to the locally trivial, fixed-volume, block-diagonal elliptic family, nonzero KK/winding tower and parity-even determinant magnitudes. Self-dual global phases, nontrivial torus bundles, background gauge fields and the cusp/EFT breakdown remain separate.

References: Ferrara--Riccioni--Sagnotti (1998); Ohmori--Shimizu--Tachikawa--Yonekura (2014); Henningson--Nilsson--Salomonson (1999); Gustavsson (2002); Witten (1997); Belov--Moore (2006); Monnier (2014); Huang--Roiban--Tseytlin (2018); Model XXII references.

---

## v0.24 — multiplet threshold / anomaly-polynomial comparison — ACTIVE

The next task is not to fit more field multiplicities. It is to compare, for the **same independently specified multiplets**, the kinetic-response coefficients above with their established 6d anomaly polynomials.

### Gate DI — canonical anomaly-polynomial table

Record vector, hyper and tensor multiplet contributions to the purely gravitational and any relevant background-gauge pieces of \(I_8\), with conventions fixed to one primary source.

### Gate DJ — coefficient-space comparison

Compare the linear functionals on multiplet number space:

\[
(n_V,n_H,n_T)
\mapsto
2n_V-n_H+2n_T
\]

for the finite elliptic kinetic threshold and the independent anomaly-polynomial combinations. Determine their kernels/intersections without identifying them.

### Gate DK — independently motivated combinations

Only test combinations coming from an external 6d model or standard anomaly-cancellation condition. Do not choose multiplicities to force a preferred kinetic sign.

### Gate DL — self-dual global phase audit

For tensor-containing combinations, keep the Monnier/Witten global self-dual phase/anomaly data distinct from the parity-even determinant magnitude.

### Gate DM — scope/no-gravity rule

Even simultaneous anomaly cancellation and a positive finite moduli metric do not constitute an Einstein equation, horizon law or UV completion.

**Pass condition:** a citation-audited anomaly-polynomial table and an exact comparison of the anomaly and kinetic linear conditions on fixed multiplet content.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
