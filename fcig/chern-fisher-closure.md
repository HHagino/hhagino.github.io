# FCIG: Chern–Fisher Closure on a Statistical Hilbert Bundle

**Status:** exact abstract identity + connection-model application  
**Date:** 2026-09-10  
**Depends on:** [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md), [`kodaira-spencer-information.md`](kodaira-spencer-information.md).

> **Terminology warning.** “Chern–Fisher” is an **FCIG definition**, not a standard name for classical Fisher information. It retains complex amplitude/phase data together with a chosen Hermitian connection, so it is a projective-Hilbert / quantum-information tensor. Ordinary Fisher information of the Bergman position process is a measurement of this richer object.

---

## 1. Motivation: a moving sample space needs a connection

For a fixed probability space the ordinary score is

\[
S_\xi=\partial_\xi\log p_b.
\]

For moving fibers, [`kodaira-spencer-information.md`](kodaira-spencer-information.md) proves that changing the local fiber transport by an infinitesimal vertical field \(V_\xi\) changes the pulled-back classical score by

\[
S_\xi\mapsto S_\xi+\operatorname{div}_{P}V_\xi.
\]

Thus raw moving-fiber classical Fisher information is not intrinsic before a transport is chosen.

A holomorphic quantization family carries more data: a Hermitian Hilbert bundle and a connection. The natural covariant operation is therefore to differentiate the **state** and remove the component tangent to its complex ray.

---

# Part I. Exact projective identity

## 2. Hermitian Hilbert bundle and projective derivative

Let

\[
(\mathscr H,h,\nabla)\longrightarrow B
\]

be a Hermitian Hilbert bundle with unitary connection. Let \(\Psi_b\in\mathscr H_b\setminus\{0\}\) be a smooth state family and set

\[
\widehat\Psi_b=\frac{\Psi_b}{\|\Psi_b\|}.
\]

Let

\[
Q_\Psi=1-|\widehat\Psi\rangle\langle\widehat\Psi|
\]

be the orthogonal projector normal to the state ray. Define

\[
D_\xi^\perp\widehat\Psi
:=Q_\Psi\nabla_\xi\widehat\Psi.
\tag{2.1}
\]

The connection-dependent projective Hermitian metric is

\[
\boxed{
 g_{\rm proj}^{\nabla}(\xi,\bar\eta)
 =
 \left\langle
 D_\xi^\perp\widehat\Psi,
 D_\eta^\perp\widehat\Psi
 \right\rangle .
}
\tag{2.2}
\]

For a constant Hilbert bundle with its trivial connection this is the usual pullback of the Fubini–Study metric.

---

## 3. FCIG projective Chern score

Suppose locally the Hilbert norm is represented on a configuration space by a unitary realization. Away from the nodal set of \(\widehat\Psi\), define

\[
\boxed{
\mathscr S_\xi^{\nabla}(y)
:=
\frac{(D_\xi^\perp\widehat\Psi)(y)}{\widehat\Psi(y)}.
}
\tag{3.1}
\]

At the same parameter value let

\[
dP_\Psi(y)=|\widehat\Psi(y)|^2d\nu(y).
\]

Define the **Chern–Fisher Hermitian tensor**

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

The ratio in (3.1) is only local. The quadratic expression is nevertheless well-defined across the nodal set in the \(L^2\) sense because the factor \(|\widehat\Psi|^2\) cancels the denominator.

### Theorem 3.1 — exact Chern–Fisher/Fubini–Study identity

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}
=
g_{\rm proj}^{\nabla}.
}
\tag{3.3}
\]

### Proof

Directly,

\[
\begin{aligned}
\mathcal I_{\rm CF}^{\nabla}(\xi,\bar\eta)
&=
\int
\frac{D_\xi^\perp\widehat\Psi}{\widehat\Psi}
\frac{\overline{D_\eta^\perp\widehat\Psi}}{\overline{\widehat\Psi}}
|\widehat\Psi|^2d\nu
\\
&=
\int
(D_\xi^\perp\widehat\Psi)
\overline{(D_\eta^\perp\widehat\Psi)}d\nu
\\
&=
g_{\rm proj}^{\nabla}(\xi,\bar\eta).
\end{aligned}
\]

