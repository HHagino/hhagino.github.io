# FCIG Explicit Model VI: Differential Cohomology, Determinant Connections, and Local/Global Anomaly Data

**Status:** v0.6 worked synthesis  
**Date:** 2026-09-09

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are deductions made from those established structures in the conventions fixed below. Statements marked **FCIG interpretation** or **no-go** are not attributed to the cited literature.

The earlier FCIG models separated two phenomena:

1. local determinant curvature;
2. global flat or spectral holonomy.

This note packages them into the standard degree-two differential-cohomology class of a Hermitian line bundle with unitary connection.

The principal mathematical conclusion is not that FCIG has discovered a new anomaly object. It is the opposite: the correct object was already known. A determinant line with connection belongs naturally to differential cohomology, where curvature and holonomy are compatible outputs of one class [CS85; Bry93; ADH21].

---

## 1. Degree-two differential cohomology

Use the modern convention in which

\[
\widehat H^2(B;\mathbf Z)
\]

classifies Hermitian \(U(1)\) line bundles with unitary connection up to isomorphism [CS85; Bry93; ADH21].

Thus a line with connection

\[
(L,\nabla)
\]

defines

\[
\boxed{
\widehat c_1(L,\nabla)
\in
\widehat H^2(B;\mathbf Z).
}
\tag{1.1}
\]

There are two standard structure maps:

\[
I:\widehat H^2(B;\mathbf Z)\to H^2(B;\mathbf Z)
\]

and

\[
R:\widehat H^2(B;\mathbf Z)\to\Omega^2_{\mathbf Z}(B),
\]

where \(\Omega^2_{\mathbf Z}(B)\) denotes closed two-forms with integral periods in the chosen normalization. For a unitary line connection,

\[
\boxed{
I(\widehat c_1)=c_1(L),
\qquad
R(\widehat c_1)=\frac{F_\nabla}{2\pi i}.
}
\tag{1.2}
\]

Their real cohomology classes agree:

\[
[R(\widehat c_1)]_{\mathrm{dR}}
=
I(\widehat c_1)\otimes_{\mathbf Z}\mathbf R.
\tag{1.3}
\]

---

## 2. Differential characters and holonomy

In the Cheeger--Simons model, a degree-two differential character is represented by a homomorphism

\[
\boxed{
h:Z_1(B)\to\mathbf R/\mathbf Z
}
\tag{2.1}
\]

such that there exists a closed two-form \(\omega\) with integral periods satisfying

\[
\boxed{
h(\partial C)=\int_C\omega\pmod{\mathbf Z}}
\tag{2.2}
\]

for smooth two-chains \(C\) [CS85].

For a line with unitary connection,

\[
\boxed{
\operatorname{Hol}_\nabla(\gamma)
=
\exp\bigl(2\pi i\,h(\gamma)\bigr).
}
\tag{2.3}
\]

Equation (2.2) is the compatibility between local curvature and global loop holonomy. In particular, if \(\gamma=\partial C\), then

\[
\boxed{
\operatorname{Hol}_\nabla(\partial C)
=
\exp\left(\int_C F_\nabla\right).
}
\tag{2.4}
\]

with the unitary-curvature convention \(F_\nabla\in\Omega^2(i\mathbf R)\).

---

## 3. The flat sector

Differential cohomology has the curvature exact sequence [CS85; ADH21]

\[
\boxed{
0
\longrightarrow
H^1(B;\mathbf R/\mathbf Z)
\longrightarrow
\widehat H^2(B;\mathbf Z)
\xrightarrow{\;R\;}
\Omega^2_{\mathbf Z}(B)
\longrightarrow0.
}
\tag{3.1}
\]

Hence

\[
R(\widehat x)=0
\]

does **not** imply

\[
\widehat x=0.
\]

Instead, a curvature-zero class may remain as

\[
\boxed{
\widehat x_{\mathrm{flat}}
\in
H^1(B;\mathbf R/\mathbf Z).
}
\tag{3.2}
\]

Its information is precisely a flat \(U(1)\) holonomy character on one-cycles.

