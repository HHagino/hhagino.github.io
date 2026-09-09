# FCIG Explicit Model XI: Determinant Trace, Spin\(^c\) Extension, and the Nonabelian Reconstruction No-Go

**Status:** citation-audited research note  
**Milestone:** v0.11 — target-structure / nonabelian bridge audit  
**Updated:** 2026-09-09

## Citation policy

This note continues the repository-wide distinction:

- **Established** — standard results with explicit references;
- **Derived here** — elementary consequences proved in this note from the established structure;
- **FCIG consequence** — interpretation for the FCIG architecture;
- **No-go** — a failed inverse extrapolation recorded explicitly.

The purpose is not to claim that a determinant line *is* a frame connection. It is to determine exactly what information a determinant line can carry from a nonabelian connection, and exactly what information it necessarily forgets.

---

## 1. Executive result

The previous FCIG milestones closed the canonical smooth curve-family determinant/intersection sector at the level of topology, curvature, and global holonomy:

\[
\widehat\kappa_1=12\widehat\lambda_Q.
\]

That equality still lives in degree-two \(U(1)\) differential cohomology. The present note asks whether a line connection can determine a nonabelian target/frame connection.

The answer has a clean two-sided form.

### Positive direction

A nonabelian unitary connection has a canonical determinant/trace projection

\[
\boxed{
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
}
\]

so a \(U(n)\) connection canonically induces a \(U(1)\) determinant connection. In Kähler geometry this determinant curvature is the Ricci form. [Hall15; Huy05]

Likewise, a \(Spin^c\) structure combines orthogonal/frame data and determinant-line data. With the frame connection supplied independently, a determinant-line connection participates in a genuine \(Spin^c\) connection. [LM89; Yam20]

### Negative direction

The inverse reconstruction fails.

For \(n>1\), fixing the determinant connection leaves the traceless \(SU(n)\) connection sector free. Equivalently,

\[
\boxed{
\text{determinant data}
=
\text{trace part only};
\qquad
\text{traceless nonabelian curvature is invisible}.
}
\]

A fixed homomorphism \(U(1)\to G\) cannot repair this: its Lie-algebra image is at most one-dimensional and abelian, so it cannot generate generic noncommuting curvature in a nonabelian frame group.

The sharp FCIG conclusion is therefore

\[
\boxed{
\text{the determinant/anomaly sector can constrain a trace sector of geometry,}
\;
\text{but it cannot by itself reconstruct full frame geometry.}
}
\]

---

## 2. The bridge must first live on the same base

Let the FCIG determinant/anomaly differential character live on a parameter space \(B\):

\[
\widehat{\mathcal A}_B\in\widehat H^2(B;\mathbf Z).
\]

Let the proposed target geometry live on a manifold \(M\). Before any structure-group comparison, one needs an actual map

\[
\boxed{
f:M\to B
}
\]

or a specified correspondence replacing it.

Only then is there a pulled-back line-with-connection class

\[
\boxed{
\widehat{\mathcal A}_M=f^*\widehat{\mathcal A}_B
\in\widehat H^2(M;\mathbf Z).
}
\]

This note studies the **structure-group problem after such a base-space map has been supplied**. It does not manufacture \(f\).

---

## 3. Established determinant sequence

For the unitary group there is the standard short exact sequence [Hall15]

\[
\boxed{
1\longrightarrow SU(n)
\longrightarrow U(n)
\xrightarrow{\det}
U(1)
\longrightarrow1.
}
\]

At the Lie-algebra level,

\[
\mathfrak u(n)
=
\mathfrak{su}(n)
\oplus
i\mathbf R\,I_n
\]

as real vector spaces.

The differential of the determinant is the trace map:

\[
\boxed{
(d\det)_e(X)=\operatorname{Tr}X.
}
\]

Thus determinant geometry is the abelian quotient of unitary geometry by the traceless \(SU(n)\) sector.

---

