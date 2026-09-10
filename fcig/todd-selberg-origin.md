# FCIG: Todd–Selberg Origin of the Finite Information Offset

**Status:** derived structural theorem + exponential refinement  
**Date:** 2026-09-10  
**Scope:** Hirzebruch/Grothendieck–Riemann–Roch, Todd classes, Bernoulli numbers, determinant of cohomology, Quillen curvature, Selberg/spectral zeta, constant-curvature Bergman kernels, and the Fisher–Kodaira–Spencer finite-q offset.  
**Depends on:** [`finite-q-information-offset.md`](finite-q-information-offset.md), [`bls-position-transport.md`](bls-position-transport.md), [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md).

> **Claim policy.** **Established** means a cited theorem/construction. **Derived here** means an explicit deduction from those inputs in the conventions stated below; it is not a novelty certification. **Interpretation** marks FCIG language. The central point of this note is that the coefficient `1/12` is not fitted: it is forced by the degree-four Todd term in relative complex dimension one, while the remaining geometry is exponentially small and encoded by global geodesic/periodization data.
>
> Dedicated bibliography: [`todd-selberg-origin.bib`](todd-selberg-origin.bib). Citation audit: [`todd-selberg-origin-citation-audit.md`](todd-selberg-origin-citation-audit.md).

---

## 0. Result in one page

Let

\[
\pi:\mathcal X\to B
\]

be a smooth family of compact hyperbolic Riemann surfaces of genus \(g\ge2\), and set

\[
\lambda_q:=\det R\pi_*K_{\mathcal X/B}^q.
\]

Write

\[
x:=c_1(K_{\mathcal X/B}).
\]

The relative tangent line has first Chern class \(-x\), hence

\[
\operatorname{Td}(T_\pi)
=\frac{x}{e^x-1}
=1-\frac{x}{2}+\frac{x^2}{12}+O(x^4).
\tag{0.1}
\]

Since

\[
\operatorname{ch}(K^q)=e^{qx},
\]

we obtain

\[
\boxed{
 e^{qx}\frac{x}{e^x-1}
 =1+
 \left(q-\frac12\right)x
 +\left(\frac{q^2}{2}-\frac q2+\frac1{12}\right)x^2
 +O(x^3).
}
\tag{0.2}
\]

Two different degree projections of this single characteristic series give the two basic FCIG quantities.

### Degree two on a fiber: state count

For \(q\ge2\),

\[
\chi(X,K_X^q)=h^0(X,K_X^q)
\]

and Hirzebruch–Riemann–Roch gives

\[
\boxed{
N_q
=(q-\tfrac12)\int_Xx
=(2q-1)(g-1).
}
\tag{0.3}
\]

### Degree four in a family: determinant/Quillen response

Bismut–Gillet–Soulé refine GRR to the curvature form of the Quillen metric. Up to the determinant-line sign convention,

\[
\boxed{
 c_1(\lambda_q,\|\cdot\|_Q)
 =
 \frac{6q^2-6q+1}{12}\,
 \pi_*(x^2).
}
\tag{0.4}
\]

In the Takhtajan–Zograf hyperbolic normalization this is the familiar

\[
\boxed{
F_q^{Q}
=\frac{6q(q-1)+1}{12\pi}
G_{\rm WP}
}
\tag{0.5}
\]

at the Hermitian quadratic-form level used in the companion notes.

The constant term is therefore

\[
\boxed{
\frac1{12}
=\frac{B_2}{2!}
=-\zeta_{\mathbb R}(-1).
}
\tag{0.6}
\]

This is the precise arithmetic origin of the coefficient: the second Bernoulli number in the Todd genus, equivalently the classical special value of the Riemann zeta function.

Now let \(\mathfrak B_q\) be the minimal-solution/second-fundamental/Grassmannian (hence Hermitian Born–Fisher) channel and \(\mathfrak K_q\) the positive Kodaira–Spencer resolvent channel of the preceding notes. The previous result was

