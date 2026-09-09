# FCIG Model XIX — Intrinsic elliptic spectral metric

**Status:** exact spectral calculation in the area-one flat elliptic model + standard Kronecker-limit / Dedekind-eta input. No spacetime kinetic term or gravitational field equation is inferred.

## 1. Why this model is different from Model XVIII

Model XVIII showed that arbitrary parameter-dependent masses can induce a target metric, but also that sufficiently free spectral data can encode the desired geometry by inverse design.

Model XIX removes that freedom. The operator is fixed geometrically by the elliptic FCIG laboratory itself:

\[
E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),
\qquad \tau=u+iY,\quad Y>0,
\]

with the **area-one** flat metric

\[
\boxed{
ds_\tau^2=\frac{|dz|^2}{Y}.
}
\]

No adjustable mass functions \(V_i(\tau)\) are introduced.

The question is whether the actual scalar-Laplacian spectrum on this torus reproduces the Poincare/Hodge geometry already present in Models I--II.

References for the determinant side include Ray--Singer [RaySinger1973], Osgood--Phillips--Sarnak [OPS1988], and the Kronecker-limit formula in the flat-torus normalization summarized in the modern determinant literature [Faulhuber2020]. Dedekind-eta modular transformations are fixed by DLMF \S23.18 [DLMF23].

---

## 2. Exact area-one metric and Laplacian spectrum

Write

\[
z=x+\tau t,
\qquad (x,t)\in\mathbb R^2/\mathbb Z^2.
\]

Then

\[
|dz|^2
=dx^2+2u\,dx\,dt+(u^2+Y^2)dt^2,
\]

so the metric matrix is

\[
(g_{ab})
=\frac1Y
\begin{pmatrix}
1 & u\\
u & u^2+Y^2
\end{pmatrix}.
\]

Its determinant is exactly one:

\[
\det g=1.
\]

Thus the coordinate square \([0,1)^2\) has area one. The inverse metric is

\[
(g^{ab})
=\frac1Y
\begin{pmatrix}
|\tau|^2 & -u\\
-u & 1
\end{pmatrix}.
\]

Because the coefficients are constant, the positive scalar Laplacian is

\[
\Delta_\tau=-g^{ab}\partial_a\partial_b.
\]

For the Fourier modes

\[
\phi_{m,n}(x,t)=e^{2\pi i(mx+nt)},
\qquad (m,n)\in\mathbb Z^2,
\]

we get

\[
\boxed{
\Delta_\tau\phi_{m,n}
=\lambda_{m,n}(\tau)\phi_{m,n},
\qquad
\lambda_{m,n}(\tau)
=\frac{4\pi^2}{Y}|m\tau-n|^2.
}
\]

The only zero mode is \((m,n)=(0,0)\).

> **Result XIX.1.** The complete nonzero scalar spectrum is fixed by the elliptic modulus and the area-one normalization; there are no adjustable spectral functions.

---

## 3. Modular covariance of the spectrum

Let

\[
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb Z),
\qquad
\tau'=\gamma\tau=\frac{a\tau+b}{c\tau+d}.
\]

Then

\[
Y'=\frac{Y}{|c\tau+d|^2}.
\]

Moreover,

\[
m\tau'-n
=\frac{(am-cn)\tau+(bm-dn)}{c\tau+d}.
\]

Define the integer relabeling

\[
\boxed{
(m',n')=(am-cn,\;dn-bm).
}
\]

Its determinant is one, so it is a bijection of \(\mathbb Z^2\). Therefore

\[
\boxed{
\frac{|m\tau'-n|^2}{Y'}
=\frac{|m'\tau-n'|^2}{Y}.
}
\]

Hence the spectrum is modular invariant as a multiset.

> **Result XIX.2.** Modular invariance is built into the integer lattice spectrum; it is not imposed by fitting a modular function after the fact.

---

## 4. Spectral zeta function

Define

\[
\zeta_{\Delta_\tau}(s)
:=\sum_{(m,n)\neq(0,0)}\lambda_{m,n}(\tau)^{-s}.
\]

Using the exact eigenvalues,

\[
\boxed{
\zeta_{\Delta_\tau}(s)
=(4\pi^2)^{-s}
E(\tau,s),
}
\]