This gives a standard mathematical home for the distinction used in Explicit Models II and IIIc:

\[
\boxed{
\text{zero local curvature}
\not\Rightarrow
\text{trivial global line-with-connection class}.
}
\tag{3.3}
\]

---

## 4. Characteristic-class exact sequence

The complementary exact sequence is

\[
\boxed{
0
\longrightarrow
\frac{\Omega^1(B)}{\Omega^1_{\mathbf Z}(B)}
\longrightarrow
\widehat H^2(B;\mathbf Z)
\xrightarrow{\;I\;}
H^2(B;\mathbf Z)
\longrightarrow0,
}
\tag{4.1}
\]

where \(\Omega^1_{\mathbf Z}\) denotes closed one-forms with integral periods [ADH21].

Thus differential cohomology simultaneously refines:

\[
\boxed{
\text{topological line class}
+
\text{connection form data}
+
\text{curvature}
+
\text{holonomy}.
}
\tag{4.2}
\]

These are linked pieces of one object, not four independent labels.

**Gate N — PASS.** The differential-cohomology object and its structural maps are fixed.

---

## 5. Flat ppav corrected lines as flat differential characters

In Explicit Model IIIc, on the appropriate theta/metaplectic quotient or cover where the corrected line descends, one has

\[
\mathscr A_{g,k}
=
\det\mathcal H_k\otimes\lambda_H^{k^g/2}
\]

for even level, with

\[
F_{\mathscr A_{g,k}}=0.
\]

The remaining modular descent multiplier is a character

\[
\chi_{g,k}:\pi_1(B_{\mathrm{theta}})\to U(1).
\]

Therefore the descended corrected line with its flat connection defines

\[
\boxed{
\widehat c_1(\mathscr A_{g,k},\nabla^{\mathrm{flat}})
\in
H^1(B_{\mathrm{theta}};\mathbf R/\mathbf Z)
\hookrightarrow
\widehat H^2(B_{\mathrm{theta}};\mathbf Z).
}
\tag{5.1}
\]

**Derived here.** This is not a new theorem about Weil representations. It is the reinterpretation of the already-computed flat corrected line through the standard exact sequence (3.1).

For the explicit genus-two, level-two shear of Model IIIc,

\[
\chi_{2,2}(T_{B_\times})=-1.
\]

On the corresponding loop,

\[
\boxed{
h(T_{B_\times})=\frac12\pmod{\mathbf Z}.}
\tag{5.2}
\]

This is an explicit nonzero flat differential character.

---

## 6. Quillen/Bismut--Freed determinant connection

For a smooth family of Dirac-type operators, the determinant line carries the Quillen metric and the Bismut--Freed unitary connection [BF86a; BF86b]. In the holomorphic family setting, the Quillen/Bismut--Gillet--Soul\'e construction gives the corresponding Chern connection and local-index curvature [Qui85; BGS88].

Write schematically

\[
(\lambda,\nabla^Q)
\]

for the determinant line with its natural unitary determinant connection. It defines

\[
\boxed{
\widehat c_1(\lambda,\nabla^Q)
\in
\widehat H^2(B;\mathbf Z).
}
\tag{6.1}
\]

Its curvature is the local family-index form. For the compact hyperbolic canonical family of Models IV--V,

\[
\boxed{
R\bigl(\widehat c_1(\lambda_k,\nabla^Q)\bigr)
=
c_1(\lambda_k,h_Q)
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}},
}
\tag{6.2}
\]

where the equality uses the first-Chern-form normalization already fixed in Model V [ZT87].

Thus the curved determinant character is not in the flat kernel of \(R\).

---

## 7. Bismut--Freed holonomy theorem

The determinant differential character also evaluates on loops. For a smooth loop

\[
c:S^1\to B,
\]

Bismut--Freed relate the holonomy of the determinant connection to the adiabatic limit of the reduced eta invariant of the odd-dimensional mapping torus over \(c\) [BF86b].

In the determinant convention used by Bismut--Freed, the theorem has the form

