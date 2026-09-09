# FCIG Model XXII — Spin-connection automorphic thresholds

**Status:** derived in the restricted fixed-volume elliptic family. The parity-even finite two-derivative thresholds for a complex Dirac fermion, Maxwell plus Faddeev–Popov ghost, and a 6d \(\mathcal N=(1,0)\) vector multiplet are fixed in the conventions below. Chiral determinant phases/anomalies remain separate.

## 1. Purpose and citation policy

Model XX found, for one real scalar,

\[
G_{\rm scalar}^{\rm fin}
=-\frac{1}{16\pi^3L^2}
\operatorname{Re}\!\left[\mathcal G_4(\tau)(d\tau)^2\right],
\]

where

\[
\mathcal G_4(\tau)=\sum_{(m,n)\ne(0,0)}(m\tau-n)^{-4}.
\]

Model XXI showed that true spinors and vectors cannot in general be obtained by multiplying this answer by a signed component count because their Laplace-type operators carry nontrivial Lorentz connections and curvature endomorphisms.

The standard background used here is the periodic torus heat-kernel expansion of von Gersdorff [vonGersdorff2008]. In that formalism the nonlocal heat kernel contains the spin Wilson line

\[
W(\lambda)=\exp(i\lambda\cdot\omega)
\]

and the Laplace-type endomorphism \(E\). The coefficients \(\alpha_{d,r}\), the periodic coincidence limits, and the separation between local and nonlocal terms are **Established** results. The Lichnerowicz and one-form Weitzenbock formulas used below are also standard [LawsonMichelsohn1989, Vassilevich2003].

All elliptic spin-connection identities and the final representation-dependent threshold coefficients below are **Derived here** in the fixed Model-XX convention.

---

## 2. Fixed elliptic family

Use

\[
ds_6^2=g_{\mu\nu}(x)dx^\mu dx^\nu+L^2G_{ab}(\tau(x))dy^ady^b,
\qquad \det G=1,
\]

with

\[
G(\tau)=\frac1Y
\begin{pmatrix}
1&u\\
u&u^2+Y^2
\end{pmatrix},
\qquad \tau=u+iY,
\]

and define

\[
K_\tau:=g_{\rm hyp}^{AB}\partial_\mu\tau^A\partial^\mu\tau^B
=\frac{(\partial u)^2+(\partial Y)^2}{Y^2}.
\]

For a winding vector \(\lambda=(p,q)\in\mathbb Z^2\),

\[
Q_\lambda(\tau):=\lambda^TG\lambda
=\frac{|p\tau+q|^2}{Y},
\]

up to the harmless lattice relabeling \(q\mapsto-q\) relative to Model XIX. Its physical squared length is

\[
|\lambda|^2=L^2Q_\lambda.
\]

The nonholomorphic Epstein series is

\[
Z_\tau(2)=\sum_{\lambda\ne0}Q_\lambda^{-2}>0.
\]

---

## 3. Fiber spin connection: exact quadratic identity

Let \(\Gamma_a\) denote the Levi-Civita connection matrix acting on tangent vectors along the two fiber directions. Direct evaluation of the block-metric Christoffel symbols gives, for every winding vector,

\[
\boxed{
\operatorname{tr}_{\rm vec}
\left[(\lambda^a\Gamma_a)^2\right]
=-\frac{L^2}{2}Q_\lambda K_\tau.
}
\]

Passing to Hermitian Lorentz generators, \(\omega_a=-i\Gamma_a\), gives

\[
\boxed{
\operatorname{tr}_{\rm vec}
\left[(\lambda\cdot\omega)^2\right]
=\frac{L^2}{2}Q_\lambda K_\tau.
}
\tag{XXII.1}
\]

The uncontracted identity is equivalently

\[
\operatorname{tr}_{\rm vec}(\omega_a\omega_b)
=\frac{L^2}{2}G_{ab}K_\tau,
\]

hence

\[
\boxed{
\operatorname{tr}_{\rm vec}(\omega_a\omega^a)=K_\tau.
}
\tag{XXII.2}
\]

These formulas are **Derived here**. They show that the spin-transport sector is forced into the Poincare trace tensor rather than the holomorphic weight-four trace-free tensor of Model XX.

---

## 4. Representation trace normalization

Normalize Lorentz Dynkin indices by

\[
\operatorname{tr}_R(\Sigma_{AB}\Sigma_{CD})
=C_R\,\delta_{AB,CD},
\]

with the six-dimensional vector representation normalized to

\[
C_{\rm vec}=2.
\]

For a rotation in one orthonormal two-plane, a six-dimensional complex Dirac spinor has four eigenvalues \(+1/2\) and four eigenvalues \(-1/2\), so

\[
C_{\rm Dirac}=8\left(\frac12\right)^2=2.
\]

A complex Weyl spinor has half the trace,

\[
C_{\rm Weyl}=1.
\]