\(\square\)

**Derived here.** This is an elementary identity. Its role is to state exactly which Fisher-like quantity is covariant once a Hermitian connection is part of the data.

A unitary change of Hilbert-bundle frame transforms state and connection together and leaves (3.3) invariant. A local phase change of \(\widehat\Psi\) changes only the ray direction removed by \(Q_\Psi\).

**Slogan:**

\[
\boxed{
\text{differentiate amplitudes covariantly, then quotient the ray.}
}
\]

---

# Part II. Moving subspaces and Slater states

## 4. Abstract Grassmannian lemma

Let \(E\subset\mathscr H\) be a rank-\(N\) Hermitian subbundle. Write \(P_E\) for the orthogonal projector onto \(E\), \(Q_E=1-P_E\), and define the second fundamental form relative to \(\nabla\) by

\[
\boxed{
\mathbb B_\xi:=Q_E\nabla_\xi|_E.
}
\tag{4.1}
\]

Choose an orthonormal frame \(u_1,\ldots,u_N\) at a point and form the normalized Slater/Plücker ray

\[
\Psi_E=u_1\wedge\cdots\wedge u_N.
\]

In a gauge whose tangential connection matrix vanishes at the point,

\[
D_\xi^\perp\Psi_E
=
\sum_{a=1}^{N}
 u_1\wedge\cdots\wedge(\mathbb B_\xi u_a)\wedge\cdots\wedge u_N.
\]

The summands are mutually orthogonal. Therefore

\[
\boxed{
 g_{\rm Gr}^{\nabla}(\xi,\bar\eta)
 =
 \operatorname{Tr}_E(\mathbb B_\eta^*\mathbb B_\xi).
}
\tag{4.2}
\]

By Theorem 3.1,

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}
=
g_{\rm Gr}^{\nabla}
}
\tag{4.3}
\]

for the Slater ray.

**Established background / derived formula.** Slater determinant rays are Plücker points in a Grassmannian; see [AS20] in the companion bibliography. Equation (4.2) is the standard second-fundamental-form calculation written explicitly here.

---

# Part III. Hyperbolic \(q\)-differentials

## 5. Minimal-solution connection model

Let

\[
E_q=\pi_*K_{\mathcal X/B}^{q}
\]

over a smooth hyperbolic Teichmüller family. For a harmonic Kodaira–Spencer tensor \(\mu_\xi\) and \(u_a\in H^0(X_b,K_{X_b}^q)\), set

\[
\eta_{a,\xi}=-\mu_\xi\cdot u_a.
\]

Fedosova–Rowlett–Zhang use the \(L^2\)-minimal solution \(\chi_{a,\xi}\) of

\[
\boxed{
\bar\partial\chi_{a,\xi}
=-\nabla'\eta_{a,\xi}
}
\tag{5.1}
\]

in the direct-image curvature formula [FRZ20]. Berndtsson's Hilbert-subbundle discussion identifies the negative second-fundamental contribution with a minimal \(\bar\partial\)-solution [Bern09].

We therefore make the following **connection-model definition**:

\[
\boxed{
\mathbb B_\xi u_a:=\chi_{a,\xi}.
}
\tag{5.2}
\]

This should not be read as a proof that every natural global trivialization of the moving \(L^2\) spaces produces (5.2). Global construction and naturality of the ambient connection remain publication-level obligations.

With (5.2),

\[
\boxed{
\mathcal I_{{\rm CF},q}^{\rm min}
=
\sum_a
\langle\chi_{a,\xi},\chi_{a,\eta}\rangle
=:
\mathfrak B_q(\xi,\bar\eta).
}
\tag{5.3}
\]

---

