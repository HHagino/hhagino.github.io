# FCIG: Chern–Fisher Closure on a Statistical Hilbert Bundle

**Status:** exact abstract identity + application to the hyperbolic \(H^0(K^q)\) family  
**Date:** 2026-09-10  
**Depends on:** [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md), [`kodaira-spencer-information.md`](kodaira-spencer-information.md).

> **Terminology warning.** “Chern–Fisher” is an **FCIG definition**, not a standard replacement name for classical Fisher information. It retains complex amplitude/phase data and is therefore a projective-Hilbert/quantum information tensor. Ordinary Fisher information of the position DPP remains a measurement/coarse-graining of this object.

---

## 1. Why introduce a covariant score?

For a probability law \(p_b\) on a fixed sample space, the ordinary score

\[
S_\xi=\partial_\xi\log p_b
\]

is unambiguous. For a family of sample fibers, the preceding FCIG note proved that changing the fiber transport by a vertical vector field \(V_\xi\) changes the pulled-back score by

\[
S_\xi\mapsto S_\xi+\operatorname{div}_{P}V_\xi.
\]

Thus a raw moving-fiber classical Fisher tensor is not intrinsic.

A quantum/holomorphic family comes with more structure than a probability density: it comes with a Hermitian Hilbert bundle and a connection. Instead of differentiating only the norm square, we can differentiate the state covariantly and remove its projective gauge direction.

This produces an exact information metric.

---

# Part I. Abstract projective identity

## 2. Hermitian Hilbert bundle

Let

\[
(\mathscr H,h,\nabla)\to B
\]

be a Hermitian Hilbert bundle with unitary connection. Let \(\Psi_b\in\mathscr H_b\) be a smooth nonzero state family and write

\[
\widehat\Psi_b
=
\frac{\Psi_b}{\|\Psi_b\|}.
\]

Let

\[
Q_\Psi
=
1-|\widehat\Psi\rangle\langle\widehat\Psi|
\]

be the projector normal to the state ray.

Define the projective covariant derivative

\[
D_\xi^{\perp}\widehat\Psi
:=
Q_\Psi\nabla_\xi\widehat\Psi.
\tag{2.1}
\]

The associated projective Hermitian metric is

\[
\boxed{
g_{\rm proj}^{\nabla}(\xi,\bar\eta)
=
\left\langle
D_\xi^{\perp}\widehat\Psi,
D_\eta^{\perp}\widehat\Psi
\right\rangle.
}
\tag{2.2}
\]

For a fixed Hilbert space this is the ordinary Fubini–Study pullback. With a Hilbert-bundle connection it is its covariant analogue.

---

## 3. Projective Chern score

Suppose locally the Hilbert norm has a configuration-space realization. Away from the nodal set of \(\widehat\Psi\), define

\[
\boxed{
\mathscr S_\xi^{\nabla}(y)
:=
\frac{(D_\xi^{\perp}\widehat\Psi)(y)}
{\widehat\Psi(y)}.
}
\tag{3.1}
\]

Let

\[
dP_\Psi(y)=|\widehat\Psi(y)|^2d\nu(y)
\]

in a unitary local realization. Then define the **Chern–Fisher Hermitian tensor**

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}(\xi,\bar\eta)
:=
\mathbb E_{P_\Psi}
\left[
\mathscr S_\xi^{\nabla}
\overline{\mathscr S_\eta^{\nabla}}
\right].
}
\tag{3.2}
\]

The ratio in (3.1) is only a local expression; the expectation below extends through the nodal set because multiplication by \(|\widehat\Psi|^2\) cancels the denominator in the \(L^2\) identity.

---

## 4. Theorem 4.1 — exact Chern–Fisher/Fubini–Study identity

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}
=
g_{\rm proj}^{\nabla}.
}
\tag{4.1}
\]

### Proof

By definition,

\[
\begin{aligned}
\mathcal I_{\rm CF}^{\nabla}(\xi,\bar\eta)
&=
\int
\frac{D_\xi^{\perp}\widehat\Psi}{\widehat\Psi}
\frac{\overline{D_\eta^{\perp}\widehat\Psi}}
{\overline{\widehat\Psi}}
|\widehat\Psi|^2d\nu
\\
&=
\int
(D_\xi^{\perp}\widehat\Psi)
\overline{(D_\eta^{\perp}\widehat\Psi)}d\nu
\\
&=
\langle
D_\xi^{\perp}\widehat\Psi,
D_\eta^{\perp}\widehat\Psi
\rangle
\\
&=
g_{\rm proj}^{\nabla}(\xi,\bar\eta).
\end{aligned}
\]

