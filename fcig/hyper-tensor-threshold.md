# FCIG Model XXIII — Hyper/tensor multiplet automorphic thresholds

**Status:** derived in the same locally trivial, fixed-volume elliptic family and parity-even determinant convention as Models XX–XXII. Hypermultiplet and tensor-multiplet two-derivative thresholds are fixed below. The self-dual two-form is treated through the determinant-magnitude/holomorphic-factorization literature; its global chiral phase, theta characteristic, zero-mode data and anomaly line remain separate.

## 1. Purpose and citation policy

Model XXII fixed the two finite automorphic tensor structures

\[
\mathcal T_4:=\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
\qquad
\mathcal T_0:=Z_\tau(2)g_{\rm hyp},
\]

and found for one 6d \(\mathcal N=(1,0)\) vector multiplet

\[
G_{\rm vec}^{\rm fin}=\frac{1}{8\pi^3L^2}\mathcal T_0.
\]

The standard 6d \(\mathcal N=(1,0)\) multiplet contents are **Established** [FerraraRiccioniSagnotti1998, OhmoriShimizuTachikawaYonekura2014]. The gauge-fixed determinant of a non-chiral two-form and the three physical degrees of freedom of a self-dual 6d two-form are standard [HuangRoibanTseytlin2018]. Holomorphic factorization of a non-chiral \(2k\)-form into chiral/anti-chiral pieces is standard [HenningsonNilssonSalomonson1999, Gustavsson2002], while the global definition and anomaly bundle of the self-dual field require the refined constructions of Witten, Belov--Moore and Monnier [Witten1997, BelovMoore2006, Monnier2012].

The combinatorial \(p\)-form Lorentz-index reduction and the final Model-XXIII threshold coefficients are **Derived here** in the Model-XXII convention.

---

## 2. Coefficient convention

Write any parity-even two-derivative result as

\[
\boxed{
G^{\rm fin}
=\frac{1}{\pi^3L^2}
\left(
A\,\mathcal T_4+B\,\mathcal T_0
\right).
}
\]

Also write \(C_{\rm local}\) for the local six-dimensional \(R_6\) heat-kernel coefficient normalized to one real minimal scalar, as in Model XXI.

Thus each field or multiplet is summarized by

\[
(C_{\rm local},A,B).
\]

The Model-XXII entries are

\[
\begin{array}{c|ccc}
\text{field} & C_{\rm local} & A & B\\ \hline
\text{real scalar} & 1 & -\frac1{16} & 0\\
\text{SMW/Weyl magnitude} & 2 & \frac14 & -\frac1{16}\\
\text{Maxwell+FP ghost} & -2 & -\frac14 & \frac3{16}.
\end{array}
\]

---

## 3. Hypermultiplet

A 6d \(\mathcal N=(1,0)\) hypermultiplet contains four real scalars and one symplectic-Majorana-Weyl fermion. Chirality changes the phase/anomaly sector but not the parity-even determinant magnitude used here.

Therefore

\[
C_{\rm local}^{\rm hyper}=4(1)+2=6,
\]

\[
A_{\rm hyper}=4\left(-\frac1{16}\right)+\frac14=0,
\]

and

\[
B_{\rm hyper}=0-\frac1{16}=-\frac1{16}.
\]

Hence

\[
\boxed{
(C_{\rm local},A,B)_{\rm hyper}
=\left(6,0,-\frac1{16}\right),
}
\]

and

\[
\boxed{
G_{\rm hyper}^{\rm fin}
=-\frac{Z_\tau(2)}{16\pi^3L^2}\,g_{\rm hyp}.
}
\tag{XXIII.1}
\]

Since \(Z_\tau(2)>0\), the isolated hypermultiplet contribution is negative definite in this parity-even threshold convention. This is a one-loop contribution, not a statement that a complete renormalized target metric is negative.

---

## 4. Non-chiral two-form determinant

For a real non-chiral two-form gauge field, the standard ghost-for-ghost gauge fixing gives

