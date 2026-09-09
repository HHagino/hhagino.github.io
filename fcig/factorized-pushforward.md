# FCIG Explicit Model VIII: Canonical Couplings and the Factorized-Pushforward No-Go

**Status:** v0.8 worked theorem / no-go  
**Date:** 2026-09-09

> **Citation policy.** Bracketed keys cite established mathematics only. Statements marked **Derived here** are deductions made from those standard operations in the conventions fixed below. Statements marked **FCIG interpretation** are not attributed to the cited literature.

This note asks whether the degree-restoring coupling proposed in Model VII can be supplied canonically by geometry already present in a family, and whether such a coupling can generate genuinely new degree-two response data.

The answer for the entire **factorized** ansatz is negative.

The mechanism is the standard projection / up-down formula for differential-character fiber integration [BB14]. The canonical-bundle example on a family of curves then reduces to the classical identity \(\deg K_X=2g-2\) [HM98].

---

## 1. Differential-cohomology convention

We work with degree-\(n\) differential characters

\[
\widehat H^n(-;\mathbf Z)
\]

in the convention used in Models VI--VII. Degree two classifies Hermitian \(U(1)\) line bundles with unitary connection, while degree zero is ordinary locally constant integral data:

\[
\widehat H^0(B;\mathbf Z)
\cong
H^0(B;\mathbf Z).
\tag{1.1}
\]

For a smooth proper fiber bundle

\[
p:Z\to M
\]

with closed oriented real \(d\)-dimensional fibers, differential-character fiber integration has degree shift [BB14]

\[
\boxed{
p_!:
\widehat H^n(Z;\mathbf Z)
\longrightarrow
\widehat H^{n-d}(M;\mathbf Z).
}
\tag{1.2}
\]

The product and fiber integration obey the standard projection / up-down formula. For

\[
\widehat x\in\widehat H^r(M;\mathbf Z),
\qquad
\widehat y\in\widehat H^s(Z;\mathbf Z),
\]

one has, with the standard graded sign convention,

\[
 p_!\bigl(p^*\widehat x\cup\widehat y\bigr)
 =(-1)^{rd}\widehat x\cup p_!(\widehat y).
\tag{1.3}
\]

For the FCIG anomaly degree \(r=2\), the sign is always \(+1\).

---

## 2. General factorized-pushforward theorem

Let

\[
\widehat{\mathcal A}
\in
\widehat H^2(M;\mathbf Z)
\tag{2.1}
\]

be any degree-two differential character, and let

\[
\widehat u
\in
\widehat H^d(Z;\mathbf Z)
\tag{2.2}
\]

be a degree-restoring coupling class.

Consider the factorized response

\[
\widehat{\mathcal R}_{\widehat u}
:=
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
\in
\widehat H^2(M;\mathbf Z).
\tag{2.3}
\]

By (1.3),

\[
\boxed{
\widehat{\mathcal R}_{\widehat u}
=
\widehat{\mathcal A}\cup p_!(\widehat u).
}
\tag{2.4}
\]

But

\[
p_!(\widehat u)
\in
\widehat H^0(M;\mathbf Z)
\cong
H^0(M;\mathbf Z).
\tag{2.5}
\]

Therefore, on each connected component \(M_a\subset M\), there is an integer \(n_a\) such that

\[
p_!(\widehat u)|_{M_a}=n_a.
\tag{2.6}
\]

Hence

\[
\boxed{
\widehat{\mathcal R}_{\widehat u}|_{M_a}
=
n_a\,\widehat{\mathcal A}|_{M_a}.
}
\tag{2.7}
\]

### Theorem 2.1 — factorized-pushforward no-go

**Derived here from the established projection formula.**

For a connected base \(M\), any degree-preserving response of the factorized form

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr),
\qquad
\widehat u\in\widehat H^d(Z;\mathbf Z),
}
\tag{2.8}
\]

is an integer multiple of the original differential character:

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
n\widehat{\mathcal A},
\qquad n\in\mathbf Z.
}
\tag{2.9}
\]

Thus a factorized degree-restoring class can rescale the original line-with-connection class, but it cannot create a new independent degree-two response direction on the base.

This is stronger than the degree obstruction of Model VII: even after the degree has been repaired, factorization itself remains an obstruction to novelty.

---

## 3. Curvature and holonomy consequences

