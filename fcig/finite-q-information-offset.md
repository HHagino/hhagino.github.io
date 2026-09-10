# FCIG: Finite-q Information Offset on Hyperbolic Moduli

**Status:** derived finite-\(q\) asymptotic refinement  
**Date:** 2026-09-10  
**Scope:** hyperbolic curve families, Bergman source trace, Berndtsson/FRZ resolvent channel, Grassmannian/Slater information, Hermitian Born--Fisher information, and the first subleading Weil--Petersson coefficient.  
**Depends on:** [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md), [`kodaira-spencer-information.md`](kodaira-spencer-information.md), [`bls-position-transport.md`](bls-position-transport.md).

> **Claim policy.** **Established** means a cited theorem/formula. **Derived here** means an algebraic/asymptotic deduction made below from those inputs; it is not a novelty claim. **Interpretation** is project language. The notation \(\mathfrak K_q\) below is the same KS resolvent tensor denoted \(\mathfrak R_q\) in the earlier 50--50 note.
>
> Dedicated bibliography: [`finite-q-information-offset.bib`](finite-q-information-offset.bib). Citation audit: [`finite-q-information-offset-citation-audit.md`](finite-q-information-offset-citation-audit.md).

---

## 0. Result in one page

Let \(X\) be a compact hyperbolic Riemann surface of genus \(g\ge2\), let \(\mu\) be a harmonic Beltrami differential, and put

\[
\mathcal H_q=H^0(X,K_X^q),\qquad q\ge2.
\]

For an \(L^2\)-orthonormal basis \(\{u_j\}\), define the source trace

\[
\mathfrak A_q(\mu)
:=
\sum_j\|\mu\cdot u_j\|^2,
\tag{0.1}
\]

the minimal-solution/second-fundamental energy \(\mathfrak B_q\), and the positive Berndtsson--Fedosova--Rowlett--Zhang resolvent term \(\mathfrak K_q\). The exact decomposition from the companion note is

\[
\boxed{
\mathfrak A_q=\mathfrak B_q+\mathfrak K_q.
}
\tag{0.2}
\]

The previous FCIG result only used

\[
\mathfrak B_q
=
\mathfrak K_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1)
\]

at leading order. The constant term can be determined.

Wan--Zhang's Bergman expansion for \(K_X\otimes L^k\), specialized to complex dimension one with

\[
L=K_X,\qquad k=q-1,
\]

and hyperbolic scalar curvature \(\rho=-1\), gives

\[
\boxed{
B_q(x)
=
\frac{2q-1}{4\pi}+O(q^{-2}).
}
\tag{0.3}
\]

The potential \(q^{-1}\) term vanishes because their \(A_2\) coefficient vanishes on a constant-curvature complex curve. Hence

\[
\boxed{
\mathfrak A_q
=
\frac{2q-1}{4\pi}G_{\rm WP}+O(q^{-2}).
}
\tag{0.4}
\]

Fedosova--Rowlett--Zhang decompose the trace curvature as

\[
\operatorname{Chern}^{(q)}=I^{(q)}+II^{(q)},
\tag{0.5}
\]

where

\[
I^{(q)}
=(q-1)\int_X f(\mu)B_q\,dA,
\qquad
f(\mu)=(1+\square_0)^{-1}|\mu|^2,
\tag{0.6}
\]

and \(II^{(q)}=\mathfrak K_q\) in the present norm convention. Since

\[
\int_X f(\mu)dA
=
\int_X|\mu|^2dA
=G_{\rm WP}(\mu,\mu),
\tag{0.7}
\]

we get

\[
I^{(q)}
=
\frac{(q-1)(2q-1)}{4\pi}G_{\rm WP}
+O(q^{-1}).
\tag{0.8}
\]

FRZ also prove

\[
\boxed{
\operatorname{Chern}^{(q)}
=
\frac{6q(q-1)+1}{12\pi}G_{\rm WP}
+O(q^2e^{-q\ell_0}),
}
\tag{0.9}
\]

where \(\ell_0\) is the shortest closed hyperbolic geodesic length of the fixed surface. Therefore

\[
\boxed{
\mathfrak K_q
=
\frac{3q-2}{12\pi}G_{\rm WP}
+O(q^{-1}),
}
\tag{0.10}
\]

and the exact source decomposition gives

