# FCIG Explicit Model XII: Mixed Characteristic Classes, Index Density, and the Degree-Six Anomaly Bridge

**Status:** citation-audited research note  
**Milestone:** v0.12 — mixed characteristic-class / anomaly-polynomial degree audit  
**Updated:** 2026-09-09

## Citation policy

- **Established** — standard Chern--Weil, index, and anomaly-descent results with references.
- **Derived here** — algebraic degree consequences or expansions carried out explicitly in this note.
- **FCIG consequence** — interpretation for the repository architecture.
- **No-go** — a tempting identification ruled out by degree, structure group, or tensor type.

Exact physical anomaly coefficients depend on chirality, charge/representation, and curvature normalization. This note therefore fixes the **topological characteristic-class normalization first** and separates it from convention-dependent physics notation.

---

## 1. Executive result

Model XI ruled out the inverse reconstruction

\[
\text{one determinant }U(1)\text{ connection}
\not\Rightarrow
\text{full nonabelian frame connection}.
\]

The correct next move is to keep both fields independent.

Let \(M\) carry

1. a Hermitian line with unitary connection \((L,\nabla^L)\), and
2. an independently specified tangent/frame connection \(\nabla^{\mathrm{fr}}\).

Then the standard characteristic classes can interact **without identifying their structure groups**.

The first canonical mixed product is

\[
\boxed{
c_1(L)\,p_1(TM)\in H^6(M;\mathbf Z),
}
\]

and in differential cohomology

\[
\boxed{
\widehat c_1(L,\nabla^L)
\cup
\widehat p_1(TM,\nabla^{\mathrm{fr}})
\in
\widehat H^6(M;\mathbf Z).
}
\]

This is a genuine positive bridge: it mixes the two curvature sectors in a gauge-invariant characteristic class while keeping their connections independent.

For a complex line twist, the degree-six Atiyah--Singer index density is

\[
\boxed{
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac{1}{6}c_1(L)^3
-
\frac{1}{24}c_1(L)p_1(TM).
}
\]

This is the standard topological skeleton behind four-dimensional chiral gauge and mixed gauge--gravitational anomaly polynomials. [LM89; AGG85; ZWZ84]

The same formula gives an immediate dimensional no-go:

\[
\boxed{
\text{degree-six anomaly polynomial}
\neq
\text{a direct local four-form action density in 4D}.
}
\]

Its four-dimensional role requires descent/transgression, anomaly inflow, or another explicitly specified construction. [ZWZ84; BZ84; AGG85; Freed14]

---

## 2. Independent-field setup

Let

\[
(L,\nabla^L)\to M
\]

be a unitary line bundle. Define

\[
\widehat a
:=
\widehat c_1(L,\nabla^L)
\in
\widehat H^2(M;\mathbf Z).
\]

Let \(TM\) have a metric/frame connection \(\nabla^{\mathrm{fr}}\). Its first differential Pontryagin class is

\[
\widehat p_1(TM,\nabla^{\mathrm{fr}})
\in
\widehat H^4(M;\mathbf Z).
\]

No map of structure groups

\[
U(1)\to SO(r)
\]

is assumed. The two connections are independent inputs.

The product in differential cohomology is therefore well typed:

\[
\boxed{
\widehat I_6^{\mathrm{mix}}
:=
\widehat a\cup\widehat p_1(TM)
\in
\widehat H^6(M;\mathbf Z).
}
\]

Naturality of differential-cohomology curvature gives

\[
\boxed{
R(\widehat I_6^{\mathrm{mix}})
=
R(\widehat a)\wedge R(\widehat p_1).
}
\]

In normalized Chern--Weil notation this is the six-form represented schematically by

\[
\boxed{
\frac{F_L}{2\pi i}
\wedge
p_1(\Omega_{\mathrm{fr}}).
}
\]

The precise matrix-trace normalization inside the Pontryagin form is fixed by the chosen convention for \(p_1\).

---

## 3. Why this is different from the failed inverse bridge

Model XI asked whether the line connection determines the frame connection. The answer was no.

Model XII asks a different question:

> Given both connections independently, can a standard invariant depend on both?

