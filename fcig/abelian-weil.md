# FCIG Explicit Model IIIc: Higher-Dimensional Weil / Metaplectic Descent

**Status:** Gate D worked derivation / v0.3  
**Date:** 2026-09-08

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are calculations carried out in this FCIG note. Statements marked **FCIG interpretation** are not attributed to the cited literature.

This note completes the higher-dimensional modular/Weil gate left open in `abelian-model.md`.

The ambient family is the principally polarized abelian variety

\[
A_\Omega
=\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g),
\qquad
\Omega\in\mathfrak H_g,
\]

with the level-\(k\) theta-state space

\[
\mathcal H_k(\Omega)=H^0(A_\Omega,L_\Omega^k),
\qquad
N_k=\operatorname{rank}\mathcal H_k=k^g.
\]

The standard modular background is the symplectic action of \(\operatorname{Sp}_{2g}(\mathbf Z)\) on Siegel space and the transformation law of Riemann theta functions with characteristics [Igu72; DLMF21]. The projective/metaplectic nature of the resulting Weil representation and its relation to the Heisenberg/Schrödinger model are standard [LV80]. A modern explicit even-level implementation of Igusa's transformation formula can also be found in [MM22].

The finite matrices, signs, determinant phases, and corrected-line holonomies below are derived in the conventions of the FCIG abelian model.

---

## 1. Symplectic action and Hodge automorphy

Write

\[
\gamma=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}
\in\operatorname{Sp}_{2g}(\mathbf Z).
\]

The standard action is

\[
\boxed{
\gamma\cdot\Omega
=(A\Omega+B)(C\Omega+D)^{-1}
}
\tag{1.1}
\]

and the corresponding fiber coordinate is

\[
\boxed{
z'=(C\Omega+D)^{-T}z.
}
\tag{1.2}
\]

**Established.** The multidimensional theta transformation law has a common factor

\[
\kappa(\gamma,\text{characteristic})
\det(C\Omega+D)^{1/2}
\exp\!\left[
\pi i\, z^T(C\Omega+D)^{-1}Cz
\right]
\]

and transforms the theta characteristic affinely; see Igusa and DLMF §21.5 [Igu72; DLMF21]. The square root and the multiplier are the source of the metaplectic/projective structure.

The rank-\(g\) Hodge bundle has factor of automorphy \(C\Omega+D\), so its determinant line \(\lambda_H\) has scalar factor \(\det(C\Omega+D)\) in modular-form convention [FC90]. In the pulled-back frame convention used below,

\[
\eta_{\gamma\Omega}
\longmapsto
\det(C\Omega+D)^{-1}\eta_\Omega.
\tag{1.3}
\]

This convention matches the metric identity

\[
F_{\lambda_H}=-\partial\bar\partial\log\det\operatorname{Im}\Omega
\]

used in Explicit Model III.

---

## 2. Even-level theta basis

Use the level-\(k\) basis

\[
\boxed{
 s_{\mathbf j}^{(k)}(z,\Omega)
=
\sum_{n\in\mathbf Z^g}
\exp\!\left[
\pi i k
\left(n+\frac{\mathbf j}{k}\right)^T
\Omega
\left(n+\frac{\mathbf j}{k}\right)
+
2\pi i k
\left(n+\frac{\mathbf j}{k}\right)^Tz
\right],
}
\tag{2.1}
\]

where

\[
\mathbf j\in(\mathbf Z/k\mathbf Z)^g.
\]

**Established background.** Such level structures and their Heisenberg/theta-group actions are standard in the theory of theta functions and polarized abelian varieties [Mum83; BL04]. Igusa's general transformation law shows that half-characteristic shifts occur under the full symplectic group [Igu72; DLMF21].

For the zero-secondary-characteristic basis (2.1), even \(k\) is the clean sector for the elementary generators below: all three generator types close on the same \(k^g\)-dimensional basis. The odd-level obstruction is treated separately in §10.

