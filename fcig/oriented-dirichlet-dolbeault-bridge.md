# FCIG: Oriented Dirichlet–Dolbeault Bridge

**Status:** exact orientation no-go + dimension-two polarization theorem + Hodge-line recovery

**Date:** 2026-09-12

**Depends on:** [Dirichlet–Hodge selector](dirichlet-hodge-operator-selector.md), [determinant normalization selector](determinant-normalization-selector.md).

> **Claim policy.** Hodge-star/Dolbeault identities, automatic integrability in real dimension two, Serre duality and determinant of cohomology are established mathematics [NN57; Qui85; KM76]. The selector diagram and its no-go/pass decomposition are derived here as an FCIG assembly. No novelty certification is claimed.
>
> Citation audit: [oriented Dirichlet–Dolbeault audit](oriented-dirichlet-dolbeault-bridge-citation-audit.md).

---

## 0. Result in one page

The real Dirichlet selector gives

\[
(p,\mathcal E)\longmapsto(d+d^*),
\]

but not a Dolbeault operator. This is unavoidable: an unoriented two-dimensional energy is invariant under reflections, whereas every orthogonal complex structure chooses an orientation.

\[
\boxed{(p,\mathcal E)\not\longmapsto J}
\]

if naturality is demanded under all energy-preserving isomorphisms.

For a smooth connected surface, one extra bit of global data repairs the obstruction:

\[
\mathfrak o\in\{\text{two orientations}\}.
\]

The metric encoded by the carré du champ and \(\mathfrak o\) define the Hodge star on one-forms,

\[
*_{\mathfrak o}^{\,2}=-1,
\]

and hence

\[
\boxed{
\bar\partial_{\mathfrak o}f
=\frac12(df-i*_{\mathfrak o}df).
}
\tag{0.1}
\]

In real dimension two the associated almost-complex structure is automatically integrable. Therefore

\[
\boxed{
(p,\mathcal E,\mathfrak o)
\longmapsto
(X,J_{\mathfrak o})
\longmapsto
D_{\bar\partial}
}
\tag{0.2}
\]

is an exact smooth-surface bridge.

For a proper oriented family of compact surfaces whose conformal structures vary holomorphically,

\[
\lambda_{\bar\partial}
=\det R\pi_*\mathcal O_{\mathcal X}
\cong
\det\pi_*K_{\mathcal X/B}
\tag{0.3}
\]

by fiberwise Serre duality and the constant section \(1\). Thus the full Dolbeault complex restores the Hodge line discarded by the exact-one-form truncation.

\[
\boxed{
\text{orientation selects complex chirality;}
\quad
\text{cohomology makes its family topology visible.}
}
\]

---

## 1. Why a real energy does not choose \(J\)

Let \((M,g)\) be a connected Riemannian surface with normalized volume probability

\[
p=\frac{d{\rm vol}_g}{{\rm vol}_g(M)}
\]

and Dirichlet form

\[
\mathcal E_g(f)
=\int_M|df|_g^2\,dp.
\tag{1.1}
\]

An orthogonal almost-complex structure is a smooth bundle map

\[
J:TM\to TM,\qquad J^2=-1,\qquad g(Ju,Jv)=g(u,v).
\tag{1.2}
\]

It determines an orientation by declaring \((v,Jv)\) positive.

### Theorem 1.1 — reflection obstruction

There is no rule assigning an orthogonal \(J_g\) to every unoriented Riemannian probability surface such that

