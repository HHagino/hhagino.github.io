# FCIG: Grassmannian Quantum Information and the 50–50 Kodaira–Spencer Law

**Status:** worked theorem / normalization note  
**Date:** 2026-09-10  
**Scope:** compact hyperbolic curve families, Kodaira–Spencer source energy, minimal-solution/second-fundamental-form energy, Grassmannian/Slater quantum geometry, and the relation to classical Fisher information.  
**Depends on:** [`fisher-bergman-quillen.md`](fisher-bergman-quillen.md), [`kodaira-spencer-information.md`](kodaira-spencer-information.md), [`hyperbolic-model.md`](hyperbolic-model.md).

> **Claim policy.** **Established** means a cited theorem or standard construction. **Derived here** means a deduction made below from those inputs in the stated convention; it is not a literature-novelty claim. **FCIG interpretation** is project terminology. **Open** is not promoted to a theorem.
>
> Dedicated bibliography: [`grassmannian-quantum-information.bib`](grassmannian-quantum-information.bib). Citation audit: [`grassmannian-quantum-information-citation-audit.md`](grassmannian-quantum-information-citation-audit.md).

---

## 0. Result in one page

Let

\[
\pi:\mathcal X\to B
\]

be a smooth holomorphic family of compact genus-\(g\ge2\) Riemann surfaces, with the fiberwise hyperbolic Kähler–Einstein metric. Let

\[
E_q=\pi_*K_{\mathcal X/B}^{q},\qquad q\ge2,
\]

and put

\[
r:=q-1.
\]

For a tangent vector \(\xi\in T_bB\), let \(\mu_\xi\) be its harmonic Kodaira–Spencer representative. For an \(L^2\)-orthonormal basis \(u_1,\dots,u_{N_q}\) of \(H^0(X_b,K_{X_b}^q)\), define the Kodaira–Spencer source

\[
\eta_{a,\xi}:=-\mu_\xi\cdot u_a.
\tag{0.1}
\]

Let \(\chi_{a,\xi}\) be the \(L^2\)-minimal solution of

\[
\bar\partial\chi_{a,\xi}
=-\nabla'\eta_{a,\xi}.
\tag{0.2}
\]

Define three Hermitian tensors:

\[
\boxed{
\mathfrak A_q(\xi,\bar\eta)
:=
\sum_a\langle\eta_{a,\xi},\eta_{a,\eta}\rangle,
}
\tag{0.3}
\]

\[
\boxed{
\mathfrak B_q(\xi,\bar\eta)
:=
\sum_a\langle\chi_{a,\xi},\chi_{a,\eta}\rangle,
}
\tag{0.4}
\]

and

\[
\boxed{
\mathfrak R_q
:=
\mathfrak A_q-\mathfrak B_q.
}
\tag{0.5}
\]

Fedosova–Rowlett–Zhang, specializing the Berndtsson/Schumacher curvature formula to Teichmüller space, prove for each state the exact identity

\[
\|\eta\|^2-\|\chi\|^2
=
\frac{q-1}{2}
\left\langle
\left(\square''+\frac{q-1}{2}\right)^{-1}\eta,
\eta
\right\rangle,
\tag{0.6}
\]

with an explicitly noted equivalent Wan–Zhang normalization [FRZ20]. After tracing, this yields the exact source decomposition

\[
\boxed{
\mathfrak A_q
=
\mathfrak B_q+
\mathfrak R_q.
}
\tag{0.7}
\]

The previous FCIG note computed the resolvent side, in the Wan–Zhang normalization,

\[
\mathfrak R_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\tag{0.8}
\]

On the other hand the Bergman trace gives

\[
\mathfrak A_q
=
\int_{X_b}
\langle\mu_\xi,\mu_\eta\rangle B_q\,dA
=
\frac{q-1}{2\pi}G_{\rm WP}+O(1).
\tag{0.9}
\]

Therefore