---

## 3. Upper symplectic shears

Let

\[
T_B=
\begin{pmatrix}
I&B\\
0&I
\end{pmatrix},
\qquad
B=B^T\in M_g(\mathbf Z).
\]

Then

\[
\Omega\mapsto\Omega+B.
\]

For even \(k\), substitute (2.1):

\[
\begin{aligned}
&\pi i k
\left(n+\frac{\mathbf j}{k}\right)^TB
\left(n+\frac{\mathbf j}{k}\right)\\
&\qquad=
\pi i k n^TBn
+2\pi i n^TB\mathbf j
+\frac{\pi i}{k}\mathbf j^TB\mathbf j.
\end{aligned}
\]

The first term is an integral multiple of \(2\pi i\) because \(k\) is even, and the second is always an integral multiple of \(2\pi i\). Therefore:

### Proposition 3.1 — shear matrix

\[
\boxed{
U_k(T_B)_{\mathbf j\mathbf m}
=
\delta_{\mathbf j\mathbf m}
\exp\!\left(\frac{\pi i}{k}\mathbf j^TB\mathbf j\right).
}
\tag{3.1}
\]

Equivalently,

\[
s_{\mathbf j}^{(k)}(z,\Omega+B)
=
\exp\!\left(\frac{\pi i}{k}\mathbf j^TB\mathbf j\right)
 s_{\mathbf j}^{(k)}(z,\Omega).
\]

**Derived here.** Equation (3.1) is the explicit matrix in the conventions of this note. General theta transformation theory is cited only as background [Igu72; DLMF21; LV80].

The shear matrices obey exactly

\[
\boxed{
U_k(T_{B_1})U_k(T_{B_2})=U_k(T_{B_1+B_2}).
}
\tag{3.2}
\]

---

## 4. The Fourier generator

Take

\[
S=
\begin{pmatrix}
0&-I\\
I&0
\end{pmatrix},
\]

so that

\[
\Omega\mapsto-\Omega^{-1},
\qquad
z\mapsto\Omega^{-1}z.
\]

Apply multidimensional Poisson summation to (2.1). Using the same Gaussian convention as the Bergman calculation in Explicit Model IIIb gives

\[
\begin{aligned}
&s_{\mathbf j}^{(k)}
\left(\Omega^{-1}z,-\Omega^{-1}\right)\\
&\quad=
\det(-i\Omega)^{1/2}
\exp\!\left(\pi i k z^T\Omega^{-1}z\right)
\frac1{k^{g/2}}
\sum_{\boldsymbol\ell\in(\mathbf Z/k\mathbf Z)^g}
 e^{-2\pi i\mathbf j^T\boldsymbol\ell/k}
 s_{\boldsymbol\ell}^{(k)}(z,\Omega).
\end{aligned}
\tag{4.1}
\]

The appearance of a Fourier transform as the intertwiner of Schrödinger models is standard in Weil representation theory [LV80]. The exact normalization and sign below are fixed by (2.1).

### Proposition 4.1 — finite Fourier matrix

\[
\boxed{
U_k(S)_{\mathbf j\boldsymbol\ell}
=
k^{-g/2}
 e^{-2\pi i\mathbf j^T\boldsymbol\ell/k}.
}
\tag{4.2}
\]

**Derived here.** Formula (4.2) follows directly from (4.1) in the FCIG theta convention.

Let

\[
C_{\mathbf j\boldsymbol\ell}
=\delta_{\boldsymbol\ell,-\mathbf j}
\]

be charge conjugation. Then the finite Fourier matrix satisfies

\[
\boxed{
U_k(S)^2=C,
\qquad
U_k(S)^4=I.
}
\tag{4.3}
\]

---

## 5. Integral change of basis

For

\[
R_A=
\begin{pmatrix}
A&0\\
0&A^{-T}
\end{pmatrix},
\qquad
A\in GL_g(\mathbf Z),
\]

we have