\[
Z_{B,\rm nonch}
\propto
\left[
\frac{(\det{}'\Delta_1)^2}
{\det{}'\Delta_2\,(\det{}'\Delta_0)^3}
\right]^{1/2},
\]

or equivalently

\[
\boxed{
W_{B,\rm nonch}
=\frac12\log\det{}'\Delta_2
-\log\det{}'\Delta_1
+\frac32\log\det{}'\Delta_0.
}
\tag{XXIII.2}
\]

This determinant structure is standard; see [HuangRoibanTseytlin2018] and the general reducible \(p\)-form gauge-fixing literature.

The scalar-like determinant multiplicity is

\[
\nu_{B,\rm nonch}
=\binom62-2\binom61+3\binom60
=15-12+3=6,
\]

which matches the six propagating degrees of freedom of a non-chiral massless two-form in six dimensions.

Hence its trace-free coefficient is

\[
\boxed{A_{B,\rm nonch}=-\frac{6}{16}=-\frac38.}
\tag{XXIII.3}
\]

---

## 5. Two-form Lorentz index and endomorphism trace

For the \(p\)-form representation \(\Lambda^p\mathbb R^d\), a rotation in one orthonormal two-plane acts nontrivially on forms containing exactly one of the two rotated directions. With the Model-XXII normalization \(C_{\rm vec}=2\),

\[
\boxed{
C_p=2\binom{d-2}{p-1}.
}
\tag{XXIII.4}
\]

For the Hodge Laplacian, evaluation on constant curvature gives

\[
\boxed{
\operatorname{tr}_{\Lambda^p}E=e_pR,
\qquad
e_p=\binom{d-2}{p-1}
}
\tag{XXIII.5}
\]

in the Model-XXII convention \(P=-D^2+E\).

For \(d=6,p=2\),

\[
C_2=8,
\qquad
e_2=4.
\]

Thus one ordinary real two-form determinant contributes

\[
\frac{2C_2-e_2}{16}=\frac{12}{16}
\]

to the \(Z_\tau(2)g_{\rm hyp}\) coefficient. The \(-\log\det\Delta_1\) term in (XXIII.2) is minus twice the standard real one-form determinant and therefore contributes

\[
-2\left(\frac3{16}\right)=-\frac6{16}.
\]

The scalar ghost-for-ghost term has no spin/endormorphism trace contribution. Hence

\[
\boxed{
B_{B,\rm nonch}=\frac{12-6}{16}=\frac38.
}
\tag{XXIII.6}
\]

For the local \(b_2\) coefficient, the corresponding one-half-log-determinant ratios are

\[
c_2=\binom62-6\binom41=15-24=-9,
\qquad
c_1=6-6=0,
\qquad
c_0=1.
\]

Applying the determinant exponents in (XXIII.2) gives

\[
\boxed{
C_{\rm local}^{B,\rm nonch}
=-9-2(0)+3(1)=-6.
}
\tag{XXIII.7}
\]

Therefore

\[
\boxed{
(C_{\rm local},A,B)_{B,\rm nonch}
=\left(-6,-\frac38,\frac38\right).
}
\]

All coefficient reductions in this section are **Derived here** from the standard determinant and Model-XXII heat-kernel convention.

---

## 6. Self-dual two-form: parity-even magnitude prescription

A chiral/self-dual two-form is not globally defined by simply writing an unconstrained covariant Gaussian action. Standard constructions instead use holomorphic factorization or a higher-dimensional Chern--Simons/holographic description [HenningsonNilssonSalomonson1999, Gustavsson2002, Witten1997, BelovMoore2006].

For the present restricted question we require only the **parity-even oscillator determinant magnitude**, not the global phase or theta-function sector. Holomorphic factorization identifies the non-chiral partition function as a chiral times anti-chiral product, and Monnier shows that the norm of the self-dual partition function is a square root of the corresponding determinant norm [Monnier2012]. Therefore, after excluding zero modes/topological flux sectors exactly as in the nonzero-tower Model XX setup, the self-dual magnitude contributes one half of the non-chiral logarithmic determinant response:

\[
\boxed{
(C_{\rm local},A,B)_{B^+}
=\frac12(C_{\rm local},A,B)_{B,\rm nonch}
=\left(-3,-\frac3{16},\frac3{16}\right).
}
\tag{XXIII.8}
\]

The same parity-even magnitude holds for opposite self-duality. This equation is **not** a claim that the complete chiral partition function is literally the positive square root of the non-chiral function globally. The theta characteristic, anomaly line, zero modes and global phase remain separate data.

---

## 7. Tensor multiplet

A 6d \(\mathcal N=(1,0)\) tensor multiplet contains one (anti-)self-dual two-form, one real scalar and one symplectic-Majorana-Weyl fermion [FerraraRiccioniSagnotti1998, OhmoriShimizuTachikawaYonekura2014].

Using (XXIII.8) and the Model-XXII scalar/Weyl entries,

\[
C_{\rm local}^{\rm tensor}
=-3+1+2=0,
\]

\[
A_{\rm tensor}
=-\frac3{16}-\frac1{16}+\frac4{16}=0,
\]

and

\[
B_{\rm tensor}
=\frac3{16}+0-\frac1{16}=\frac18.
\]

Hence

\[
\boxed{
(C_{\rm local},A,B)_{\rm tensor}
=\left(0,0,\frac18\right),
}
\]

and

\[
\boxed{
G_{\rm tensor}^{\rm fin}
=\frac{Z_\tau(2)}{8\pi^3L^2}\,g_{\rm hyp}.
}
\tag{XXIII.9}
\]

This is positive definite away from the cusp/EFT breakdown region.

A notable result is the exact equality, in this restricted parity-even convention,

\[
\boxed{
G_{\rm tensor}^{\rm fin}=G_{\rm vector}^{\rm fin}.
}
\tag{XXIII.10}
\]

Both vector and tensor multiplets cancel the local trace sector and the finite weight-four trace-free sector, leaving the same positive finite \(Z_\tau(2)g_{\rm hyp}\) response.

---

## 8. Multiplet coefficient table

The completed parity-even table is

\[
\boxed{
\begin{array}{c|ccc|c}
\text{multiplet}
& C_{\rm local}
& A_{\mathcal G_4}
& B_{Z_2}
& G^{\rm fin}\\ \hline
\text{vector}
&0&0&\frac18
&+\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp}\\[1mm]
\text{hyper}
&6&0&-\frac1{16}
&-\frac{Z_\tau(2)}{16\pi^3L^2}g_{\rm hyp}\\[1mm]
\text{tensor}
&0&0&\frac18
&+\frac{Z_\tau(2)}{8\pi^3L^2}g_{\rm hyp}
\end{array}
}
\tag{XXIII.11}
\]