where

\[
E(\tau,s)
:=\sum_{(m,n)\neq(0,0)}
\frac{Y^s}{|m\tau-n|^{2s}}
\]

is the nonholomorphic Eisenstein/Epstein lattice sum in this normalization.

The Kronecker limit formula gives [OPS1988; Faulhuber2020]

\[
E(\tau,0)=-1,
\]

and

\[
\boxed{
E'(\tau,0)
=-2\log\left(2\pi Y^{1/2}|\eta(\tau)|^2\right).
}
\]

Therefore

\[
\begin{aligned}
\zeta'_{\Delta_\tau}(0)
&=-\log(4\pi^2)E(\tau,0)+E'(\tau,0)\\
&=-\log\left(Y|\eta(\tau)|^4\right).
\end{aligned}
\]

By zeta regularization,

\[
\det{}'\Delta_\tau
:=\exp[-\zeta'_{\Delta_\tau}(0)].
\]

Thus

\[
\boxed{
\det{}'\Delta_\tau
=Y|\eta(\tau)|^4.
}
\]

This agrees with the standard area-one flat-torus determinant formula [RaySinger1973; OPS1988; Faulhuber2020].

> **Result XIX.3.** The determinant is obtained from the actual elliptic spectrum with no target-metric fitting.

---

## 5. Global modular invariance of the determinant

DLMF \S23.18 records

\[
\eta(\gamma\tau)
=\epsilon(\gamma)
[-i(c\tau+d)]^{1/2}\eta(\tau),
\]

with \(|\epsilon(\gamma)|=1\) [DLMF23]. Hence

\[
|\eta(\gamma\tau)|^4
=|c\tau+d|^2|\eta(\tau)|^4.
\]

Since

\[
Y'=\frac{Y}{|c\tau+d|^2},
\]

we obtain

\[
\boxed{
Y'|\eta(\tau')|^4
=Y|\eta(\tau)|^4.
}
\]

So \(\det{}'\Delta_\tau\) descends as a genuine modular invariant scalar.

The nonholomorphic \(Y\) factor and the holomorphic eta multiplier are both necessary: neither should be discarded independently in a global statement.

---

## 6. Intrinsic spectral curvature

Now compute the mixed complex Hessian of the determinant.

Because the Dedekind eta function is holomorphic and nonvanishing on \(\mathbb H\),

\[
\partial\bar\partial\log|\eta(\tau)|^4=0
\]

on the upper half-plane. Therefore

\[
\begin{aligned}
-\partial\bar\partial\log\det{}'\Delta_\tau
&=-\partial\bar\partial\left(\log Y+\log|\eta|^4\right)\\
&=-\partial\bar\partial\log Y.
\end{aligned}
\]

Using

\[
\partial_\tau\partial_{\bar\tau}\log Y
=-\frac1{4Y^2},
\]

we get the exact result

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=\frac1{4Y^2}\,d\tau\wedge d\bar\tau.
}
\]

But Model I fixed the Hodge-line metric by \(\|dz\|^2\propto Y\), giving

\[
\boxed{
F_{\lambda_H}
=-\partial\bar\partial\log Y
=\frac1{4Y^2}\,d\tau\wedge d\bar\tau.
}
\]

Hence:

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=F_{\lambda_H}.
}
\]

> **Result XIX.4 (intrinsic spectral--Hodge identity).** In the area-one elliptic convention already used by FCIG, the mixed complex curvature of the actual scalar spectral determinant equals the Hodge-line curvature exactly.

Equivalently, after the standard \(c_1=(i/2\pi)F\) normalization, this is the same fixed multiple of the hyperbolic/Poincare \((1,1)\) form already present in Model I.

This is the first FCIG milestone in which the pre-existing elliptic target curvature is regenerated from an intrinsic full spectrum rather than from an adjustable mass map.

---

## 7. What exactly has been derived

The result above is strong but specific.

### Derived

1. the exact area-one torus Laplacian spectrum;
2. its modular covariance by integer lattice relabeling;
3. the zeta determinant \(Y|\eta|^4\);
4. the exact mixed moduli curvature
   \[
   -\partial\bar\partial\log\det{}'\Delta=F_{\lambda_H};
   \]