\[
\boxed{
\mathfrak B_q
=
\frac{3q-1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{0.11}
\]

Hence

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
=
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{0.12}
\]

In the KE/BLS position-transport realization,

\[
I_{\rm HBF,q}^{KE}=\mathfrak B_q,
\]

so equivalently

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{0.13}
\]

Thus the two information channels not only have the same normalized Weil--Petersson limit; their first finite-quantization separation is a definite WP-direction offset.

---

# Part I. Bergman source trace to one extra order

## 1. The adjoint-power indexing

Wan--Zhang write the Bergman expansion for

\[
H^0(X,L^k\otimes K_X),
\]

whereas our state space is

\[
H^0(X,K_X^q).
\]

Therefore

\[
\boxed{L=K_X,\qquad k=q-1.}
\tag{1.1}
\]

This shift is essential: missing it changes exactly the constant term being computed.

For the canonical-bundle coefficient metric Wan--Zhang give

\[
B_k
=\frac1{(2\pi)^n}
\left[
 k^n-\frac{\rho}{2}k^{n-1}
 +A_2k^{n-2}+\cdots
\right],
\tag{1.2}
\]

with

\[
A_2
=-\frac16\Delta''\rho
+\frac1{24}
\left(
|R|^2-4|\operatorname{Ric}|^2+3\rho^2
\right).
\tag{1.3}
\]

This is an established TYZ coefficient formula in their normalization [WZ21].

---

## 2. Hyperbolic cancellation of \(A_2\)

Set \(n=1\) and normalize the hyperbolic metric by

\[
\operatorname{Ric}(\omega)=-\omega,
\qquad \rho=-1.
\tag{2.1}
\]

Then

\[
\Delta''\rho=0.
\tag{2.2}
\]

In complex dimension one the Kähler curvature tensor is determined by its scalar contraction. In an orthonormal complex frame,

\[
|R|^2=|\operatorname{Ric}|^2=\rho^2,
\]

and hence

\[
|R|^2-4|\operatorname{Ric}|^2+3\rho^2=0.
\tag{2.3}
\]

Thus

\[
\boxed{A_2=0.}
\tag{2.4}
\]

Using the full Bergman expansion with \(R=3\) in the asymptotic estimate,

\[
\begin{aligned}
B_q(x)
&=\frac1{2\pi}
\left(k+\frac12+O(k^{-2})\right)\\
&=\frac{2q-1}{4\pi}+O(q^{-2}).
\end{aligned}
\tag{2.5}
\]

**Status:** **Derived here from [WZ21].** The vanishing of \(A_2\) is special to the constant-curvature curve specialization.

### Remark 2.1 — possible exponential strengthening

Berman proves exponentially small Bergman-kernel errors for canonical determinantal processes in constant-curvature Riemann-surface settings [Ber12]. This strongly suggests a sharper remainder after the exact normalization and family-uniformity crosswalk is completed. The theorem here deliberately keeps the conservative TYZ consequence \(O(q^{-2})\).

---

## 3. Source energy

By the Bergman trace identity,

\[
\begin{aligned}
\mathfrak A_q(\mu,\bar\nu)
&=\sum_j\langle\mu\cdot u_j,\nu\cdot u_j\rangle\\
&=\int_X\langle\mu,\nu\rangle B_q\,dA.
\end{aligned}
\tag{3.1}
\]

With

\[
G_{\rm WP}(\mu,\bar\nu)
:=\int_X\langle\mu,\nu\rangle dA,
\tag{3.2}
\]

we obtain by Hermitian polarization

\[
\boxed{
\mathfrak A_q
=
\frac{2q-1}{4\pi}G_{\rm WP}
+O(q^{-2}).
}
\tag{3.3}
\]

The remainder is safest as a fixed-surface/fixed-tangent-vector statement. Uniformity over moduli requires bounded geometry, for example restriction to thick compact subsets.

---

# Part II. Extracting the resolvent constant from FRZ

## 4. Exact curvature splitting

FRZ Proposition 1 gives, for \(q\ge2\),

\[
\operatorname{Chern}^{(q)}=I^{(q)}+II^{(q)},
\tag{4.1}
\]

where

\[
\boxed{
I^{(q)}
=(q-1)\int_X f(\mu)B_q\,dA,
}
\tag{4.2}
\]

and

