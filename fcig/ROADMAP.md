# FCIG Research Roadmap

**Current target:** v0.23 — multiplet completion beyond the vector multiplet  
**Updated:** 2026-09-09

The roadmap is ordered so that every mechanism is tested before any gravitational interpretation. Failed extrapolations remain recorded as explicit no-go results.

---

## v0.3–v0.17 — geometric, determinant and response foundation — COMPLETE

Earlier milestones establish:

- theta/ppav state counting and modular holonomy;
- curved-curve Bergman and Quillen sectors;
- differential cohomology and determinant holonomy;
- factorized-pushforward and structure-group no-gos;
- global metrized Deligne--Riemann--Roch closure;
- mixed anomaly polynomial/descent;
- anomaly versus effective-response ambiguity;
- conditional semiclassical closure;
- explicit heat-kernel operator bridge;
- elliptic realization-map dynamics.

No Einstein equation is derived from these data alone.

---

## v0.18 — induced target metric from arbitrary masses — COMPLETE WITH NO-GO

\[
G^{\rm ind}_{AB}
=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N}.
\]

Unconstrained masses turn target-metric matching into inverse design. FCIG prediction therefore requires an intrinsic operator/spectrum.

---

## v0.19 — intrinsic elliptic spectral metric — COMPLETE

For the area-one torus,

\[
\lambda_{m,n}=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

and

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}.}
\]

This is a finite moduli-space Chern-curvature identity.

---

## v0.20 — adiabatic elliptic / KK response — COMPLETE IN THE RESTRICTED REAL-SCALAR MODEL

For the fixed-volume elliptic family,

\[
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau,
\qquad
M_{m,n}^2=\frac{4\pi^2}{L^2Y}|m\tau-n|^2.
\]

The local Poincare-shaped coefficient is UV/counterterm sensitive. The analytically subtracted one-real-scalar finite threshold is

\[
\boxed{
G^{\rm fin}_{\rm scalar}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
\qquad
\operatorname{tr}_{g_{\rm hyp}}G^{\rm fin}_{\rm scalar}=0.
}
\]

The finite tensor is modular and trace-free, so it is not a positive sigma metric by itself.

---

## v0.21 — field-content / supertrace audit — COMPLETE WITH SPIN-CONNECTION OBSTRUCTION

Using standard six-dimensional Laplace-type heat-kernel coefficients,

\[
\boxed{\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2}
\]

for the local \(R_6\) sector. A 6d \(\mathcal N=(1,0)\) vector multiplet gives the parity-even local cancellation

\[
\boxed{-2+2=0.}
\]

However true spinors/vectors carry nontrivial bundle connections and curvature endomorphisms, so finite thresholds are not determined by a signed component count.

Sources: `field-content-supertrace.md`, `field-content-supertrace.py`, `field-content-supertrace.bib`.

---

## v0.22 — spin-connection automorphic thresholds — COMPLETE IN THE FIXED PARITY-EVEN MODEL

Sources:

- `spin-threshold.md`
- `spin-threshold.py`
- `spin-threshold.bib`
- `spin-threshold.html`

### Gate CU — exact spin-connection geometry — PASS

For winding \(\lambda\),

\[
Q_\lambda=\lambda^TG(\tau)\lambda,
\qquad
K_\tau=\frac{(\partial u)^2+(\partial Y)^2}{Y^2},
\]

the fiber Levi-Civita connection satisfies

\[
\boxed{
\operatorname{tr}_{\rm vec}[(\lambda\cdot\omega)^2]
=\frac{L^2}{2}Q_\lambda K_\tau.
}
\]

Hence spin transport is forced into the Poincare-trace tensor.

### Gate CV — Lorentz representation trace — PASS

With \(C_{\rm vec}=2\),

\[
C_{\rm Dirac}=2,
\qquad
C_{\rm Weyl}=1,
\]

and

\[
\boxed{
\operatorname{tr}_R[(\lambda\cdot\omega)^2]
=\frac{C_RL^2}{4}Q_\lambda K_\tau.
}
\]

### Gate CW — general representation-dependent finite trace term — PASS