The answer is yes.

The mixed cup product does not require

\[
F_L=\operatorname{Tr}R,
\]

nor any other identification. It only uses functorial multiplication of characteristic classes.

Thus the mathematically correct pattern is

\[
\boxed{
\begin{array}{c}
U(1)\text{ line connection}\\
\oplus\\
\text{independent frame connection}
\end{array}
\quad\longrightarrow\quad
\text{mixed characteristic class}.
}
\]

This is a coupling in the sense of invariant data, not an inverse reconstruction.

---

## 4. The index-theoretic origin of the degree-six polynomial

For a spin Dirac operator twisted by a complex vector bundle \(E\), the Atiyah--Singer index density is governed by [LM89]

\[
\widehat A(TM)\operatorname{ch}(E).
\]

For a line bundle \(L\), write

\[
c:=c_1(L).
\]

The standard formal expansions are

\[
\boxed{
\widehat A(TM)
=
1-\frac{1}{24}p_1(TM)+O(8),
}
\]

and

\[
\boxed{
\operatorname{ch}(L)
=e^c
=
1+c+\frac{c^2}{2}+\frac{c^3}{6}+O(8).
}
\]

Here \(O(8)\) denotes terms of cohomological degree at least eight.

Multiplying and selecting degree six gives, **Derived here**,

\[
\boxed{
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac{c^3}{6}
-
\frac{c\,p_1(TM)}{24}.
}
\]

For a charge-\(q\) line \(L^{\otimes q}\),

\[
c_1(L^{\otimes q})=q c,
\]

so the same topological expansion gives

\[
\boxed{
\left[\widehat A(TM)\operatorname{ch}(L^{\otimes q})\right]_{(6)}
=
\frac{q^3}{6}c^3
-
\frac{q}{24}c\,p_1(TM).
}
\]

The overall physical sign for a chiral fermion and the translation between normalized characteristic classes and physicists' \(F,R\) conventions depend on chirality and normalization; those are not silently absorbed into this formula.

---

## 5. Established anomaly interpretation

The classic anomaly literature organizes local gauge and gravitational anomalies by characteristic polynomials in gauge and Riemann curvature and derives lower-dimensional anomalies by descent. [ZWZ84; BZ84; AGG85]

For a four-dimensional chiral theory, the relevant local anomaly polynomial is a **six-form**. In an abelian example it can contain

\[
F^3
\]

and a mixed gauge--gravitational structure of the form

\[
F\wedge\operatorname{tr}(R\wedge R),
\]

with representation-, chirality-, and normalization-dependent coefficients. [AGG85; AGW84]

The topological formula

\[
\frac{c^3}{6}-\frac{c\,p_1}{24}
\]

is the normalized index-theoretic version of this structure for a line twist.

### FCIG consequence

This supplies the first established mechanism in the program where

\[
\boxed{
\text{FCIG }U(1)\text{ data}
\quad\text{and}\quad
\text{independent frame curvature}
}
\]

appear in the same standard invariant **without pretending to be the same connection**.

---

## 6. Degree audit in four dimensions

Suppose \(M\) is a four-dimensional spacetime or Euclidean four-manifold.

A differential six-form vanishes when pulled back as an ordinary form to \(M\), simply because

\[
\Omega^6(M)=0.
\]

More conceptually, the anomaly polynomial is not a local four-form Lagrangian density. The standard descent picture starts from a closed invariant six-form \(I_6\), locally writes a transgression form

\[
I_6=dI_5^{(0)},
\]

and under an infinitesimal gauge transformation obtains

\[
\delta I_5^{(0)}=dI_4^{(1)}.
\]

The four-form \(I_4^{(1)}\) controls the local anomaly. [ZWZ84; BZ84; AGG85]

Therefore:

### No-go 6.1 — no direct 4D topological action from \(I_6\)

\[
\boxed{
I_6
\text{ cannot simply be integrated over a four-manifold as a local action.}
}
\]

A legitimate four-dimensional use requires one of the following to be specified:

1. anomaly descent;
2. a five-dimensional inflow/Chern--Simons construction;
3. a boundary or extension manifold;
4. another field whose degree changes the expression;
5. or a metric-dependent contraction/Hodge-star operation, which is no longer the same topological characteristic polynomial.

This is a degree statement, not a statement that mixed gauge--gravitational effects are absent.

Modern anomaly field theory makes the higher-dimensional/inflow interpretation structural rather than merely computational. [Freed14]

---

## 7. Why there is no generic gravitational \(c_1\) in degree two

A degree-two Chern--Weil form would arise from an invariant linear functional

\[
\ell:\mathfrak g\to\mathbf R.
\]

If \(\mathfrak g\) is semisimple, then

\[
[\mathfrak g,\mathfrak g]=\mathfrak g.
\]

An invariant linear functional annihilates commutators, so it must vanish on all of \(\mathfrak g\).

Hence, for semisimple frame Lie algebras such as

\[
\mathfrak{so}(n),\qquad n\ge3
\]

(with the familiar low-dimensional decompositions understood), there is no nonzero invariant linear Chern--Weil polynomial analogous to the trace on \(\mathfrak u(n)\).

Equivalently, in the defining orthogonal representation,

\[
\operatorname{Tr}\Omega_{\mathrm{fr}}=0.
\]

The first standard real Pontryagin class instead arises quadratically:

\[
\boxed{
p_1(TM)\in H^4(M;\mathbf Z).
}
\]

### Important exception

\[
SO(2)\cong U(1)
\]

is abelian. An oriented real two-plane bundle has the Euler class

\[
e\in H^2(-;\mathbf Z),
\]

which corresponds to the first Chern class after identifying an oriented plane with a complex line.

Thus the no-go is specifically the **generic higher-rank semisimple frame case**, not rank two.

### FCIG consequence

There is no natural degree-two orthogonal Chern--Weil class that could be equated to the FCIG determinant \(c_1\) in generic four-dimensional frame geometry.

This strengthens Model XI's structure-group obstruction with an independent **cohomological-degree obstruction**.

---

## 8. Spin\(^c\) does not remove the degree audit

A \(Spin^c\) structure naturally carries a determinant line. Its first Chern class is degree two and is related mod two to the obstruction class of the underlying oriented bundle. [LM89]

This is a genuine topological bridge, but it does not turn the Pontryagin class into degree two and does not reconstruct the frame connection.

The mixed expression

\[
c_1(L_{\det})p_1(TM)
\]

still has degree six.

Thus \(Spin^c\) makes line and frame topology compatible in one enlarged structure, while the mixed anomaly polynomial remains a higher-degree object.

---

## 9. Differential-cohomology refinement

The differential product

\[
\widehat c_1(L)\cup\widehat p_1(TM)
\]

contains more than its de Rham curvature form. It also remembers integral characteristic data and secondary/global information.

However, one must not confuse this with saying that a six-class on a four-dimensional manifold supplies a new local six-form observable there. Its curvature component is dimensionally zero on a four-manifold.

The differential class can instead participate naturally after pullback to a higher-dimensional extension or in a transgressed/inflow construction. This is the differential-cohomological version of the same degree audit.

---

## 10. A clean separation of three notions of coupling

The word “coupling” was previously too ambiguous. Model XII separates:

### A. Structure-group identification — rejected

\[
U(1)\stackrel{?}{=}SO(1,3)
\]

or any equivalent direct curvature identification is not legitimate.

### B. Mixed invariant — valid

\[
\boxed{
c_1(L)p_1(TM)}
\]

is a standard product of independent characteristic classes.

### C. Dynamical interaction — not yet supplied

A field equation or action principle coupling the fields requires additional dynamical data. The existence of a characteristic polynomial does not determine its coefficient in an action, nor does it produce Einstein's equation.

This three-way distinction is central for the next stages of FCIG.

---

## 11. Explicit symbolic checker

The companion file

`mixed-characteristic.py`

checks only the degree algebra and the \(\widehat A\operatorname{ch}\) expansion:

\[
\deg c_1=2,
\qquad
\deg p_1=4,
\qquad
\deg(c_1p_1)=6,
\]

and

