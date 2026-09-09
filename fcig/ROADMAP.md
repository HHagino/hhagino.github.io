# FCIG Research Roadmap

**Current target:** v0.25 — Green--Schwarz factorization / anomaly-lattice response audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations remain explicit no-go results.

---

## v0.3–v0.17 — geometric, determinant and response foundation — COMPLETE

Established milestones include theta/ppav state counting, curved-curve Bergman and Quillen sectors, differential cohomology, determinant holonomy, global metrized Deligne--Riemann--Roch, structure-group and pushforward no-gos, anomaly descent, functional-response ambiguity, conditional semiclassical closure, heat-kernel operators and elliptic realization-map dynamics.

No Einstein equation is derived from these data alone.

---

## v0.18–v0.20 — induced and intrinsic elliptic geometry — COMPLETE

Arbitrary heavy masses induce a pullback-Euclidean target metric and therefore do not predict the FCIG metric without an intrinsic operator. The actual area-one elliptic Laplacian then gives

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}},
\]

while the adiabatic spacetime calculation separates a UV-sensitive local Poincare term from the finite real-scalar threshold

\[
\boxed{
G^{\rm fin}_{\rm scalar}
=-\frac1{16\pi^3L^2}\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2].
}
\]

---

## v0.21–v0.23 — field-content and multiplet thresholds — COMPLETE

The six-dimensional local \(R_6\) response is not a naive signed degree count:

\[
\boxed{\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2.}
\]

Spin connections add a finite modular Poincare-trace sector. Completing standard \(\mathcal N=(1,0)\) vector, hyper and tensor multiplets gives

\[
\boxed{
\begin{array}{c|ccc}
\text{multiplet}&C_{\rm local}&A_{\mathcal G_4}&B_{Z_2}\\ \hline
\text{vector}&0&0&\frac18\\
\text{hyper}&6&0&-\frac1{16}\\
\text{tensor}&0&0&\frac18
\end{array}}
\]

and

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{2n_V-n_H+2n_T}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\]

Self-dual zero modes/global phases remain separate from the parity-even magnitude used here.

---

## v0.24 — multiplet threshold / anomaly-polynomial comparison — COMPLETE

Sources:

- `threshold-anomaly.md`
- `threshold-anomaly.py`
- `threshold-anomaly.bib`
- `threshold-anomaly.html`

### Gate DI — canonical anomaly table — PASS

Using the standard free-multiplet convention,

\[
I_8^H=\frac{7p_1^2-4p_2}{5760},
\]

\[
I_8^V=-\frac{c_2(R)^2}{24}-\frac{c_2(R)p_1}{48}-\frac{7p_1^2-4p_2}{5760},
\]

\[
I_8^T=\frac{c_2(R)^2}{24}+\frac{c_2(R)p_1}{48}+\frac{23p_1^2-116p_2}{5760}.
\]

Define

\[
R=-n_V+n_T,
\qquad
P_1=-7n_V+7n_H+23n_T,
\qquad
P_2=4n_V-4n_H-116n_T.
\]

### Gate DJ — coefficient-space rank — PASS

The independent anomaly coefficient matrix is

\[
M_\mathcal A=
\begin{pmatrix}
-1&0&1\\
-7&7&23\\
4&-4&-116
\end{pmatrix},
\qquad
\boxed{\det M_\mathcal A=720\neq0}.
\]

Thus the three independent one-loop anomaly coefficients reconstruct \((n_V,n_H,n_T)\).

### Gate DK — threshold/anomaly kernels — PASS WITH NO-GO

The finite threshold is

\[
K=2n_V-n_H+2n_T.
\]

Its kernel differs from every individual anomaly kernel. Explicitly,

\[
(1,2,0):\quad K=0,\qquad(R,P_1,P_2)=(-1,7,-4),
\]

so threshold cancellation does not imply anomaly cancellation.

Conversely,

\[
(1,1,0):\quad P_1=P_2=0,\qquad K=1,
\]

so pure-gravitational one-loop cancellation does not imply threshold cancellation.

The pure-gravitational anomaly kernel is

\[
\boxed{\ker(P_1,P_2)=\operatorname{span}\{(1,1,0)\}},
\]

while

\[
\boxed{\ker K=\{n_H=2n_V+2n_T\}}.
\]

Their intersection is trivial over \(\mathbb Q\).

### Gate DL — supergravity irreducible condition — PASS WITH HYPOTHESIS

The standard six-dimensional supergravity condition

\[
\boxed{n_H-n_V+29n_T=273}
\]

is an independently motivated necessary irreducible gravitational-anomaly condition once the gravity multiplet is included. It does not determine \(K\): for example \((0,244,1)\) satisfies the arithmetic condition but gives \(K=-242\).

This is not asserted to satisfy the remaining gauge/factorization/global consistency conditions.

### Gate DM — algebraic reconstruction — PASS WITH INTERPRETATION BOUNDARY

Because the anomaly map is invertible,

\[
\boxed{
K=-R-\frac8{45}P_1-\frac{11}{180}P_2.
}
\]

This is exact coefficient-space reconstruction, not a physical identification:

\[
\boxed{
\text{reconstructibility from field counts}
\neq
\text{equality of observables}.
}
\]

### Gate DN — scope — PASS

The comparison concerns the one-loop free-multiplet polynomial and the restricted parity-even finite threshold. Green--Schwarz data, anomaly lattices, gauge-representation anomalies, global self-dual phases and interacting SCFT sectors are not absorbed into \(K\).

References: Ohmori--Shimizu--Tachikawa--Yonekura (2014); Andrianopoli--Ferrara--Lledó (2004); milestone bibliography `threshold-anomaly.bib`.

---

## v0.25 — Green--Schwarz factorization / anomaly-lattice response audit — ACTIVE

v0.24 shows that the one-loop anomaly coefficient vector can reconstruct field counts, but its cancellation conditions are not the finite-threshold condition. The next step adds genuinely new anomaly data rather than more field-count algebra.

### Gate DO — Green--Schwarz data model

Fix the standard six-dimensional factorization form

\[
I_8^{\rm 1-loop}+I_8^{\rm GS}=0,
\qquad
I_8^{\rm GS}=\frac12\Omega_{\alpha\beta}X_4^\alpha X_4^\beta,
\]

with tensor charge lattice \(\Omega\) and four-forms \(X_4^\alpha\) in one cited convention.

### Gate DP — new-data test

Determine exactly which pieces of \((\Omega,X_4)\) are not reconstructible from \((n_V,n_H,n_T)\). Treat these as genuinely additional structure rather than rewriting multiplet counts.

### Gate DQ — threshold constraint audit

Ask whether anomaly factorization imposes any necessary relation on

\[
K=2n_V-n_H+2n_T
\]

for independently specified theories. Produce explicit counterexamples if factorization and threshold sign/vanishing remain independent.

### Gate DR — anomaly-lattice geometry versus FCIG metric

Compare the signature/integrality structure of the tensor charge lattice with the positive elliptic Poincare metric without identifying them. Any bridge must be an explicit map, not analogy.

### Gate DS — self-dual/global sector

Keep global anomaly phases and quadratic refinements separate from the parity-even determinant magnitude.

### Gate DT — scope/no-gravity rule

Even simultaneous Green--Schwarz consistency and a positive finite automorphic kinetic metric do not imply a UV completion, Einstein dynamics or a horizon law.

**Pass condition:** a citation-audited Green--Schwarz/anomaly-lattice model and an exact statement of whether it constrains the finite FCIG threshold beyond field-count reconstruction.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