5. compatibility with the Hodge/Poincare geometry already used in the elliptic FCIG model.

### Not derived

The calculation does **not** yet give a spacetime sigma kinetic term

\[
\int_M\sqrt g\,
\frac{\partial_\mu\tau\partial^\mu\bar\tau}{Y^2}.
\]

The object computed here is a curvature/Hessian on the **moduli space of constant elliptic structures**. A spacetime kinetic term requires a family \(\tau=\tau(x)\), a physical total-space operator or Kaluza--Klein tower, and an adiabatic/derivative expansion in spacetime.

Thus

\[
\boxed{
\text{moduli determinant curvature}
\neq
\text{spacetime kinetic coefficient}
}
\]

without an additional family calculation.

> **Result XIX.5 (Hessian/kinetic type no-go).** The exact spectral--Hodge identity does not by itself fix the Model-XVII coefficient \(Z_\Phi\).

---

## 8. Real Hessian versus complex mixed Hessian

One further distinction matters. Although

\[
\partial\bar\partial\log|\eta|^4=0,
\]

the full real Hessian in \((u,Y)\) of \(\log|\eta|^4\) need not vanish componentwise; it contains harmonic trace-free information.

Therefore the canonical statement is the \((1,1)\) / Chern-curvature identity

\[
-\partial\bar\partial\log\det{}'\Delta=F_{\lambda_H},
\]

not the claim that every real second derivative of \(\log\det{}'\Delta\) equals the Poincare metric.

This keeps the result aligned with the Hermitian-line / Quillen framework used throughout FCIG.

---

## 9. Quillen and previous FCIG models

Ray--Singer analytic torsion and Quillen determinant metrics are the standard framework relating spectral determinants to determinant-line geometry [RaySinger1973; Quillen1985]. Model V already separated the elementary \(L^2\) determinant metric from the Quillen refinement, while Models I, II, and X fixed the Hodge/determinant curvature conventions.

Model XIX should therefore be read as an exact **genus-one spectral consistency closure**:

\[
\boxed{
\text{lattice spectrum}
\to\zeta\text{ determinant}
\to\text{Chern curvature}
=\text{Hodge curvature}.
}
\]

It does not replace the full Quillen family-index theorem, nor does it assert that a scalar Laplacian determinant and every determinant line in earlier models are the same object.

---

## 10. No-fit prediction test

Model XVIII allowed arbitrary \(V_i(\tau)\), so matching a target metric could become inverse design.

Model XIX passes the no-fit test:

- the metric on \(E_\tau\) is fixed by area one;
- the Fourier lattice is fixed;
- the eigenvalues are fixed;
- the zeta regularization is fixed;
- modular covariance is fixed;
- the determinant is then fixed by the Kronecker limit formula;
- only after all this is the result compared with \(F_{\lambda_H}\).

Thus the equality

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}
}
\]

is not obtained by tuning a spectral map to reproduce the answer.

---

## 11. References used in this milestone

- D. B. Ray and I. M. Singer, *Analytic torsion for complex manifolds*, Ann. Math. **98** (1973), 154--177. [RaySinger1973]
- D. Quillen, *Determinants of Cauchy--Riemann Operators over a Riemann Surface*, Funct. Anal. Appl. **19** (1985), 31--34. [Quillen1985]
- B. Osgood, R. Phillips, P. Sarnak, *Extremals of determinants of Laplacians*, J. Funct. Anal. **80** (1988), 148--211. [OPS1988]
- M. Faulhuber, *Extremal determinants of Laplace--Beltrami operators for rectangular tori*, Math. Z. (2020), for an explicit modern derivation of \(\det{}'\Delta=Y|\eta|^4\) from the Kronecker limit formula. [Faulhuber2020]
- NIST Digital Library of Mathematical Functions, Chapter 23, especially \S23.18 for Dedekind eta modular transformations. [DLMF23]

## Bottom line

\[
\boxed{
\textbf{The actual elliptic Laplacian spectrum regenerates the FCIG Hodge/Poincare curvature exactly at the moduli-space Chern-curvature level.}
}
\]

The next unresolved step is to promote this intrinsic moduli response to a genuine spacetime adiabatic response for \(\tau(x)\), without simply identifying the two by analogy.