\[
\boxed{
\operatorname{Hol}_{\nabla^{BF}}(c)
=
(-1)^{\operatorname{Ind}D_+}
\exp\bigl(-2\pi i\,[\bar\eta_c]\bigr),
}
\tag{7.1}
\]

where \([\bar\eta_c]\in\mathbf R/\mathbf Z\) is the adiabatic-limit reduced eta invariant. Passing to an inverse determinant-line convention inverts the holonomy, so the sign/exponent convention must be matched before comparing literal formulas [BF86b; DF94].

The important convention-independent structural fact is

\[
\boxed{
\text{Quillen/Bismut--Freed determinant class}
\Longrightarrow
\begin{cases}
\text{local index curvature},\\
\text{global eta-invariant holonomy}.
\end{cases}
}
\tag{7.2}
\]

**Gate O — PASS.** The curved determinant line has been placed in the same degree-two differential-cohomology framework with both curvature and holonomy accounted for.

---

## 8. Flat and curved anomaly sectors: same category, different classes

The comparison is now precise.

### Flat ppav/metaplectic model

\[
\boxed{
R(\widehat c_1)=0,
\qquad
\operatorname{Hol}\neq1
}
\tag{8.1}
\]

is possible because the class lies in

\[
H^1(B;\mathbf R/\mathbf Z).
\]

### Curved Quillen model

\[
\boxed{
R(\widehat c_1)
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}
\neq0,
}
\tag{8.2}
\]

while loop holonomy is simultaneously encoded by eta data.

Therefore both models live in the category

\[
\boxed{
\text{Hermitian line bundles with unitary connection}
\simeq
\widehat H^2(-;\mathbf Z),
}
\tag{8.3}
\]

but they need not define the same class, live over the same base, or have the same holonomy mechanism.

**Derived here / no-go.** The common differential-cohomology target is a structural unification, not an identification of the ppav Weil character with the hyperbolic eta character.

**Gate P — PASS.** What is common is the degree-two differential-character architecture. What remains model-specific is the base space, curvature form, monodromy source, and determinant operator family.

---

## 9. Revised anomaly language

Earlier FCIG drafts sometimes used “anomaly” as though it meant \(c_1\neq0\) or \(F\neq0\). Differential cohomology forces a more accurate hierarchy.

For a determinant line with connection, define the anomaly datum to mean the complete differential class

\[
\boxed{
\widehat{\mathcal A}
:=
\widehat c_1(\lambda,\nabla)
\in\widehat H^2(B;\mathbf Z).
}
\tag{9.1}
\]

Then:

- **local curvature datum:** \(R(\widehat{\mathcal A})\);
- **topological datum:** \(I(\widehat{\mathcal A})\);
- **global loop datum:** evaluation/holonomy on \(Z_1(B)\);
- **flat global sector:** the component in \(\ker R\cong H^1(B;\mathbf R/\mathbf Z)\).

This captures the fact that a globally nontrivial anomaly can survive when the curvature vanishes.

**FCIG interpretation.** The mathematically safest slogan is now

\[
\boxed{
\text{anomaly geometry is differential-cohomological, not curvature-only.}
}
\tag{9.2}
\]

---

## 10. Pre-gravity type-mismatch audit

The differential-cohomology synthesis resolves the local/global determinant-line ambiguity. It does **not** resolve the gravity problem.

### Obstruction 1 — base-space mismatch

The class

\[
\widehat c_1(\lambda,\nabla)
\]

lives on a parameter/moduli base \(B\). Spacetime curvature lives on a physical spacetime manifold \(M\). No canonical map

\[
M\to B
\]

has been supplied by the FCIG models.

### Obstruction 2 — structure-group mismatch

The determinant connection is \(U(1)\)-valued. Gravitational curvature is associated to the tangent/frame connection with structure group such as \(SO(1,d-1)\) in Lorentzian signature.

\[
\boxed{
F_{\det}\in\Omega^2(B;i\mathbf R)
\not\equiv
R^{TM}\in\Omega^2(M;\mathfrak{so}(1,d-1)).
}
\tag{10.1}
\]

### Obstruction 3 — signature/causal mismatch

