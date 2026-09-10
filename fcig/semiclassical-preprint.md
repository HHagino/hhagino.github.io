# A Semiclassical Atlas for Holomorphic Discrete-Series Matrix Coefficients in FCIG

## Preprint-style consolidation draft

**Status (2026-09-10).**

This document freezes the FCIG semiclassical branch developed in the sequence

`jacobi-asymptotic-closure.md` → `proportional-k-type-rate-function.md` → `steepest-descent-rate-closure.md` → `explicit-rate-function-closure.md` → `off-diagonal-rate-surface.md` → `two-sheet-airy-normalization.md` → `global-off-diagonal-rate-closure.md` → `uniform-remainder-closure.md` → `boundary-bessel-closure.md` → `lowest-k-hermite-closure.md` → `semiclassical-atlas-closure.md`.

The purpose is theorem packaging, not a novelty claim. The exact FCIG formulas and their asymptotic assembly are separated from the classical asymptotic tools used to justify the canonical local models.

---

## Abstract

Let \(M_{m,n}^{(q)}(t)\) denote a radial \(K\)-type matrix coefficient in the holomorphic discrete series associated with \(q\)-differentials. In the FCIG normalization it admits an exact Jacobi-polynomial representation. We study the semiclassical regime in which \(q\to\infty\) while the \(K\)-type labels satisfy \(m/q\to\alpha\ge0\) and \(n/q\to\beta\ge0\). The coefficient-extraction phase has two hyperbolic caustic sheets

\[
t_-=|u_\alpha-u_\beta|,
\qquad
t_+=u_\alpha+u_\beta,
\qquad
\alpha+1=\cosh u_\alpha,
\quad
\beta+1=\cosh u_\beta.
\]

Between them the contributing saddles are complex conjugate and the coefficient is oscillatory; outside them the relevant saddle is real and gives exponential decay governed by explicit rate functions. At each simple caustic the two saddles coalesce and admit an Airy normal form. Two boundary degenerations require different canonical charts: when \(q|\alpha-\beta|=O(1)\), the inner fold reaches the identity and the exact coefficient contracts to a Bessel function; when \(q\beta=O(1)\), the two sheets merge near the lowest \(K\)-type boundary and the coefficient contracts to a Hermite--Gaussian, equivalently parabolic-cylinder, model. These charts overlap through the classical large-order Bessel-to-Airy and Hermite-to-Airy transitions. The resulting statement is a leading semiclassical atlas for radial holomorphic-discrete-series matrix coefficients. It does not identify \(K\)-type labels, Cartan radius, transverse orbital Fourier frequency, or the Harish--Chandra spectral parameter.

---

## 1. Exact starting point

For \(n\ge m\), suppressing the fixed convention-dependent compact phase,

\[
\boxed{
M_{m,n}^{(q)}(t)
=
\mathcal N_{m,n}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^{n-m}
P_m^{(n-m,2q-1)}
\left(1-2\tanh^2\frac t2\right)
}
\]

with

\[
\mathcal N_{m,n}(q)
=
\left(
\frac{m!\Gamma(2q+n)}{n!\Gamma(2q+m)}
\right)^{1/2}.
\]

The case \(m\ge n\) is obtained by the corresponding symmetry/conjugation after the phase convention is fixed.

Set

\[
r=\tanh\frac t2,
\qquad
m=\alpha q+o(q),
\qquad
n=\beta q+o(q).
\]

The coefficient-extraction phase is

\[
\boxed{
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z.
}
\]

Its saddle equation is

\[
\boxed{
\frac{\beta}{z+r}
-
\frac{r(\beta+2)}{1+rz}
-
\frac{\alpha}{z}=0.
}
\]

Equivalently,

\[
r(\alpha+2)z^2+Bz+\alpha r=0,
\qquad
B=(\alpha-\beta)+(\alpha+\beta+2)r^2.
\]

---