## 6. The 50–50 input

The companion note [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md) starts from the exact Fedosova–Rowlett–Zhang statewise identity and defines

\[
\mathfrak A_q
=
\mathfrak B_q+
\mathfrak R_q,
\tag{6.1}
\]

where \(\mathfrak A_q\) is the total Kodaira–Spencer source energy and \(\mathfrak R_q\) is the positive Berndtsson resolvent response.

In the convention crosswalk adopted there,

\[
\mathfrak A_q
=
\frac{q-1}{2\pi}G_{\rm WP}+O(1),
\tag{6.2}
\]

and

\[
\mathfrak R_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\tag{6.3}
\]

Thus

\[
\boxed{
\mathfrak B_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{6.4}
\]

The equality of the two leading halves is called the **50–50 Kodaira–Spencer law** in this project. It remains labelled **Derived here**, with a dedicated normalization and prior-art audit.

---

## 7. Theorem 7.1 — covariant information/WP closure in the model

Combining (5.3) and (6.4),

\[
\boxed{
\mathcal I_{{\rm CF},q}^{\rm min}
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{7.1}
\]

Hence

\[
\boxed{
\frac{4\pi}{q-1}
\mathcal I_{{\rm CF},q}^{\rm min}
\longrightarrow
G_{\rm WP}.
}
\tag{7.2}
\]

**Status:** Theorem 3.1 is exact for any connection-equipped Hilbert bundle. Equation (7.2) is its application inside the explicitly chosen minimal-solution connection model, using the separately audited 50–50 asymptotic. It is not a claim that “Chern–Fisher” is a standard theorem name or that the global connection problem has been solved.

With the Braunstein–Caves real pure-state convention

\[
I_Q=4g_{FS},
\]

one may equivalently write

\[
\boxed{
I_{Q,q}^{\rm min}
=
\frac{q-1}{\pi}G_{\rm WP}+O(1).
}
\tag{7.3}
\]

---

# Part IV. Ordinary classical Fisher is a measurement of the covariant state

## 8. Amplitude/phase decomposition

For a real parameter direction, in a position representation transported by the same connection write

\[
\widehat\Psi=\sqrt p\,e^{i\theta}.
\]

Let

\[
s_\xi=D_\xi\log p
\]

be the classical probability score and let

\[
a_\xi
=D_\xi\theta-\mathbb E_p[D_\xi\theta]
\]

be the centered phase score. In projective gauge,

\[
D_\xi^\perp\widehat\Psi
=
\widehat\Psi
\left(
\frac12s_\xi+i a_\xi
\right).
\]

Therefore

\[
\boxed{
 g_{FS}(\xi,\xi)
 =
 \frac14 I_{\rm pos}(\xi,\xi)
 +
 \operatorname{Var}_p(a_\xi).
}
\tag{8.1}
\]

or, with \(I_Q=4g_{FS}\),

\[
\boxed{
 I_Q
 =
 I_{\rm pos}
 +4\operatorname{Var}_p(a).
}
\tag{8.2}
\]

This is the pure-state measurement decomposition in the present convention; Braunstein–Caves [BC94] gives the standard operational quantum-information background.

Thus the geometrically aligned **quarter-Fisher** metric is

\[
\boxed{
\frac14 I_{\rm pos}
=
\mathcal I_{\rm CF}^{\nabla}
-
\operatorname{Var}(a)
}
\tag{8.3}
\]

when both sides use the same connection.

The distinction is now sharp:

\[
\boxed{
\begin{array}{c}
\text{Chern--Fisher: amplitude + phase + connection},\\
\text{classical DPP Fisher: probability of one chosen measurement}.
\end{array}
}
\tag{8.4}
\]

---

## 9. Exact criterion for classical leading closure

For the hyperbolic minimal-solution model, (7.1) and (8.3) give

\[
\boxed{
\frac14I_{{\rm pos},q}^{\rm min}
=
\frac{q-1}{4\pi}G_{\rm WP}
-
\operatorname{Cov}_{P_q}(a_q,a_q)
+O(1).
}
\tag{9.1}
\]

Therefore, if

\[
\boxed{
\operatorname{Cov}_{P_q}(a_{q,\xi},a_{q,\eta})=o(q)
}
\tag{9.2}
\]

on compact subsets for fixed tangent directions, then

\[
\boxed{
\frac{\pi}{q-1}
I_{{\rm pos},q}^{\rm min}
\longrightarrow G_{\rm WP}.
}
\tag{9.3}
\]

**Open:** (9.2) is not proved. If the phase covariance is of order \(q\), a finite fraction of the projective quantum information is invisible to the position DPP measurement.

This is now the smallest unresolved classical-Fisher problem in the chain.

---

# Part V. Fixed-measure holomorphic consistency check

## 10. Proposition 10.1 — complex Fisher equals Fubini–Study in the holomorphic fixed-measure model

Let

\[
B\ni z\longmapsto F_z\in L^2(Y,\nu)
\]

be a holomorphic nonzero Hilbert-space-valued map over a **fixed** measure space. Put

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
\tag{10.1}
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
\tag{10.2}
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

The expectation of the first term is \(\partial_\alpha\log Z\), while its Hermitian second moment is \(\langle\partial_\beta F,\partial_\alpha F\rangle/Z\). Subtracting the mean product gives the standard Fubini–Study formula, which is also \(\partial\bar\partial\log Z\). \(\square\)

**Derived here.** This proposition is a consistency check for the Fisher–Bergman theme. The moving hyperbolic family is harder precisely because its \(L^2\) measure and complex type decomposition vary; the connection is the additional datum needed for a covariant formulation.

---

# 11. Relation to Quillen: filtered, not equal

For the hyperbolic \(H^0(K^q)\) family, the full direct-image/Quillen curvature has leading order \(q^2\), while

\[
\mathfrak B_q,
\mathfrak R_q
=O(q).
\]

Thus

\[
\boxed{
\text{Chern--Fisher / Grassmannian KS response}
\neq
\text{full Quillen curvature}.
}
\tag{11.1}
\]

The correct research language is a **filtered Fisher–Bergman–Quillen correspondence**: the \(O(q)\) Kodaira–Spencer information channel is a subleading component inside a determinant geometry whose total response is \(O(q^2)\).

The companion audit records the relevant FRZ, Berndtsson, Wan–Zhang, Takhtajan–Teo, and Braunstein–Caves prior art.

---

# 12. What is solved, and what remains

### Exact

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}
=
g_{\rm proj}^{\nabla}
}
\]