## 4. Connection-level trace map

Let \(E\to M\) be a rank-\(n\) Hermitian bundle with unitary connection \(\nabla^E\). In a local unitary frame write

\[
\nabla^E=d+A,
\qquad
A\in\Omega^1(M;\mathfrak u(n)).
\]

The induced connection on

\[
\det E=\Lambda^n E
\]

has local connection one-form

\[
\boxed{
a_{\det}=\operatorname{Tr}A.
}
\]

The curvature is

\[
F_E=dA+A\wedge A.
\]

Since the trace kills commutators,

\[
\operatorname{Tr}(A\wedge A)=0,
\]

and therefore

\[
\boxed{
F_{\det E}
=
\operatorname{Tr}F_E.
}
\]

This is the precise forward bridge:

\[
\boxed{
(U(n)\text{ connection})
\longmapsto
(U(1)\text{ determinant connection})
}
\]

by taking the trace.

### Differential-cohomology form

At degree two, this means

\[
\widehat c_1(\det E,\det\nabla^E)
\in\widehat H^2(M;\mathbf Z)
\]

packages precisely the determinant line, its trace curvature, and its determinant holonomy.

A genuine FCIG trace bridge would therefore require an isomorphism of lines with connection

\[
\boxed{
(\det E,\det\nabla^E)
\cong
f^*(L_{\mathcal A},\nabla^{\mathcal A}).
}
\]

This is a mathematically valid bridge condition. It is **extra geometric data**, not something implied merely by equality of two scalar curvature forms.

---

## 5. Derived theorem: the fiber of the determinant map on connections

Fix a Hermitian bundle \(E\to M\) and fix a connection on \(\det E\).