\[
\Omega\mapsto A\Omega A^T,
\qquad
z\mapsto Az.
\]

Changing the summation variable by \(A^Tn\) gives

\[
\boxed{
 s_{\mathbf j}^{(k)}(Az,A\Omega A^T)
=
 s_{A^T\mathbf j}^{(k)}(z,\Omega).
}
\tag{5.1}
\]

Thus

\[
\boxed{
U_k(R_A)_{\mathbf j\mathbf m}
=
\delta_{\mathbf m,A^T\mathbf j\;(\mathrm{mod}\;k)}.
}
\tag{5.2}
\]

**Derived here.** The matrix is a permutation matrix in the chosen indexing convention.

The elementary covariance relation is

\[
\boxed{
U_k(R_A)
U_k(T_B)
U_k(R_A)^{-1}
=
U_k(T_{ABA^T}).
}
\tag{5.3}
\]

Together with \(S\), the upper shears and these integral basis changes generate the standard symplectic/Weil calculus; the general representation-theoretic background is classical [LV80].

---

## 6. Explicit metaplectic phase

For

\[
B=I_g,
\qquad
T=T_{I_g},
\]

both \(U_k(S)\) and \(U_k(T)\) factor as \(g\)-fold tensor products of the genus-one matrices. Therefore the genus-one Gauss relation tensorizes.

### Theorem 6.1 — higher-dimensional Gauss phase

For even \(k\),

\[
\boxed{
\left(U_k(S)U_k(T)\right)^3
=
e^{\pi i g/4}\,C.
}
\tag{6.1}
\]

Together with \(U_k(S)^2=C\), this shows explicitly that the finite transport is projective before a metaplectic lift is chosen.

**Derived here.** Equation (6.1) is obtained from the explicit matrices (3.1) and (4.2). The interpretation of the scalar cocycle as a Weil/metaplectic or Maslov phase is standard [LV80].

A convenient metaplectic normalization can absorb the scalar phase into the chosen lift of \(S\) and \(T\). Different lifts redistribute constant roots of unity between generators; the projective class is the invariant object.

---

## 7. Determinant of the finite shear

Because \(U_k(T_B)\) is diagonal,

\[
\det U_k(T_B)
=
\exp\!\left[
\frac{\pi i}{k}
\sum_{\mathbf j\in(\mathbf Z/k\mathbf Z)^g}
\mathbf j^TB\mathbf j
\right].
\tag{7.1}
\]

Let

\[
S_1=\sum_{r=0}^{k-1}r=\frac{k(k-1)}2,
\qquad
S_2=\sum_{r=0}^{k-1}r^2
=\frac{k(k-1)(2k-1)}6.
\]

Summing coordinatewise gives:

### Proposition 7.1 — determinant character on shears

\[
\boxed{
\begin{aligned}
\det U_k(T_B)
=\exp\Bigg\{\pi i k^{g-1}\Bigg[
&\frac{(k-1)(2k-1)}6\operatorname{tr}B\\
&+\frac{(k-1)^2}{2}
\sum_{a<b}B_{ab}
\Bigg]\Bigg\}.
\end{aligned}
}
\tag{7.2}
\]

**Derived here.** This is a finite sum over the theta labels; no literature attribution is made for this normalization-dependent determinant formula.

---

## 8. Corrected determinant line and flat descent

Explicit Model III proved

\[
F_{\det\mathcal H_k}
=-\frac{N_k}{2}F_{\lambda_H},
\qquad
N_k=k^g.
\]

For even \(N_k\), define

\[
\boxed{
\mathscr A_{g,k}
=
\det\mathcal H_k
\otimes
\lambda_H^{N_k/2}.
}
\tag{8.1}
\]

Then

\[
\boxed{
F_{\mathscr A_{g,k}}=0.
}
\tag{8.2}
\]

Now include modular transport. In pulled-back frame convention, the theta-state determinant contributes

