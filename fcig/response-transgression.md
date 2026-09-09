# FCIG Explicit Model VII: Loop Transgression, Pullback Response, and the Degree Obstruction

**Status:** v0.7 worked response/transgression test  
**Date:** 2026-09-09

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are deductions from those structures with the conventions fixed below. Statements marked **FCIG interpretation** or **no-go** are not attributed to the cited literature.

Model VI replaced a curvature-only anomaly datum by a differential character

\[
\widehat{\mathcal A}
\in
\widehat H^2(B;\mathbf Z).
\]

The next question is whether one can transport this class to another geometric space by an actual mathematical operation, rather than by verbally identifying the moduli base \(B\) with another manifold.

This note tests three standard operations:

1. pullback;
2. loop-space transgression;
3. fiber integration / pushforward.

The main result is a useful combination of a positive statement and a no-go:

\[
\boxed{
\text{holonomy is a genuine transgressed response, but a degree-two determinant class does not by itself push forward to another degree-two line across positive-dimensional fibers.}
}
\]

---

## 1. The source differential character

Let

\[
\boxed{
\widehat{\mathcal A}
=
\widehat c_1(L,\nabla)
\in
\widehat H^2(B;\mathbf Z)
}
\tag{1.1}
\]

be the determinant differential character of Model VI.

Its curvature and holonomy are

\[
R(\widehat{\mathcal A})
=
\frac{F_\nabla}{2\pi i},
\qquad
\operatorname{Hol}_{\widehat{\mathcal A}}(\gamma)
=
\exp\bigl(2\pi i h_{\widehat{\mathcal A}}(\gamma)\bigr).
\]

Degree-two differential cohomology classifies line bundles with connection, while degree-one differential cohomology corresponds to smooth \(U(1)\)-valued functions [CS85; BB14].

---

## 2. Pullback is a genuine response operation

For any smooth map

\[
f:M\to B,
\]

functoriality gives

\[
\boxed{
f^*\widehat{\mathcal A}
\in
\widehat H^2(M;\mathbf Z).
}
\tag{2.1}
\]

This is again a Hermitian line with unitary connection, now on \(M\). The structure maps commute with pullback:

\[
\boxed{
I(f^*\widehat{\mathcal A})=f^*I(\widehat{\mathcal A}),
\qquad
R(f^*\widehat{\mathcal A})=f^*R(\widehat{\mathcal A}).
}
\tag{2.2}
\]

For a loop \(c:S^1\to M\),

\[
\boxed{
\operatorname{Hol}_{f^*\widehat{\mathcal A}}(c)
=
\operatorname{Hol}_{\widehat{\mathcal A}}(f\circ c).
}
\tag{2.3}
\]

This is a completely legitimate response map.

**No-go boundary.** The mathematics supplies \(f^*\), but it does not supply a physically preferred map \(f:M\to B\). If \(M\) is proposed to be spacetime, constructing such an \(f\) is extra structure, not a consequence of differential cohomology.

**Gate R — PASS.** The source, target, and map are explicit.

---

## 3. Pullback to a loop: curvature disappears but holonomy remains

Take a loop directly in the parameter base,

\[
c:S^1\to B.
\]

Then

\[
c^*\widehat{\mathcal A}
\in
\widehat H^2(S^1;\mathbf Z).
\]

Since \(S^1\) has no nonzero differential two-forms,

\[
\boxed{
R(c^*\widehat{\mathcal A})=0.
}
\tag{3.1}
\]

Also \(H^2(S^1;\mathbf Z)=0\), so the pulled-back class is entirely flat. Nevertheless,

\[
\boxed{
\operatorname{Hol}_{c^*\widehat{\mathcal A}}(S^1)
=
\operatorname{Hol}_{\widehat{\mathcal A}}(c)
}
\tag{3.2}
\]

can be nontrivial.

For a Bismut--Freed determinant connection, the right-hand side is governed by the adiabatic reduced eta invariant of the mapping torus over \(c\) [BF86b; DF94].

**Derived here.** This is a particularly transparent curved-to-flat operation: restriction of a nonflat differential character to a one-dimensional probe necessarily kills the curvature form while retaining its global holonomy.

---

## 4. Loop-space transgression

Let

\[
LB=C^\infty(S^1,B)
\]

be the free loop space, with evaluation and projection

\[
\operatorname{ev}:LB\times S^1\to B,
\qquad
\pi:LB\times S^1\to LB.
\]

Fiber integration in differential cohomology defines the standard transgression [BB14]

\[
\boxed{
\tau_{S^1}
:=
\widehat\pi_!\operatorname{ev}^*:
\widehat H^n(B;\mathbf Z)
\longrightarrow
\widehat H^{n-1}(LB;\mathbf Z).
}
\tag{4.1}
\]

For \(n=2\),