\[
\mathfrak B_q-\mathfrak K_q
=\frac1{12\pi}G_{\rm WP}+O(q^{-1}).
\]

On a fixed compact hyperbolic surface this can be sharpened beyond all algebraic orders.

Let

\[
C_q:=\frac{2q-1}{4\pi},
\qquad
\beta_q(x):=B_q(x)-C_q,
\tag{0.7}
\]

and

\[
f_\mu=(1+\square_0)^{-1}|\mu|^2.
\tag{0.8}
\]

Using the exact Takhtajan–Zograf/FRZ local-index relation and the exact FRZ curvature splitting gives the identity

\[
\boxed{
\begin{aligned}
\mathfrak B_q-\mathfrak K_q
-\frac1{12\pi}G_{\rm WP}
={}&
2\,\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
\\
&+\int_X
\left(
|\mu|^2+2(q-1)f_\mu
\right)
\beta_q\,dA.
\end{aligned}
}
\tag{0.9}
\]

**Derived here.** Equation (0.9) is the key local/global decomposition.

Berman proves for constant-curvature Riemann surfaces that the diagonal Bergman kernel has an exponentially small error,

\[
\beta_q=O(e^{-\delta_X q}),
\tag{0.10}
\]

with \(\delta_X>0\) controlled by the injectivity radius [Ber12]. Fedosova–Rowlett–Zhang prove

\[
\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
=O(q^2e^{-q\ell_0}),
\tag{0.11}
\]

where \(\ell_0\) is the systole [FRZ20]. Therefore, for some \(c_X>0\),

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
=
\frac1{12\pi}G_{\rm WP}
+O(q^2e^{-c_Xq}).
}
\tag{0.12}
\]

Equivalently, in the BLS/KE statistical realization,

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=
\frac1{12\pi}G_{\rm WP}
+O(q^2e^{-c_Xq}).
}
\tag{0.13}
\]

Thus there are **no further inverse-power corrections** to the offset on a fixed compact hyperbolic surface. The remainder is nonperturbative in \(q\).

The structural summary is

\[
\boxed{
\text{local Todd/GRR arithmetic}
\quad+
\quad
\text{global Selberg/Bergman geodesic tunneling}.
}
\tag{0.14}
\]

The first term gives the universal \(1/(12\pi)\) coefficient. The second is exponentially small and remembers the global quotient geometry through the injectivity radius, systole, and primitive closed geodesics.

---

# Part I. Hirzebruch–Riemann–Roch already contains both state count and anomaly

## 1. Relative curve setup

Let \(K=K_{\mathcal X/B}\) and

\[
x=c_1(K).
\]

Since

\[
T_\pi\simeq K^{-1},
\]

we have

\[
c_1(T_\pi)=-x.
\]

For a complex line with Chern root \(y\),

\[
\operatorname{Td}(y)=\frac{y}{1-e^{-y}}.
\]

Putting \(y=-x\),

\[
\operatorname{Td}(T_\pi)
=\frac{-x}{1-e^x}
=\frac{x}{e^x-1}.
\tag{1.1}
\]

The Bernoulli generating series is

\[
\boxed{
\frac{x}{e^x-1}
=\sum_{n=0}^{\infty}\frac{B_n}{n!}x^n
=1-\frac x2+\frac{x^2}{12}-\frac{x^4}{720}+\cdots.
}
\tag{1.2}
\]

For \(K^q\),

\[
\operatorname{ch}(K^q)=e^{qx}.
\tag{1.3}
\]

Multiplying (1.2) and (1.3),

\[
\boxed{
\operatorname{ch}(K^q)\operatorname{Td}(T_\pi)
=
1+(q-\tfrac12)x
+\left(\frac{q^2-q}{2}+\frac1{12}\right)x^2
+O(x^3).
}
\tag{1.4}
\]

The expression

\[
\frac{q^2-q}{2}+\frac1{12}
=\frac{6q^2-6q+1}{12}
\tag{1.5}
\]

