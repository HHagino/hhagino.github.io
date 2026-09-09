# FCIG Explicit Model IX: The Non-Factorized \(\widehat\kappa_1\) Class and the Quillen Flat Ambiguity

**Status:** v0.9 worked comparison  
**Date:** 2026-09-09

> **Citation policy.** Bracketed keys cite established mathematics only. Statements marked **Derived here** are consequences obtained by combining those standard results in the conventions fixed below. No gravitational interpretation is attributed to the cited literature.

Model VIII proved that every factorized degree-restored response

\[
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
\]

collapses to an integer multiple of the original degree-two differential character. The next canonical possibility is therefore a total-space class which is **not** factorized through the original base anomaly.

For a smooth family of compact complex curves, the first such class is

\[
\boxed{
\widehat\kappa_1
:=
\pi_!\left(
\widehat c_1(\omega)^2
\right),
}
\]

where

\[
\pi:X\to B,
\qquad
\omega=K_{X/B}.
\]

The result of this note is sharp:

1. \(\widehat\kappa_1\) is a genuine non-factorized degree-two class;
2. its characteristic class is \(12\) times the Hodge class;
3. its curvature is \(12\) times the Quillen determinant curvature;
4. therefore its difference from \(12\) times the Quillen differential character is a **topologically trivial flat character**;
5. this difference vanishes on any base with \(H^1(B;\mathbf R)=0\), in particular on a simply connected base.

Thus the first non-factorized canonical direction does escape the scalar-multiplication theorem of Model VIII, but it does **not** open an arbitrary new local curvature direction. The only remaining discrepancy is global flat holonomy.

---

## 1. Setup and conventions

Let

\[
\pi:X\to B
\tag{1.1}
\]

be a smooth proper family of connected compact complex curves of fixed genus \(g\ge2\). Let

\[
\omega=K_{X/B}
\tag{1.2}
\]

be the relative canonical line, equipped with a Hermitian metric and compatible Chern connection \(\nabla^\omega\).

Write

\[
\widehat x
:=
\widehat c_1(\omega,\nabla^\omega)
\in
\widehat H^2(X;\mathbf Z).
\tag{1.3}
\]

Its characteristic class and normalized curvature are

\[
I(\widehat x)=x:=c_1(\omega),
\qquad
R(\widehat x)=\Omega_\omega:=\frac{F_{\nabla^\omega}}{2\pi i}.
\tag{1.4}
\]

Differential-character products and fiber integration are taken in the Bär--Becker/Cheeger--Simons convention [BB14]. They are compatible with both the integral characteristic class and curvature maps.

Define the non-factorized degree-two class

\[
\boxed{
\widehat\kappa_1
:=
\pi_!(\widehat x\cup\widehat x)
\in
\widehat H^2(B;\mathbf Z).
}
\tag{1.5}
\]

This construction is standard differential cohomology; the use of it as the next FCIG response test is the project-specific step.

---

## 2. Characteristic class: the ordinary \(\kappa_1\) direction

Compatibility of fiber integration with \(I\) gives

\[
I(\widehat\kappa_1)
=
\pi_*\bigl(c_1(\omega)^2\bigr).
\tag{2.1}
\]

Define

\[
\boxed{
\kappa_1
:=
\pi_*\bigl(x^2\bigr)
\in
H^2(B;\mathbf Z).
}
\tag{2.2}
\]

Hence

\[
\boxed{
I(\widehat\kappa_1)=\kappa_1.
}
\tag{2.3}
\]

This is the first Mumford--Morita--Miller direction for a smooth curve family, in the convention (2.2).

---

## 3. GRR computation: \(\kappa_1=12\lambda\) on the smooth locus

Let

\[
\lambda
:=
\det R\pi_*\omega.
\tag{3.1}
\]

For connected curve fibers, relative Serre duality identifies the degree-one contribution so that this determinant is the usual Hodge determinant line up to the canonically trivial factor. The standard moduli-theoretic background is reviewed in [HM98].

Apply Grothendieck--Riemann--Roch [Stacks-GRR] to \(\omega\). Since

\[
T_\pi\cong\omega^{-1},
\tag{3.2}
\]

write

\[
x=c_1(\omega).
\]

Then

\[
\operatorname{ch}(\omega)=e^x
=1+x+\frac{x^2}{2}+O(x^3),
\tag{3.3}
\]

and

\[
\operatorname{Td}(T_\pi)
=
1-\frac{x}{2}+\frac{x^2}{12}+O(x^3).
\tag{3.4}
\]

Therefore

\[
\boxed{
\operatorname{ch}(\omega)\operatorname{Td}(T_\pi)
=
1+\frac{x}{2}+\frac{x^2}{12}+O(x^3).
}
\tag{3.5}
\]