## 2. Main theorem: caustic geometry and canonical atlas

Define

\[
\alpha+1=\cosh u_\alpha,
\qquad
\beta+1=\cosh u_\beta.
\]

Then the saddle discriminant factorizes as

\[
\boxed{
\Delta_{\rm sad}
=(\alpha+\beta+2)^2(r^2-r_-^2)(r^2-r_+^2)
}
\]

with

\[
\boxed{
r_-=\tanh\frac{|u_\alpha-u_\beta|}{2},
\qquad
r_+=\tanh\frac{u_\alpha+u_\beta}{2}.}
\]

Hence the caustic sheets are exactly

\[
\boxed{
t_-=|u_\alpha-u_\beta|,
\qquad
t_+=u_\alpha+u_\beta.}
\]

For fixed positive \((\alpha,\beta)\) away from the boundary degenerations, the leading phase diagram is

\[
\boxed{
\begin{array}{ccl}
0<t<t_-&:&\text{inner forbidden},\\
t_-<t<t_+&:&\text{oscillatory},\\
t>t_+&:&\text{outer forbidden}.
\end{array}}
\]

At both sheets the saddles coalesce at the same projective point

\[
\boxed{z_*=-\sqrt{\frac{\alpha}{\alpha+2}}.}
\]

The two cubic coefficients have opposite sign while the radial unfolding coefficient is common:

\[
\boxed{
\partial_t\Psi'(z_*,t_-)
=
\partial_t\Psi'(z_*,t_+)
=-(\alpha+2).
}
\]

Therefore each nondegenerate sheet is a fold and admits a Chester--Friedman--Ursell Airy chart with

\[
\boxed{z-z_*=O(q^{-1/3}),
\qquad t-t_\pm=O(q^{-2/3}).}
\]

The two boundary critical scales are

\[
\boxed{q|\alpha-\beta|=O(1)}
\]

and

\[
\boxed{q\beta=O(1).}
\]

They are not uniformly described by the ordinary separated-fold Airy model.

---

## 3. Generic forbidden rates

Let

\[
\Delta=B^2-4\alpha(\alpha+2)r^2.
\]

For \(\alpha\ge\beta>0\), the decaying saddles are

\[
\boxed{
z_{\rm in}=
\frac{-B-\sqrt\Delta}{2r(\alpha+2)},
\qquad 0<t<t_-,}
\]

and

\[
\boxed{
z_{\rm out}=
\frac{-B+\sqrt\Delta}{2r(\alpha+2)},
\qquad t>t_+.}
\]

With

\[
s(\gamma)
=
\frac12\bigl[(\gamma+2)\log(\gamma+2)
-\gamma\log\gamma-2\log2\bigr],
\]

define

\[
\boxed{
\begin{aligned}
\Phi_{\alpha,\beta}(t;z_*)
={}&2\log\cosh\frac t2+s(\alpha)-s(\beta)\\
&-\beta\log|z_*+r|
+(\beta+2)\log|1+rz_*|
+\alpha\log|z_*|.
\end{aligned}}
\]

Then

\[
\Phi_-(\alpha,\beta,t)
=
\Phi_{\alpha,\beta}(t;z_{\rm in}),
\qquad
\Phi_+(\alpha,\beta,t)
=
\Phi_{\alpha,\beta}(t;z_{\rm out}),
\]

with

\[
\boxed{\Phi_->0\text{ in }0<t<t_-},
\qquad
\boxed{\Phi_+>0\text{ in }t>t_+},
\]

and

\[
\boxed{\Phi_-(t_-)=0,
\qquad
\Phi_+(t_+)=0.}
\]

Near either caustic the rate has the fold law

\[
\boxed{\Phi_\pm(t)\asymp C_\pm|t-t_\pm|^{3/2}}
\]

with \(C_\pm>0\) given by the Airy normalization in `two-sheet-airy-normalization.md`.

---

## 4. Boundary chart I: Bessel contraction