\(\square\)

**Derived here.** The identity is elementary. Its purpose is to make explicit which “Fisher-like” object is genuinely connection-covariant.

### Gauge covariance

Under a unitary change of Hilbert-bundle frame, the connection and state transform together. The norm in (2.2) is unchanged. Under a local phase change

\[
\widehat\Psi\mapsto e^{i\vartheta(b)}\widehat\Psi,
\]

the projector \(Q_\Psi\) removes the vertical ray component. Hence \(\mathcal I_{\rm CF}^\nabla\) is projective-gauge invariant.

This is the precise sense in which the connection cures the arbitrary-transport problem: the connection is not discarded; it is part of the geometric datum.

---

# Part II. Slater/Grassmannian specialization

## 5. Moving \(N\)-plane

Let \(E\subset\mathscr H\) be a rank-\(N\) Hermitian subbundle. With \(P_E\) the orthogonal projector and \(Q_E=1-P_E\), define its second fundamental form relative to \(
abla\) by

\[
\mathbb B_\xi
=
Q_E\nabla_\xi|_E.
\tag{5.1}
\]

For an orthonormal frame \(u_1,\ldots,u_N\), form the normalized Slater ray

\[
\Psi_E=u_1\wedge\cdots\wedge u_N.
\]

The wedge derivative gives

\[
\boxed{
g_{\rm proj}^{\nabla}(\xi,\bar\eta)
=
\operatorname{Tr}_E
(\mathbb B_\eta^*\mathbb B_\xi).
}
\tag{5.2}
\]

Thus

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}
=
\operatorname{Tr}_E
(\mathbb B_\eta^*\mathbb B_\xi).
}
\tag{5.3}
\]

The Slater/Grassmannian interpretation of such rays is standard; see Aoto–da Silva [AS20] in the bibliography of the companion note.

---

# Part III. Hyperbolic \(q\)-differentials

## 6. Minimal-solution connection model

Take

\[
E_q=\pi_*K_{\mathcal X/B}^q
\]

over Teichmüller space. For a harmonic Kodaira–Spencer tensor \(\mu_\xi\) and \(u_a\in H^0(K^q)\), put

\[
\eta_{a,\xi}=-\mu_\xi\cdot u_a.
\]

Fedosova–Rowlett–Zhang use the \(L^2\)-minimal solution

\[
\bar\partial\chi_{a,\xi}
=-\nabla'\eta_{a,\xi}
\tag{6.1}
\]

in the direct-image curvature formula [FRZ20]. Berndtsson's Hilbert-subbundle discussion identifies the relevant negative curvature contribution with the norm of a minimal \(ar\partial\)-solution [Bern09].

Accordingly, in the local Hilbert realization whose normal covariant derivative is selected by (6.1),

\[
\mathbb B_\xi u_a=\chi_{a,\xi}.
\tag{6.2}
\]

Equation (6.2) is the **minimal-solution connection model**. Globalizing that ambient connection is a publication-level obligation; arbitrary other transports are not silently identified with it.

Then

\[
\boxed{
\mathcal I_{{\rm CF},q}^{\rm min}
=
\sum_a
\langle\chi_{a,\xi},\chi_{a,\eta}\rangle
=
\mathfrak B_q.
}
\tag{6.3}
\]

---

## 7. Theorem 7.1 — Chern–Fisher/Weil–Petersson high-power closure

The companion note proves

\[
\mathfrak B_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\]

Therefore, in the minimal-solution connection model,