Thus **all three supersymmetric multiplets cancel the finite weight-four trace-free tensor** in the present background. Spin/self-dual structure reorganizes the finite answer entirely into the Poincare-trace automorphic tensor.

For independently fixed multiplicities \((n_V,n_H,n_T)\), linearity gives

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{2n_V-n_H+2n_T}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp}.
}
\tag{XXIII.12}
\]

This formula is bookkeeping, not a license to choose multiplet numbers to engineer positivity or cancellation.

---

## 9. Anomaly coefficients are different observables

Six-dimensional chiral multiplets also carry local/global anomaly data [OhmoriShimizuTachikawaYonekura2014]. The coefficients in their anomaly polynomials are not equal to \((C_{\rm local},A,B)\). Model XXIII therefore does **not** infer anomaly cancellation from (XXIII.11), nor does an anomaly-free multiplet combination imply cancellation of the kinetic threshold.

In particular:

\[
\boxed{
\text{anomaly polynomial}
\neq
\text{local kinetic counterterm}
\neq
\text{finite automorphic kinetic threshold}.
}
\]

This maintains the separation established in Models XII--XIV and XXI--XXII.

---

## 10. Scope and validity

The result assumes:

1. the locally trivial, block-diagonal, fixed-volume elliptic family of Model XX;
2. the nonzero KK/winding tower with the same Epstein analytic-subtraction convention;
3. parity-even determinant magnitudes;
4. no background gauge fields, torsion twists or nontrivial torus-bundle monodromy beyond the modular covariance already tracked;
5. the self-dual determinant-magnitude prescription only after separating zero modes, theta data and chiral/global phases.

As \(Y\to\infty\), tower modes become light and the heavy-tower derivative expansion fails uniformly. No Einstein equation, horizon law or full supersymmetric background is derived.

---

## 11. References used in this milestone

- [FerraraRiccioniSagnotti1998] — standard 6d \(\mathcal N=(1,0)\) vector/tensor multiplets.
- [OhmoriShimizuTachikawaYonekura2014] — standard 6d multiplet/anomaly conventions.
- [HenningsonNilssonSalomonson1999] — holomorphic factorization of non-chiral \((4k+2)\)-dimensional form theory into chiral factors.
- [Gustavsson2002] — chiral two-form partition functions on a flat six-torus by holomorphic factorization.
- [Witten1997] — definition of the self-dual five-brane partition function and its global subtleties.
- [BelovMoore2006] — Chern--Simons/holographic construction of self-dual field theory.
- [Monnier2012] — self-dual anomaly bundle; norm of the self-dual partition function and determinant-line square-root structure.
- [HuangRoibanTseytlin2018] — explicit 6d two-form determinant/degree-of-freedom bookkeeping and self-dual quantum corrections.
- Model XXII references — periodic heat kernel, Lichnerowicz/Weitzenbock and elliptic automorphic normalization.