The degree-two class on the base comes from the degree-four term on the total space, so GRR yields

\[
\operatorname{ch}_1(R\pi_*\omega)
=
\frac1{12}\pi_*(x^2).
\tag{3.6}
\]

Since \(\operatorname{ch}_1=c_1\) for a virtual complex bundle,

\[
\boxed{
c_1(\lambda)
=
\frac1{12}\kappa_1.
}
\tag{3.7}
\]

Equivalently,

\[
\boxed{
\kappa_1=12\,c_1(\lambda).
}
\tag{3.8}
\]

**Derived here from established GRR.** This calculation fixes the smooth-locus convention used throughout this note. Boundary corrections on a compactified moduli space are a separate statement and are not silently imported here.

The algebraic Deligne--Riemann--Roch framework gives a stronger line-bundle-level relation; see [Eri08]. We use it only as background and do not yet infer equality of unitary connections from the algebraic isomorphism alone.

---

## 4. Curvature of \(\widehat\kappa_1\)

Compatibility of differential-character fiber integration with the curvature map gives [BB14]

\[
\boxed{
R(\widehat\kappa_1)
=
\pi_*\left(\Omega_\omega\wedge\Omega_\omega\right).
}
\tag{4.1}
\]

This is a genuine two-form on the parameter base. Unlike the factorized response of Model VIII, it is not obtained by multiplying a pre-existing base curvature by a fiberwise integer.

---

## 5. Quillen determinant differential character

Equip the determinant line \(\lambda\) with its Quillen metric and natural determinant connection. Write

\[
\widehat\lambda_Q
:=
\widehat c_1(\lambda,\nabla^Q)
\in
\widehat H^2(B;\mathbf Z).
\tag{5.1}
\]

Then

\[
I(\widehat\lambda_Q)=c_1(\lambda).
\tag{5.2}
\]

The Bismut--Gillet--Soulé local family index theorem gives the normalized curvature of the Quillen determinant connection as the degree-two component of the fiber integral of the Chern character times the Todd form [BGS88III]:

\[
R(\widehat\lambda_Q)
=
\left[
\pi_*\left(
\operatorname{ch}(\omega,\nabla^\omega)
\operatorname{Td}(T_\pi,\nabla^{T_\pi})
\right)
\right]_{(2)}.
\tag{5.3}
\]

Using the same normalized first Chern form \(\Omega_\omega\) as in (4.1), the identical formal expansion (3.5) gives

\[
\boxed{
R(\widehat\lambda_Q)
=
\frac1{12}
\pi_*\left(
\Omega_\omega\wedge\Omega_\omega
\right).
}
\tag{5.4}
\]

Therefore

\[
\boxed{
R(\widehat\kappa_1)
=
12\,R(\widehat\lambda_Q).
}
\tag{5.5}
\]

This comparison is convention-safe because both sides use the normalized Chern form \(F/(2\pi i)\) and the same relative canonical connection.

---

## 6. The flat-ambiguity theorem

Define

\[
\boxed{
\widehat\delta_{\mathrm{DR}}
:=
\widehat\kappa_1
-
12\widehat\lambda_Q
\in
\widehat H^2(B;\mathbf Z).
}
\tag{6.1}
\]

Using (2.3) and (3.8),

\[
I(\widehat\delta_{\mathrm{DR}})
=
\kappa_1-12c_1(\lambda)
=
0.
\tag{6.2}
\]

Using (4.1) and (5.5),

\[
R(\widehat\delta_{\mathrm{DR}})=0.
\tag{6.3}
\]

Hence

\[
\boxed{
I(\widehat\delta_{\mathrm{DR}})=0,
\qquad
R(\widehat\delta_{\mathrm{DR}})=0.
}
\tag{6.4}
\]

### Theorem 6.1 — Quillen/MMM flat ambiguity

**Derived here from established differential fiber integration, GRR and the Quillen local index theorem.**

The difference

\[
\widehat\kappa_1-12\widehat\lambda_Q
\]

is a topologically trivial flat differential character.

In the standard degree-two differential-cohomology exact sequences, such classes are represented by

\[
\boxed{
\widehat\delta_{\mathrm{DR}}
\in
H^1(B;\mathbf R)/H^1(B;\mathbf Z).
}
\tag{6.5}
\]

Thus all local Chern--Weil data and all integral topological data agree. The only possible discrepancy is global flat holonomy.

---

## 7. Simply connected / \(H^1=0\) corollary

If

\[
H^1(B;\mathbf R)=0,
\tag{7.1}
\]

then the group in (6.5) vanishes. Therefore