Therefore (XXII.1) generalizes to

\[
\boxed{
\operatorname{tr}_R[(\lambda\cdot\omega)^2]
=\frac{C_RL^2}{4}Q_\lambda K_\tau.
}
\tag{XXII.3}
\]

This representation-trace calculation is **Derived here**; it agrees with the standard Dynkin-index role of spin generators in periodic heat-kernel traces [vonGersdorff2008].

---

## 5. Periodic heat-kernel coefficients in six dimensions

For the standard operator convention used by von Gersdorff,

\[
P=-D^2+E,
\]

the nonlocal effective action is built from

\[
\alpha_{d,r}=
\frac{\Gamma(d/2-r)}{2^{2r+1}\pi^{d/2}}.
\]

Thus

\[
\boxed{
\alpha_{6,0}=\frac1{\pi^3},
\qquad
\alpha_{6,1}=\frac1{8\pi^3}.
}
\]

At two derivatives, the representation-dependent pieces in the full unorbifolded torus sector are:

1. the quadratic spin Wilson-line term
   \[
   W(\lambda)=1-\frac12(\lambda\cdot\omega)^2+O(\partial^3),
   \]
2. the \(-E\) term in \(a_1\).

The Van Vleck and scalar-curvature pieces are representation-independent and are already contained in the scalar-like multiplicity sector. Terms involving curvature field strengths \(\Omega\), derivatives of \(E\), or higher covariant Taylor coefficients start beyond the two-derivative order in the restricted \(y\)-independent background.

For a representation \(R\) of statistics \(F\in\{0,1\}\), the Wilson-line correction becomes

\[
\boxed{
\Delta G_W^{(R)}
=
\frac{(-1)^F C_R}{8\pi^3L^2}
Z_\tau(2)\,g_{\rm hyp}.
}
\tag{XXII.4}
\]

If

\[
\operatorname{tr}_R E=e_RR_6,
\]

and the two-derivative part of the total-space scalar curvature is

\[
R_6^{(2)}=-\frac12K_\tau,
\]

then

\[
\boxed{
\Delta G_E^{(R)}
=-\frac{(-1)^F e_R}{16\pi^3L^2}
Z_\tau(2)\,g_{\rm hyp}.
}
\tag{XXII.5}
\]

Hence the spin/endormorphism trace coefficient is

\[
\boxed{
\Delta G_{\rm tr}^{(R)}
=
\frac{(-1)^F(2C_R-e_R)}{16\pi^3L^2}
Z_\tau(2)\,g_{\rm hyp}.
}
\tag{XXII.6}
\]

---

## 6. Complex Dirac fermion

The Lichnerowicz formula gives

\[
\slashed D^2=-\nabla^2+\frac14R_6,
\]

so for a complex six-dimensional Dirac spinor

\[
C_D=2,
\qquad
\operatorname{tr}E=8\frac{R_6}{4}=2R_6,
\qquad e_D=2,
\qquad F=1.
\]

Equation (XXII.6) yields