\[
\boxed{
\mathfrak B_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{0.10}
\]

Hence the high-power Kodaira–Spencer source splits equally, to leading order:

\[
\boxed{
\frac{\mathfrak B_q}{\mathfrak A_q}\to\frac12,
\qquad
\frac{\mathfrak R_q}{\mathfrak A_q}\to\frac12
}
\tag{0.11}
\]

on every nonzero diagonal direction. We call this the **50–50 Kodaira–Spencer law**.

There is a second, information-geometric interpretation. In the minimal-solution/Chern gauge, \(\mathfrak B_q\) is the squared normal motion of the \(N_q\)-plane \(H^0(X_b,K^q)\) in the ambient Hilbert space of smooth \(q\)-differentials. Thus it is the Grassmannian/Plücker quantum metric of the normalized Slater ray:

\[
\boxed{
g^{\rm Gr}_q=\mathfrak B_q.}
\tag{0.12}
\]

Consequently

\[
\boxed{
\frac{4\pi}{q-1}g^{\rm Gr}_q
\longrightarrow G_{\rm WP}.
}
\tag{0.13}
\]

With the standard pure-state quantum Fisher convention \(I_Q=4g_{FS}\) [BC94],

\[
\boxed{
I_{Q,q}^{\rm Chern}
=
\frac{q-1}{\pi}G_{\rm WP}+O(1).
}
\tag{0.14}
\]

This is an **intrinsic-to-the-chosen Chern/minimal-solution connection quantum-information closure**. It does not identify the full Quillen curvature with quantum Fisher information.

Finally, a position measurement of the Slater state produces the Bergman DPP. For a real parameter direction, the classical Fisher information satisfies

\[
\boxed{
I_{\rm pos,q}
=
I_{Q,q}^{\rm Chern}
-4\operatorname{Var}_{P_q}(a_q),
}
\tag{0.15}
\]

where \(a_q\) is the centered phase score of the Chern-covariant Slater amplitude. Equivalently, in the quarter-Fisher convention

\[
\boxed{
g_{\rm pos,q}:=\frac14I_{\rm pos,q}
=
g^{\rm Gr}_q-\operatorname{Var}_{P_q}(a_q).
}
\tag{0.16}
\]

Thus the remaining classical Information Closure problem is no longer to compute an entire moving-fiber Fisher tensor from scratch. It is to estimate one positive defect:

\[
\boxed{
\operatorname{Var}_{P_q}(a_q).
}
\tag{0.17}
\]

If it is \(o(q)\), then the quarter-Fisher metric has the same Weil–Petersson leading limit as the Grassmannian metric. If it is order \(q\), classical position Fisher loses a finite fraction of the intrinsic quantum information.

---

# Part I. Exact source / second-fundamental / resolvent decomposition

## 1. Hyperbolic Teichmüller setup

Fix a fiber \(X=X_b\). We use the hyperbolic metric of Gaussian curvature \(-1\). Tangent vectors to Teichmüller space are represented by harmonic Beltrami differentials

\[
\mu\in A^{0,1}(X,T^{1,0}X),
\]

and the Hermitian Weil–Petersson pairing is

\[
G_{\rm WP}(\mu,\bar\nu)
=
\int_X\langle\mu,\nu\rangle\,dA.
\tag{1.1}
\]

For \(q\ge2\), let

\[
\mathcal H_q=H^0(X,K_X^q),
\qquad
N_q=(2q-1)(g-1).
\tag{1.2}
\]

Choose an \(L^2\)-orthonormal basis \(u_a\).

The Kodaira–Spencer action sends

\[
(\mu,u_a)
\longmapsto
\eta_{a,\mu}:=-\mu\cdot u_a,
\tag{1.3}
\]

an object of type \((q-1,1)\).

---

## 2. Established minimal-solution identity

Fedosova–Rowlett–Zhang recall the curvature formula for the bundle of holomorphic \(q\)-differentials over Teichmüller space. In their notation, if

\[
\eta=-\mu\cdot u,
\]

then the second term is obtained by taking the \(L^2\)-minimal solution \(\chi\) of

\[
\bar\partial\chi=-\nabla'\eta.
\tag{2.1}
\]

They derive

\[
\boxed{
\|\eta\|^2-\|\chi\|^2
=
\frac{q-1}{2}
\left\langle
\left(\square''+\frac{q-1}{2}\right)^{-1}\eta,
\eta
\right\rangle.
}
\tag{2.2}
\]

They also explain that the same geometric term appears in Wan–Zhang with the alternative normalization

\[
(q-1)
\langle(\Delta+q-1)^{-1}\eta,\eta\rangle.
\tag{2.3}
\]

**Established:** [FRZ20, Proposition 1 and its proof].

The distinction between (2.2) and (2.3) is a norm/Laplacian convention, not two different geometric terms.

---

## 3. Definition of the three response tensors

For base directions \(\xi,\eta\), define

\[
\mathfrak A_q(\xi,\bar\eta)
=
\sum_a
\langle\eta_{a,\xi},\eta_{a,\eta}\rangle,
\tag{3.1}
\]

\[
\mathfrak B_q(\xi,\bar\eta)
=
\sum_a
\langle\chi_{a,\xi},\chi_{a,\eta}\rangle,
\tag{3.2}
\]

and in the FRZ normalization

\[
\begin{aligned}
\mathfrak R_q(\xi,\bar\eta)
:=&\frac{q-1}{2}
\sum_a
\left\langle
\left(\square''+\frac{q-1}{2}\right)^{-1}
\eta_{a,\xi},
\eta_{a,\eta}
\right\rangle.
\end{aligned}
\tag{3.3}
\]

Each is basis-independent because it is a trace of an invariant Hermitian quadratic form on \(\mathcal H_q\).

### Proposition 3.1 — exact 50–50 precursor

\[
\boxed{
\mathfrak A_q
=
\mathfrak B_q+
\mathfrak R_q
}
\tag{3.4}
\]

exactly for every \(q\ge2\).

### Proof

Apply (2.2) to each basis vector and sum. The diagonal identity polarizes to the Hermitian bilinear identity. \(\square\)

**Derived here from the established statewise identity.**

### Positivity

On diagonal directions,

\[
\mathfrak A_q\ge0,
\qquad
\mathfrak B_q\ge0,
\qquad
\mathfrak R_q\ge0.
\]

Consequently

\[
0\le\mathfrak R_q\le\mathfrak A_q,
\qquad
0\le\mathfrak B_q\le\mathfrak A_q.
\tag{3.5}
\]

**FCIG slogan:**

\[
\boxed{
\text{KS source energy}
=
\text{normal-motion energy}
+
\text{positive curvature-response energy}.
}
\tag{3.6}
\]

---

# Part II. The 50–50 asymptotic law

## 4. The full KS source is a Bergman trace

Pointwise contraction gives

\[
\langle\eta_{a,\xi},\eta_{a,\eta}\rangle
=
\langle\mu_\xi,\mu_\eta\rangle |u_a|^2.
\]

Therefore

\[
\boxed{
\mathfrak A_q(\xi,\bar\eta)
=
\int_X
\langle\mu_\xi,\mu_\eta\rangle
B_q(x)\,dA(x),
}
\tag{4.1}
\]

where

\[
B_q(x)=\sum_a|u_a(x)|^2.
\]

For the hyperbolic canonical quantization, the curve Bergman expansion is

\[
B_q(x)
=
\frac{q-1}{2\pi}+rac1{4\pi}+O(q^{-1})
\tag{4.2}
\]

in the local asymptotic normalization used by the preceding FCIG notes. On thick compact subsets the nonlocal geodesic sector is exponentially small in \(q\); see [`hyperbolic-model.md`](hyperbolic-model.md) and its sources.

Hence

\[
\boxed{
\mathfrak A_q
=
\frac{q-1}{2\pi}G_{\rm WP}+O(1).
}
\tag{4.3}
\]

**Derived here from the Bergman trace.**

---

## 5. The resolvent half

The previous note [`kodaira-spencer-information.md`](kodaira-spencer-information.md), using the Wan–Zhang high-power curvature expansion and the explicit identification of the FRZ/WZ norm convention, gives the intrinsic KS resolvent channel

\[
\boxed{
\mathfrak R_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{5.1}
\]

The coefficient is not fitted: the resolvent channel contributes the spectral factor \(1/2\), while the leading Bergman state density contributes \((q-1)/(2\pi)\).

---

## 6. Theorem 6.1 — 50–50 Kodaira–Spencer law

From (3.4), (4.3), and (5.1),

\[
\boxed{
\mathfrak B_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{6.1}
\]

Therefore, for every nonzero tangent direction \(\xi\),

\[
\boxed{
\frac{\mathfrak B_q(\xi,\bar\xi)}
{\mathfrak A_q(\xi,\bar\xi)}
\longrightarrow\frac12,
\qquad
\frac{\mathfrak R_q(\xi,\bar\xi)}
{\mathfrak A_q(\xi,\bar\xi)}
\longrightarrow\frac12.
}
\tag{6.2}
\]

Equivalently,

\[
\boxed{
\frac{4\pi}{q-1}\mathfrak B_q
\to G_{\rm WP},
\qquad
\frac{4\pi}{q-1}\mathfrak R_q
\to G_{\rm WP}.
}
\tag{6.3}
\]

### Proof

Equation (3.4) is exact. Subtract (5.1) from (4.3):

\[
\mathfrak B_q
=
\left(\frac{1}{2\pi}-\frac{1}{4\pi}\right)
(q-1)G_{\rm WP}+O(1)
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\]

The ratios follow because \(G_{\rm WP}(\xi,\bar\xi)>0\) for nonzero Teichmüller tangent vectors. \(\square\)

**Status:** **Derived here** from [FRZ20] plus the high-power KS/Bergman asymptotics already audited in the preceding FCIG notes. It is not a claim that an equivalent asymptotic splitting has never been stated elsewhere.

**Slogan:**

\[
\boxed{
\text{at high quantization power, half of the KS source survives as curvature response,}
\\
\text{and half is spent on normal motion of the holomorphic state space.}
}
\tag{6.4}
\]

---

# Part III. The normal-motion half is Grassmannian quantum geometry

## 7. Abstract Hilbert-subbundle lemma

Let \(\mathscr H\to B\) be a Hermitian Hilbert bundle equipped with a unitary connection \(\nabla^{\mathscr H}\), and let

\[
E\subset\mathscr H
\]

be a rank-\(N\) Hermitian subbundle. Let \(P\) be the orthogonal projector onto \(E\), \(Q=1-P\), and define the second fundamental form

\[
\mathbb B_\xi
:=
Q\nabla^{\mathscr H}_\xi|_E.
\tag{7.1}
\]

Choose an orthonormal frame \(u_1,\dots,u_N\) at a point and use a gauge with vanishing tangential connection coefficients there. The normalized Slater/Plücker state is

\[
\Psi_E=u_1\wedge\cdots\wedge u_N.
\tag{7.2}
\]

Differentiation gives

\[
\nabla_\xi\Psi_E
=
\sum_{a=1}^N
u_1\wedge\cdots\wedge(\mathbb B_\xi u_a)\wedge\cdots\wedge u_N.
\tag{7.3}
\]

The summands are mutually orthogonal. Hence the Fubini–Study/Grassmannian Hermitian metric pulled back by the Plücker map is

\[
\boxed{
g^{\rm Gr}(\xi,\bar\eta)
=
\operatorname{Tr}_E
(\mathbb B_\eta^*\mathbb B_\xi).
}
\tag{7.4}
\]

Equivalently, in a fixed ambient Hilbert space,

\[
g^{\rm Gr}
=\frac12\operatorname{Tr}(dP\,dP)
\tag{7.5}
\]

up to the conventional placement of complex/real factors.

The identification of normalized Slater determinants with a Plücker image of a Grassmannian is standard; see [AS20]. Equation (7.4) is the elementary differential calculation included here.

---

## 8. Minimal-solution gauge for the hyperbolic family

A family of spaces \(H^0(X_b,K_{X_b}^q)\) is not literally a family of subspaces of one canonically fixed Hilbert space without a comparison rule. This is the same typing issue found for classical moving-fiber Fisher information.

However, locally on Teichmüller space the hyperbolic metric and the Chern connection provide a natural smooth Hilbert-bundle realization. Differentiating the holomorphicity equation produces the inhomogeneous \(\bar\partial\) equation (2.1). The orthogonal/minimal solution is exactly the normal correction selected in the Berndtsson–Schumacher calculation [Bern09; FRZ20].

Accordingly, define the **Chern/minimal-solution Grassmannian metric** by

\[
\boxed{
g^{\rm Gr,C}_q(\xi,\bar\eta)
:=
\sum_a
\langle\chi_{a,\xi},\chi_{a,\eta}\rangle
=
\mathfrak B_q(\xi,\bar\eta).
}
\tag{8.1}
\]

This is not a claim that arbitrary parameter-dependent Hilbert trivializations give the same projector derivative. The connection is part of the definition.

### Theorem 8.1 — Grassmannian/WP closure

\[
\boxed{
 g^{\rm Gr,C}_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1),
\qquad
\frac{4\pi}{q-1}g^{\rm Gr,C}_q
\to G_{\rm WP}.
}
\tag{8.2}
\]

This is simply Theorem 6.1 interpreted through (8.1).

There is precedent for finite-dimensional quantized metrics converging to Weil–Petersson geometry: Keller–Lukic construct a sequence of finite-dimensional Kähler metrics on polarized Calabi–Yau moduli and prove convergence to WP [KL15]. Their setting and metric are not identical to the hyperbolic-curve construction here, so [KL15] is supporting precedent, not a proof of (8.2).

---

# Part IV. Quantum Fisher and the factor-of-four firewall

## 9. Pure-state quantum Fisher convention

For a normalized pure state \(|\Psi_b\rangle\), define the Fubini–Study metric

\[
g_{FS}(\xi,\bar\eta)
=
\langle D_\xi\Psi,D_\eta\Psi\rangle
-
\langle D_\xi\Psi,\Psi\rangle
\langle\Psi,D_\eta\Psi\rangle,
\tag{9.1}
\]

with the appropriate real part on real tangent vectors.

In the standard Braunstein–Caves normalization, the pure-state quantum Fisher information is

\[
\boxed{I_Q=4g_{FS}.}
\tag{9.2}
\]

[BC94].

Therefore for the Chern-covariant Slater ray,

\[
\boxed{
I_{Q,q}^{\rm C}
=4g_q^{\rm Gr,C}
=
\frac{q-1}{\pi}G_{\rm WP}+O(1).
}
\tag{9.3}
\]

### Normalization firewall

The earlier FCIG notes used the classical statistical convention

\[
I_{\rm cl}=\mathbb E[(\partial\log p)^2]
\]

without a factor \(1/4\). Therefore **one must not numerically compare** \(I_{\rm cl}\), \(g_{FS}\), and \(\mathfrak K_q\) as if they used the same normalization.

The geometrically aligned objects are

\[
\boxed{
\frac14 I_{\rm cl},
\qquad
g_{FS},
\qquad
g^{\rm Gr,C},
\qquad
\mathfrak R_q,
}
\tag{9.4}
\]

not raw \(I_{\rm cl}\) and \(g_{FS}\).

This corrects a factor-of-four ambiguity in the earlier formulation of Gate FI-H.

---

# Part V. Classical Bergman-DPP Fisher as a measurement of the Slater ray

## 10. Exact classical/quantum decomposition

Fix a real tangent direction and a unitary/Chern transport of the ambient Hilbert bundle. In the position representation of the normalized Slater state, write locally off the nodal set

\[
\Psi_b(\mathbf x)
=
\sqrt{p_b(\mathbf x)}e^{i\theta_b(\mathbf x)}.
\tag{10.1}
\]

The probability density \(p_b=|\Psi_b|^2\) is exactly the normalized Bergman DPP density.

Choose the projective gauge in which the mean phase derivative has been removed, and define the centered phase score

\[
a_\xi(\mathbf x)
:=
D_\xi\theta_b(\mathbf x)
-
\mathbb E_p[D_\xi\theta_b].
\tag{10.2}
\]

The logarithmic probability score is

\[
s_\xi= D_\xi\log p_b.
\tag{10.3}
\]

A direct calculation gives

\[
\left(D_\xi-\langle\Psi,D_\xi\Psi\rangle\right)\Psi
=
\Psi\left(\frac12s_\xi+i a_\xi\right).
\tag{10.4}
\]

Taking the squared norm,

\[
g_{FS}(\xi,\xi)
=
\frac14\mathbb E_p[s_\xi^2]
+
\mathbb E_p[a_\xi^2].
\tag{10.5}
\]

Thus

\[
\boxed{
I_Q(\xi,\xi)
=
I_{\rm pos}(\xi,\xi)
+4\operatorname{Var}_p(a_\xi).
}
\tag{10.6}
\]

For bilinear real directions the last term is the phase-score covariance.

**Derived here from the standard pure-state/Fubini–Study formula.** This is also the familiar statement that a chosen measurement can access at most the quantum Fisher information [BC94].

Equivalently define the **quarter-Fisher geometric metric**

\[
\boxed{
g^{\rm pos}:=\frac14I_{\rm pos}.}
\tag{10.7}
\]

Then

\[
\boxed{
g^{\rm pos}
=
g_{FS}-\operatorname{Cov}(a,a).
}
\tag{10.8}
\]

The defect is positive semidefinite.

---

## 11. The remaining classical closure is one phase-variance estimate

In the Chern/minimal-solution gauge, Theorem 8.1 gives

\[
g_{FS,q}^{\rm C}
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\tag{11.1}
\]

Therefore

\[
\boxed{
\frac14I_{\rm pos,q}^{\rm C}
=
\frac{q-1}{4\pi}G_{\rm WP}
-
\operatorname{Cov}_{P_q}(a_q,a_q)
+O(1).
}
\tag{11.2}
\]

This is a much sharper research target than the earlier phrase “compute the whole moving-fiber Fisher metric.”

### Corollary 11.1 — exact criterion for leading classical closure

If, on compact subsets of Teichmüller space,

\[
\boxed{
\operatorname{Cov}_{P_q}(a_{q,\xi},a_{q,\eta})=o(q)
}
\tag{11.3}
\]

for fixed tangent directions, then

\[
\boxed{
\frac{\pi}{q-1}I_{\rm pos,q}^{\rm C}
\longrightarrow
G_{\rm WP}.
}
\tag{11.4}
\]

Equivalently,

\[
\frac{4\pi}{q-1}g_{\rm pos,q}^{\rm C}
\to G_{\rm WP}.
\tag{11.5}
\]

### Proof

Multiply (11.2) by \(4\pi/(q-1)\), use (11.3), and recall \(I_{\rm pos}=4g_{\rm pos}\). \(\square\)

**Open:** whether (11.3) actually holds for the KE/Chern position measurement.

If instead

\[
\operatorname{Var}(a_{q,\xi})
\sim c_\xi q,
\]

then position Fisher retains only a strict fraction of the intrinsic quantum information at leading order.

Thus the classical question is falsifiable.

---

# Part VI. What this says about Fisher–Bergman–Quillen closure

## 12. A more accurate triangle

The previous triangle should now be refined into two levels.

### Intrinsic/covariant level

\[
\boxed{
\begin{array}{ccc}
\text{KS source }\mathfrak A_q
&=&
\text{normal/Grassmannian }\mathfrak B_q
+
\text{resolvent }\mathfrak R_q
\\[2mm]
&&\searrow\qquad\swarrow
\\[-1mm]
&&G_{\rm WP}
\end{array}}
\tag{12.1}
\]

with

\[
\mathfrak B_q\sim\mathfrak R_q
\sim\frac12\mathfrak A_q.
\]

This level is highly promising and is already controlled at leading order.

### Classical-measurement level

\[
\boxed{
\frac14I_{\rm DPP}
=
\mathfrak B_q
-
\text{phase-information defect}
}
\tag{12.2}
\]

in the Chern-covariant Slater realization.

Therefore the position DPP is not automatically an information-complete measurement of the moving Slater ray.

---

## 13. Relation to Quillen curvature

The result here concerns the **Kodaira–Spencer subchannel** of direct-image geometry. It must not be confused with the total determinant curvature.

For \(H^0(K^q)\) over Teichmüller space, Fedosova–Rowlett–Zhang obtain

\[
\operatorname{Chern}^{(q)}(\mu,\mu)
=
\frac{6q(q-1)+1}{12\pi}
\|\mu\|_{\rm WP}^2
+O(q^2e^{-q\ell_0}),
\tag{13.1}
\]

and relate this to the Quillen curvature [FRZ20]. The total curvature is order \(q^2\), whereas

\[
\mathfrak R_q,
\mathfrak B_q
=O(q).
\]

So

\[
\boxed{
\text{quantum Fisher/Grassmannian KS response}
\neq
\text{full Quillen curvature}.
}
\tag{13.2}
\]

The full determinant response also contains the larger horizontal/geodesic-curvature channel.

This scale separation is useful:

\[
\boxed{
O(q^2):\text{ total determinant/Quillen response},
\qquad
O(q):\text{ KS normal + resolvent information response}.
}
\tag{13.3}
\]

Hence FCIG should speak of a **filtered Fisher–Bergman–Quillen correspondence**, not an equality of the full tensors.

---

# Part VII. Assessment and next theorem

## 14. Is this promising?

Yes, with an important qualification.

The strongest route is no longer

\[
\text{arbitrary classical Fisher}\stackrel?=\text{WP}.
\]

That route is obstructed by transport gauge and measurement phase.

The promising route is

\[
\boxed{
\text{KS deformation}
\to
\text{minimal-solution/Grassmannian quantum metric}
\to
\text{WP},
}
\tag{14.1}
\]

because:

1. the source/normal/resolvent decomposition is exact;
2. the leading coefficient of the resolvent channel is already fixed;
3. the Bergman trace fixes the total source coefficient;
4. subtraction forces the same WP coefficient for the normal/Grassmannian channel;
5. the remaining classical problem is a single nonnegative phase covariance.

A structurally related quantization-to-WP convergence is known in polarized Calabi–Yau moduli [KL15], which makes the strategy plausible beyond the particular curve calculation, though it is not evidence for a universal coefficient.

---

## 15. Next theorem target: phase-information defect

The next calculation should determine the asymptotic order of

\[
\boxed{
\mathfrak P_q(\xi,\bar\eta)
:=
\operatorname{Cov}_{P_q}(a_{q,\xi},a_{q,\eta}).
}
\tag{15.1}
\]

There are three outcomes:

### A. Saturation

\[
\mathfrak P_q=o(q).
\]

Then the Bergman position DPP asymptotically saturates the quantum Fisher bound and

\[
\frac{\pi}{q-1}I_{\rm DPP,q}^{\rm C}
\to G_{\rm WP}.
\]

### B. Partial information loss

\[
q^{-1}\mathfrak P_q\to P_\infty\neq0.
\]

Then

\[
\frac{4\pi}{q-1}g_{\rm DPP,q}^{\rm C}
\to
G_{\rm WP}-4\pi P_\infty.
\]

The defect itself becomes a new moduli tensor.

### C. Position measurement is the wrong observable

If the phase defect is as large as the full Grassmannian metric in some directions, then classical position Fisher discards the leading KS quantum information. FCIG should use the Chern-covariant Grassmannian metric rather than insist on a classical position Fisher interpretation.

All three outcomes are mathematically meaningful.

---

# 16. Publication-level obligations

Before calling the quantum statement a standalone novel theorem, the following must be completed:

- [ ] literature search for an equivalent asymptotic of the second-fundamental/Plücker metric of \(H^0(K^q)\) over Teichmüller space;
- [ ] write the ambient smooth-Hilbert-bundle/Chern connection construction globally on a marked Teichmüller family;
- [ ] prove that the FRZ minimal solution is exactly the normal component of that chosen covariant derivative with all signs/norms fixed;
- [ ] crosswalk the FRZ and Wan–Zhang Laplacian/norm conventions line by line;
- [ ] audit the factor \(4\) between classical Fisher, Fubini–Study metric, and quantum Fisher;
- [ ] determine the phase-score covariance asymptotics;
- [ ] only then state whether the **classical** Fisher–WP edge closes.

The 50–50 asymptotic itself is retained as **Derived here**, not asserted as literature-new.

---

# 17. Reference map

- **Berndtsson direct-image curvature / second fundamental mechanism:** [Bern09].
- **Exact minimal-solution decomposition and Teichmüller curvature asymptotics:** [FRZ20].
- **High-power direct-image / KS resolvent normalization:** [WZ21].
- **Slater determinants as a Grassmannian/Plücker manifold:** [AS20].
- **Pure-state quantum Fisher / optimal statistical distinguishability:** [BC94].
- **Finite-dimensional quantization metrics converging to WP in polarized Calabi–Yau moduli:** [KL15].
- **DPP information geometry context:** [HY24].

No reference is used to claim that the complete FCIG chain is already a named theorem.