\[
\boxed{
\tau_{S^1}(\widehat{\mathcal A})
\in
\widehat H^1(LB;\mathbf Z).
}
\tag{4.2}
\]

Bär--Becker identify this degree-one differential character exactly with the holonomy map of the original line bundle with connection [BB14]:

\[
\boxed{
\tau_{S^1}(\widehat{\mathcal A})(\gamma)
=
\operatorname{Hol}_{\widehat{\mathcal A}}(\gamma)
\in U(1).
}
\tag{4.3}
\]

Thus holonomy is literally a transgressed response.

This is also consistent with the transgression/regression picture for bundles with connection and fusion maps on loop spaces [Wal09].

---

## 5. Curvature of the transgressed response

Fiber integration is compatible with curvature [BB14]. Hence

\[
\boxed{
R\bigl(\tau_{S^1}\widehat{\mathcal A}\bigr)
=
\int_{S^1}\operatorname{ev}^*R(\widehat{\mathcal A}).
}
\tag{5.1}
\]

The right-hand side is a one-form on \(LB\). At a loop \(\gamma\) and tangent vector \(V\) along \(\gamma\), it has the familiar transgressed-curvature form

\[
\boxed{
\left(\int_{S^1}\operatorname{ev}^*R\right)_\gamma(V)
=
\int_{S^1}
R_{\gamma(t)}\bigl(\dot\gamma(t),V(t)\bigr)\,dt.
}
\tag{5.2}
\]

Thus the infinitesimal variation of determinant holonomy over loop space is controlled by the original determinant curvature.

**FCIG interpretation.** This is a rigorous version of “local curvature controls the response of global holonomy,” but only in the standard loop-space transgression sense.

**Gate S — PASS.** A genuine differential-cohomology operation with the correct degree shift has been exhibited.

---

## 6. The degree obstruction

The same degree shift gives an immediate no-go.

A line with connection is degree two. Transgression along a one-dimensional fiber gives degree one:

\[
\widehat H^2
\xrightarrow{\int_{S^1}}
\widehat H^1.
\]

Therefore

\[
\boxed{
\text{ordinary loop transgression of a determinant line does not produce another line bundle with connection.}
}
\tag{6.1}
\]

It produces a \(U(1)\)-valued function: holonomy.

More generally, let

\[
p:Z\to M
\]

be a proper oriented submersion with compact real \(d\)-dimensional fibers. Differential-character fiber integration lowers degree by \(d\) [BB14]:

\[
\boxed{
p_!: \widehat H^r(Z;\mathbf Z)
\to
\widehat H^{r-d}(M;\mathbf Z).
}
\tag{6.2}
\]

If a correspondence

\[
M\xleftarrow{\;p\;}Z\xrightarrow{\;q\;}B
\]

is given, then directly pushing the determinant class gives

\[
\boxed{
p_!q^*\widehat{\mathcal A}
\in
\widehat H^{2-d}(M;\mathbf Z).
}
\tag{6.3}
\]

For every positive-dimensional fiber \(d>0\), this is **not** a degree-two line-with-connection class.

**Derived here / degree no-go.** A positive-dimensional pushforward cannot by itself turn a degree-two determinant anomaly into another degree-two response line.

---

## 7. What would be required to preserve degree two

Differential cohomology has a graded cup product [CS85; BB14]. Suppose, in addition to the correspondence, one is given a differential class

\[
\widehat u\in\widehat H^d(Z;\mathbf Z).
\]

Then

\[
q^*\widehat{\mathcal A}\cup\widehat u
\in
\widehat H^{d+2}(Z;\mathbf Z),
\]

and fiber integration yields

\[
\boxed{
\widehat{\mathcal R}_{p,q,\widehat u}
:=
p_!\bigl(q^*\widehat{\mathcal A}\cup\widehat u\bigr)
\in
\widehat H^2(M;\mathbf Z).
}
\tag{7.1}
\]

This is a mathematically valid **template** for a degree-preserving response line, provided the orientation and product hypotheses are satisfied.

Its characteristic class and curvature obey

\[
\boxed{
I(\widehat{\mathcal R})
=
p_!\bigl(q^*I(\widehat{\mathcal A})\cup I(\widehat u)\bigr),
}
\tag{7.2}
\]

and

\[
\boxed{
R(\widehat{\mathcal R})
=
\int_{Z/M}
q^*R(\widehat{\mathcal A})\wedge R(\widehat u).
}
\tag{7.3}
\]

**No-go boundary.** FCIG does not currently possess a canonical \(\widehat u\) with a physical interpretation. Introducing one solely to repair the degree mismatch would be definition by convenience rather than a derivation.

Equation (7.1) is therefore a constrained research template, not a completed physical coupling.

---

## 8. Why the universal-curve pushforward does not rescue the inverse problem

For a family of curves

\[
\pi:\mathcal X\to B,
\]

