# FCIG: Antisymmetric Response Chirality Selector

**Status:** gradient no-go + exact two-dimensional response selector + integral-curvature/flat-ambiguity theorem

**Date:** 2026-09-12

**Depends on:** [oriented Dirichlet–Dolbeault bridge](oriented-dirichlet-dolbeault-bridge.md), [determinant normalization selector](determinant-normalization-selector.md).

> **Claim policy.** Two-dimensional compatible-complex linear algebra and the curvature integrality theorem are established. Geometric phases in stochastic pumps are established examples of parameter-space antisymmetric response [SN07; Sin09]. The FCIG selector and its gate decomposition are derived here; no universal identification of stochastic-pump curvature with Quillen curvature is claimed.
>
> Citation audit: [antisymmetric-response citation audit](antisymmetric-response-chirality-selector-citation-audit.md).

---

## 0. Result in one page

Let \(B\) be a connected real two-dimensional statistical parameter manifold with Fisher metric \(g^F\). A free-energy gradient flow

\[
v=-\nabla_{g^F}F
\tag{0.1}
\]

does not select an orientation:

\[
dF\wedge v^\flat=-dF\wedge dF=0.
\tag{0.2}
\]

Gradient descent supplies only one line field. Chirality requires an ordered two-dimensional area element.

Suppose instead that the statistical dynamics supplies a smooth nowhere-vanishing antisymmetric response

\[
\Omega\in\Omega^2(B).
\]

Define \(A\in\operatorname{End}(TB)\) by

\[
g^F(Au,v)=\Omega(u,v),
\tag{0.3}
\]

and

\[
\rho=\sqrt{-\frac12\operatorname{tr}(A^2)}>0.
\tag{0.4}
\]

Then

\[
\boxed{J_\Omega=\rho^{-1}A}
\tag{0.5}
\]

satisfies

\[
J_\Omega^2=-1,\qquad
g^F(J_\Omega u,J_\Omega v)=g^F(u,v).
\tag{0.6}
\]

It is the unique \(g^F\)-orthogonal complex structure whose orientation agrees with \(\Omega\). Since \(\dim_{\mathbb R}B=2\), it is automatically integrable.

If additionally

\[
\left[\frac{\Omega}{2\pi}\right]\in H^2(B;\mathbb Z),
\tag{0.7}
\]

there exists a Hermitian line bundle with unitary connection satisfying

\[
F_\nabla=-i\Omega,
\qquad
c_1(L)=\left[\frac{\Omega}{2\pi}\right].
\tag{0.8}
\]

But \(\Omega\) does not choose the flat holonomy: fixed-curvature solutions form a torsor under \(H^1(B;U(1))\).

\[
\boxed{
\text{circulation selects chirality and Chern class;}
\quad
\text{holonomy still requires phase data.}
}
\]

---

## 1. Gradient descent cannot orient a surface

The FCIG inference slogan begins with a gradient law such as

\[
\dot b=-\nabla_gF.
\tag{1.1}
\]

At a regular point, \(dF\) determines a one-dimensional normal direction to a level set. The metric converts it to the same direction as a vector:

\[
v^\flat=-dF.
\tag{1.2}
\]

### Proposition 1.1 — collinearity no-go

No orientation two-form can be constructed by alternating \(dF\) and the metric dual of its own gradient:

\[
\boxed{dF\wedge v^\flat=0.}
\tag{1.3}
\]

#### Proof

Substitution of (1.2) gives

\[
dF\wedge v^\flat=-dF\wedge dF=0.
\]

\(\square\)

More generally, every construction using only \(g\), \(F\), and tensor contractions remains invariant under an isometry preserving \(F\). If such a symmetry reverses orientation, it obstructs any natural chirality selector.

Entropy production

\[
-dF(v)=\|\nabla_gF\|^2\ge0
\tag{1.4}
\]

selects a direction of relaxation, but it is a scalar and does not select left versus right.

\[
\boxed{
\text{an arrow of relaxation is not an orientation of state space.}
}
\tag{1.5}
\]

---

## 2. Antisymmetric response is the missing datum

Let \((B,g)\) be a Riemannian surface and let \(\Omega\) be a nowhere-zero two-form. Define \(A=g^{-1}\Omega\) by (0.3). It is skew-adjoint:

\[
g(Au,v)=-g(u,Av).
\tag{2.1}
\]

### Lemma 2.1

In real dimension two,

\[
\boxed{A^2=-\rho^2\,1,}
\tag{2.2}
\]

where \(\rho\) is given by (0.4).

#### Proof

In a \(g\)-orthonormal frame,

\[
\Omega=\omega\,e^1\wedge e^2,
\qquad
A=
\begin{pmatrix}
0&-\omega\\
\omega&0
\end{pmatrix}.
\]