\[
\boxed{
II^{(q)}
=\frac{q-1}{2}\sum_j
\left\langle
\left(\square''+\frac{q-1}{2}\right)^{-1}
(\mu\cdot u_j),
\mu\cdot u_j
\right\rangle.
}
\tag{4.3}
\]

Here

\[
f(\mu)=(1+\square_0)^{-1}|\mu|^2.
\tag{4.4}
\]

We identify

\[
\boxed{\mathfrak K_q:=II^{(q)}}
\tag{4.5}
\]

in the FRZ norm convention. This is the same channel denoted \(\mathfrak R_q\) in `grassmannian-quantum-information.md`.

---

## 5. Integral of the Schumacher potential

Equation (4.4) implies

\[
(1+\square_0)f=|\mu|^2.
\tag{5.1}
\]

On compact \(X\), the integrated Laplacian vanishes. Therefore

\[
\boxed{
\int_X f(\mu)dA
=
\int_X|\mu|^2dA
=G_{\rm WP}(\mu,\mu).
}
\tag{5.2}
\]

Substitute (2.5) into (4.2):

\[
\begin{aligned}
I^{(q)}
&=(q-1)
\left[
\frac{2q-1}{4\pi}G_{\rm WP}
+O(q^{-2})
\right]\\
&=\boxed{
\frac{(q-1)(2q-1)}{4\pi}G_{\rm WP}
+O(q^{-1}).
}
\end{aligned}
\tag{5.3}
\]

---

## 6. FRZ full Chern polynomial

FRZ prove on a fixed compact hyperbolic surface

\[
\boxed{
\operatorname{Chern}^{(q)}(\mu,\mu)
=
\frac{6q(q-1)+1}{12\pi}
G_{\rm WP}(\mu,\mu)
+O(q^2e^{-q\ell_0}).
}
\tag{6.1}
\]

This is an established theorem [FRZ20]. Subtract (5.3):

\[
\begin{aligned}
\mathfrak K_q
&=\operatorname{Chern}^{(q)}-I^{(q)}\\
&=
\left[
\frac{6q(q-1)+1}{12\pi}
-
\frac{(q-1)(2q-1)}{4\pi}
\right]G_{\rm WP}
+O(q^{-1})\\
&=\boxed{
\frac{3q-2}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\end{aligned}
\tag{6.2}
\]

---

# Part III. The finite-q 1/(12π) offset

## 7. Theorem — refined second-fundamental and resolvent channels

The exact source relation is

\[
\mathfrak B_q=\mathfrak A_q-\mathfrak K_q.
\tag{7.1}
\]

Using (3.3) and (6.2),

\[
\boxed{
\mathfrak B_q
=
\frac{3q-1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{7.2}
\]

Consequently

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
=
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{7.3}
\]

**Status:** **Derived here from [WZ21] + [FRZ20] + the exact source decomposition established in the companion note.** No claim is made that (7.3) is absent from all prior literature.

The source formulas are usually stated on diagonal directions. All quantities are Hermitian quadratic forms, so polarization gives

\[
\boxed{
\mathfrak B_q(\mu,\bar\nu)
-
\mathfrak K_q(\mu,\bar\nu)
=
\frac{1}{12\pi}G_{\rm WP}(\mu,\bar\nu)
+O(q^{-1})
}
\tag{7.4}
\]

for fixed tangent vectors.

---

## 8. Refined 50--50 law

On a nonzero diagonal direction,

\[
\boxed{
\frac{\mathfrak B_q}{\mathfrak A_q}
=
\frac12+\frac{1}{12q}+O(q^{-2}),
}
\tag{8.1}
\]

and

\[
\boxed{
\frac{\mathfrak K_q}{\mathfrak A_q}
=
\frac12-\frac{1}{12q}+O(q^{-2}).
}
\tag{8.2}
\]

Thus the 50--50 law is the semiclassical limit. At first finite order the second-fundamental/Grassmannian channel carries a small excess, while the resolvent channel carries the matching deficit.

Equivalently,

\[
\mathfrak B_q
=
\frac{q}{4\pi}G_{\rm WP}
-
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}),
\tag{8.3}
\]

whereas

\[
\mathfrak K_q
=
\frac{q}{4\pi}G_{\rm WP}
-
\frac{1}{6\pi}G_{\rm WP}
+O(q^{-1}).
\tag{8.4}
\]