\[
[\widehat A\operatorname{ch}(L^q)]_6
=
\frac{q^3}{6}c^3
-
\frac{q}{24}cp_1.
\]

It is a convention checker, not a proof of the anomaly theorem.

---

## 12. Gate results

### Gate AI — independent-field setup: PASS

The line and frame connections are separate fields on a common base. No structure-group identification is used.

### Gate AJ — mixed degree-six class: PASS

Established differential-cohomology multiplication gives

\[
\boxed{
\widehat c_1(L)\cup\widehat p_1(TM)
\in\widehat H^6(M;\mathbf Z).
}
\]

### Gate AK — index/anomaly polynomial: PASS

The index expansion gives

\[
\boxed{
[\widehat A(TM)\operatorname{ch}(L)]_6
=
\frac16c_1^3-rac1{24}c_1p_1.
}
\]

Classic anomaly descent identifies the same gauge/gravitational characteristic structures as the source of local chiral anomalies, subject to physical convention factors. [AGG85; ZWZ84; BZ84]

### Gate AL — four-dimensional degree audit: PASS WITH NO-GO

The degree-six polynomial is not itself a four-dimensional local action density. Descent/inflow or additional structure is required.

### Gate AM — degree-two gravitational audit: PASS WITH QUALIFIED NO-GO

For generic semisimple higher-rank orthogonal frame groups there is no nonzero invariant linear Chern--Weil polynomial, so there is no generic gravitational first-Chern analogue in degree two. The \(SO(2)\) / oriented-plane exception is recorded explicitly.

---

## 13. v0.12 conclusion

Model XI closed the inverse reconstruction problem. Model XII supplies the first positive mixed bridge that survives the audit:

\[
\boxed{
\text{independent }U(1)\text{ connection}
+
\text{independent frame connection}
\longrightarrow
\text{mixed characteristic/anomaly class}.
}
\]

The canonical topological degree-six combination for a line-twisted Dirac index is

\[
\boxed{
\frac16c_1^3-rac1{24}c_1p_1.
}
\]

This is meaningful anomaly/index data, but

\[
\boxed{
\text{anomaly polynomial}
\neq
\text{gravitational field equation}.
}
\]

No Einstein dynamics has been derived.

---

## 14. Next controlled milestone

The next mathematically meaningful step is no longer to search for another mixed polynomial. It is to make the degree-six result act on four-dimensional data through a **specific descent/inflow geometry**.

A natural v0.13 target is:

1. choose a five-dimensional manifold \(Y\) with boundary \(M=\partial Y\), or a differential-cohomology transgression construction;
2. represent the degree-six class by a five-dimensional secondary/Chern--Simons datum;
3. compute its boundary variation/holonomy;
4. distinguish anomaly inflow from ordinary dynamical stress-energy response;
5. audit whether any horizon/causal information enters. It should not be assumed.

Only after such a descent model is explicit would it be sensible to compare anomaly response with thermodynamic/gravitational response.

---

## References used in this note

- **[LM89]** H. Blaine Lawson, Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989.
- **[AGW84]** Luis Alvarez-Gaumé and Edward Witten, “Gravitational Anomalies,” *Nuclear Physics B* 234 (1984), 269–330.
- **[ZWZ84]** Bruno Zumino, Yong-Shi Wu, and A. Zee, “Chiral Anomalies, Higher Dimensions, and Differential Geometry,” *Nuclear Physics B* 239 (1984), 477–507.
- **[BZ84]** William A. Bardeen and Bruno Zumino, “Consistent and Covariant Anomalies in Gauge and Gravitational Theories,” *Nuclear Physics B* 244 (1984), 421–453.
- **[AGG85]** Luis Alvarez-Gaumé and Paul Ginsparg, “The Structure of Gauge and Gravitational Anomalies,” *Annals of Physics* 161 (1985), 423–490; erratum 171 (1986), 233.
- **[Freed14]** Daniel S. Freed, “Anomalies and Invertible Field Theories,” *Proceedings of Symposia in Pure Mathematics* 88 (2014), arXiv:1404.7224.

The exact topological expansion in Section 4 is standard index theory. The FCIG degree/no-go consequences are derived here from those established ingredients.