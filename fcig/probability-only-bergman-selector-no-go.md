# FCIG: Probability-Only Bergman Selector No-Go

**Status:** exact symmetry obstruction + minimal geometric repair

**Date:** 2026-09-12

**Depends on:** [`determinant-normalization-selector.md`](determinant-normalization-selector.md), [`born-slater-information.md`](born-slater-information.md), [`bls-position-transport.md`](bls-position-transport.md).

> **Claim policy.** The DPP and Bergman constructions are established background [HKPV06; Ber08]. The no-go theorem below is proved directly. It is a theorem about a precisely defined naturality demand, not a claim that every conceivable statistical-to-operator construction is impossible.
>
> Citation audit: [`probability-only-bergman-selector-no-go-citation-audit.md`](probability-only-bergman-selector-no-go-citation-audit.md).

---

## 0. Result in one page

The preceding determinant selector solved

\[
(p,D)\longmapsto (\lambda_D,h_D,\nabla^D),
\]

but left open whether the probability law itself can canonically choose \(D\). The Bergman/DPP route makes that question precise: can a probability space canonically select a finite-rank projection

\[
P_p:L^2(\Omega,p)\to L^2(\Omega,p)
\]

whose kernel defines a nontrivial projection DPP?

If “canonically” means natural under all measure-preserving isomorphisms, the answer on a standard atomless probability space is no.

\[
\boxed{
\text{full probabilistic symmetry permits only the constant one-particle sector.}
}
\]

More exactly, every finite-dimensional subspace of \(L^2(\Omega,p)\) invariant under all Koopman operators is contained in the constants. Therefore a natural finite-rank orthogonal projection has rank \(0\) or is the rank-one projection onto constants. Its projection DPP has at most one point and its determinant line is trivial.

The repair is not to search harder inside \(p\), but to reduce its automorphism group by adding geometric polarization data:

\[
(X,L,h,J,\mu)
\longmapsto
D_{\bar\partial,k}
\longmapsto
H^0(X,L^k)
\longmapsto
P_{B,k}
\longmapsto
\operatorname{DPP}(K_{B,k}).
\]

Thus Bergman quantization gives an intrinsic selector relative to a polarized complex model, not relative to a bare probability measure.

---

## 1. The category and the demanded naturality

Let \(\mathsf{Prob}_{\rm iso}^{\rm na}\) be the groupoid of standard atomless probability spaces and measure-preserving isomorphisms modulo null sets. An isomorphism

\[
T:(\Omega,p)\to(\Omega',p')
\]

induces the Koopman unitary

\[
U_T:L^2(\Omega',p')\to L^2(\Omega,p),
\qquad U_Tf=f\circ T.
\tag{1.1}
\]

### Definition 1.1 — probability-only projection selector

A probability-only finite-rank selector assigns to every object an orthogonal projection \(P_p\) of finite rank and satisfies