All explicit Models I--VI are complex/K\"ahler, Euclidean, or moduli-geometric. None supplies Lorentzian causal horizons.

### Obstruction 4 — entropy-functional mismatch

The state-capacity quantities

\[
\log\dim H^0(X,L^k)
\]

and local Bergman densities are not yet a horizon entropy functional satisfying the hypotheses of a Jacobson-type thermodynamic derivation.

### Obstruction 5 — logical-direction mismatch

Family index theory gives

\[
\text{geometric operator family}
\longrightarrow
\text{determinant curvature/holonomy}.
\]

FCIG has not proved the inverse implication

\[
\text{information/anomaly data}
\longrightarrow
\text{spacetime field equation}.
\]

**Gate Q — PASS AS A NO-GO AUDIT.** Every currently known mismatch is now explicit. Gravity Closure therefore remains inactive.

---

## 11. v0.6 synthesis

The determinant/anomaly sector can now be written as a single object

\[
\boxed{
\widehat{\mathcal A}
=
\widehat c_1(\lambda,\nabla)
\in\widehat H^2(B;\mathbf Z),
}
\tag{11.1}
\]

with three primary projections/evaluations:

\[
\boxed{
\begin{aligned}
I(\widehat{\mathcal A})
&=c_1(\lambda),\\
R(\widehat{\mathcal A})
&=F_\nabla/(2\pi i),\\
h_{\widehat{\mathcal A}}(\gamma)
&=(2\pi i)^{-1}\log\operatorname{Hol}_\nabla(\gamma)\pmod{\mathbf Z}.
\end{aligned}
}
\tag{11.2}
\]

The previous FCIG models become two limiting patterns:

\[
\boxed{
\begin{array}{lll}
\text{flat modular model:}
& R=0,& h\neq0,\\[1mm]
\text{curved Quillen model:}
& R\neq0,& h\text{ supplied by eta/holonomy data}.
\end{array}
}
\tag{11.3}
\]

This is the cleanest mathematical formulation so far of the local/global anomaly distinction.

It is still a determinant-line theory on parameter spaces, not a gravitational field theory.

---

## 12. Status of v0.6 gates

- **Gate N — differential-cohomology object:** PASS.
- **Gate O — Quillen/Bismut--Freed determinant class:** PASS.
- **Gate P — flat/curved comparison:** PASS WITH NON-IDENTIFICATION.
- **Gate Q — pre-gravity no-go audit:** PASS.

The next research stage should **not** jump directly to Einstein equations. A mathematically controlled next step is to investigate whether the determinant differential character participates in a transgression or response map to a geometrically distinct connection, with tensor types and base spaces explicitly specified.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[CS85]** J. Cheeger and J. Simons, *Differential Characters and Geometric Invariants*, LNM 1167 (1985), 50--80.
- **[Bry93]** J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkh\"auser (1993).
- **[ADH21]** A. Amabel, A. Debray, P. Haine, *Differential Cohomology: Categories, Characteristic Classes, and Connections*, arXiv:2109.12250.
- **[BF86a]** J.-M. Bismut and D. S. Freed, *The Analysis of Elliptic Families I*, CMP 106 (1986).
- **[BF86b]** J.-M. Bismut and D. S. Freed, *The Analysis of Elliptic Families II: Dirac Operators, Eta Invariants, and the Holonomy Theorem*, CMP 107 (1986).
- **[DF94]** X. Dai and D. S. Freed, *Eta-Invariants and Determinant Lines*, J. Math. Phys. 35 (1994).
- **[Qui85]** D. Quillen, *Determinants of Cauchy--Riemann Operators over a Riemann Surface*, Funct. Anal. Appl. 19 (1985).
- **[BGS88]** J.-M. Bismut, H. Gillet, C. Soul\'e, *Analytic Torsion and Holomorphic Determinant Bundles III*, CMP 115 (1988).
- **[ZT87]** P. G. Zograf and L. A. Takhtajan, *A Local Index Theorem for Families of \(\bar\partial\)-Operators on Riemann Surfaces*, Russian Math. Surveys 42:6 (1987).