for any connection-equipped state family, and

\[
\boxed{
\mathcal I_{\rm CF}^{\nabla}
=
\operatorname{Tr}(\mathbb B^*\mathbb B)
}
\]

for its Slater/Grassmannian realization.

### Derived in the hyperbolic minimal-solution model

\[
\boxed{
\frac{4\pi}{q-1}
\mathcal I_{{\rm CF},q}^{\rm min}
\to G_{\rm WP}.
}
\]

### Still open

1. global construction and naturality/uniqueness of the ambient minimal-solution Hilbert connection on the marked Teichmüller family;
2. line-by-line FRZ/Wan–Zhang normalization crosswalk for publication;
3. the phase-score covariance asymptotics (9.2);
4. comparison of the \(O(q)\) information channel with the \(O(q^2)\) Quillen expansion beyond leading scale separation;
5. a dedicated prior-art search before any standalone novelty claim.

The current mathematical slogan is therefore

\[
\boxed{
\textbf{local probability is a measurement; covariant amplitude is the geometric state.}
}
\]

and, conditionally on the specified minimal-solution connection model,

\[
\boxed{
\textbf{the normal quantum information of the moving holomorphic state space has Weil--Petersson as its semiclassical limit.}
}
\]

No Lorentzian or gravitational conclusion is asserted here.