Hence \(A^2=-\omega^2 1\) and \(\rho=|\omega|\). \(\square\)

### Theorem 2.2 — response-to-chirality selector

The normalized endomorphism

\[
J_\Omega=A/\rho
\]

is the unique \(g\)-orthogonal complex structure satisfying

\[
\frac{\Omega(u,v)}{\rho}=g(J_\Omega u,v).
\tag{2.3}
\]

It is natural under diffeomorphisms preserving \(g\) and \(\Omega\).

#### Proof

Lemma 2.1 gives \(J_\Omega^2=-1\). Skew-adjointness and \(J_\Omega^2=-1\) imply orthogonality. Equation (2.3) fixes \(J_\Omega\) uniquely by nondegeneracy of \(g\). Pullback preserves the defining equation, proving naturality. \(\square\)

Changing the sign of response reverses chirality:

\[
J_{-\Omega}=-J_\Omega.
\tag{2.4}
\]

Changing only its magnitude does not:

\[
J_{f\Omega}=J_\Omega\qquad(f>0).
\tag{2.5}
\]

Thus orientation is the sign sector of antisymmetric response.

---

## 3. Integrability and Kähler form

Every two-form on a surface is closed:

\[
d\Omega=0,
\tag{3.1}
\]

because there are no three-forms. The normalized form

\[
\omega_J=\rho^{-1}\Omega
\tag{3.2}
\]

is the fundamental form of \((g,J_\Omega)\).

### Corollary 3.1

\((B,g,J_\Omega)\) is a Riemann surface and hence a Kähler manifold of complex dimension one.

#### Proof

The algebraic compatibility follows from Theorem 2.2. Integrability is automatic in real dimension two, as established in the oriented Dirichlet–Dolbeault note. The fundamental two-form is top-degree and therefore closed. \(\square\)

Notice the normalization distinction:

- \(J_\Omega\) depends only on the sign/orientation of \(\Omega\);
- the curvature and flux quantization below depend on its magnitude and periods.

---

## 4. Curvature integrality

### Theorem 4.1 — response prequantization

There exists a Hermitian line bundle \(L\to B\) with unitary connection \(\nabla\) and

\[
F_\nabla=-i\Omega
\tag{4.1}
\]

if and only if

\[
\boxed{
\left[\frac{\Omega}{2\pi}\right]
\in\operatorname{im}\bigl(H^2(B;\mathbb Z)\to H^2_{\rm dR}(B;\mathbb R)\bigr).
}
\tag{4.2}
\]

For every such pair,

\[
c_1(L)=\left[\frac{iF_\nabla}{2\pi}\right]
=\left[\frac{\Omega}{2\pi}\right].
\tag{4.3}
\]

This is the standard curvature integrality or prequantization theorem.

### Proposition 4.2 — residual flat ambiguity

If \((L,\nabla)\) and \((L',\nabla')\) have the same curvature \(-i\Omega\), their ratio is a flat unitary line. Consequently the set of fixed-curvature isomorphism classes, when nonempty, is a torsor under

\[
\boxed{H^1(B;U(1)).}
\tag{4.4}
\]

Thus \(\Omega\) selects the real Chern class and curvature, but not the differential character or all Wilson-loop phases.

---

## 5. Čech–de Rham form

Choose a good cover \(\{U_i\}\). Since \(d\Omega=0\), locally

\[
\Omega=dA_i.
\tag{5.1}
\]

On overlaps,

\[
A_j-A_i=d\chi_{ij},
\qquad
g_{ij}=e^{i\chi_{ij}}.
\tag{5.2}
\]

On triple overlaps,

\[
\chi_{ij}+\chi_{jk}+\chi_{ki}=2\pi n_{ijk},
\qquad n_{ijk}\in\mathbb Z.
\tag{5.3}
\]

The integers \(\{n_{ijk}\}\) represent \(c_1(L)\). Adding a flat cocycle changes \(g_{ij}\) without changing \(\Omega\).

This is the exact local/global hierarchy:

\[
\boxed{
\Omega
\Longrightarrow
\{A_i\}
\Longrightarrow
\{g_{ij}\}
\Longrightarrow
\{n_{ijk}\},
}
\tag{5.4}
\]

with the last two arrows requiring integral compatibility and retaining phase data beyond local curvature.

---

## 6. Statistical source candidates

For a parameter-dependent Markov generator, adiabatic transport of counting statistics can carry a geometric contribution represented locally by a connection and globally by a curvature two-form. Stochastic-pump geometric phases are established examples [SN07; Sin09].

This motivates, but does not prove, an FCIG realization

\[
\Omega_{\rm resp}
=d\mathcal A_{\rm resp}.
\tag{6.1}
\]

