# FCIG Explicit Model X: Global Deligne--Riemann--Roch Closure of the Flat Ambiguity

**Status:** v0.10 connection-level closure  
**Date:** 2026-09-09

> **Citation policy.** Bracketed keys cite established mathematics only. Statements marked **Derived here** are consequences obtained by specializing and combining those results in the conventions fixed below. No gravitational interpretation is attributed to the cited literature.

Model IX proved, using differential-character fiber integration, GRR and the Quillen local family index theorem, that

\[
\widehat\delta_{\mathrm{DR}}
:=
\widehat\kappa_1-12\widehat\lambda_Q
\]

has zero characteristic class and zero curvature. At that stage it was therefore only known to be a topologically trivial flat differential character.

This note closes that ambiguity after fixing the standard **metrized Deligne-pairing realization** of the differential pushforward.

The result is

\[
\boxed{
\widehat\kappa_1
=
12\widehat\lambda_Q
}
\]

globally for the smooth curve family in the conventions below.

The key established inputs are:

1. Deligne's canonical Riemann--Roch isomorphism for a family of curves [Del87; FMW20];
2. its compatibility with the Quillen metric and the metrized Deligne pairing, up to an overall topological constant, hence preservation of the associated Chern connections [Del87; FMW20];
3. the Hermitian Deligne-pairing/cup-product realization and the uniqueness/equivalence of ordinary differential-cohomology products and fiber integration [Ald05; BB14].

---

## 1. Setup

Let

\[
\pi:X\to B
\]

be a smooth proper holomorphic family of connected compact curves, and let

\[
\omega=K_{X/B}
\]

carry a smooth Hermitian metric with Chern connection \(\nabla^\omega\).

Set

\[
\lambda
:=
\det R\pi_*\omega,
\]

with Quillen metric and Quillen Chern connection \(\nabla^Q\). Its differential first Chern class is

\[
\widehat\lambda_Q
:=
\widehat c_1(\lambda,\nabla^Q)
\in
\widehat H^2(B;\mathbf Z).
\]

On the total space, write

\[
\widehat x
:=
\widehat c_1(\omega,\nabla^\omega).
\]

---

## 2. Metrized Deligne pairing as the geometric pushforward model

For two Hermitian holomorphic line bundles \(L,M\) on a family of curves, the Deligne pairing

\[
\langle L,M\rangle_\pi
\]

is a holomorphic line bundle on the base with its canonical Deligne metric. Its Chern connection will be denoted \(\nabla^{\mathrm{Del}}\).

The standard Chern-form identity is

\[
\boxed{
R\!\left(
\widehat c_1(\langle L,M\rangle_\pi,\nabla^{\mathrm{Del}})
\right)
=
\pi_*\left(
R(\widehat c_1(L))\wedge R(\widehat c_1(M))
\right).
}
\tag{2.1}
\]

The Deligne pairing is also the geometric realization of the Hermitian-holomorphic Deligne cup-product/intersection construction [Ald05]. Bär--Becker show that ordinary differential cohomology, its product, and fiber integration are unique up to the canonical natural equivalence once the standard axioms and normalization are fixed [BB14].

Accordingly, from this point onward we fix the canonical identification

\[
\boxed{
\pi_!\left(
\widehat c_1(L)\cup\widehat c_1(M)
\right)
=
\widehat c_1(\langle L,M\rangle_\pi,\nabla^{\mathrm{Del}})
}
\tag{2.2}
\]

as the geometric model of the degree-two differential pushforward used by FCIG.

This is a convention-fixing/model-identification step, not a new physical postulate.

For \(L=M=\omega\), define

\[
\boxed{
\widehat\kappa_1^{\mathrm{Del}}
:=
\widehat c_1(\langle\omega,\omega\rangle_\pi,
\nabla^{\mathrm{Del}})
=
\pi_!(\widehat x^2).
}
\tag{2.3}
\]

Thus Model IX's abstract \(\widehat\kappa_1\) is now represented by a specific global Hermitian line with connection.

---

## 3. Deligne's curve-family Riemann--Roch isomorphism

For any holomorphic line bundle \(L\) on \(X\), Deligne constructs a canonical functorial isomorphism, up to the standard sign convention [Del87; FMW20],

\[
\boxed{
\det R\pi_*L^{\otimes12}
\simeq
\langle\omega,\omega\rangle_π
\otimes
\langle L,L\otimes\omega^{-1}\rangle_π^{\otimes6}.
}
\tag{3.1}
\]

For

\[
L=\omega,
\]

the second factor becomes

\[
\langle\omega,\mathcal O_X\rangle_\pi^{\otimes6},
\]

which is canonically trivial by the standard normalization of the Deligne pairing. Hence

\[
\boxed{
\lambda^{\otimes12}
\simeq
\langle\omega,\omega\rangle_\pi.
}
\tag{3.2}
\]

This is the line-bundle-level refinement of the smooth-locus cohomological relation

\[
12c_1(\lambda)=\pi_*c_1(\omega)^2.
\]

---

## 4. Metric compatibility removes the flat ambiguity

Equip the determinant line in (3.2) with the Quillen metric and the Deligne pairing with its canonical Deligne metric.

For these choices, the Deligne isomorphism is an isometry up to an overall topological constant [Del87; FMW20]. In particular, the induced Chern connections agree. An overall positive constant rescales the norm but does not change

\[
\partial\log h
\]

and therefore does not change the Chern connection.

Thus (3.2) is connection-preserving:

\[
\boxed{
(\lambda^{\otimes12},(\nabla^Q)^{\otimes12})
\simeq
(\langle\omega,\omega\rangle_\pi,
\nabla^{\mathrm{Del}}).
}
\tag{4.1}
\]

Passing to degree-two differential cohomology gives