---

# Part IV. Statistical meaning

## 9. BLS/KE Hermitian Born--Fisher consequence

The BLS position-transport note establishes, in the local KE/BLS covariant realization,

\[
\boxed{
I_{\rm HBF,q}^{KE}=g_{\rm Pl,q}^{KE}=\mathfrak B_q.
}
\tag{9.1}
\]

Therefore

\[
\boxed{
I_{\rm HBF,q}^{KE}
=
\frac{3q-1}{12\pi}G_{\rm WP}
+O(q^{-1}),
}
\tag{9.2}
\]

and

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{9.3}
\]

This replaces the previous stopping point

\[
I_{\rm HBF,q}^{KE}-\mathfrak K_q=O(1).
\]

The raw J-paired Fisher tensor is four times (9.2):

\[
\boxed{
I_q^{KE}+J^*I_q^{KE}
=
\frac{3q-1}{3\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{9.4}
\]

---

# Part V. Index/Bernoulli interpretation

## 10. Why 1/(12π) is suggestive

FRZ's coefficient is

\[
\frac{6q(q-1)+1}{12\pi}
=
\frac1{2\pi}
\left(q^2-q+\frac16\right).
\tag{10.1}
\]

The second Bernoulli number is

\[
B_2=\frac16,
\]

so its constant part is

\[
\frac{B_2}{2\pi}=\frac1{12\pi}.
\tag{10.2}
\]

The polynomial \(6q^2-6q+1\) is also the standard coefficient occurring in local-index/Quillen formulas for powers of the canonical bundle over moduli of curves [TZ87; FRZ20].

**Interpretation, not an additional theorem:** the finite Fisher--KS mismatch can therefore be viewed as an **index/Bernoulli offset** left after the leading semiclassical 50--50 split. The analytic proof of (7.3) is still the explicit subtraction above; no new topological derivation is asserted.

---

# Part VI. What this changes in FCIG

## 11. Two resolved asymptotic layers

The information closure now separates into

\[
\boxed{
\begin{array}{rcl}
O(q):&&
I_{\rm HBF,q}^{KE}
\sim\mathfrak K_q
\sim\dfrac{q}{4\pi}G_{\rm WP},\\[2mm]
O(1):&&
I_{\rm HBF,q}^{KE}-\mathfrak K_q
\sim\dfrac1{12\pi}G_{\rm WP}.
\end{array}}
\tag{11.1}
\]

The next analytic target has moved one order lower: determine the \(q^{-1}\) coefficient, or obtain a fully audited exponential improvement in the constant-curvature setting.

---

# 12. Remaining proof obligations

1. **Uniformity on moduli.** The displayed asymptotics are safest on a fixed surface or on thick compact subsets. Degenerating families require separate short-geodesic/cusp analysis.
2. **FRZ/BLS operator sign.** The metric-level identification \(I_{\rm HBF}=\mathfrak B_q\) is sign-insensitive, but a submission version should finish the local-coordinate sign crosswalk for the second fundamental form.
3. **WP/Quillen normalization.** All coefficients here use the repository's Hermitian WP convention. Conversion to first-Chern-form conventions must preserve the appropriate \(i\) and \(2\pi\) factors.
4. **Exponential improvement.** Berman's constant-curvature result suggests a sharper Bergman remainder; promote it only after matching normalization and the desired family-uniform statement.
5. **Novelty audit.** The coefficient follows naturally by combining known formulas. A broad MathSciNet/zbMATH/reference-chain search is required before any originality claim about the packaged identity.

---

# 13. Reference map

- **FRZ direct-image curvature splitting and complete hyperbolic curvature polynomial:** [FRZ20].
- **TYZ coefficient formula for \(K_X\otimes L^k\):** [WZ21], with background [Lu00; MM07].
- **Exponentially accurate constant-curvature Bergman asymptotics:** [Ber12].
- **Local-index coefficient \(6q^2-6q+1\) and Weil--Petersson/Quillen context:** [TZ87] and [FRZ20].
- **BLS/KE statistical identification \(I_{\rm HBF}=\mathfrak B_q\):** derived in the preceding FCIG notes from Varolin/Schumacher/direct-image machinery.

No reference is cited as proving the full FCIG statistical interpretation of the offset.