Let \(\nabla\) and \(\nabla'\) be unitary connections on \(E\). Their difference is

\[
\alpha:=\nabla'-\nabla
\in\Omega^1(M;\mathfrak u(E)).
\]

The induced determinant connections agree if and only if

\[
\boxed{
\operatorname{Tr}\alpha=0.
}
\]

Hence

\[
\boxed{
\det\nabla'=\det\nabla
\iff
\alpha\in\Omega^1(M;\mathfrak{su}(E)).
}
\]

Therefore:

### Theorem 5.1 — determinant-lift nonuniqueness

For fixed \(E\) and fixed determinant connection, the space of unitary connections inducing it is an affine space modeled on

\[
\boxed{
\Omega^1(M;\mathfrak{su}(E)).
}
\]

whenever this space is nonzero.

This is elementary but decisive. The determinant connection fixes the central/trace part and leaves the traceless nonabelian part undetermined.

Locally one may write

\[
A
=
\frac{a_{\det}}{n}I_n+A_0,
\qquad
\operatorname{Tr}A_0=0.
\]

Then \(a_{\det}\) is fixed by the determinant line, while \(A_0\) is additional \(SU(n)\) connection data.

The corresponding curvature decomposes schematically as

\[
\boxed{
F_E
=
\frac{1}{n}\operatorname{Tr}(F_E)I_n
+
F_E^{0},
\qquad
\operatorname{Tr}F_E^{0}=0.
}
\]

The determinant line sees the first summand and forgets the second.

---

## 6. Dimension-one exception

For \(n=1\),

\[
SU(1)=\{1\},
\qquad
U(1)=\det U(1).
\]

So there is **no traceless connection sector**.

This gives a structural explanation for why the curve-level laboratories of FCIG can look unusually complete from the determinant viewpoint:

\[
\boxed{
\text{complex dimension }1:
\quad
\text{unitary tangent holonomy is already abelian at the structure-group level}.
}
\]

For \(n>1\), the kernel \(SU(n)\) is nontrivial and the determinant loses information.

This is not a failure of differential cohomology. It is information discarded by the determinant functor itself.

---

## 7. Kähler test: determinant curvature is Ricci curvature

Let \((M^{2n},\omega)\) be Kähler. The Levi-Civita connection preserves the complex structure and agrees with the Chern connection on \(T^{1,0}M\). Standard Kähler geometry identifies [Huy05]

\[
\det T^{1,0}M
=
K_M^{-1}.
\]

For the induced Chern connection, the normalized first Chern form is the Ricci form:

\[
\boxed{
c_1\!\left(T^{1,0}M,\nabla\right)
=
\frac{1}{2\pi}\rho_\omega,
}
\]

with the corresponding sign convention for the canonical/anticanonical curvature. Equivalently, the determinant connection is the trace of the \(U(n)\) tangent connection. [Huy05]

Thus the strongest canonical geometric statement available from a determinant line is not

\[
\text{determinant curvature}=\text{full Riemann curvature},
\]

but rather

\[
\boxed{
\text{determinant curvature}
\longleftrightarrow
\text{Ricci/trace curvature}.
}
\]

### No-go 7.1 — Ricci does not determine full curvature

For \(n>1\), the traceless curvature \(F^0\) can vary while

\[
\operatorname{Tr}F
\]

is fixed. Therefore determinant/Ricci data cannot determine the full Chern or Riemann curvature tensor.

This is exactly the connection-level counterpart of Theorem 5.1.

---

## 8. Explicit geometric witness: Ricci-flat does not mean flat

The information loss above is not merely formal.

A K3 surface has trivial canonical bundle. By Yau's solution of the Calabi conjecture, every Kähler class on a K3 surface contains a Ricci-flat Kähler metric. [Yau78; HuyK3]

For such a metric,

\[
\boxed{
\rho_\omega=0,
}
\]

so the curvature of the determinant/canonical connection vanishes.

Nevertheless a K3 Ricci-flat metric is not a flat metric; its restricted holonomy is \(SU(2)\) in the generic hyperkähler situation, and the full Riemann curvature is nonzero. [HuyK3]

Hence there exist canonical geometric situations with

\[
\boxed{
F_{\det T^{1,0}M}=0
\qquad\text{while}\qquad
F_{T^{1,0}M}\neq0.
}
\]

This is a direct curved witness that a flat determinant sector can coexist with nontrivial nonabelian frame holonomy.

It is the higher-dimensional analogue of the lesson already suggested by the flat ppav models, now realized inside actual tangent geometry rather than an auxiliary quantization bundle.

---

## 9. Spin\(^c\): a genuine extension bridge, not an inverse reconstruction

The standard group is [LM89]

\[
\operatorname{Spin}^c(n)
=
\frac{\operatorname{Spin}(n)\times U(1)}{\{\pm1\}}.
\]

There is a standard projection to \(SO(n)\) and a determinant map to \(U(1)\). A convenient convention is

\[
\det([g,z])=z^2.
\]

The associated Hermitian line is the determinant line of the \(Spin^c\) structure. Modern treatments explicitly include a unitary connection on this determinant line as part of a differential \(Spin^c\) structure. [Yam20]

At the Lie-algebra level,

\[
\boxed{
\mathfrak{spin}^c(n)
\cong
\mathfrak{so}(n)\oplus\mathfrak u(1).
}
\]

Therefore, once an orthogonal/frame connection \(\omega_{\mathrm{fr}}\) is already supplied, a determinant-line connection \(A_{\det}\) combines with it to determine the corresponding \(Spin^c\) connection, with the conventional factor fixed by the chosen determinant map.

This is a genuine positive bridge:

\[
\boxed{
(\text{frame connection},\;\text{determinant }U(1)\text{ connection})
\longrightarrow
\operatorname{Spin}^c\text{ connection}.
}
\]

But it is not an inverse reconstruction:

\[
\boxed{
\text{determinant }U(1)\text{ connection alone}
\not\longrightarrow
\text{frame }SO(n)\text{ connection}.
}
\]

The frame connection is an independent input.

### FCIG compatibility condition

If one wants the FCIG anomaly line to play the determinant-line role of a \(Spin^c\) structure on \(M\), the necessary data include

1. a map \(f:M\to B\);
2. a \(Spin^c\) structure \(P_{\operatorname{Spin}^c}\to M\);
3. an isomorphism of determinant lines with connection
   \[
   L_{\det}(P_{\operatorname{Spin}^c})
   \cong
   f^*L_{\mathcal A};
   \]
4. an independently specified metric/frame connection on \(M\).

Without item 4, the \(Spin^c\) extension does not generate spacetime geometry.

---

## 10. Derived theorem: fixed-homomorphism nonabelian no-go

Suppose one tries to create a target \(G\)-connection from a single \(U(1)\) connection by extension of structure group along a fixed Lie-group homomorphism

\[
\varphi:U(1)\to G.
\]

Its Lie-algebra map is

\[
d\varphi:i\mathbf R\to\mathfrak g.
\]

Since \(i\mathbf R\) is one-dimensional and abelian,

\[
\boxed{
\dim\operatorname{im}(d\varphi)\le1,
\qquad
[\operatorname{im}(d\varphi),\operatorname{im}(d\varphi)]=0.
}
\]

If \(A\) is a \(U(1)\) connection, the induced \(G\)-connection has curvature

\[
\boxed{
F_G=d\varphi(F_A),
}
\]

so every curvature value lies in this same one-dimensional abelian subalgebra.

Hence for all tangent vectors,

\[
\boxed{
[F_G(X,Y),F_G(Z,W)]=0.
}
\]

### Theorem 10.1 — fixed-homomorphism no-go

A connection obtained from one \(U(1)\) connection by a fixed structure-group homomorphism cannot reproduce a generic nonabelian connection whose curvature takes noncommuting values.

In particular, a generic orthogonal/frame connection cannot be reconstructed in this way.

This statement is independent of whether the eventual target signature is Euclidean or Lorentzian; it is a Lie-algebra obstruction before causal structure is considered.

---

## 11. What the determinant line can legitimately constrain

The previous sections give a useful hierarchy.

### Level 1 — line data

\[
\widehat{\mathcal A}
\in
\widehat H^2(M;\mathbf Z)
\]

gives a \(U(1)\) line with connection.

### Level 2 — determinant/trace constraint

If

\[
(\det E,\det\nabla^E)
\cong
(L_{\mathcal A},\nabla^{\mathcal A}),
\]

then FCIG data constrains

\[
\boxed{
\operatorname{Tr}F_E=F_{\mathcal A}.
}
\]

For Kähler tangent geometry this is a Ricci-form constraint.

### Level 3 — full nonabelian geometry

To obtain the full connection one still needs

\[
\boxed{
A_0\in\Omega^1(M;\mathfrak{su}(E))
}
\]

or the analogous traceless/frame data.

Thus any future FCIG geometric closure must either

1. supply this extra nonabelian sector independently;
2. derive it from another field/equation not contained in the determinant character;
3. or restrict to a special class of geometries where independent theorems determine the traceless sector from additional conditions.

The determinant line alone cannot do it.

---

## 12. FCIG architecture after v0.11

The earlier three-object architecture

\[
(L_Q,\lambda_{\mathrm{an}},TM)
\]

can now be sharpened.

The determinant/anomaly sector can be related to target geometry only through an explicit bridge datum such as

\[
\boxed{
\left(
 f:M\to B,
 E\to M,
 \nabla^E,
 \det(E,\nabla^E)\cong f^*(L_{\mathcal A},\nabla^{\mathcal A})
\right).
}
\]

For tangent Kähler geometry, this identifies FCIG determinant curvature with a Ricci/trace response.

For \(Spin^c\) geometry, it identifies the FCIG line with the determinant factor in an enlarged frame structure, while leaving the orthogonal connection independent.

This is a stronger and safer statement than any direct identification

\[
F_{\mathcal A}=R_{\mathrm{Riem}}.
\]

The latter is type-incorrect in general.

---

## 13. Gate results

### Gate AD — determinant trace bridge: PASS

Established:

\[
1\to SU(n)\to U(n)\to U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

### Gate AE — lift nonuniqueness: PASS WITH NO-GO

Derived here:

\[
\det\nabla'=\det\nabla
\iff
\nabla'-\nabla\in\Omega^1(\mathfrak{su}(E)).
\]

So determinant data does not determine the full connection for \(n>1\).

### Gate AF — Kähler canonical test: PASS WITH NO-GO

Established:

\[
\det T^{1,0}M=K_M^{-1},
\qquad
c_1(T^{1,0}M,\nabla)=\frac{\rho_\omega}{2\pi}.
\]

Therefore the determinant sees Ricci/trace curvature, not full Riemann curvature. The Ricci-flat K3 witness makes the loss explicit. [Huy05; Yau78; HuyK3]

### Gate AG — Spin\(^c\) audit: PASS WITH NON-IDENTIFICATION

Established:

\[
\operatorname{Spin}^c(n)
=(\operatorname{Spin}(n)\times U(1))/\{\pm1\},
\]

with a determinant line and its unitary connection. Frame connection plus determinant connection gives a \(Spin^c\) connection; the determinant line alone does not provide the frame connection. [LM89; Yam20]

### Gate AH — fixed-homomorphism audit: PASS WITH NO-GO

Derived here: every fixed \(U(1)\to G\) extension has curvature in a one-dimensional abelian Lie subalgebra and cannot represent generic nonabelian frame curvature.

---

## 14. v0.11 conclusion

\[
\boxed{
\begin{aligned}
\text{nonabelian connection}
&\longrightarrow
\text{determinant/trace }U(1)
&&\text{canonical},\\
\text{determinant }U(1)
&\longrightarrow
\text{full nonabelian connection}
&&\text{not canonical and generically impossible without extra data}.
\end{aligned}
}
\]

For FCIG this means:

\[
\boxed{
\text{determinant information may source or constrain a trace sector,}
\text{ but the traceless frame sector must enter independently.}
}
\]

The determinant sector is therefore **not** a hidden complete theory of gravity.

What it can plausibly provide is one controlled input into a larger coupled system.

---

## 15. Next controlled milestone

The next question should no longer be

> Can a \(U(1)\) anomaly line secretly equal the frame connection?

v0.11 answers that in the negative.

The next useful question is:

> Given an **independent** frame connection and the FCIG \(U(1)\) determinant connection on the same base, what standard gauge-invariant mixed characteristic classes or transgression terms can couple them without identifying their structure groups?

This becomes a degree/tensor audit of mixed Chern--Weil data, not an inverse-reconstruction problem.

A natural v0.12 candidate is therefore a **mixed characteristic-class / anomaly-polynomial audit**, beginning with the degree of expressions involving \(c_1(L)\) and Pontryagin classes of the frame bundle.

No Lorentzian field equation is claimed at this stage.

---

## References used in this note

- **[Hall15]** Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Springer, 2015.
- **[Huy05]** Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.
- **[LM89]** H. Blaine Lawson, Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989.
- **[Yam20]** Mayuko Yamashita, “A Topological Approach to Indices of Geometric Operators on Manifolds with Fibered Boundaries,” *Communications in Mathematical Physics* 377 (2020), 77–147.
- **[Yau78]** Shing-Tung Yau, “On the Ricci Curvature of a Compact Kähler Manifold and the Complex Monge–Ampère Equation, I,” *Communications on Pure and Applied Mathematics* 31 (1978), 339–411.
- **[HuyK3]** Daniel Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016.

These references support the standard Lie-group, Kähler, Spin\(^c\), and Ricci-flat/K3 background. The determinant-lift affine-space theorem and fixed-homomorphism no-go are elementary consequences derived in this note.