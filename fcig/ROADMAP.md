# FCIG Research Roadmap

**Current target:** v0.26 — charged elliptic / Jacobi threshold  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations remain explicit no-go results.

---

## v0.3–v0.17 — geometric, determinant and response foundation — COMPLETE

Established milestones include theta/ppav state counting, curved-curve Bergman and Quillen sectors, differential cohomology, determinant holonomy, global metrized Deligne--Riemann--Roch, structure-group and pushforward no-gos, anomaly descent, functional-response ambiguity, conditional semiclassical closure, heat-kernel operators and elliptic realization-map dynamics.

No Einstein equation is derived from these data alone.

---

## v0.18–v0.20 — induced and intrinsic elliptic geometry — COMPLETE

Arbitrary heavy masses induce a pullback-Euclidean target metric and therefore do not predict the FCIG metric without an intrinsic operator. The actual area-one elliptic Laplacian gives

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
=\frac{K}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp},
\qquad K=2n_V-n_H+2n_T.
}
\]

Self-dual zero modes/global phases remain separate from the parity-even magnitude used here.

---

## v0.24 — multiplet threshold / anomaly-polynomial comparison — COMPLETE

Using the standard free-multiplet anomaly coefficients,

\[
R=-n_V+n_T,
\qquad
P_1=-7n_V+7n_H+23n_T,
\qquad
P_2=4n_V-4n_H-116n_T,
\]

with

\[
\det
\begin{pmatrix}
-1&0&1\\
-7&7&23\\
4&-4&-116
\end{pmatrix}
=720,
\]

the full anomaly coefficient vector reconstructs the field counts and therefore

\[
\boxed{
K=-R-\frac8{45}P_1-\frac{11}{180}P_2.
}
\]

This is algebraic reconstruction only. The natural cancellation kernels remain inequivalent.

Sources: `threshold-anomaly.*`.

---

## v0.25 — Green--Schwarz factorization / anomaly-lattice audit — COMPLETE WITH NO-GO

Sources:

- `green-schwarz-lattice.md`
- `green-schwarz-lattice.py`
- `green-schwarz-lattice.bib`
- `green-schwarz-lattice.html`

### Gate DO — canonical local Green--Schwarz model — PASS

In the Kumar--Morrison--Taylor convention,

\[
I_8^{\rm 1-loop}=\frac12\Omega_{\alpha\beta}X_4^\alpha X_4^\beta,
\]

with tensor-space signature \((1,T)\), gravitational vector \(a\), gauge vectors \(b_i\), and the standard local equations

\[
H-V=273-29T,
\qquad
a\cdot a=9-T,
\]

plus the representation-dependent \(a\cdot b_i\), \(b_i\cdot b_j\) and quartic-Casimir relations.

### Gate DP — global lattice refinement — PASS

The string charges take values in a lattice \(\Lambda_S\). Global consistency adds data absent from the multiplet totals: unimodularity/quantization, characteristic gravitational coefficient \(a\), gauge-coefficient integrality, global gauge-group information and possible residual global anomaly data.

References: Kumar--Morrison--Taylor; Monnier--Moore--Park; Monnier--Moore.

### Gate DQ — threshold-blindness theorem — PASS

Using

\[
H=273+V-29T
\]

inside

\[
K=2V-H+2T
\]

gives

\[
\boxed{
K=V+31T-273.
}
\]

Hence the restricted Model-XXIII threshold depends only on \((V,T)\) after gravitational anomaly cancellation. At fixed \((V,T)\), refinements of

\[
a,\quad b_i,\quad
\Lambda_S\text{ embedding},\quad
G_{\rm global}
\]

do not change \(K\).

### Gate DR — same counts, different global consistency — PASS

On the even unimodular lattice

\[
U=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

both

\[
a_{\rm good}=(2,2),
\qquad
a_{\rm bad}=(4,1)
\]

satisfy

\[
a^2=8=9-T
\]

for \(T=1\), but only \((2,2)\) is characteristic. Monnier--Moore--Park discuss the \((4,1)\) candidate with

\[
(V,H,T)=(0,244,1),
\]

which passes the earlier local tests but fails the characteristic requirement. A standard elliptic \(\mathbb F_0\) realization has the same counts with characteristic \(a\) and therefore the same

\[
\boxed{K=-242}.
\]

Thus the lattice refinement can change quantum admissibility without changing the threshold.

### Gate DS — sign audit — PASS WITH COUNTEREXAMPLES

A standard elliptic \(\mathbb F_0\) model gives

\[
K=-242<0.
\]

Wang's generalized \(dP_9\) F-theory model has

\[
T=9,
\qquad
G=U(1)^8,
\qquad
h^{1,1}(X)=h^{2,1}(X)=19,
\]

hence standard six-dimensional counting gives

\[
(V,H,T)=(8,20,9)
\]

and

\[
\boxed{K=14>0}.
\]

Therefore

\[
\boxed{
\text{GS/F-theory consistency does not force a universal sign or vanishing of }K.
}
\]

### Gate DT — interpretation boundary — PASS

The new Green--Schwarz/lattice data are genuine quantum-consistency data. The no-go is narrower: the present gauge-blind finite elliptic threshold has no variable on which \(b_i\), charge weights or cocharacter-lattice data can act directly.

### Gate DU — next typed bridge — PASS AS DESIGN REQUIREMENT

A gauge-sensitive extension must introduce elliptic gauge holonomies. For charge \(q\), schematically

\[
(m,n)\mapsto(m+q\alpha,n+q\beta),
\qquad
z=\alpha\tau+\beta.
\]

The spectral determinant should then become theta/Jacobi-like. Only such a model provides an explicit channel from charge / gauge-lattice data to a finite spectral response.

---

## v0.26 — charged elliptic / Jacobi threshold — ACTIVE

### Gate DV — charged spectrum

Fix a charged scalar/fermion on the area-one elliptic torus with flat gauge holonomy \(z\). Derive the exact shifted KK eigenvalues with no fitted masses.

### Gate DW — spectral determinant

Compute the zeta-regularized determinant in terms of theta/Jacobi data, with normalization and zero-mode treatment explicit.

### Gate DX — Jacobi covariance

Verify the combined modular and elliptic transformations

\[
(\tau,z)\mapsto\left(\frac{a\tau+b}{c\tau+d},\frac{z}{c\tau+d}\right),
\qquad
z\mapsto z+r\tau+s,
\]

including the multiplier/index rather than imposing invariance by hand.

### Gate DY — finite response tensor

Extract the finite two-derivative response on \((\tau,z)\)-space. Separate local counterterms from genuinely nonlocal Jacobi data.

### Gate DZ — charge-lattice channel

For several charges/representations, determine exactly how charge bilinears and weight lattices enter the Jacobi index. Only then compare that index with Green--Schwarz gauge-anomaly vectors \(b_i\).

### Gate EA — no-identification rule

A numerical relation between Jacobi index and anomaly coefficient is not enough. Any bridge to \(b_i\) must follow from the same microscopic charge data and compatible normalization.

**Pass condition:** an exact charged elliptic spectrum/determinant with checked Jacobi covariance and a citation-audited statement of whether Green--Schwarz gauge data enter the finite response through a genuine common microscopic structure.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