\[
\kappa_\gamma^{N_k}
\det(C\Omega+D)^{N_k/2}
\det U_k(\gamma),
\]

while \(\lambda_H^{N_k/2}\) contributes

\[
\det(C\Omega+D)^{-N_k/2}.
\]

The holomorphic \(\Omega\)-dependent factors cancel exactly.

Therefore the corrected line descends with the purely constant multiplier

\[
\boxed{
\chi_{g,k}(\widetilde\gamma)
=
\kappa_{\widetilde\gamma}^{N_k}
\det U_k(\widetilde\gamma),
}
\tag{8.3}
\]

where \(\widetilde\gamma\) denotes a chosen metaplectic/theta lift.

**Derived here.** Equation (8.3) is the FCIG corrected-line consequence of the standard theta/Hodge automorphy factors [Igu72; DLMF21; FC90] together with the determinant identity derived in Explicit Model III.

**FCIG interpretation.** The local curvature cancellation removes the continuous Hodge factor, leaving a finite/unitary descent character. Thus local anomaly cancellation does not imply trivial global anomaly.

---

## 9. A nontrivial genus-two holonomy

Take

\[
g=2,
\qquad
k=2,
\qquad
N_k=4,
\]

and choose the symmetric integral shear

\[
\boxed{
B_\times=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
}
\tag{9.1}
\]

Since \(C=0\), \(D=I\), the Hodge automorphy factor is exactly one. Thus the corrected-line multiplier is simply

\[
\chi_{2,2}(T_{B_\times})
=
\det U_2(T_{B_\times}).
\]

The four theta labels are

\[
(0,0),(0,1),(1,0),(1,1),
\]

and the diagonal phases are

\[
1,\;1,\;1,\;-1.
\]

Therefore

\[
\boxed{
\chi_{2,2}(T_{B_\times})=-1.
}
\tag{9.2}
\]

This is the simplest explicit higher-dimensional witness that

\[
\boxed{
F_{\mathscr A_{g,k}}=0
\quad\not\Rightarrow\quad
\operatorname{Hol}(\mathscr A_{g,k})=1.
}
\tag{9.3}
\]

**Derived here.** Equation (9.2) is an exact finite-dimensional calculation, independently reproduced by `abelian-weil.py`.

Thus the higher-dimensional abelian model now contains an explicit flat but globally nontrivial determinant sector.

---

## 10. Odd level and characteristic transport

For odd \(k\), the same zero-secondary-characteristic basis is not stable under every integral shear. Indeed,

\[
e^{\pi i k n^TBn}
\]

is no longer automatically one when \(B\) has odd diagonal entries. This is the level-\(k\) version of the affine half-characteristic shifts in the general theta transformation law [Igu72; DLMF21].

Therefore the odd-level object should not be forced into the even-level formula by choosing ad hoc signs. One must instead use one of the equivalent standard refinements:

1. enlarge the theta state bundle to include the transported characteristic sectors;
2. restrict to an appropriate theta/congruence subgroup preserving the chosen characteristic;
3. pass to the metaplectic/theta cover where the square-root data are part of the object.

This is consistent with the general Weil representation being naturally attached to a metaplectic central extension/projective symplectic action [LV80].

For FCIG, the corrected object is therefore written schematically as

\[
\boxed{
\widetilde{\mathscr A}_{g,k}
=
\det\widetilde{\mathcal H}_k
\otimes
\widetilde\lambda_H^{\,N_k/2}
}
\tag{10.1}
\]

on the chosen metaplectic/theta cover when \(N_k\) is odd.

**FCIG interpretation.** The need for the cover is not an extra anomaly invented by FCIG; it is the standard half-integral-weight/metaplectic datum already present in theta transformation theory. FCIG uses it only to keep the local-curvature and global-holonomy sectors separate.

---

## 11. Numerical and direct-theta verification

The verifier `abelian-weil.py` checks two logically different layers.

### Finite matrix layer

For small even \(k\) and \(g\), it verifies