\[
\boxed{P_pU_T=U_TP_{p'}}
\tag{1.2}
\]

for every measure-preserving isomorphism \(T\).

Equation (1.2) is the minimum relabelling invariance expected of an intrinsic construction. In particular, for every automorphism \(T\in\operatorname{Aut}(\Omega,p)\), the range

\[
E_p:=\operatorname{ran}P_p
\]

must be invariant under \(U_T\).

---

## 2. Mixing lemma

### Lemma 2.1

Let \(T\) be a strongly mixing invertible probability-preserving transformation. The Koopman operator \(U_T\) has no nonzero finite-dimensional invariant subspace in

\[
L^2_0(\Omega,p)
:=\left\{f:\int f\,dp=0\right\}.
\]

#### Proof

Strong mixing implies, first for indicators and then by density for all \(f,g\in L^2_0\),

\[
\langle U_T^nf,g\rangle\longrightarrow0.
\tag{2.1}
\]

Suppose a nonzero finite-dimensional invariant subspace \(V\subset L^2_0\) existed. The restrictions \(U_T^n|_V\) lie in the compact unitary group \(U(V)\). Hence some subsequence \(n_j\to\infty\) satisfies

\[
U_T^{n_j}|_V\longrightarrow A
\]

for a unitary \(A\). Taking \(g=Af\) for nonzero \(f\in V\) gives

\[
\langle U_T^{n_j}f,Af\rangle\longrightarrow\|f\|^2,
\]

contradicting (2.1). \(\square\)

Standard atomless probability spaces admit strongly mixing automorphisms: after identifying the measure algebra with a nonatomic Lebesgue model, one may transport a two-sided Bernoulli shift. Mixing and Koopman formulations are classical ergodic theory [Hal56].

---

## 3. Probability-only selector theorem

### Theorem 3.1 — full-symmetry no-go

Let \((\Omega,p)\) be a standard atomless probability space. If a finite-dimensional subspace

\[
E\subset L^2(\Omega,p)
\]

is invariant under every measure-preserving automorphism, then

\[
\boxed{E\subset\mathbb C\mathbf1.}
\tag{3.1}
\]

#### Proof

The constants and \(L^2_0\) are invariant under every Koopman operator, and

\[
L^2=\mathbb C\mathbf1\oplus L^2_0.
\]

Let \(Q_0\) be orthogonal projection onto \(L^2_0\). Since \(Q_0\) commutes with every Koopman operator, \(Q_0E\) is finite-dimensional and invariant under every automorphism. Choose one strongly mixing automorphism \(T\). Lemma 2.1 gives \(Q_0E=0\). Hence \(E\subset\mathbb C\mathbf1\). \(\square\)

### Corollary 3.2 — classification of natural finite-rank projections

Every selector satisfying Definition 1.1 has

\[
\boxed{P_p=0\quad\text{or}\quad P_p=\Pi_{\mathbf1}.}
\tag{3.2}
\]

If the rank is required to be constant on the groupoid, these are the only two selectors.

### Corollary 3.3 — DPP obstruction

A rank-\(N\) projection kernel defines a projection DPP with exactly \(N\) particles almost surely [HKPV06]. Consequently a probability-only natural projection DPP on a standard atomless probability space has

\[
\boxed{N\le1.}
\tag{3.3}
\]

For \(N=1\), the normalized constant vector has kernel \(K(x,y)=1\) relative to \(p\), so the one-point process is just the original law \(p\). No higher Bergman/fermionic determinant structure has been recovered.

---

## 4. Consequence for the determinant normalization selector

The theorem strengthens the earlier underdetermination statement. Under full relabelling naturality,

\[
\boxed{
p\not\longmapsto P_{B,p}\not\longmapsto D_p
}
\tag{4.1}
\]

for any nontrivial finite-rank Bergman-style sector.

The rank-one constant sector has a canonically trivial determinant line:

\[
\det(\mathbb C\mathbf1)\cong\mathbb C.
\]

It therefore cannot generate the hidden normalization topology sought in the FCIG program.

This is a symmetry obstruction, not a cardinality obstruction:

\[
\boxed{
\text{a bare probability law has too many automorphisms to select a nontrivial mode space.}
}
\]

---

## 5. Minimal repair: polarization before projection

Let \(X\) be a compact complex manifold, \(L\to X\) a positive holomorphic line bundle, \(h\) a Hermitian metric, \(J\) the complex structure, and \(\mu\) a volume form. For \(k\ge1\), define

\[
D_{J,L,h,k}
=\sqrt2\left(\bar\partial_{L^k}+\bar\partial_{L^k}^{*}\right).
\tag{5.1}
\]

Its degree-zero harmonic sector is

\[
\ker D_{J,L,h,k}\cap\Omega^{0,0}(X,L^k)
=H^0(X,L^k).
\tag{5.2}
\]

The orthogonal projection

\[
P_{B,k}:L^2(X,L^k;h^k,\mu)\to H^0(X,L^k)
\tag{5.3}
\]

is the Bergman projector. Its kernel defines the standard Bergman projection DPP; in complex geometry this is the free-fermion/DPP construction studied by Berman [Ber08].

### Theorem 5.1 — polarized Bergman selector

The assignment

\[
\boxed{
(X,J,L,h,\mu,k)
\longmapsto
(D_{J,L,h,k},H^0(X,L^k),P_{B,k},\operatorname{DPP}(K_{B,k}))
}
\tag{5.4}
\]

is natural under biholomorphisms equipped with compatible unitary line-bundle isomorphisms preserving \(h\) and \(\mu\).

#### Proof

Such an isomorphism intertwines \(\bar\partial_{L^k}\), its metric adjoint, and therefore \(D_{J,L,h,k}\). It identifies the kernels and conjugates the orthogonal projections. The determinantal correlation functions, being determinants of the transported kernel, are preserved. \(\square\)

This closes the selector only on the enriched category:

\[
\boxed{
\mathrm{PolGeom}
\xrightarrow{\ D_{\bar\partial}\ }
\mathrm{OpStat}
\xrightarrow{\ \operatorname{Sel}_{\det}\ }
\mathrm{NormLift}.
}
\tag{5.5}
\]

It does not factor through the forgetful map to bare probability spaces.

---

## 6. Family version and FCIG interface

For a proper polarized holomorphic family

\[
\pi:(\mathcal X,\mathcal L,h)\to B,
\]

constant-rank hypotheses give

\[
E_k=\pi_*\mathcal L^k,
\qquad
\lambda_k=\det R\pi_*\mathcal L^k.
\tag{6.1}
\]

The fiberwise Dolbeault family selects the determinant/Quillen data, while the Bergman projector selects the Slater state and its DPP. The BLS/KE note already supplies the covariant transport needed to compare the resulting moving probability laws.

Thus the coherent diagram is

\[
\boxed{
\begin{array}{ccccc}
(\mathcal X/B,\mathcal L,h,J)
&\longrightarrow&D_{\bar\partial,k}
&\longrightarrow&(\lambda_k,h_Q,\nabla^Q)\\
\downarrow&&\downarrow&&\downarrow\\
P_{B,k}&\longrightarrow&\operatorname{DPP}(K_{B,k})
&\longrightarrow&p_k.
\end{array}}
\tag{6.2}
\]

The top row carries phase, index and anomaly data. The bottom row is its Born/statistical image. Forgetting the top row is irreversible.

---

## 7. What the result changes

The previous gate

\[
\text{construct }p\mapsto D_p
\]

was too strong on the bare probability category. It should be replaced by two distinct tasks:

1. **No-go/classification:** classify selectors under a declared statistical morphism category. The full isomorphism groupoid gives only the constant sector.
2. **Realization:** identify minimal extra structure that reduces symmetry and canonically produces \(D\). Polarized complex geometry gives one exact realization.

The remaining substantive bridge is not an arbitrary \(p\mapsto D_p\), but a reconstruction theorem of the form

\[
\boxed{
\text{statistical axioms + locality + complex polarization}
\Longrightarrow
D_{\bar\partial}\text{ or an equivalent elliptic family}.
}
\tag{7.1}
\]

Fisher compatibility then remains a separate condition. In the current hyperbolic model, the established target is the Hermitianized identity and its Weil--Petersson limit from `bls-position-transport.md`, not the generally false scalar identity \(\partial\bar\partial\log Z_Q=g^F\).

---

## 8. Gate ledger

- **PBS-A — PASS:** precise category of probability-only finite-rank projection selectors.
- **PBS-B — PASS:** mixing lemma excludes nonzero finite-dimensional sectors in \(L^2_0\).
- **PBS-C — PASS:** natural selectors have only rank \(0\) or the rank-one constant projection.
- **PBS-D — PASS:** nontrivial projection DPP/Bergman sectors cannot be recovered from bare atomless probability.
- **PBS-E — PASS:** polarized complex geometry canonically selects the Dolbeault operator, Bergman projector and DPP.
- **PBS-F — PASS:** the polarized family feeds the determinant normalization selector and BLS transport already constructed.
- **PBS-G — OPEN:** axiomatize why FCIG statistical data should determine a complex polarization.
- **PBS-H — OPEN:** extend the classification from isomorphisms to chosen Markov/locality categories.

\[
\boxed{
\text{Probability supplies mass; polarization supplies modes; the index supplies topology.}
}
\]

**Update:** [dirichlet-hodge-operator-selector.md](dirichlet-hodge-operator-selector.md) closes the first enriched step. A reversible Dirichlet form \(\mathcal E\) canonically selects a real exact Hodge–Dirac operator. Its scalar determinant line is nevertheless canonically trivial, so complex polarization and twisting remain independent reconstruction data.

---

## References

- [Hal56] P. R. Halmos, *Lectures on Ergodic Theory*, Chelsea, 1956.
- [HKPV06] J. B. Hough, M. Krishnapur, Y. Peres and B. Virág, “Determinantal Processes and Independence,” *Probability Surveys* 3 (2006), 206–229; [arXiv:math/0503110](https://arxiv.org/abs/math/0503110).
- [Ber08] R. J. Berman, “Determinantal Point Processes and Fermions on Complex Manifolds: Bulk Universality,” [arXiv:0811.3341](https://arxiv.org/abs/0811.3341).

Machine-readable entries are in `probability-only-bergman-selector-no-go.bib`.