\[
\boxed{
\widehat\kappa_1
=
12\widehat\lambda_Q.
}
\tag{7.2}
\]

In particular, this holds on any simply connected base.

### Corollary 7.1

On a simply connected parameter chart, the canonical non-factorized MMM differential character and twelve times the Quillen/Hodge determinant differential character agree exactly.

The obstruction to global equality can therefore only appear after quotienting/gluing in a way that creates nontrivial loop holonomy.

This mirrors, but does not identify with, the flat global-holonomy sectors found in Models II, IIIc and VI.

---

## 8. Holonomy formulation of the remaining obstruction

For any loop \(\gamma\subset B\), define the residual holonomy

\[
\boxed{
\chi_{\mathrm{DR}}(\gamma)
:=
\frac{
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
}{
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}
}.
}
\tag{8.1}
\]

Because \(\widehat\delta_{\mathrm{DR}}\) is flat and topologically trivial, \(\chi_{\mathrm{DR}}\) is the complete remaining obstruction to global equality.

Thus

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q
\quad\Longleftrightarrow\quad
\chi_{\mathrm{DR}}(\gamma)=1
\text{ for every loop }\gamma.
}
\tag{8.2}
\]

Bismut--Freed/Dai--Freed type holonomy theorems provide the natural analytic language for the determinant side; a full comparison with the holonomy of the differential pushforward/Deligne pairing is the next separate audit. We do not assert its vanishing here.

---

## 9. What v0.9 settles

The non-factorized class does evade the Model-VIII scalar-multiplication theorem:

\[
\widehat\kappa_1
=
\pi_!(\widehat x^2)
\]

is built entirely from total-space geometry, not from the pullback of a pre-existing base anomaly.

But it does not create an arbitrary independent local curvature direction. Instead,

\[
\boxed{
\begin{array}{rcl}
I(\widehat\kappa_1)
&=&12I(\widehat\lambda_Q),\\[1mm]
R(\widehat\kappa_1)
&=&12R(\widehat\lambda_Q),\\[1mm]
\widehat\kappa_1-12\widehat\lambda_Q
&=&\text{topologically trivial flat class}.
\end{array}
}
\tag{9.1}
\]

So the first canonical non-factorized direction reduces the possible novelty to a **secondary global holonomy class**.

---

## 10. Deligne--Riemann--Roch boundary

The algebraic Deligne--Riemann--Roch theorem gives a canonical relation between powers of the determinant of cohomology and Deligne pairings [Eri08]. For \(L=\omega\), its schematic specialization is the familiar relation between

\[
\lambda^{\otimes12}
\]

and the self-pairing

\[
\langle\omega,\omega\rangle.
\]

The differential pushforward \(\widehat\kappa_1\) is the natural differential-character counterpart of the Chern class of this self-pairing.

However, an algebraic line-bundle isomorphism does not by itself settle the global unitary connection/holonomy comparison in the exact conventions used here. The remaining question is therefore deliberately isolated:

\[
\boxed{
\text{Does the metric/connection-refined Deligne--RR identification force }
\widehat\delta_{\mathrm{DR}}=0
\text{ globally?}
}
\tag{10.1}
\]

That is the next controlled milestone, not an assumption in the present one.

---

## 11. Gravity/type audit

Even exact equality

\[
\widehat\kappa_1=12\widehat\lambda_Q
\]

would still be an equality of degree-two \(U(1)\) differential characters on a parameter/moduli base. It would not identify this class with Lorentzian tangent/frame curvature.

The previously recorded mismatches therefore remain unchanged.

---

## 12. Reproducibility note

`kappa1-quillen.py` checks the formal GRR coefficient

\[
(1+x+x^2/2)(1-x/2+x^2/12)
=
1+x/2+x^2/12+O(x^3),
\]

and verifies the factor \(12\) in the characteristic/curvature comparison symbolically. It does not prove GRR or the Bismut--Gillet--Soulé theorem.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Stacks-GRR]** The Stacks Project, Grothendieck--Riemann--Roch, Tag 02UO.
- **[BB14]** C. Bär and C. Becker, *Differential Characters and Geometric Chains*, LNM 2112 (2014).
- **[BGS88III]** J.-M. Bismut, H. Gillet and C. Soulé, *Analytic Torsion and Holomorphic Determinant Bundles III*, CMP 115 (1988).
- **[Eri08]** D. Eriksson, *A Deligne--Riemann--Roch Isomorphism* (2008).
- **[HM98]** J. Harris and I. Morrison, *Moduli of Curves* (1998).

All statements about GRR, differential fiber integration and Quillen curvature are established background. The isolation of the residual class \(\widehat\delta_{\mathrm{DR}}\) as the only remaining FCIG discrepancy is the **Derived here** synthesis.