\[
\boxed{
\Delta G_{\rm tr}^{D}
=-\frac1{8\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\tag{XXII.7}
\]

Ignoring connection/endormorphism data, the parity-even complex Dirac determinant contains eight scalar-like components with the fermionic sign, so

\[
\nu_D=-8.
\]

Using Model XX,

\[
\boxed{
G_D^{\rm fin}
=
\frac1{2\pi^3L^2}
\operatorname{Re}\!\left[\mathcal G_4(\tau)(d\tau)^2\right]
-
\frac1{8\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\tag{XXII.8}
\]

This is the parity-even determinant contribution only. The phase of a chiral determinant and its anomaly belong to the anomaly/differential-cohomology sector, not to this kinetic calculation.

---

## 7. Maxwell field plus Faddeev--Popov ghost

In Feynman gauge, the one-form operator is

\[
(\Delta_1)_M{}^N=-\delta_M{}^N\nabla^2+R_M{}^N,
\]

so

\[
C_{\rm vec}=2,
\qquad
\operatorname{tr}E=R_6,
\qquad e_{\rm vec}=1,
\qquad F=0.
\]

The complex scalar ghost carries no Lorentz spin connection and has \(E=0\). Therefore the representation-dependent trace correction is entirely the one-form contribution:

\[
\boxed{
\Delta G_{\rm tr}^{A+gh}
=
\frac3{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\tag{XXII.9}
\]

The scalar-like determinant multiplicity is

\[
\nu_{A+gh}=6-2=4,
\]

so

\[
\boxed{
G_{A+gh}^{\rm fin}
=-\frac1{4\pi^3L^2}
\operatorname{Re}\!\left[\mathcal G_4(\tau)(d\tau)^2\right]
+
\frac3{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\tag{XXII.10}
\]

The gauge and ghost determinants are kept together throughout; no statement is made about a gauge field determinant in isolation.

---

## 8. Weyl / symplectic-Majorana-Weyl parity-even sector

A complex Weyl determinant has half the parity-even Dirac trace:

\[
\nu_W=-4,
\qquad C_W=1,
\qquad e_W=1.
\]

Thus

\[
\boxed{
G_W^{\rm fin}
=
\frac1{4\pi^3L^2}
\operatorname{Re}\!\left[\mathcal G_4(\tau)(d\tau)^2\right]
-
\frac1{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
}
\tag{XXII.11}
\]

For the parity-even magnitude of the 6d \(\mathcal N=(1,0)\) symplectic-Majorana-Weyl gaugino, this is the same determinant weight used in Model XXI. Chiral phases are not included.

---

## 9. 6d \(\mathcal N=(1,0)\) vector multiplet

A free vector multiplet contains one gauge vector and one symplectic-Majorana-Weyl gaugino [FerraraRiccioniSagnotti1998, OhmoriEtAl2014].

Adding (XXII.10) and (XXII.11), the weight-four trace-free terms cancel exactly:

\[
-\frac1{4\pi^3L^2}
\operatorname{Re}[\mathcal G_4(d\tau)^2]
+
\frac1{4\pi^3L^2}
\operatorname{Re}[\mathcal G_4(d\tau)^2]
=0.
\]

The spin/endormorphism trace terms do **not** cancel:

\[
\frac3{16}-\frac1{16}=\frac18.
\]

Therefore

\[
\boxed{
G_{\rm vm}^{\rm fin}
=
\frac{Z_\tau(2)}{8\pi^3L^2}
\,g_{\rm hyp}.
}
\tag{XXII.12}
\]

This is the central result of Model XXII.

Because

\[
Z_\tau(2)>0
\]

on \(\mathbb H\), the finite parity-even vector-multiplet threshold is positive definite in the controlled region where the heavy-tower derivative expansion is valid.

This is particularly sharp when compared with Model XXI:

\[
\boxed{
\begin{array}{ll}
\text{local UV Poincare sector:}&-2+2=0,\\[1mm]
\text{finite trace-free weight-4 sector:}&4-4=0,\\[1mm]
\text{finite spin-transport trace sector:}&\displaystyle \frac3{16}-\frac1{16}=\frac18.
\end{array}}
\]

Thus local supersymmetric cancellation does not imply cancellation of the finite nonlocal gravitational-modulus response in this restricted metric background.

---

## 10. Modular and cusp audit

Both tensors appearing in the general answer are modular:

\[
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2]
\]

is invariant because \(\mathcal G_4\) has holomorphic weight four, while

\[
Z_\tau(2)g_{\rm hyp}
\]

is invariant because \(Z_\tau(2)\) is the modular-invariant nonholomorphic Epstein/Eisenstein series and \(g_{\rm hyp}\) is invariant.

For the vector multiplet the surviving finite tensor is therefore globally modular and positive in the interior.

The cusp remains outside a uniform heavy-tower EFT: as \(Y\to\infty\), modes with one lattice quantum number zero become light. The growth of \(Z_\tau(2)\) at the cusp must not be interpreted using the same integrated-out-tower EFT beyond its validity domain.

---

## 11. What is and is not established

### Established background

- periodic heat-kernel / winding expansion and spin Wilson line: von Gersdorff [vonGersdorff2008];
- general Laplace-type heat-kernel structure: Vassilevich [Vassilevich2003];
- Lichnerowicz formula: Lawson--Michelsohn [LawsonMichelsohn1989];
- vector multiplet field content: Ferrara--Riccioni--Sagnotti and Ohmori et al. [FerraraRiccioniSagnotti1998, OhmoriEtAl2014].

### Derived here

- equations (XXII.1)--(XXII.3), the exact elliptic spin-connection quadratic identities;
- equations (XXII.4)--(XXII.6), the representation-dependent torus threshold formula in the fixed convention;
- equations (XXII.8), (XXII.10), (XXII.11), the explicit Dirac/vector/Weyl finite tensors;
- equation (XXII.12), the positive vector-multiplet finite threshold.

### Not claimed

- no chiral anomaly cancellation follows from (XXII.12);
- no supersymmetric completion of an arbitrary \(\tau(x)\) metric background has been constructed;
- no Einstein equation or horizon law follows;
- no claim is made beyond the locally trivial, fixed-volume, block-diagonal torus family and the stated parity-even determinant convention.

## Bottom line

\[
\boxed{
\textbf{Spin transport changes the scalar Model-XX answer qualitatively:}
\quad
G^{\rm fin}_R
\in
\operatorname{span}\left\{
\operatorname{Re}[\mathcal G_4(d\tau)^2],
Z_\tau(2)g_{\rm hyp}
\right\}.
}
\]

For the independently specified 6d \(\mathcal N=(1,0)\) vector multiplet, the first tensor cancels and the second survives with a fixed positive coefficient.