\[
U_S^\dagger U_S=I,
\qquad
U_{T_B}^\dagger U_{T_B}=I,
\]

\[
U_S^2=C,
\]

\[
(U_SU_{T_I})^3=e^{\pi i g/4}C,
\]

and

\[
U_{R_A}U_{T_B}U_{R_A}^{-1}=U_{T_{ABA^T}}.
\]

It also checks the closed determinant formula (7.2).

### Direct theta layer

For a non-diagonal genus-two period matrix, it independently evaluates the truncated theta sums and verifies

\[
\Theta_k(z,\Omega+B)=U_k(T_B)\Theta_k(z,\Omega)
\]

and

\[
\Theta_k(\Omega^{-1}z,-\Omega^{-1})
=
\det(-i\Omega)^{1/2}
 e^{\pi i k z^T\Omega^{-1}z}
U_k(S)\Theta_k(z,\Omega).
\]

At the included cutoffs the displayed errors are near floating-point precision for the tested \(g=2,k=2\) example.

Numerical agreement is a convention check; Propositions 3.1–7.1 are analytic finite/Gaussian calculations.

---

## 12. Gate D result

The v0.3 modular gate now has a precise answer.

For even \(k\):

\[
\boxed{
\begin{aligned}
U_k(T_B)_{\mathbf j\mathbf m}
&=\delta_{\mathbf j\mathbf m}
 e^{\pi i\mathbf j^TB\mathbf j/k},\\
U_k(S)_{\mathbf j\boldsymbol\ell}
&=k^{-g/2}e^{-2\pi i\mathbf j^T\boldsymbol\ell/k},\\
U_k(R_A)_{\mathbf j\mathbf m}
&=\delta_{\mathbf m,A^T\mathbf j},\\
(U_k(S)U_k(T_I))^3
&=e^{\pi i g/4}C.
\end{aligned}
}
\]

The corrected determinant line satisfies

\[
\boxed{
F_{\mathscr A_{g,k}}=0,
\qquad
\operatorname{Hol}(\mathscr A_{g,k})
\text{ can be nontrivial}.
}
\]

The explicit witness is

\[
\boxed{
\chi_{2,2}(T_{B_\times})=-1.
}
\]

For odd \(k\), the same statement lives naturally on a characteristic/metaplectic refinement rather than on the fixed zero-characteristic basis.

Hence the elliptic mechanism

\[
\text{local curvature cancellation}
+
\text{residual metaplectic/global holonomy}
\]

survives in higher-dimensional principally polarized abelian geometry.

This completes the mathematical content of FCIG milestone v0.3. It is not a derivation of spacetime gravity and no claim of literature novelty is made.

---

## 13. Next gate

The next milestone is the curved test:

\[
\boxed{
\text{flat ppav fibers}
\longrightarrow
\text{compact genus-}g\ge2\text{ curves}.
}
\]

There the local Bergman polynomial sector is nonzero, so the project can finally test whether

\[
\text{local curvature}
\oplus
\text{global/geodesic sector}
\oplus
\text{determinant holonomy}
\]

remain cleanly distinguishable in a genuinely curved family.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Igu72]** J. Igusa, *Theta Functions*, Springer, 1972.
- **[DLMF21]** NIST Digital Library of Mathematical Functions, Chapter 21, especially §21.5, multidimensional theta modular transformations.
- **[LV80]** G. Lion and M. Vergne, *The Weil Representation, Maslov Index and Theta Series*, Birkhäuser, 1980.
- **[MM22]** D. Markushevich and A. Moreau, *Action of the automorphism group on the Jacobian of Klein's quartic curve II: Invariant theta functions*, arXiv:2208.08737 (2022).
- **[Mum83]** D. Mumford, *Tata Lectures on Theta I*, Birkhäuser, 1983.
- **[BL04]** C. Birkenhake and H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer, 2004.
- **[FC90]** G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Springer, 1990.
