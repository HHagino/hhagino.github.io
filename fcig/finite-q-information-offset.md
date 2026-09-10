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

at leading order. The constant term can in fact be determined.

Wan--Zhang's Bergman expansion for \(K_X\otimes L^k\), specialized to complex dimension one with \(L=K_X\), \(k=q-1\), and hyperbolic scalar curvature \(\rho=-1\), gives

\[
\boxed{
B_q(x)
=
\frac{2q-1}{4\pi}+O(q^{-2}).
}
\tag{0.3}
\]

The potential \(q^{-1}\) coefficient vanishes because their \(A_2\) coefficient is zero on a constant-curvature complex curve. Therefore

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

and \(II^{(q)}\) is exactly \(\mathfrak K_q\) in the present norm convention. Since

\[
\int_Xf(\mu)dA
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

FRZ also prove the full curvature asymptotic

\[
\boxed{
\operatorname{Chern}^{(q)}
=
\frac{6q(q-1)+1}{12\pi}G_{\rm WP}
+O(q^2e^{-q\ell_0}),
}
\tag{0.9}
\]

where \(\ell_0\) is the length of the shortest closed hyperbolic geodesic on the fixed surface.

Subtracting (0.8) from (0.9) yields the first refinement:

\[
\boxed{
\mathfrak K_q
=
\frac{3q-2}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{0.10}
\]

Using the exact source decomposition (0.2) then gives

\[
\boxed{
\mathfrak B_q
=
\frac{3q-1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{0.11}
\]

Hence the former \(O(1)\) Fisher--KS mismatch has a definite constant term:

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
=
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{0.12}
\]

In the KE/BLS position-transport realization established in the companion note,

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

Thus the two information channels do not merely share the same normalized WP limit. Their first finite-quantization separation is a universal WP-direction offset in the fixed hyperbolic normalization.

---

# Part I. Bergman source trace to one extra order

## 1. The adjoint-power indexing

Wan--Zhang write the Bergman kernel for

\[
H^0(X,L^k\otimes K_X).
\]

Our state space is

\[
H^0(X,K_X^q).
\]

Therefore the correct specialization is

\[
\boxed{L=K_X,\qquad k=q-1.}
\tag{1.1}
\]

This shift is essential for the constant coefficient.

For the canonical-bundle coefficient metric, Wan--Zhang give

\[
B_k
=\frac1{(2\pi)^n}
\left[
 k^n-\frac{\rho}{2}k^{n-1}
 +A_2k^{n-2}+\cdots
\right],
\tag{1.2}
\]

where

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

Set \(n=1\) and use the hyperbolic Kähler metric normalized by

\[
\operatorname{Ric}(\omega)=-\omega,
\qquad \rho=-1.
\tag{2.1}
\]

Since \(\rho\) is constant,

\[
\Delta''\rho=0.
\tag{2.2}
\]

In complex dimension one every Kähler curvature contraction is determined by the scalar curvature. In an orthonormal complex frame,

\[
|R|^2=|\operatorname{Ric}|^2=\rho^2,
\]

so

\[
|R|^2-4|\operatorname{Ric}|^2+3\rho^2=0.
\tag{2.3}
\]

Therefore

\[
\boxed{A_2=0.}
\tag{2.4}
\]

Apply the full Bergman expansion with enough terms retained. From \(k=q-1\),

\[
\begin{aligned}
B_q(x)
&=\frac1{2\pi}
\left(k+\frac12+O(k^{-2})\right)\\
&=\frac{2q-1}{4\pi}+O(q^{-2}).
\end{aligned}
\tag{2.5}
\]

**Status:** **Derived here from the established coefficient formula.** The vanishing of \(A_2\) is special to the constant-curvature curve specialization.

### Remark 2.1 — possible exponential strengthening

Berman proves exponentially small Bergman-kernel errors for canonical determinantal processes in constant-curvature Riemann-surface settings [Ber12]. This strongly suggests a sharper remainder is available after the exact convention and uniformity crosswalk is completed. The theorem in this note deliberately keeps the conservative TYZ consequence \(O(q^{-2})\); no exponential remainder is needed for the constant term.

---

## 3. Source energy

By definition,

\[
\begin{aligned}
\mathfrak A_q(\mu,\bar\nu)
&=\sum_j\langle\mu\cdot u_j,\nu\cdot u_j\rangle\\
&=\int_X\langle\mu,\nu\rangle B_q\,dA.
\end{aligned}
\tag{3.1}
\]

With the repository convention

\[
G_{\rm WP}(\mu,\bar\nu)
:=\int_X\langle\mu,\nu\rangle dA,
\tag{3.2}
\]

(2.5) gives, by Hermitian polarization,

\[
\boxed{
\mathfrak A_q
=
\frac{2q-1}{4\pi}G_{\rm WP}
+O(q^{-2}).
}
\tag{3.3}
\]

The remainder is to be read on a fixed surface and fixed tangent vectors; uniformity over moduli requires the usual bounded-geometry/thick-part hypotheses.

---

# Part II. Extracting the resolvent constant from FRZ

## 4. Exact curvature splitting

FRZ Proposition 1 states, for \(q\ge2\),

\[
\operatorname{Chern}^{(q)}=I^{(q)}+II^{(q)},
\tag{4.1}
\]

with

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

Their

\[
f(\mu)=(1+\square_0)^{-1}|\mu|^2.
\tag{4.4}
\]

Our intrinsic KS resolvent tensor is exactly

\[
\boxed{\mathfrak K_q:=II^{(q)}}
\tag{4.5}
\]

in this FRZ norm convention. It is the quantity denoted \(\mathfrak R_q\) in `grassmannian-quantum-information.md`.

---

## 5. Integral of the Schumacher potential

Equation (4.4) is equivalent to

\[
(1+\square_0)f=|\mu|^2.
\tag{5.1}
\]

On compact \(X\), integration kills the scalar Laplacian term, hence

\[
\boxed{
\int_X f(\mu)dA
=
\int_X|\mu|^2dA
=G_{\rm WP}(\mu,\mu).
}
\tag{5.2}
\]

Consequently the pointwise-constant part of the Bergman kernel factors out of \(I^{(q)}\):

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

FRZ prove, on a fixed compact hyperbolic surface,

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

This is an established theorem [FRZ20]. The exponential remainder comes from the Selberg-zeta/hyperbolic contribution; it is much smaller than the conservative \(O(q^{-1})\) Bergman remainder used in (5.3).

Subtract (5.3) from (6.1):

\[
\begin{aligned}
\mathfrak K_q
&=
\operatorname{Chern}^{(q)}-I^{(q)}\\
&=
\left[
\frac{6q(q-1)+1}{12\pi}
-
\frac{(q-1)(2q-1)}{4\pi}
\right]G_{\rm WP}
+O(q^{-1})\\
&=
\boxed{
\frac{3q-2}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\end{aligned}
\tag{6.2}
\]

This upgrades the earlier leading-only estimate

\[
\mathfrak K_q=\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\]

---

# Part III. The finite-q 1/(12π) offset

## 7. Theorem — refined second-fundamental and resolvent channels

Combine the exact relation

\[
\mathfrak B_q=\mathfrak A_q-\mathfrak K_q
\tag{7.1}
\]

with (3.3) and (6.2). Then

\[
\begin{aligned}
\mathfrak B_q
&=
\left[
\frac{2q-1}{4\pi}
-
\frac{3q-2}{12\pi}
\right]G_{\rm WP}
+O(q^{-1})\\
&=
\boxed{
\frac{3q-1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\end{aligned}
\tag{7.2}
\]

Therefore

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
=
\frac{1}{12\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{7.3}
\]

**Status:** **Derived here from [WZ21] + [FRZ20] + the exact source decomposition already established in the companion note.** No claim is made that equation (7.3) is absent from all prior literature.

### Hermitian polarization

The derivation above is written on a diagonal \((\mu,\mu)\), matching the source statements. Because all terms are Hermitian quadratic forms, polarization gives the tensor identity

\[
\boxed{
\mathfrak B_q(\mu,\bar\nu)
-
\mathfrak K_q(\mu,\bar\nu)
=
\frac{1}{12\pi}G_{\rm WP}(\mu,\bar\nu)
+O(q^{-1}).
}
\tag{7.4}
\]

on fixed tangent vectors.

---

## 8. Refined 50--50 law

Since

\[
\mathfrak A_q
=
\frac{2q-1}{4\pi}G_{\rm WP}+O(q^{-2}),
\]

we can divide on a nonzero diagonal direction. From (6.2) and (7.2),

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

Thus “50--50” is the semiclassical limit, but at first finite order the second-fundamental/Grassmannian side carries a small excess and the resolvent side an equal deficit.

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

while

\[
\mathfrak K_q
=
\frac{q}{4\pi}G_{\rm WP}
-
\frac{1}{6\pi}G_{\rm WP}
+O(q^{-1}).
\tag{8.4}
\]

Their difference is the positive offset (7.3).

---

# Part IV. Statistical meaning

## 9. BLS/KE Hermitian Born--Fisher consequence

The BLS position-transport note established, in the local KE/BLS covariant realization,

\[
\boxed{
I_{\rm HBF,q}^{KE}=g_{\rm Pl,q}^{KE}=\mathfrak B_q.
}
\tag{9.1}
\]

Therefore Theorem 7 becomes

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

The previous result only showed that the left-hand side was \(O(1)\). Equation (9.3) identifies its leading finite-quantization value.

The raw J-paired Fisher tensor consequently has

\[
\boxed{
I_q^{KE}+J^*I_q^{KE}
=
\frac{3q-1}{3\pi}G_{\rm WP}
+O(q^{-1}).
}
\tag{9.4}
\]

This is just four times (9.2); the factor \(1/4\) convention must not be dropped.

---

# Part V. Index/Bernoulli interpretation

## 10. Why the coefficient 1/(12π) is suggestive

The FRZ polynomial is

\[
\frac{6q(q-1)+1}{12\pi}
=
\frac1{2\pi}
\left(q^2-q+\frac16\right).
\tag{10.1}
\]

Since

\[
B_2=\frac16
\]

is the second Bernoulli number, the constant part is

\[
\frac{B_2}{2\pi}=\frac1{12\pi}.
\tag{10.2}
\]

The same quadratic polynomial \(6q^2-6q+1\) is the familiar coefficient in local-index/Quillen formulas for powers of the canonical bundle on moduli of curves [TZ; FRZ20].

**Interpretation, not an additional theorem:** the finite Fisher--KS mismatch can therefore be viewed as an **index/Bernoulli offset** surviving after the leading semiclassical 50--50 split. This observation does not by itself prove a new topological derivation of (7.3); equation (7.3) was obtained analytically by the subtraction above.

---

# Part VI. What this changes in FCIG

## 11. Before and after

Previously the information closure stopped at

\[
I_{\rm HBF,q}^{KE}-\mathfrak K_q=O(1).
\]

It now reads

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=
\frac1{12\pi}G_{\rm WP}+O(q^{-1}).
}
\tag{11.1}
\]

Thus the first two levels are separated cleanly:

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
\tag{11.2}
\]

The remaining analytic problem has therefore moved one order lower: determine the \(q^{-1}\) coefficient (or prove a sharper constant-curvature remainder after convention matching).

---

# 12. Remaining proof obligations

1. **Uniformity on moduli.** The displayed asymptotics are safest on a fixed surface or uniformly on compact/thick subsets. Degenerating families require separate cusp/short-geodesic estimates.
2. **FRZ/BLS operator sign.** The metric-level identification \(I_{\rm HBF}=\mathfrak B_q\) is sign-insensitive, but a submission version should finish the local-coordinate sign crosswalk for the second fundamental form.
3. **WP/Quillen normalization.** All coefficients here use the repository's Hermitian WP convention. Conversion to first-Chern-form conventions must preserve the appropriate \(i\) and \(2\pi\) factors.
4. **Exponential improvement.** Berman's constant-curvature result suggests a much sharper Bergman remainder. Promote it only after matching his normalization and establishing the desired family-uniform statement.
5. **Novelty audit.** The coefficient follows naturally by combining known formulas. A broad MathSciNet/zbMATH/reference-chain search is required before making any originality claim about the packaged identity.

---

# 13. Reference map

- **FRZ direct-image curvature splitting and complete hyperbolic curvature polynomial:** [FRZ20].
- **TYZ coefficient formula for \(K_X\otimes L^k\):** [WZ21], with background [Lu00; MM07].
- **Exponentially accurate constant-curvature Bergman asymptotics:** [Ber12].
- **Local-index coefficient \(6q^2-6q+1\) and Weil--Petersson/Quillen context:** [TZ91] and the references discussed in [FRZ20].
- **BLS/KE statistical identification \(I_{\rm HBF}=\mathfrak B_q\):** derived in the preceding FCIG notes from Varolin/Schumacher/direct-image machinery.

No reference is cited as proving the full FCIG statistical interpretation of the offset.