\[
\boxed{
\mathcal I_{{\rm CF},q}^{\rm min}
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{7.1}
\]

and

\[
\boxed{
\frac{4\pi}{q-1}
\mathcal I_{{\rm CF},q}^{\rm min}
\longrightarrow
G_{\rm WP}.
}
\tag{7.2}
\]

**Status:** exact identity (4.1) + the derived 50–50 asymptotic from the companion note. This is **not** a claim that “Chern–Fisher” is a standard theorem name.

With the standard real pure-state quantum Fisher normalization,

\[
I_Q=4g_{FS},
\]

one instead writes

\[
I_{Q,q}^{\rm min}
=
\frac{q-1}{\pi}G_{\rm WP}+O(1).
\tag{7.3}
\]

---

# Part IV. Relation to ordinary classical Fisher

## 8. Classical position measurement forgets phase

The configuration-position measurement of the Slater state produces the Bergman DPP. For a real tangent direction, write the normalized state locally as

\[
\widehat\Psi=\sqrt p\,e^{i\theta}.
\]

The companion note derives

\[
\boxed{
I_Q
=
I_{\rm pos}
+4\operatorname{Var}(a),
}
\tag{8.1}
\]

where \(a\) is the centered phase score. Hence

\[
\boxed{
\frac14 I_{\rm pos}
=
\mathcal I_{\rm CF}^{\nabla}
-
\operatorname{Var}(a)
}
\tag{8.2}
\]

when the same connection is used.

Thus there is no contradiction between exact Chern–Fisher closure and the previous classical transport no-go:

\[
\boxed{
\text{Chern--Fisher keeps amplitude + phase + connection;}
\\
\text{classical DPP Fisher keeps only the probability measurement.}
}
\tag{8.3}
\]

Braunstein–Caves characterize the quantum statistical metric operationally through optimization over measurements [BC94]. Equation (8.1) is the explicit pure-state position-measurement decomposition in the present convention.

---

# Part V. A fixed-measure holomorphic model as a consistency check

## 9. Proposition 9.1 — holomorphic square-root Fisher identity

Let \(B\ni z\mapsto F_z\in L^2(Y,\nu)\) be a holomorphic nonzero Hilbert-space-valued map over a **fixed** measure space. Set

\[
Z(z)=\|F_z\|^2,
\qquad
p_z(y)=\frac{|F_z(y)|^2}{Z(z)}.
\]

Define the Hermitian complex Fisher block

\[
I_{\alpha\bar\beta}
=
\int_Y
(\partial_\alpha\log p_z)
(\partial_{\bar\beta}\log p_z)
p_zd\nu.
\tag{9.1}
\]

Then

\[
\boxed{
I_{\alpha\bar\beta}
=
\partial_\alpha\partial_{\bar\beta}\log Z
=
g_{FS,\alpha\bar\beta}.
}
\tag{9.2}
\]

### Proof

Holomorphicity gives

\[
\partial_\alpha\log p
=
\frac{\partial_\alpha F}{F}
-
\partial_\alpha\log Z.
\]

Moreover,

\[
\mathbb E_p\left[\frac{\partial_\alpha F}{F}\right]
=
\frac{\langle F,\partial_\alpha F\rangle}{Z}
=
\partial_\alpha\log Z,
\]

and

\[
\mathbb E_p
\left[
\frac{\partial_\alpha F}{F}
\overline{\frac{\partial_\beta F}{F}}
\right]
=
\frac{\langle\partial_\beta F,\partial_\alpha F\rangle}{Z}.
\]

Subtracting the mean term gives exactly the Fubini–Study expression, which is also \(\partial\bar\partial\log Z\). \(\square\)

**Derived here.** This is a useful normalization check, closely analogous to the Fisher–Bergman identities discussed in the main FCIG information note.

### Why the moving hyperbolic case is harder

In the hyperbolic family, the \(L^2\) weight, volume form, and type decomposition move. A marking alone does not turn the problem into the fixed-measure hypothesis of Proposition 9.1. The Chern/minimal-solution connection is precisely the extra geometric datum needed to formulate a covariant analogue without pretending that the measure is fixed.

---

# 10. What has and has not been solved

### Closed in the connection-equipped model

\[
\boxed{
\text{projective Chern score covariance}
=
\text{Fubini--Study/Grassmannian metric}
}
\]

exactly, and for the hyperbolic \(H^0(K^q)\) minimal-solution model,

\[
\boxed{
\frac{4\pi}{q-1}\mathcal I_{{\rm CF},q}^{\rm min}
\to G_{\rm WP}.
}
\]

### Still open

1. global construction and uniqueness/naturality of the ambient minimal-solution Hilbert connection on the marked family;
2. comparison of that connection with a concrete Kähler–Einstein/Chern horizontal transport on configuration space;
3. asymptotics of the classical phase-information defect;
4. relation of the \(O(q)\) Chern–Fisher/KS sector to the \(O(q^2)\) full Quillen determinant curvature beyond the already known direct-image decomposition.

---

# 11. FCIG interpretation

The information-geometric moral is not that a probability manifold must be globally dually flat. It is that a **bundle of statistical state spaces may carry a connection, and information response should then be differentiated covariantly**.

The resulting slogan is

\[
\boxed{
\textbf{local probability is a measurement; covariant amplitude is the geometric state.}
}
\]

and, in the hyperbolic high-power model,

\[
\boxed{
\textbf{the normal quantum information of the moving holomorphic state space converges to Weil--Petersson geometry.}
}
\]

This is the currently most promising mathematical version of FCIG Information Closure. It remains entirely on the Kähler/Teichmüller side; no Lorentzian gravity statement is activated.
