# FCIG: The Determinant Normalization Selector

**Status:** exact relative selector theorem + functoriality + no-go boundaries  
**Date:** 2026-09-12

> **Claim policy.** Determinant-line and Quillen/Bismut--Freed constructions are **Established** [BF86a; BF86b; Zin16]. The probability interface is **Derived here** as an assembly. “Canonical” means canonical relative to the operator-enhanced model, never from the probability density alone.

---

## 1. The obstruction

The normalization audit proved that a probability family \(p_b\) admits arbitrary Hermitian line-bundle lifts:

\[
q_i=h_i p,\qquad Z_i=h_i,\qquad p=q_i/Z_i.
\]

Thus \(p\) alone does not select \((L,h,\nabla)\). A Fredholm or elliptic family supplies a line through its determinant:

\[
\boxed{\text{probability normalizes the weights; the index problem selects their line.}}
\]

---

## 2. Operator-enhanced statistical models

### Definition 2.1

An **operator-enhanced statistical model** is

\[
\mathfrak S=(B,\Omega,\nu,p,\mathcal H^+,\mathcal H^-,D),
\]

where \(B\) is a parameter manifold, \((\Omega,\nu)\) is measured,

\[
\int_\Omega p(x|b)d\nu(x)=1,
\]

\(\mathcal H^\pm\to B\) are Hermitian Hilbert bundles, and

\[
D_b:\mathcal H_b^+\to\mathcal H_b^-
\]

is a smooth Fredholm family. For Quillen/Bismut--Freed geometry, \(D\) comes from a regular elliptic family over compact fibers with the requisite geometric data [BF86a; BF86b]. The operator is constitutive data, not something inferred from normalization.

### Definition 2.2

\[
\boxed{\lambda_D=\det\ker D\otimes(\det\operatorname{coker}D)^{-1}.}
\tag{2.1}
\]

Equivalently, \(\lambda_D=\det(\operatorname{Ind}D)\). Compatible determinant-line systems are established in [Zin16]; determinants of perfect complexes and their additivity belong to determinant-functor theory [KM76; Knu02].

---

## 3. Construction

Let \((\lambda_D,h_D,\nabla^D)\) be selected by \(D\). In the elliptic setting use the Quillen metric and Bismut--Freed connection. For a local nonzero frame \(\sigma_i\), put

\[
h_i=\|\sigma_i\|_{h_D}^2,\qquad
q_i(x|b)=h_i(b)p(x|b),
\tag{3.1}
\]

\[
Z_i(b)=\int_\Omega q_i(x|b)d\nu(x)=h_i(b).
\tag{3.2}
\]

Define

\[
\operatorname{Sel}_{\det}(\mathfrak S)
=(\lambda_D,h_D,\nabla^D,\{q_i,Z_i\}).
\tag{3.3}
\]

---

## 4. Relative determinant-selector theorem

### Theorem 4.1

If \(\sigma_i=t_{ij}\sigma_j\), then

\[
h_i=|t_{ij}|^2h_j,\qquad
q_i=|t_{ij}|^2q_j,\qquad
Z_i=|t_{ij}|^2Z_j.
\tag{4.1}
\]

Consequently

\[
\boxed{q_i/Z_i=p.}
\tag{4.2}
\]

For \(K_i=\log Z_i\), using

\[
F_{\nabla^D}=-\partial\bar\partial\log h_i,
\]

one has

\[
\boxed{F_{\nabla^D}=-\partial\bar\partial K_i.}
\tag{4.3}
\]

The resulting line with metric, connection, descended probability, and curvature is independent up to canonical isomorphism of the local frames.

#### Proof

Equation (4.1) is the Hermitian metric transformation law; globality of \(p\) gives the same law for \(q_i\). Equation (3.2) gives it for \(Z_i\), so the ratio descends. Equation (4.3) is the Chern formula. Frame changes alter representatives but preserve \(p\), the line with connection, and curvature. \(\square\)

**Status:** determinant geometry is **Established**; the interface is **Derived here**. It proves

\[
\boxed{\mathrm{NT\!-\!E}_D:\mathrm{PASS},\qquad
\mathrm{NT\!-\!E}_p:\mathrm{NO\!-\!GO}.}
\]