is therefore not a mysterious spectral fit. It is the degree-four coefficient of the Riemann–Roch characteristic class.

---

## 2. First projection: rank / capacity

On a single compact genus-\(g\) fiber,

\[
\int_Xx=\deg K_X=2g-2.
\tag{2.1}
\]

The degree-two term in (1.4) gives

\[
\chi(K_X^q)
=\left(q-\frac12\right)(2g-2).
\tag{2.2}
\]

For \(q\ge2\), Serre duality gives \(H^1(X,K^q)=0\), hence

\[
\boxed{
h^0(X,K^q)=(2q-1)(g-1).}
\tag{2.3}
\]

**Established:** this is Riemann–Roch for pluricanonical forms.

**FCIG interpretation:** the state-count/capacity sector is the first nontrivial degree projection of the same index density that later controls the determinant curvature.

---

## 3. Second projection: determinant curvature

For a family, GRR states

\[
\operatorname{ch}(R\pi_*K^q)
=
\pi_*
\left[
 e^{qx}\operatorname{Td}(T_\pi)
\right].
\tag{3.1}
\]

Because the fibers have complex dimension one, the rank on the base is produced by total degree two on \(\mathcal X\), whereas \(c_1\) of the determinant/direct image is produced by total degree four.

Thus

\[
\boxed{
\operatorname{rk}(R\pi_*K^q)
=\pi_*[(q-\tfrac12)x],
}
\tag{3.2}
\]

while

\[
\boxed{
 c_1(\det R\pi_*K^q)
=
\frac{6q^2-6q+1}{12}\,\pi_*(x^2)
}
\tag{3.3}
\]

in cohomology, subject to the chosen determinant convention.

Bismut–Gillet–Soulé refine (3.3) from cohomology to differential forms: the Quillen Chern curvature is the degree-two fiber integral of the Chern–Weil representatives of \(\operatorname{Td}(T_\pi)\operatorname{ch}(K^q)\) [BGS88].

This gives an exact mathematical realization of the FCIG slogan

\[
\boxed{
\text{state count and determinant anomaly are degree projections of one index class.}
}
\tag{3.4}
\]

Here it is not an analogy: equations (3.2) and (3.3) literally come from one characteristic series.

---

# Part II. Why 1/12 is arithmetic

## 4. Bernoulli origin

The second Bernoulli number is

\[
B_2=\frac16.
\]

Its Todd coefficient is

\[
\boxed{
\frac{B_2}{2!}=\frac1{12}.
}
\tag{4.1}
\]

The classical identity

\[
\zeta_{\mathbb R}(1-n)=-\frac{B_n}{n}
\tag{4.2}
\]

therefore gives, at \(n=2\),

\[
\boxed{
\zeta_{\mathbb R}(-1)=-\frac1{12}.
}
\tag{4.3}
\]

So the same number can be written

\[
\boxed{
\frac1{12}
=\frac{B_2}{2!}
=-\zeta_{\mathbb R}(-1).
}
\tag{4.4}
\]

**Interpretation boundary.** Equation (4.4) does not mean that the FCIG offset was derived by directly summing \(1+2+3+\cdots\). The rigorous origin here is the Todd class in GRR. The zeta special value is the number-theoretic identity relating Bernoulli numbers to the Riemann zeta function.

---

## 5. Mumford/Deligne–Riemann–Roch globalizes the same polynomial

Let

\[
\lambda_q=\det R\pi_*K^q.
\]

The Mumford isomorphism, in a canonical rational form, reads

\[
\boxed{
\lambda_q
\simeq
\lambda_1^{\otimes(6q^2-6q+1)}
}
\tag{5.1}
\]

for a smooth family of curves [Mum83; Eri08].

Thus the polynomial appearing in the local Quillen curvature is not merely analytic. It is also the exponent of a global algebraic determinant-line relation.

This gives three incarnations of the same coefficient:

\[
\boxed{
\begin{array}{ccc}
\text{Todd/GRR coefficient}
&\longleftrightarrow&
6q^2-6q+1
\\
\updownarrow&&\updownarrow
\\
\text{Quillen curvature}
&\longleftrightarrow&
\text{Mumford determinant isomorphism}.
\end{array}
}
\tag{5.2}
\]

This is the strongest sense in which the coefficient is index-theoretic rather than model-dependent.

---

# Part III. The three zeta functions must not be conflated

## 6. Riemann zeta: arithmetic coefficients

The Riemann zeta function enters through (4.2), i.e. through the Bernoulli numbers in the Todd series. Its role is **local/characteristic-class arithmetic**.

It determines the universal rational coefficient \(1/12\), not the geometry of individual closed geodesics.

---

## 7. Spectral zeta: determinant regularization

For a positive elliptic operator \(A\), the spectral zeta function

\[
\zeta_A(s)=\sum_{\lambda>0}\lambda^{-s}
\]

is meromorphically continued and gives the zeta-regularized determinant

\[
\boxed{
\det{}'A=\exp[-\zeta_A'(0)].
}
\tag{7.1}
\]

This is the analytic regularization entering Ray–Singer/Quillen theory.

For the hyperbolic scalar operator considered by FRZ,

\[
A_s=\Delta_0+s(s-1),
\]

its zeta-regularized determinant is related explicitly to the Selberg zeta function by gamma/Barnes-double-gamma factors [FRZ20]. These extra factors depend on \(s\) and genus but not on the Teichmüller point, so their moduli second variation vanishes.

Consequently,

\[
\boxed{
\bar\partial_\mu\partial_\mu
\log\det(\Delta_0+s(s-1))
=
\bar\partial_\mu\partial_\mu
\log Z_{\rm Sel}(s).
}
\tag{7.2}
\]

Thus spectral zeta is the regularization bridge from Laplace determinants to Selberg dynamics.

---

## 8. Selberg zeta: global closed-geodesic sector

For a compact hyperbolic surface,

\[
\boxed{
Z_{\rm Sel}(s)
=
\prod_{\{\gamma\}_{\rm prim}}
\prod_{k=0}^{\infty}
\left(1-e^{-(s+k)\ell(\gamma)}\right).
}
\tag{8.1}
\]

Its logarithm is built from primitive closed geodesic lengths. Therefore the shortest geodesic \(\ell_0\) sets the leading large-\(s\) exponential scale.

FRZ prove

\[
\boxed{
\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
=O(q^2e^{-q\ell_0})
}
\tag{8.2}
\]

and more precise asymptotics determined by the systole geodesics [FRZ20].

They also give the exact local-index identity

\[
\boxed{
\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
=
-\operatorname{Chern}^{(q)}(\mu,\mu)
+
\frac{6q(q-1)+1}{12\pi}
G_{\rm WP}(\mu,\mu).
}
\tag{8.3}
\]

Hence

\[
\boxed{
\operatorname{Chern}^{(q)}
=
\text{local-index polynomial}
-
\text{Selberg geodesic variation}.
}
\tag{8.4}
\]

This is the precise local/global split.

---

# Part IV. Constant-curvature Bergman periodization is also nonperturbative

## 9. Berman's exponential Bergman theorem

For a positive line bundle over a Riemann surface with constant scalar curvature, Berman proves that the diagonal Bergman function satisfies

\[
B_k=k+\frac R2+O(e^{-\delta k})
\tag{9.1}
\]

uniformly, with \(\delta>0\) related explicitly to the injectivity radius [Ber12].

For \(L=K_X\) on a compact hyperbolic surface, use the cohomological Kähler form

\[
\omega=c_1(K_X)=\frac{dA}{2\pi}
\tag{9.2}
\]

and \(R=-1\) in Berman's normalization. For \(H^0(X,K_X^q)\), his tensor-power index is directly \(k=q\). Converting the density from \(\omega\) to hyperbolic area \(dA\) gives