In the periodic heat-kernel convention \(P=-D^2+E\), write

\[
\operatorname{tr}_R E=e_RR_6.
\]

Combining the quadratic spin Wilson line with the \(-E\) part of \(a_1\) gives

\[
\boxed{
\Delta G_{\rm tr}^{(R)}
=\frac{(-1)^F(2C_R-e_R)}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
}
\]

This is finite and modular because \(Z_\tau(2)\) and \(g_{\rm hyp}\) are modular invariant.

### Gate CX — complex Dirac threshold — PASS

\[
\boxed{
G_D^{\rm fin}
=\frac1{2\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2]
-\frac1{8\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\]

Only the parity-even determinant magnitude is included; chiral phase/anomaly data are separate.

### Gate CY — Maxwell plus ghost threshold — PASS

Keeping gauge and Faddeev--Popov ghost determinants together,

\[
\boxed{
G_{A+gh}^{\rm fin}
=-\frac1{4\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2]
+\frac3{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\]

### Gate CZ — Weyl/SMW parity-even threshold — PASS

\[
\boxed{
G_W^{\rm fin}
=\frac1{4\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2]
-\frac1{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\]

### Gate DA — 6d \(\mathcal N=(1,0)\) vector multiplet — PASS WITH POSITIVE FINITE SURVIVOR

The trace-free weight-four pieces cancel,

\[
-\frac14+\frac14=0,
\]

while the spin/endormorphism trace pieces leave

\[
\frac3{16}-\frac1{16}=\frac18.
\]

Therefore

\[
\boxed{
G_{\rm vm}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp}.
}
\]

Since \(Z_\tau(2)>0\), this finite parity-even tensor is positive definite away from the cusp/degeneration region where the heavy-tower EFT fails.

### Gate DB — local versus finite SUSY cancellation — PASS WITH STRICT DISTINCTION

For the specified vector multiplet:

\[
\boxed{
\begin{array}{ll}
\text{local UV Poincare sector:}&-2+2=0,\\
\text{finite weight-four sector:}&4-4=0,\\
\text{finite spin-transport trace sector:}&3/16-1/16=1/8.
\end{array}}
\]

Thus local supersymmetric cancellation does not imply finite nonlocal cancellation on the restricted varying-metric background.

### Scope

The result is restricted to the locally trivial, fixed-volume, block-diagonal torus family and the parity-even determinant convention. It does not establish chiral-anomaly cancellation, a fully supersymmetric curved background, an Einstein equation, or a horizon law.

References: von Gersdorff (2008); Vassilevich (2003); Lawson--Michelsohn (1989); Ferrara--Riccioni--Sagnotti (1998); Ohmori et al. (2014); Apostol (1990).

---

## v0.23 — multiplet completion beyond the vector multiplet — ACTIVE

The next controlled question is whether the positive

\[
Z_\tau(2)g_{\rm hyp}
\]

survivor is special to the vector multiplet or persists/cancels in other independently specified 6d \(\mathcal N=(1,0)\) multiplets.

### Gate DC — hypermultiplet

Use four real scalars plus the appropriate chiral fermion content. Compute local, weight-four and spin-trace sectors without fitting multiplicities.

### Gate DD — tensor multiplet

Treat the chiral/self-dual two-form determinant carefully. Do not replace it by an unconstrained two-form degree count. Keep determinant magnitude and global/chiral phase data distinct.

### Gate DE — multiplet table

Produce a checked table of

\[
(C_{\rm local},\ A_{\mathcal G_4},\ B_{Z_2})
\]

for vector, hyper and tensor multiplets in one convention.

### Gate DF — larger field contents

Only after individual multiplets are fixed, test independently motivated combinations. Do not choose multiplicities merely to obtain cancellation or positivity.

### Gate DG — anomaly consistency

Compare the same multiplets with their known 6d anomaly polynomials, while keeping anomaly coefficients distinct from kinetic thresholds.

**Pass condition:** explicit hypermultiplet and tensor-multiplet finite thresholds with determinant/chirality caveats fully stated.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