---

## 5. Naturality

A unitary equivalence \(U=(U^+,U^-):D\to D'\) satisfies

\[
U^-D=D'U^+.
\tag{5.1}
\]

It induces \(\det U:\lambda_D\to\lambda_{D'}\).

### Theorem 5.1

If \(U\) preserves the elliptic data used by the Quillen construction, then \(\det U\) preserves the determinant metric and connection. If probability families correspond, it induces

\[
\boxed{\operatorname{Sel}_{\det}(\mathfrak S)\cong
\operatorname{Sel}_{\det}(\mathfrak S').}
\]

#### Proof

Unitary equivalence identifies kernels, cokernels, and nonzero spectra. It preserves the determinant line, \(L^2\) metric, zeta-regularized Quillen factor, and induced connection. Equations (3.1)--(3.2) transport the normalization data. \(\square\)

This is functoriality only for morphisms remembering the operator enhancement. A general Markov map need not supply an intertwiner.

---

## 6. Symmetric monoidality

For orthogonal direct sums, the determinant functor gives

\[
\boxed{\lambda_{D\oplus D'}\cong\lambda_D\otimes\lambda_{D'}.}
\tag{6.1}
\]

Quillen norms multiply, hence

\[
Z_i^{D\oplus D'}=Z_i^DZ_i^{D'},\qquad
K_i^{D\oplus D'}=K_i^D+K_i^{D'},
\tag{6.2}
\]

\[
\boxed{F_{D\oplus D'}=F_D+F_{D'}.}
\tag{6.3}
\]

Thus, up to determinant grading/sign conventions, \(\operatorname{Sel}_{\det}\) is symmetric monoidal. This is additivity of operator sectors, not automatically statistical independence.

---

## 7. Index-theoretic constraint

For a geometric Dirac family, Bismut--Freed curvature is schematically

\[
\boxed{
\frac{i}{2\pi}F_{\nabla^D}
=
\left[\pi_*\!\left(\widehat A(R^{T_\pi})
\operatorname{ch}(F^E)\right)\right]_{(2)}.
}
\tag{7.1}
\]

Thus

\[
-\frac{i}{2\pi}\partial\bar\partial\log Z_i
=\text{degree-two local index density}.
\tag{7.2}
\]

This constrains the lift after \(D\) is fixed. It does not infer \(D\) from \(p\).

---

## 8. Residual no-go theorems

### No-go 8.1 — operator underdetermination

Distinct operator families can accompany the same \(p\) and have determinant lines with different Chern classes:

\[
\boxed{p\not\Rightarrow D\not\Rightarrow\lambda_D.}
\tag{8.1}
\]

The selector is a relative solution, not reconstruction from classical probability.

### No-go 8.2 — positive weights forget flat phase

The weights use only \(|t_{ij}|^2\). Replacing

\[
t_{ij}\mapsto u_{ij}t_{ij},\qquad |u_{ij}|=1,
\]

leaves \(q_i,Z_i\) unchanged. A flat unitary cocycle can change holonomy without changing positive weights or curvature. Hence

\[
\boxed{\{q_i,Z_i\}\text{ do not reconstruct }
\widehat c_1(\lambda_D,\nabla^D).}
\tag{8.2}
\]

The selector must retain the full \((\lambda_D,h_D,\nabla^D)\).

\[
\boxed{\text{modulus detects local curvature; phase is required for global holonomy.}}
\]

---

## 9. Fisher compatibility is extra

The selector gives \(-\partial\bar\partial\log Z_i=F_{\nabla^D}\), but not automatically

\[
\partial\bar\partial\log Z_i=g^F(p).
\]

### Definition 9.1

Call \((p,D)\) **Fisher-compatible** when, in fixed conventions,

\[
\boxed{g^F_{a\bar b}(p)
=\partial_a\partial_{\bar b}\log Z_i^D.}
\tag{9.1}
\]

This is a condition, not a consequence of taking determinants. A likelihood operator, coherent-state amplitude, or Bergman determinantal process must tie the score of \(p\) to variation of \(D\).

---

## 10. Categorical form

Let \(\mathsf{OpStat}\) have operator-enhanced models as objects and compatible parameter, probability, and operator morphisms. The FCIG interface is

\[
\boxed{
\operatorname{Sel}_{\det}:
\mathsf{OpStat}\to\mathsf{NormLift},\quad
(p,D)\mapsto(\lambda_D,h_D,\nabla^D,\{h_ip,h_i\}).
}
\tag{10.1}
\]

It commutes with forgetting to probability:

\[
\begin{array}{ccc}
\mathsf{OpStat} & \xrightarrow{\operatorname{Sel}_{\det}} & \mathsf{NormLift}\\
\downarrow & & \downarrow\\
\mathsf{Prob} & = & \mathsf{Prob}.
\end{array}
\tag{10.2}
\]

Publication-level completion requires exact analytic categories, pullback rules, coherence diagrams, comparison with determinant-functor universal properties, and a non-tautological class of Fisher-compatible enhancements.

---

## 11. FCIG specialization

For a family of compact curves \(\pi:\mathcal X\to B\) and \(q\ge2\), take

\[
E_q=\pi_*K_{\mathcal X/B}^q,\qquad
\lambda_q=\det R\pi_*K_{\mathcal X/B}^q.
\]

The Dolbeault family with Quillen metric and connection gives

\[
\operatorname{Sel}_{\det}(p,D_{\bar\partial,q}).
\]

This connects to the audited Weil--Petersson curvature in quillen-refinement.md. But direct-image-information-connection.md proves

\[
\boxed{
F_{\det E_q}=\operatorname{Tr}F_{E_q}
\text{ does not recover the traceless part of }F_{E_q}.}
\]

The selector chooses the abelian normalization/anomaly channel, not full operator-valued transport.

---

## 12. Gate ledger

- **DNS-A — PASS:** define \((p,D)\) and its determinant normalization lift.
- **DNS-B — PASS:** descent, frame independence, and Chern-potential identity.
- **DNS-C — PASS:** naturality under compatible unitary equivalence.
- **DNS-D — PASS:** direct-sum monoidality.
- **DNS-E — PASS WITH NO-GO:** canonical relative to \(D\), not from \(p\).
- **DNS-F — PASS WITH NO-GO:** positive weights forget flat phase/holonomy.
- **DNS-G — OPEN:** construct a non-tautological assignment \(p\mapsto D_p\).
- **DNS-H — OPEN:** prove Fisher compatibility in a concrete realization.
- **DNS-I — OPEN:** complete categorical coherence and a dedicated novelty audit.

\[
\boxed{\text{Next: which intrinsic statistical or quantum construction assigns }D_p?}
\]

**Update:** [`probability-only-bergman-selector-no-go.md`](probability-only-bergman-selector-no-go.md) proves that DNS-G is impossible for nontrivial finite-rank Bergman/projection-DPP selectors if the input is only a standard atomless probability space and naturality is required under every measure-preserving isomorphism. Polarized complex geometry gives an enriched relative selector through the Dolbeault operator. The remaining target is therefore reconstruction of the polarization, not selection from \(p\) alone.

---

## References

- [BF86a] Bismut--Freed, “The Analysis of Elliptic Families. I,” *Commun. Math. Phys.* 106 (1986), 159--176.
- [BF86b] Bismut--Freed, “The Analysis of Elliptic Families. II,” *Commun. Math. Phys.* 107 (1986), 103--163.
- [KM76] Knudsen--Mumford, “The Projectivity of the Moduli Space of Stable Curves. I,” *Math. Scand.* 39 (1976), 19--55.
- [Knu02] Knudsen, “Determinant Functors on Exact Categories and Their Extensions to Categories of Bounded Complexes,” *Michigan Math. J.* 50 (2002), 407--444.
- [Qui85] Quillen, “Determinants of Cauchy--Riemann Operators over a Riemann Surface,” *Funct. Anal. Appl.* 19 (1985), 31--34.
- [Zin16] Zinger, “The Determinant Line Bundle for Fredholm Operators: Construction, Properties, and Classification,” *Math. Scand.* 118 (2016), 203--268; [arXiv:1304.6368](https://arxiv.org/abs/1304.6368).

Machine-readable entries are in determinant-normalization-selector.bib.