\[
\boxed{
B_q^{dA}(x)
=
\frac{q-1/2}{2\pi}
+O(e^{-\delta_Xq})
=
\frac{2q-1}{4\pi}
+O(e^{-\delta_Xq}).
}
\tag{9.3}
\]

Berman explicitly notes that in the globally hyperbolic canonical-bundle case the exponential error can also be understood by lifting to \(\mathbb H\), where the kernel is homogeneous, and estimating the effect of \(\Gamma\)-periodization [Ber12].

Thus the Bergman correction is global quotient data, not a new local power-series coefficient.

---

# Part V. Exact Todd–Selberg–Bergman decomposition of the offset

## 10. Notation

Fix a harmonic Beltrami differential \(\mu\). Write

\[
G:=G_{\rm WP}(\mu,\mu),
\]

\[
C_q:=\frac{2q-1}{4\pi},
\qquad
\beta_q(x):=B_q(x)-C_q,
\]

and

\[
f_\mu=(1+\square_0)^{-1}|\mu|^2.
\]

Then

\[
\int_X f_\mu dA=G.
\tag{10.1}
\]

The source trace is exactly

\[
\boxed{
\mathfrak A_q
=C_qG+
\int_X|\mu|^2\beta_qdA.
}
\tag{10.2}
\]

FRZ's first direct-image curvature summand is exactly

\[
\boxed{
I^{(q)}
=(q-1)C_qG
+(q-1)\int_Xf_\mu\beta_qdA.
}
\tag{10.3}
\]

Their local-index identity gives

\[
\boxed{
\operatorname{Chern}^{(q)}
=P_qG
-\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q),
}
\tag{10.4}
\]

where

\[
P_q:=\frac{6q(q-1)+1}{12\pi}.
\tag{10.5}
\]

The intrinsic resolvent channel is

\[
\boxed{
\mathfrak K_q
=\operatorname{Chern}^{(q)}-I^{(q)}.
}
\tag{10.6}
\]

The exact source decomposition is

\[
\boxed{
\mathfrak A_q=\mathfrak B_q+\mathfrak K_q.
}
\tag{10.7}
\]

---

## 11. Theorem — exact remainder formula

From (10.6)--(10.7),

\[
\mathfrak B_q-\mathfrak K_q
=\mathfrak A_q-2\mathfrak K_q
=\mathfrak A_q-2\operatorname{Chern}^{(q)}+2I^{(q)}.
\tag{11.1}
\]

Insert (10.2)--(10.4):

\[
\begin{aligned}
\mathfrak B_q-\mathfrak K_q
={}&
\left[C_q-2P_q+2(q-1)C_q\right]G
\\
&+2\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
\\
&+\int_X
\left(|\mu|^2+2(q-1)f_\mu\right)
\beta_qdA.
\end{aligned}
\tag{11.2}
\]

A direct algebra calculation gives

\[
\boxed{
C_q-2P_q+2(q-1)C_q=\frac1{12\pi}.
}
\tag{11.3}
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathfrak B_q-\mathfrak K_q
-\frac1{12\pi}G
={}&
2\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
\\
&+\int_X
\left(|\mu|^2+2(q-1)f_\mu\right)
\beta_qdA.
\end{aligned}
}
\tag{11.4}
\]

**Status:** **Derived here from the exact FRZ identities plus definitions.** This is stronger conceptually than an asymptotic subtraction because it identifies the complete remainder as the sum of two explicit global terms.

---

## 12. Theorem — exponential rigidity of the 1/(12π) offset

By Berman,

\[
\|\beta_q\|_{L^\infty}
\le C_Xe^{-\delta_Xq}.
\tag{12.1}
\]

For fixed \(\mu\), \(f_\mu\) is smooth and bounded, so

\[
\int_X
\left(|\mu|^2+2(q-1)f_\mu\right)\beta_qdA
=O(qe^{-\delta_Xq}).
\tag{12.2}
\]

By FRZ,