Because differential cohomology is multiplicative and the degree-zero factor is the integer \(n\), equation (2.9) immediately implies

\[
\boxed{
R(\widehat{\mathcal R}_{\widehat u})
=
n\,R(\widehat{\mathcal A}).
}
\tag{3.1}
\]

For any loop \(\gamma\subset M\),

\[
\boxed{
\operatorname{Hol}_{\widehat{\mathcal R}_{\widehat u}}(\gamma)
=
\operatorname{Hol}_{\widehat{\mathcal A}}(\gamma)^n.
}
\tag{3.2}
\]

Thus the factorized response does not generate an independent curvature form or an independent holonomy character. It only applies the integer multiplication endomorphism

\[
[n]:\widehat H^2(M;\mathbf Z)\to\widehat H^2(M;\mathbf Z).
\tag{3.3}
\]

### Flat-sector corollary

If

\[
R(\widehat{\mathcal A})=0,
\tag{3.4}
\]

then

\[
R(\widehat{\mathcal R}_{\widehat u})=0.
\tag{3.5}
\]

So factorized pushforward cannot turn a flat global-anomaly class into a curved local-anomaly class.

### Curved-sector corollary

If

\[
R(\widehat{\mathcal A})\ne0,
\tag{3.6}
\]

then the factorized response changes only its integral multiplicity. It does not rotate the curvature into another tensor type or another structure group.

---

## 4. Canonical curve-family example

Now take a smooth proper family of compact genus-\(g\ge2\) complex curves

\[
\pi:X\to B,
\tag{4.1}
\]

with relative canonical line

\[
K_{X/B}.
\tag{4.2}
\]

Equip it with a Hermitian metric and compatible Chern connection, giving

\[
\widehat u_K
:=
\widehat c_1(K_{X/B})
\in
\widehat H^2(X;\mathbf Z).
\tag{4.3}
\]

The real fiber dimension is two, so this has exactly the degree required by the Model-VII template.

On each fiber \(X_b\), standard curve theory gives [HM98]

\[
\boxed{
\int_{X_b}c_1(K_{X_b})
=
\deg K_{X_b}
=
2g-2.
}
\tag{4.4}
\]

Compatibility of differential-character fiber integration with the characteristic class and curvature maps therefore gives

\[
\boxed{
\pi_!\widehat c_1(K_{X/B})
=
2g-2
\in
\widehat H^0(B;\mathbf Z)
}
\tag{4.5}
\]

on a connected fixed-genus base.

Let

\[
\widehat{\mathcal A}
\in
\widehat H^2(B;\mathbf Z)
\tag{4.6}
\]

be the determinant differential character from Model VI. Then

\[
\begin{aligned}
\widehat{\mathcal R}_K
&:=
\pi_!\left(
\pi^*\widehat{\mathcal A}
\cup
\widehat c_1(K_{X/B})
\right)\\[1mm]
&=
\widehat{\mathcal A}
\cup
\pi_!\widehat c_1(K_{X/B})\\[1mm]
&=
(2g-2)\widehat{\mathcal A}.
\end{aligned}
\tag{4.7}
\]

Therefore

\[
\boxed{
\widehat{\mathcal R}_K
=
(2g-2)\widehat{\mathcal A}.
}
\tag{4.8}
\]

This is the canonical-coupling result anticipated at the end of Model VII.

### Consequences

\[
\boxed{
R(\widehat{\mathcal R}_K)
=(2g-2)R(\widehat{\mathcal A}),
}
\tag{4.9}
\]

and

\[
\boxed{
\operatorname{Hol}_{\widehat{\mathcal R}_K}(\gamma)
=
\operatorname{Hol}_{\widehat{\mathcal A}}(\gamma)^{2g-2}.
}
\tag{4.10}
\]

So the most obvious canonical coupling restores the differential-cohomology degree exactly as hoped, but produces no new independent response geometry.

---

## 5. Why this is a genuine no-go rather than a failed guess

The obstruction does not depend on the special choice \(K_{X/B}\).

For **every**

\[
\widehat u\in\widehat H^2(X;\mathbf Z)
\tag{5.1}
\]

in a connected curve family,

\[
\pi_!\widehat u
\in
\widehat H^0(B;\mathbf Z)
\cong\mathbf Z.
\tag{5.2}
\]

Therefore