If \(\Omega_{\rm resp}\) is smooth and nowhere zero on a two-dimensional parameter region, Theorem 2.2 gives \(J_{\rm resp}\). If it also has integral periods, Theorem 4.1 gives a line with that curvature.

Three independent gates must not be conflated:

1. **nondegeneracy:** \(\Omega_{\rm resp}\neq0\), needed for chirality;
2. **integrality:** \([\Omega_{\rm resp}/2\pi]\) integral, needed for a line bundle;
3. **holonomy choice:** a differential character, needed to remove flat ambiguity.

A generic stochastic-pump curvature need satisfy neither nondegeneracy nor integrality. No equality with Quillen curvature is asserted without a model-specific comparison.

---

## 7. Two-vector alternative and its failure locus

Suppose instead that inference supplies two vector fields \(v,w\). Then

\[
\Omega_{v,w}
=v^\flat\wedge w^\flat
\tag{7.1}
\]

orients exactly the open set where

\[
\det_g(v,w)\neq0.
\tag{7.2}
\]

For pure gradient inference with \(w=\nabla F\) and \(v=-\nabla F\), this determinant vanishes identically. A transverse current

\[
j=j_{\rm grad}+j_{\rm circ},
\qquad
g(j_{\rm circ},\nabla F)=0
\tag{7.3}
\]

can provide the missing direction where both components are nonzero.

This gives the operational slogan:

\[
\boxed{
\text{dissipation fixes downhill;}
\quad
\text{circulation distinguishes clockwise from counterclockwise.}
}
\tag{7.4}
\]

---

## 8. Relation to the Hodge/Quillen selector

Let the statistical base \(B\) itself be the real two-dimensional space to be polarized. The current result gives

\[
(g^F,\Omega_{\rm resp})
\longmapsto
(J_{\rm resp},\omega_J).
\tag{8.1}
\]

The preceding oriented bridge then supplies the Dolbeault splitting. If the response curvature is integral, a prequantum line \(L_{\rm resp}\) exists and one may form

\[
D_{\bar\partial,L_{\rm resp}}
=\sqrt2\bigl(\bar\partial_{L_{\rm resp}}
+\bar\partial_{L_{\rm resp}}^*\bigr).
\tag{8.2}
\]

Its determinant line enters the established Quillen/Bismut–Freed selector.

The complete conditional chain is therefore

\[
\boxed{
(p_b,\text{dynamics})
\longrightarrow
(g^F,\Omega_{\rm resp})
\longrightarrow
(J,L,\nabla)
\longrightarrow
D_{\bar\partial,L}
\longrightarrow
(\lambda_Q,h_Q,\nabla^Q).
}
\tag{8.3}
\]

Only the middle algebraic arrows are closed here. The first and final curvature comparison remain model-dependent.

---

## 9. Gate ledger

- **ARC-A — PASS:** a single gradient flow cannot orient a two-dimensional parameter space.
- **ARC-B — PASS:** a nowhere-zero antisymmetric response and Fisher metric uniquely select a compatible \(J\).
- **ARC-C — PASS:** the selected \(J\) is automatically integrable in real dimension two.
- **ARC-D — PASS:** integral response curvature is exactly the existence condition for a Hermitian line with unitary connection.
- **ARC-E — NO-GO:** curvature does not determine flat holonomy; the ambiguity is \(H^1(B;U(1))\).
- **ARC-F — CONDITIONAL:** stochastic-pump curvature is a candidate \(\Omega_{\rm resp}\), not universally nondegenerate or integral.
- **ARC-G — OPEN:** compute \(\Omega_{\rm resp}\) for the concrete FCIG Bergman/BLS family.
- **ARC-H — OPEN:** compare its differential character with the Hodge/Quillen line, not only its de Rham curvature.
- **ARC-I — OPEN:** determine whether level structure fixes the residual flat character.

\[
\boxed{
\text{Gradient gives an arrow; curvature gives an orientation; differential cohomology gives the phase.}
}
\]

---

## References

- [SN07] N. A. Sinitsyn and I. Nemenman, “The Berry Phase and the Pump Flux in Stochastic Chemical Kinetics,” *Europhysics Letters* 77 (2007), 58001.
- [Sin09] N. A. Sinitsyn, “The Stochastic Pump Effect and Geometric Phases in Dissipative and Stochastic Systems,” *Journal of Physics A* 42 (2009), 193001.
- [Kos70] B. Kostant, “Quantization and Unitary Representations,” in *Lectures in Modern Analysis and Applications III*, Lecture Notes in Mathematics 170, Springer, 1970, 87–208.

Machine-readable entries are in antisymmetric-response-chirality-selector.bib.