\[
\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
=O(q^2e^{-q\ell_0}).
\tag{12.3}
\]

Let

\[
c_X<\min(\delta_X,\ell_0)
\]

be any fixed positive number. Then polynomial prefactors may be absorbed into a slightly weaker exponential, giving

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
=
\frac1{12\pi}G_{\rm WP}
+O(q^2e^{-c_Xq}).
}
\tag{12.4}
\]

The same holds after Hermitian polarization on fixed tangent vectors.

In the BLS/KE statistical realization,

\[
I_{\rm HBF,q}^{KE}=\mathfrak B_q,
\]

so

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=
\frac1{12\pi}G_{\rm WP}
+O(q^2e^{-c_Xq}).
}
\tag{12.5}
\]

**Consequence.** The formal asymptotic series of the difference contains no \(q^{-1},q^{-2},\ldots\) terms:

\[
\boxed{
\mathfrak B_q-\mathfrak K_q
\sim
\frac1{12\pi}G_{\rm WP}
\quad\text{to all algebraic orders in }q^{-1}.
}
\tag{12.6}
\]

All further information is beyond-all-orders / nonperturbative.

---

# Part VI. Why the remainder is geometric rather than another Todd coefficient

## 13. Relative dimension one forces polynomial truncation

For the first Chern form of the determinant line, the fiber integral lowers real degree by two. Hence only total degree four in

\[
e^{qx}\operatorname{Td}(T_\pi)
\]

can contribute.

That degree-four coefficient is exactly

\[
\frac{q^2-q}{2}+\frac1{12}.
\]

Terms \(x^3,x^4,\ldots\) cannot contribute to this first-Chern calculation in a relative curve family.

Therefore

\[
\boxed{
\text{the local Quillen/index contribution is exactly quadratic in }q.
}
\tag{13.1}
\]

There is no local characteristic-class mechanism that could generate an infinite \(q^{-1}\) tail in this sector.

---

## 14. Global topology enters through two exponentials

The exact remainder (11.4) has two pieces.

### 14.1 Selberg sector

\[
2\bar\partial\partial\log Z_{\rm Sel}(q)
\]

is a primitive-closed-geodesic contribution. Its scale is set by the systole \(\ell_0\).

### 14.2 Bergman periodization sector

\[
\int_X
\left(|\mu|^2+2(q-1)f_\mu\right)\beta_qdA
\]

measures the difference between the compact quotient Bergman kernel and its homogeneous universal-cover model. Berman's proof identifies the exponential scale with the injectivity radius.

Thus the correction has a natural transseries-style split:

\[
\boxed{
\text{perturbative/local}
=\frac1{12\pi}G_{\rm WP},
\qquad
\text{nonperturbative/global}
\sim e^{-q\times\text{length}}.
}
\tag{14.1}
\]

The “instanton scale” language should be used only as an analogy; mathematically the exponents are controlled by closed-geodesic/injectivity-radius data.

---

# Part VII. Relation to spectral determinants and Barnes gamma

## 15. Selberg determinant formula

FRZ recall the exact relation

\[
\det(\Delta_0+s(s-1))
=Z_{\rm Sel}(s)
\left[
 e^{E-s(s-1)}
 \frac{\Gamma_2(s)^2}{\Gamma(s)}
 (2\pi)^s
\right]^{2g-2},
\tag{15.1}
\]

where \(\Gamma_2\) is the Barnes double gamma function and \(E\) contains the Glaisher–Kinkelin constant [FRZ20].

The bracket depends on \(s\) and \(g\), not on the Teichmüller modulus. Hence its moduli Hessian vanishes and (7.2) follows.

This formula shows explicitly that the determinant bridge contains classical special-function regularization data—Gamma, Barnes Gamma, Glaisher constants—while the moduli-dependent nonlocal content is isolated in \(Z_{\rm Sel}\).

**Interpretation:** the same calculation naturally separates