\[
\boxed{
\pi_!\left(\pi^*\widehat{\mathcal A}\cup\widehat u\right)
=
n_{\widehat u}\widehat{\mathcal A}.
}
\tag{5.3}
\]

Changing the degree-two coupling class cannot evade this conclusion as long as the response remains factorized through the pullback of the same base anomaly class.

This rules out an entire class of FCIG response ansätze at once.

---

## 6. What can escape the theorem?

The theorem applies to

\[
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr).
\tag{6.1}
\]

A genuinely new degree-two class must therefore leave at least one assumption of this form.

### 6.1 Non-factorized total-space class

A class

\[
\widehat W
\in
\widehat H^{d+2}(Z;\mathbf Z)
\tag{6.2}
\]

which is **not** of the form

\[
p^*\widehat{\mathcal A}\cup\widehat u
\tag{6.3}
\]

can have

\[
p_!\widehat W
\in
\widehat H^2(M;\mathbf Z)
\tag{6.4}
\]

without the scalar-multiplication collapse.

For a curve family, the simplest natural topological prototype is

\[
c_1(K_{X/B})^2
\in
H^4(X;\mathbf Z),
\tag{6.5}
\]

whose ordinary fiber integral is the first Mumford--Morita--Miller type class. A differential refinement of this direction is the natural next controlled test. No formula identifying it with a gravitational connection is asserted here.

### 6.2 Nontrivial correspondence

In a genuine correspondence

\[
M\xleftarrow{p}Z\xrightarrow{q}B,
\tag{6.6}
\]

with \(q\ne p\), the class \(q^*\widehat{\mathcal A}\) need not be pulled back from the target \(M\), so the simple projection-formula collapse need not apply in the same way.

### 6.3 Nonabelian or different generalized cohomology target

Ordinary degree-two differential cohomology still describes \(U(1)\) line-with-connection data. Producing tangent/frame geometry would require an additional construction with the correct nonabelian structure group or a different geometric cohomology theory.

---

## 7. Status relative to FCIG

The result sharpens the response hierarchy:

\[
\boxed{
\begin{array}{rcl}
\text{pullback} &:& \text{valid, preserves degree},\\
\text{loop transgression} &:& \text{valid, lowers degree to holonomy function},\\
\text{bare pushforward} &:& \text{valid, lowers degree},\\
\text{factorized degree-restored pushforward}
&:& \text{valid, but only integer multiplication},\\
\text{non-factorized degree-}(d+2)\text{ class}
&:& \text{next open controlled direction}.
\end{array}
}
\tag{7.1}
\]

**FCIG interpretation.** The mathematics is now restrictive enough that a future response law cannot be justified merely by choosing a coupling class of the required degree. Factorized couplings have no capacity to create a new degree-two response direction.

---

## 8. Gravity/type audit

Nothing in this note resolves the remaining mismatch with gravity.

Even if one obtains a new class

\[
p_!\widehat W\in\widehat H^2(M;\mathbf Z),
\]

it remains an abelian \(U(1)\) differential character unless additional geometric structure is supplied.

Therefore the following remain unresolved:

1. parameter/moduli base versus physical spacetime;
2. \(U(1)\) line connection versus \(SO(1,d-1)\) / frame connection;
3. Euclidean/Kähler family geometry versus Lorentzian causal geometry;
4. state-count information versus horizon entropy;
5. forward family-index constructions versus an inverse dynamical response law.

No gravitational derivation is claimed.

---

## 9. Reproducibility note

`factorized-pushforward.py` checks the degree bookkeeping and the canonical multiplier

\[
2g-2
\]

for representative genera, and verifies the corresponding holonomy-power rule for sample \(U(1)\) phases. It is a convention / arithmetic sanity checker, not a proof of the projection formula.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[BB14]** C. Bär and C. Becker, *Differential Characters and Geometric Chains*, in *Differential Characters*, LNM 2112, Springer (2014). Product, fiber integration, up-down/projection formula and transgression.
- **[HM98]** J. Harris and I. Morrison, *Moduli of Curves*, Springer (1998). Standard geometry of smooth curves and the canonical class.

The projection formula and fiber integration are established mathematics. The theorem that this specific FCIG factorized response ansatz collapses to integer multiplication is the **Derived here** consequence of applying those operations to a degree-two base anomaly class.