\[
T_*J_g=J_{g'}
\tag{1.3}
\]

for every measure- and energy-preserving isometry

\[
T:(M,g,p)\to(M',g',p').
\]

#### Proof

Apply the rule to the round sphere. On a connected Riemannian surface there are exactly two smooth orthogonal complex structures, \(J_+\) and \(J_-=-J_+\), corresponding to its two orientations. Let \(r:S^2\to S^2\) be an orientation-reversing isometry. It preserves \(p\) and \(\mathcal E_g\), but

\[
r_*J_+=J_-,
\qquad
r_*J_-=J_+.
\tag{1.4}
\]

Neither choice is fixed by \(r\), contradicting (1.3). \(\square\)

This is the two-dimensional counterpart of the probability-only symmetry obstruction:

\[
\boxed{
\text{an invariant quadratic energy knows angles but not handedness.}
}
\tag{1.5}
\]

The theorem concerns a natural smooth orthogonal selector. It does not say that an individual surface admits no complex structure.

---

## 2. Orientation supplies the missing polarization

Fix an orientation \(\mathfrak o\). It defines the area form \({\rm vol}_{g,\mathfrak o}\) and the Hodge star by

\[
\alpha\wedge *_\mathfrak o\beta
=\langle\alpha,\beta\rangle_g\,{\rm vol}_{g,\mathfrak o}.
\tag{2.1}
\]

On one-forms in dimension two,

\[
*_\mathfrak o^2=-1.
\tag{2.2}
\]

Equivalently there is a unique compatible tangent complex structure satisfying

\[
g(J_\mathfrak o u,v)
={\rm vol}_{g,\mathfrak o}(u,v).
\tag{2.3}
\]

Reversing orientation changes the sign:

\[
*_{-\mathfrak o}=-*_\mathfrak o,
\qquad
J_{-\mathfrak o}=-J_\mathfrak o.
\tag{2.4}
\]

### Theorem 2.1 — oriented surface selector

The assignment

\[
\boxed{
(M,g,p,\mathcal E_g,\mathfrak o)
\longmapsto J_\mathfrak o
}
\tag{2.5}
\]

is unique and natural under orientation-preserving isometries.

#### Proof

In every oriented orthonormal frame \((e_1,e_2)\), compatibility forces

\[
J_\mathfrak o e_1=e_2,\qquad
J_\mathfrak o e_2=-e_1.
\]

This proves existence and uniqueness pointwise. The defining equation (2.3) is preserved by every orientation-preserving isometry, proving naturality. \(\square\)

Only the conformal class matters: in two dimensions the star on one-forms is unchanged by

\[
g\longmapsto e^{2u}g.
\tag{2.6}
\]

Thus the selector is naturally conformal rather than tied to a particular scale.

---

## 3. Dolbeault splitting

Complexify the cotangent bundle. Since \(*^2=-1\), its eigenbundles give

\[
T^*M\otimes\mathbb C
=\Lambda^{1,0}\oplus\Lambda^{0,1}.
\tag{3.1}
\]

With the convention

\[
*\alpha=-i\alpha\quad(\alpha\in\Lambda^{1,0}),
\qquad
*\beta=+i\beta\quad(\beta\in\Lambda^{0,1}),
\tag{3.2}
\]

the projectors are

\[
\Pi^{1,0}=\frac12(1+i*),
\qquad
\Pi^{0,1}=\frac12(1-i*).
\tag{3.3}
\]

Hence on functions,

\[
\boxed{
\partial_J=\frac12(d+i*d),
\qquad
\bar\partial_J=\frac12(d-i*d).
}
\tag{3.4}
\]

### Theorem 3.1 — automatic integrability in dimension two

The almost-complex structure \(J_\mathfrak o\) on a smooth surface is integrable. Consequently

\[
\bar\partial_J^2=0
\tag{3.5}
\]

on the full Dolbeault complex.

#### Proof

The Nijenhuis tensor has complex type obstruction in \(\Lambda^{0,2}\otimes T^{1,0}\). In complex dimension one,

\[
\Lambda^{0,2}=0,
\]

so the obstruction vanishes identically. Equivalently, local isothermal coordinates provide complex charts. This is the dimension-one specialization of the Newlander–Nirenberg criterion [NN57]. \(\square\)

This automatic step is special to surfaces. In real dimension \(2n\ge4\), an orthogonal \(J\) is additional tensor data and \(N_J=0\) is a genuine differential condition.

---

## 4. Energy and Laplacian identities

Orthogonality of the type splitting gives

\[
\|df\|^2
=\|\partial_Jf\|^2+\|\bar\partial_Jf\|^2.
\tag{4.1}
\]

For real \(f\), complex conjugation exchanges the two terms:

\[
\|\partial_Jf\|^2=\|\bar\partial_Jf\|^2
=\frac12\|df\|^2.
\tag{4.2}
\]

On a Riemann surface, the Kähler identity on functions becomes

\[
\boxed{
\Delta_d
=2\Delta_{\bar\partial}
=2\bar\partial^*\bar\partial
}
\tag{4.3}
\]

for the stated positive-Laplacian convention.

Therefore the real Markov generator and the scalar Dolbeault Laplacian contain the same local second-order information:

\[
\boxed{A=2\bar\partial^*\bar\partial}
\tag{4.4}
\]

when \(A\) is the Laplace–Beltrami generator defined by the Dirichlet energy.

What changes is not the scalar spectrum but the complex and cohomological organization of its first-order square root.

---

## 5. The exact-sector truncation and what it forgot

The previous Dirichlet–Hodge selector used

\[
\mathcal H_{\rm ex}=\overline{\operatorname{ran}d}
\]

and consequently

\[
\ker d^*|_{\mathcal H_{\rm ex}}=0.
\]

That was deliberate: it constructed an operator from scalar energy without importing extra cohomology. Its determinant line was therefore

\[
\det H^0(M;\mathbb C)\cong\mathbb C.
\]

After orientation and integrable polarization are supplied, the full Dolbeault operator

\[
\bar\partial:\Omega^{0,0}(M)\to\Omega^{0,1}(M)
\tag{5.1}
\]

has

\[
\ker\bar\partial=H^0(M,\mathcal O),
\qquad
\operatorname{coker}\bar\partial=H^{0,1}(M).
\tag{5.2}
\]

For a compact connected genus-\(g\) surface,

\[
\dim H^0(M,\mathcal O)=1,
\qquad
\dim H^{0,1}(M)=g.
\tag{5.3}
\]

Thus

\[
\operatorname{ind}\bar\partial=1-g.
\tag{5.4}
\]

### Slogan

\[
\boxed{
\text{the real exact complex sees gradients;}
\quad
\text{the Dolbeault complex also remembers global holes.}
}
\tag{5.5}
\]

---

## 6. Family theorem: recovery of the Hodge line

Let

\[
\pi:\mathcal X\to B
\]

be a proper holomorphic submersion whose fibers are compact connected Riemann surfaces. The determinant of cohomology of the trivial holomorphic line is

\[
\lambda(\mathcal O)
=\det R\pi_*\mathcal O
=\det R^0\pi_*\mathcal O
\otimes
(\det R^1\pi_*\mathcal O)^{-1}.
\tag{6.1}
\]

The constant section \(1\) canonically trivializes

\[
R^0\pi_*\mathcal O\cong\mathcal O_B.
\tag{6.2}
\]

Relative Serre duality gives

\[
R^1\pi_*\mathcal O
\cong
(\pi_*K_{\mathcal X/B})^\vee.
\tag{6.3}
\]

### Theorem 6.1 — scalar Dolbeault/Hodge-line identification

There is a canonical holomorphic isomorphism

\[
\boxed{
\lambda(\mathcal O)
\cong
\det\pi_*K_{\mathcal X/B}.
}
\tag{6.4}
\]

#### Proof

Substitute (6.2) and (6.3) into (6.1):

\[
\lambda(\mathcal O)
\cong
\mathcal O_B\otimes
\det\!\left((\pi_*K)^\vee\right)^{-1}
\cong
\det\pi_*K.
\]

\(\square\)

Equipped with Quillen metric and connection, this is precisely a determinant-line input for the normalization selector. Unlike the exact scalar line, the Hodge line can have nonzero Chern class over moduli.

---

## 7. The completed selector ladder in dimension two

For smooth surface models arising from metric Dirichlet forms, the chain is now

\[
\boxed{
\begin{array}{ccccc}
(p,\mathcal E)
&\xrightarrow{\ +\mathfrak o\ }&
(J,\partial,\bar\partial)
&\xrightarrow{\ \det R\pi_*\ }&
(\lambda_H,h_Q,\nabla^Q)
\\
\downarrow&&\downarrow&&\downarrow\\
\text{reversible diffusion}
&&\text{Riemann-surface calculus}
&&\text{normalization curvature/holonomy}.
\end{array}
}
\tag{7.1}
\]

The corresponding functor is defined on the enriched category whose morphisms preserve probability, energy and orientation. It cannot descend to the unoriented category by Theorem 1.1.

This sharpens the prior reconstruction hierarchy:

\[
\boxed{
\begin{array}{c|c}
\text{input}&\text{selected structure}\\ \hline
p&\text{normalization only}\\
(p,\mathcal E)&\text{real first-order operator}\\
(p,\mathcal E,\mathfrak o),\ \dim_{\mathbb R}=2
&\text{integrable complex polarization}\\
\text{holomorphic family}&\text{Hodge determinant line}
\end{array}
}
\tag{7.2}
\]

---

## 8. Scope boundary for singular Dirichlet spaces

The smooth two-dimensional theorem must not be silently extended to arbitrary Dirichlet spaces. A measurable cotangent module may have a rank function rather than a rank-two vector bundle. Even if rank two holds almost everywhere and an operator

\[
\mathcal J:\mathcal H_1\to\mathcal H_1,
\qquad
\mathcal J^2=-1,
\qquad
\mathcal J^*\mathcal J=1
\tag{8.1}
\]

is supplied, the first-order Cipriani–Sauvageot calculus alone does not automatically provide:

- a canonical exterior algebra free of junk forms;
- a second differential with \(d^2=0\);
- a Nijenhuis tensor;
- holomorphic coordinate charts;
- a coherent analytic sheaf.

Thus

\[
\bar\partial_{\mathcal J}
=\frac12(1-i\mathcal J)\partial
\tag{8.2}
\]

is a valid projected first derivative, but the notation

\[
\bar\partial_{\mathcal J}^{\,2}=0
\]

requires an extended differential graded calculus and cannot be inferred from the first-order module alone.

This is the remaining singular-space wall.

---

## 9. Relation to Fisher geometry

Orientation changes the organization of the sample-space differential calculus, not the definition of Fisher information on parameter space. Hence the bridge does not by itself prove

\[
g^F
=\partial\bar\partial\log\|\cdot\|_Q^2.
\tag{9.1}
\]

In the hyperbolic FCIG family, the BLS/KE transport theorem supplies the additional coupling between moving fibers, position probabilities and the direct-image connection. That is why the Hermitianized Bergman-DPP Fisher/Weil–Petersson result can hold there without becoming a universal Dirichlet-form identity.

---

## 10. Gate ledger

- **ODD-A — PASS:** no natural orthogonal \(J\) exists on all unoriented probability-energy surfaces.
- **ODD-B — PASS:** an orientation uniquely selects \(J\) and the Hodge star in real dimension two.
- **ODD-C — PASS:** the selected \(J\) is automatically integrable.
- **ODD-D — PASS:** \(d\) splits into \(\partial_J+\bar\partial_J\), with \(\Delta_d=2\Delta_{\bar\partial}\) on functions.
- **ODD-E — PASS:** the full scalar Dolbeault family recovers the Hodge determinant line.
- **ODD-F — PASS:** the determinant/Quillen normalization selector now receives a nontrivial family line without an externally chosen coefficient bundle.
- **ODD-G — NO-GO:** forgetting orientation destroys the natural complex selector.
- **ODD-H — OPEN:** formulate orientation and integrability intrinsically on singular rank-two Dirichlet modules.
- **ODD-I — OPEN:** prove a reconstruction theorem selecting the orientation from statistical or physical axioms rather than supplying it.
- **ODD-J — OPEN:** determine whether level structure or anomaly cancellation can select between \(\mathfrak o\) and \(-\mathfrak o\).

\[
\boxed{
\text{Diffusion determines conformal energy;}
\quad
\text{orientation turns conformal energy into complex analysis.}
}
\]

**Update:** [antisymmetric-response-chirality-selector.md](antisymmetric-response-chirality-selector.md) proves that pure gradient inference cannot select \(\mathfrak o\), while a nowhere-zero antisymmetric response two-form on a Fisher surface does. Integral response curvature selects a Chern class, but not the residual flat holonomy.

---

## References

- [NN57] A. Newlander and L. Nirenberg, “Complex Analytic Coordinates in Almost Complex Manifolds,” *Annals of Mathematics* 65 (1957), 391–404.
- [KM76] F. Knudsen and D. Mumford, “The Projectivity of the Moduli Space of Stable Curves. I,” *Mathematica Scandinavica* 39 (1976), 19–55.
- [Qui85] D. Quillen, “Determinants of Cauchy–Riemann Operators over a Riemann Surface,” *Functional Analysis and Its Applications* 19 (1985), 31–34, DOI 10.1007/BF01086021.
- [CS03] F. Cipriani and J.-L. Sauvageot, “Derivations as Square Roots of Dirichlet Forms,” *Journal of Functional Analysis* 201 (2003), 78–120.

Machine-readable entries are in oriented-dirichlet-dolbeault-bridge.bib.