\[
\boxed{
\text{universal regularization constants}
\quad\text{from}\quad
\text{moduli-sensitive geodesic arithmetic/dynamics}.
}
\tag{15.2}
\]

---

# Part VIII. FCIG synthesis

## 16. A three-level arithmetic/index picture

The present calculation suggests the following precise hierarchy.

### Level A — Bernoulli/Todd arithmetic

\[
\frac{x}{e^x-1}
=1-\frac x2+\frac{x^2}{12}+\cdots,
\qquad
\frac1{12}=-\zeta_{\mathbb R}(-1).
\]

This fixes universal local rational coefficients.

### Level B — GRR/Quillen determinant geometry

\[
\operatorname{ch}(R\pi_*K^q)
=
\pi_*(e^{qx}\operatorname{Td}(T_\pi)),
\]

whose rank and determinant curvature are different degree projections.

### Level C — Selberg/Bergman global spectral geometry

The discrepancy between local index geometry and finite compact-surface realizations is exponentially small and encoded by primitive closed geodesics and quotient periodization.

Thus

\[
\boxed{
\text{arithmetic characteristic class}
\to
\text{determinant geometry}
\to
\text{global spectral/geodesic correction}.
}
\tag{16.1}
\]

---

## 17. The strongest current FCIG statement

For compact hyperbolic curve quantization by \(H^0(K^q)\), the same Riemann–Roch density simultaneously produces

\[
\boxed{
N_q=(2q-1)(g-1)
}
\]

and the Quillen local-index polynomial

\[
\boxed{
\frac{6q(q-1)+1}{12\pi}G_{\rm WP}.
}
\]

After resolving the Born/DPP transport and Kodaira–Spencer channels, their finite statistical mismatch satisfies

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=
-\frac{\zeta_{\mathbb R}(-1)}{\pi}G_{\rm WP}
+O(q^2e^{-c_Xq}).
}
\tag{17.1}
\]

because \(-\zeta_{\mathbb R}(-1)=1/12\).

This formula should be read as a structural identity linking three distinct notions, not as an identification of the Riemann and Selberg zeta functions.

---

# Part IX. What remains open

## 18. Next proof obligations

1. **Uniformity over moduli.** Upgrade the fixed-surface exponential theorem to compact subsets of the thick part with uniform \(c>0\). Degeneration toward the Deligne–Mumford boundary necessarily changes the systole scale.
2. **Leading nonperturbative coefficient.** Use FRZ's systole formula and an explicit Poincaré-series expansion of \(\beta_q\) to determine the first coefficient multiplying \(e^{-q\ell_0}\) (or the smaller of the Selberg and Bergman exponents).
3. **Boundary/compactification.** Replace smooth \(\mathcal M_g\) by \(\overline{\mathcal M}_g\) and track boundary divisor corrections in Mumford/GRR/Quillen formulas.
4. **Arithmetic Riemann–Roch.** Investigate whether an Arakelov refinement gives an arithmetic-height interpretation of the finite information offset. This is a new direction, not established by the present calculation.
5. **Higher dimension.** In relative dimension \(n>1\), higher Todd components can contribute. Determine which Bernoulli numbers survive in the analog of the filtered Fisher–Quillen sector.
6. **Novelty audit.** The ingredients are classical/known. The exact equation (11.4) and its FCIG information interpretation require a broader MathSciNet/zbMATH/reference-chain audit before any originality claim.

---

# 19. Reference map

- **Hirzebruch/Grothendieck–Riemann–Roch and determinant of cohomology:** [Mum83; Eri08].
- **Quillen curvature as a differential-form GRR refinement:** [BGS88].
- **Local index theorem on compact hyperbolic moduli:** [TZ87].
- **Selberg-zeta second variation and exponential curvature remainder:** [FRZ20].
- **Constant-curvature Bergman kernel with exponentially small error:** [Ber12].
- **General high-power direct-image curvature coefficients:** [WZ21].

No cited source is claimed to state the full FCIG Todd–Selberg information decomposition (11.4).