Let

\[
n-m=k\in\mathbb Z_{\ge0}\quad\text{fixed},
\qquad
\frac mq\to\alpha>0,
\qquad
t=\frac{s}{q}.
\]

Then the terminating Gauss hypergeometric series contracts to \({}_0F_1\), and the exact normalization yields

\[
\boxed{
M_{m,m+k}^{(q)}(s/q)
\longrightarrow
J_k\!\left(\sqrt{\alpha(\alpha+2)}\,s\right)
}
\]

uniformly for bounded \(s\), up to the fixed line-bundle/representation phase.

The collapsing inner caustic satisfies

\[
qt_-
\to
\frac{k}{\sqrt{\alpha(\alpha+2)}},
\]

so the Bessel argument at the transition is

\[
\boxed{\sqrt{\alpha(\alpha+2)}\,qt_-=k.}
\]

Thus the large-order Bessel turning region matches the generic inner Airy fold.

---

## 5. Boundary chart II: Hermite--Gaussian contraction

Let

\[
n=\nu\in\mathbb Z_{\ge0}\quad\text{fixed},
\qquad
\frac mq\to\alpha>0,
\qquad
t=u_\alpha+\frac{\tau}{\sqrt q}.
\]

Then the fixed-degree Jacobi equation contracts to the Hermite equation, and the exact FCIG normalization gives

\[
\boxed{
q^{1/4}M_{\nu,m}^{(q)}
\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\longrightarrow
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}.
}
\]

Equivalently,

\[
\boxed{
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{D_\nu(-\sqrt2\tau)}{\sqrt{\nu!}}.
}
\]

The two generic caustics become

\[
\boxed{\tau_\pm\to\pm\sqrt{2\nu}.}
\]

Hence the large-order Hermite turning regions recover the two separated Airy folds.

---

## 6. Semiclassical atlas theorem

Combining the preceding results gives the leading canonical atlas

\[
\boxed{
\begin{array}{ccl}
\text{generic forbidden bulk}&:&e^{-q\Phi_\pm}\times\text{saddle amplitude},\\
\text{generic allowed bulk}&:&\text{conjugate-saddle oscillation},\\
\text{simple caustic}&:&\operatorname{Ai},\\
q|\alpha-\beta|=O(1)&:&J_k,\\
q\beta=O(1)&:&H_\nu e^{-\tau^2/2}\text{ / }D_\nu.
\end{array}}
\]

with overlap relations

\[
\boxed{\text{Bessel}\xrightarrow{k\to\infty}\text{Airy},
\qquad
\text{Hermite}\xrightarrow{\nu\to\infty}\text{two Airy folds}.}
\]

This is the content of the FCIG gate

\[
\boxed{\textbf{SAC-A: PASS — leading proportional-K semiclassical atlas closed.}}
\]

The statement is intentionally weaker than a single all-derivatives, globally uniform Harish--Chandra-Schwartz remainder theorem.

---

## 7. Proof map

The proof architecture is modular.

1. `jacobi-asymptotic-closure.md` gives the exact Jacobi coefficient and fixed-\(K\) uniform estimates.
2. `proportional-k-type-rate-function.md` derives the coefficient-extraction phase and saddle equation.
3. `off-diagonal-rate-surface.md` factorizes the discriminant and identifies \(t_\pm\).
4. `two-sheet-airy-normalization.md` computes the common coalescing saddle, cubic coefficients, and Airy coordinates.
5. `global-off-diagonal-rate-closure.md` selects the correct real saddle in both forbidden chambers and gives the global rates.
6. `uniform-remainder-closure.md` identifies compact generic domains and the two \(q^{-1}\) boundary critical scales.
7. `boundary-bessel-closure.md` gives the identity-endpoint Bessel contraction.
8. `lowest-k-hermite-closure.md` gives the lowest-\(K\) Hermite--Gaussian contraction.
9. `semiclassical-atlas-closure.md` assembles the leading atlas.