the real fiber dimension is two. A degree-four characteristic/differential class on \(\mathcal X\) may push forward to degree two on \(B\):

\[
\widehat H^4(\mathcal X)
\xrightarrow{\pi_!}
\widehat H^2(B).
\]

This is structurally compatible with families index / differential Riemann--Roch constructions: higher-degree characteristic data on the total space produce determinant-line data on the base.

But the reverse operation

\[
\widehat H^2(B)
\longrightarrow
\widehat H^2(\mathcal X)
\]

is only the pullback \(\pi^*\), unless additional data are supplied. Pullback does not reconstruct tangent curvature or invert the family index theorem.

**Derived here / no-go.** Differential fiber integration reinforces the logical direction already found in Models V--VI:

\[
\boxed{
\text{higher-degree geometry on the family}
\longrightarrow
\text{degree-two determinant data on the base}
}
\]

is standard, while the inverse map is not supplied automatically.

---

## 9. Target structure-group audit

Even when (7.1) produces a degree-two response class on \(M\), its target is still

\[
\widehat H^2(M;\mathbf Z),
\]

hence a \(U(1)\) line with connection.

It does not become a tangent/frame connection merely because both possess curvature two-forms:

\[
\boxed{
F_{U(1)}\in\Omega^2(M;i\mathbf R),
\qquad
R^{TM}\in\Omega^2(M;\mathfrak{so}(1,d-1)).
}
\tag{9.1}
\]

To connect them one needs additional structure such as an explicit Lie-algebra homomorphism, associated-bundle construction, action functional, or response equation. None has yet been derived.

**Gate T — PASS AS A TYPE AUDIT.** The target of every operation in this note is explicit.

---

## 10. Explicit response example: determinant holonomy on loop space

The clean explicit v0.7 response is therefore

\[
\boxed{
\widehat{\mathcal A}
\in\widehat H^2(B)
\quad\xmapsto{\;\tau_{S^1}\;}
\operatorname{Hol}_{\widehat{\mathcal A}}
\in C^\infty(LB,U(1)).
}
\tag{10.1}
\]

For the flat ppav Model IIIc, this recovers the finite metaplectic multiplier on modular loops.

For the curved Quillen/Bismut--Freed Model VI, it recovers the eta-invariant determinant holonomy on loops where the holonomy theorem applies [BF86b; DF94].

This is a shared response operation despite the two models having different curvature sectors.

**Gate U — PASS WITH DEGREE NO-GO.** We have one exact, standard response observable—holonomy—but ordinary transgression does not yield a new degree-two connection.

---

## 11. v0.7 synthesis

The response architecture is now

\[
\boxed{
\begin{aligned}
\text{pullback:}&\quad
\widehat H^2(B)\to\widehat H^2(M),\\[1mm]
\text{loop transgression:}&\quad
\widehat H^2(B)\to\widehat H^1(LB),\\[1mm]
\text{fiber pushforward:}&\quad
\widehat H^r(Z)\to\widehat H^{r-d}(M),\\[1mm]
\text{degree-preserving coupled response:}&\quad
p_!(q^*\widehat{\mathcal A}\cup\widehat u)\in\widehat H^2(M).
\end{aligned}
}
\tag{11.1}
\]

The first three are standard operations. The fourth is a standard construction **once** the correspondence and coupling class are supplied, but FCIG has not derived a canonical physical choice of those data.

The main no-go is therefore sharper than before:

\[
\boxed{
\text{differential-cohomology functoriality does not manufacture the missing spacetime map or coupling class.}
}
\tag{11.2}
\]

Gravity Closure remains inactive.

---

## 12. Status of v0.7 gates

- **Gate R — correspondence/source/target:** PASS.
- **Gate S — genuine differential-cohomology operation:** PASS.
- **Gate T — target tensor/structure group:** PASS AS AUDIT.
- **Gate U — explicit response or no-go:** PASS WITH DEGREE NO-GO.

The next controlled question is whether the geometry already present in the family—rather than a newly invented field—provides a canonical degree-restoring class \(\widehat u\), or whether the absence of such a class is itself a structural obstruction.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[CS85]** J. Cheeger and J. Simons, *Differential Characters and Geometric Invariants*, LNM 1167 (1985).
- **[BB14]** C. Bär and C. Becker, *Differential Characters and Geometric Chains*, in *Differential Characters*, LNM 2112 (2014), 1--90.
- **[Wal09]** K. Waldorf, *Transgression to Loop Spaces and its Inverse, I: Diffeological Bundles and Fusion Maps*, arXiv:0911.3212.
- **[BF86b]** J.-M. Bismut and D. S. Freed, *The Analysis of Elliptic Families II: Dirac Operators, Eta Invariants, and the Holonomy Theorem*, CMP 107 (1986).
- **[DF94]** X. Dai and D. S. Freed, *Eta-Invariants and Determinant Lines*, J. Math. Phys. 35 (1994).