\[
\boxed{
12\widehat\lambda_Q
=
\widehat c_1(\langle\omega,\omega\rangle_\pi,
\nabla^{\mathrm{Del}}).
}
\tag{4.2}
\]

Using (2.3),

\[
\boxed{
\widehat\kappa_1^{\mathrm{Del}}
=
12\widehat\lambda_Q.
}
\tag{4.3}
\]

### Theorem 4.1 — global connection-level closure

**Derived here by specializing the established metrized Deligne--Riemann--Roch theorem and fixing the standard differential-cohomology/Deligne-pairing realization.**

For a smooth family of compact complex curves with the conventions above,

\[
\boxed{
\pi_!\left(
\widehat c_1(\omega)^2
\right)
=
12\widehat c_1(\det R\pi_*\omega,\nabla^Q).
}
\tag{4.4}
\]

Consequently, the residual flat class isolated in Model IX vanishes:

\[
\boxed{
\widehat\delta_{\mathrm{DR}}=0.
}
\tag{4.5}
\]

This is global; no simply-connectedness hypothesis is needed once the connection-preserving Deligne isomorphism is included.

---

## 5. Holonomy identity

Since (4.1) is an isomorphism of lines with connection, for every loop \(\gamma\subset B\),

\[
\boxed{
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
=
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}.
}
\tag{5.1}
\]

Hence the residual character defined in Model IX,

\[
\chi_{\mathrm{DR}}(\gamma)
=
\frac{
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
}{
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}
},
\]

obeys

\[
\boxed{
\chi_{\mathrm{DR}}(\gamma)=1
\quad
\text{for every loop }\gamma.
}
\tag{5.2}
\]

Thus the flat ambiguity in Model IX was not an additional anomaly sector. It was exactly the ambiguity left when one compared only characteristic class and curvature without yet invoking the global metrized Deligne--RR isomorphism.

---

## 6. Relation to the Quillen / eta-holonomy picture

The Quillen determinant connection belongs to the Bismut--Freed/Dai--Freed determinant-line framework. For Dirac-type families, its loop holonomy has the established adiabatic eta-invariant description [BF86b; DF94].

Equation (5.1) therefore transports that global determinant holonomy to the Deligne self-pairing side. This does not assert a new eta formula; it is a consequence of the connection-preserving isomorphism.

The correct synthesis is now

\[
\boxed{
\text{MMM/Deligne self-intersection differential character}
=
12\times
\text{Quillen determinant differential character}.
}
\tag{6.1}
\]

---

## 7. What is and is not new

### Established

- Deligne's functorial curve-family determinant isomorphism [Del87; FMW20].
- Its metric compatibility with Quillen and Deligne metrics, up to a base-independent/topological constant, hence preservation of Chern connections [Del87; FMW20].
- Hermitian Deligne cup-product / Deligne-pairing compatibility and standard differential-cohomology product/fiber-integration equivalence [Ald05; BB14].

### Derived here

- Specializing those ingredients to \(L=\omega\) in the FCIG convention gives the exact global identity (4.4).
- The Model-IX residual flat character is therefore zero once the canonical Deligne-pairing realization is fixed.

### Not claimed

- No new theorem about Deligne pairings, Quillen metrics, or analytic torsion is claimed.
- No identification with tangent/frame curvature is claimed.
- No gravitational field equation is derived.

---

## 8. Consequence for the FCIG architecture

The determinant/intersection sector is now unusually rigid:

\[
\boxed{
\begin{aligned}
\kappa_1
&=12c_1(\lambda),\\
R(\widehat\kappa_1)
&=12R(\widehat\lambda_Q),\\
\operatorname{Hol}_{\widehat\kappa_1}
&=\operatorname{Hol}_{\widehat\lambda_Q}^{12},\\
\widehat\kappa_1
&=12\widehat\lambda_Q.
\end{aligned}
}
\tag{8.1}
\]

So topology, local curvature, and global holonomy are not three independent pieces in this canonical non-factorized curve-family construction. They are three evaluations of a single connection-level Deligne--Riemann--Roch identity.

This sharply narrows the search space for any genuinely new FCIG response mechanism.

---

## 9. Remaining no-go boundary

Equation (8.1) remains an identity in

\[
\widehat H^2(B;\mathbf Z),
\]

i.e. among \(U(1)\) line-with-connection data on a parameter/moduli base.

It does not produce

\[
\Omega^2(M;\mathfrak{so}(1,d-1))
\]

or any Lorentzian causal structure.

Therefore the principal type mismatch remains exactly where Models VI--IX placed it:

\[
\boxed{
\text{complete abelian determinant response}
\not\Rightarrow
\text{spacetime gravity}.
}
\tag{9.1}
\]

The next controlled milestone must introduce a genuinely specified target geometric structure rather than another identity inside the determinant-line sector.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Del87]** P. Deligne, *Le déterminant de la cohomologie*, Contemp. Math. 67 (1987).
- **[FMW20]** G. Freixas i Montplet and R. A. Wentworth, *Deligne Pairings and Families of Rank One Local Systems on Algebraic Curves*, J. Differential Geom. 115 (2020), 475--528.
- **[Ald05]** E. Aldrovandi, *Hermitian-holomorphic Deligne cohomology, Deligne pairing for singular metrics, and hyperbolic metrics*, IMRN (2005), 1015--1046.
- **[BB14]** C. Bär and C. Becker, *Differential Characters and Geometric Chains*, LNM 2112 (2014).
- **[BF86b]** J.-M. Bismut and D. Freed, *The Analysis of Elliptic Families II*, CMP 107 (1986).
- **[DF94]** X. Dai and D. Freed, *Eta-Invariants and Determinant Lines*, JMP 35 (1994).