---

## 8. Relation to the FCIG orbital side

The exact Sun/Bergman orbital kernel uses the same hyperbolic disk coordinate

\[
r=\tanh\frac L2
\]

and its transverse Fourier transform is a Gamma window peaked at

\[
\boxed{|\xi|\sim2q\tanh(L/2)}.
\]

The representation-side saddle geometry is likewise organized by

\[
r=\tanh(t/2).
\]

This is a quantitative compatibility of semiclassical scales and hyperbolic coordinates. It is **not** an identification of variables:

\[
\boxed{\xi\neq t\neq n\neq\text{Harish--Chandra spectral parameter}.}
\]

A stronger equality requires a typed orbital/Fourier transform theorem.

---

## 9. Publication-status ledger

### Closed in this branch

- JA-A1 — fixed \(K\)-window pointwise decay: PASS.
- JA-A2 / JA-B lineage — superseded by the RF/UR/BC sequence and SAC-A.
- RF-B1 — exact off-diagonal caustic surface: PASS.
- RF-B2 — two-sheet Airy normalization: PASS.
- RF-C — global off-diagonal forbidden rates: PASS.
- UR-A1 — generic saddle/Airy uniform architecture: PASS.
- UR-A2 — exact boundary critical scales: PASS.
- BC-A1 — Bessel boundary: PASS.
- BC-A2 — Hermite--Gaussian boundary: PASS.
- SAC-A — master leading atlas: PASS.

### Still distinct / not claimed closed

- UQ-A2 — full pointwise Harish--Chandra-Schwartz control uniform in \(q\) and unrestricted \(K\)-type indices.
- A single globally explicit all-orders remainder theorem with constants uniform simultaneously across every stratum.
- Global phase normalization under all \(m\leftrightarrow n\), orientation, and covering conventions.
- Any identification of the FCIG transverse Fourier variable with a Harish--Chandra spectral variable.

---

## 10. Claim firewall

1. The objects studied here are radial matrix coefficients, not Harish--Chandra characters and not ordinary operator traces.
2. The Airy, Bessel, and Hermite canonical models are classical asymptotic structures; no novelty claim is made for their existence.
3. What is derived in FCIG conventions is the exact scaling map, caustic geometry, saddle selection, normalization, and matching of those canonical charts.
4. The master theorem is a leading semiclassical atlas, not a claim of global all-orders uniformity.
5. The compact quotient Toeplitz block and the universal-cover discrete-series operator remain distinct until an automorphic multiplicity identification is supplied.

---

## 11. References

1. NIST Digital Library of Mathematical Functions, §2.4(v), *Coalescing Saddle Points: Chester, Friedman, and Ursell's Method*.
2. NIST Digital Library of Mathematical Functions, §18.7(iii), Jacobi-to-Hermite and related limit relations.
3. NIST Digital Library of Mathematical Functions, §18.15(vi), large-parameter Jacobi approximations including Hermite approximants.
4. C. L. Frenzen and R. Wong, *A Uniform Asymptotic Expansion of the Jacobi Polynomials with Error Bounds*, Canadian Journal of Mathematics **37** (1985), 979–1007, DOI 10.4153/CJM-1985-053-5.
5. A. Gil, J. Segura, and N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss-Jacobi quadrature for large degree and parameters in terms of elementary functions*, Journal of Mathematical Analysis and Applications **494** (2021), 124642, DOI 10.1016/j.jmaa.2020.124642.
6. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975.
7. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs of the AMS **76** (1988), no. 393.

---

## 12. Freeze statement

For the FCIG research site, this file is the preferred theorem-level entry point for the proportional-\(K\) semiclassical branch. The older JA/RF/UR/BC notes remain as derivation notebooks and proof components. If an older note contains an OPEN/provisional statement about a proportional-\(K\) regime now covered here, this document and `semiclassical-atlas-closure.md` supersede that status.
