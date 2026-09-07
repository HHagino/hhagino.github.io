# FCIG Explicit Model IIIb: Exact Multidimensional Bergman Lattice Formula

**Status:** Gate E worked derivation / v0.3  
**Date:** 2026-09-08

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are calculations carried out in this FCIG note. Statements marked **FCIG interpretation** are not attributed to the cited literature.

This note closes the multidimensional Bergman-lattice gate left open in `abelian-model.md`.

The ambient geometry is the principally polarized abelian variety

\[
A_\Omega=\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g),
\qquad
\Omega=X+iY\in\mathfrak H_g,
\]

with the same theta basis, Hermitian metric, and normalized volume conventions as Explicit Model III.

**Established background.** Several-variable theta functions and the line-bundle description of principally polarized abelian varieties are classical [Mum83; BL04]. Explicit links between theta embeddings and Bergman/balanced geometry on principally polarized abelian varieties are studied by Wang and Yu [WY09]. General local Bergman-kernel asymptotics are standard [Zel98; Lu00; MM07]. Generalized Poisson summation is classical and has long been used in theta-function theory [Han69]. None of these references is cited as the source of the normalization-dependent exact Fourier formula derived below.

---

## 1. Theta-state Bergman density

Let

\[
\mathbf j\in(\mathbf Z/k\mathbf Z)^g
\]

and use the level-\(k\) theta sections

\[
s_{\mathbf j}^{(k)}(z,\Omega)
=
\sum_{n\in\mathbf Z^g}
\exp\!\left[
\pi i k
\left(n+\frac{\mathbf j}{k}\right)^T
\Omega
\left(n+\frac{\mathbf j}{k}\right)
+
2\pi i k
\left(n+\frac{\mathbf j}{k}\right)^Tz
\right].
\]

From Explicit Model III,

\[
\left\langle
s_{\mathbf j}^{(k)},s_{\mathbf m}^{(k)}
\right\rangle
=
\delta_{\mathbf j\mathbf m}\det(2kY)^{-1/2}.
\]

Hence an orthonormal basis is

\[
\widehat s_{\mathbf j}^{(k)}
=
\det(2kY)^{1/4}s_{\mathbf j}^{(k)}.
\]

Write

\[
z=x+\Omega t,
\qquad x,t\in[0,1)^g.
\]

The pointwise Hermitian metric is

\[
\|f(z)\|_{h_k}^2
=
|f(z)|^2
\exp\!\left[-2\pi k(\operatorname{Im}z)^TY^{-1}(\operatorname{Im}z)\right].
\]

Since \(\operatorname{Im}z=Yt\), define

\[
\boxed{
B_{g,k}(x,t;\Omega)
=
\det(2kY)^{1/2}
 e^{-2\pi k t^TYt}
\sum_{\mathbf j\in(\mathbf Z/k\mathbf Z)^g}
\left|s_{\mathbf j}^{(k)}(x+\Omega t,\Omega)\right|^2.
}
\tag{1.1}
\]

By orthonormality and the normalized volume convention,

\[
\int_{A_\Omega}B_{g,k}\,\frac{\omega_\Omega^g}{g!}=k^g.
\]

---

## 2. Normalized period-lattice quadratic form

For

\[
p,\ell\in\mathbf Z^g,
\]

define

\[
\boxed{
Q_\Omega(p,\ell)
=
(\ell-\Omega p)^*Y^{-1}(\ell-\Omega p).
}
\tag{2.1}
\]

Since \(\Omega=X+iY\), this is equivalently

\[
\boxed{
Q_\Omega(p,\ell)
=
(\ell-Xp)^TY^{-1}(\ell-Xp)+p^TYp.
}
\tag{2.2}
\]

Thus \(Q_\Omega\) is positive definite on the rank-\(2g\) lattice \(\mathbf Z^{2g}\).

Define its shortest nonzero value

\[
\boxed{
\mu(\Omega)
=
\min_{(p,\ell)\in\mathbf Z^{2g}\setminus\{0\}}
Q_\Omega(p,\ell)>0.
}
\tag{2.3}
\]

This is the higher-dimensional normalized shortest-vector scale that will control the nonzero Bergman modes.

---

## 3. Exact Poisson-resummed formula

### Theorem 3.1 — exact multidimensional Bergman lattice formula

In the conventions above,

\[
\boxed{
\begin{aligned}
B_{g,k}(x,t;\Omega)
&=
k^g
\sum_{p,\ell\in\mathbf Z^g}
\exp\!\left[-\frac{\pi k}{2}Q_\Omega(p,\ell)\right]\\
&\qquad\times
\exp\!\left[
2\pi i k(p^Tx+\ell^Tt)
+\pi i k p^T\ell
\right].
\end{aligned}
}
\tag{3.1}
\]

**Derived here.** Equation (3.1) follows from the explicit theta basis, the exact Gram normalization from Explicit Model III, and multivariate Poisson summation. The general theta/Bergman and Poisson literature [Mum83; WY09; Han69] supplies background, not this exact convention-dependent phase and normalization.

### Proof

Rewrite each theta section using

\[
r=kn+\mathbf j\in\mathbf Z^g,
\]

so that

\[
s_{\mathbf j}^{(k)}
=
\sum_{r\equiv\mathbf j\; (\mathrm{mod}\;k)}
\exp\!\left[
\frac{\pi i}{k}r^T\Omega r+2\pi i r^Tz
\right].
\]

Summing \(|s_{\mathbf j}^{(k)}|^2\) over \(\mathbf j\) enforces

\[
r-s\in k\mathbf Z^g.
\]

Set

\[
r=m+kp,
\qquad
s=m,
\qquad
m,p\in\mathbf Z^g.
\]

After inserting \(z=x+\Omega t\) and the Hermitian Gaussian, the exponent simplifies to

\[
-\frac{2\pi}{k}u^TYu
-\frac{\pi k}{2}p^TYp
+2\pi i p^TXu
+2\pi i k p^Tx,
\]

where

\[
u=m+k\left(t+\frac p2\right).
\]

Therefore the remaining \(m\)-sum is

\[
\sum_{m\in\mathbf Z^g}
\exp\!\left[
-\frac{2\pi}{k}u^TYu+2\pi i p^TXu
\right].
\]

Apply the multivariate Poisson formula

\[
\sum_{m\in\mathbf Z^g}f(m+a)
=
\sum_{\ell\in\mathbf Z^g}
 e^{2\pi i\ell^Ta}\widehat f(\ell),
\]

with Fourier convention

\[
\widehat f(\ell)
=
\int_{\mathbf R^g}f(u)e^{-2\pi i\ell^Tu}\,du.
\]

For

\[
f(u)
=
\exp\!\left[-\frac{2\pi}{k}u^TYu+2\pi i p^TXu\right],
\]

the Gaussian Fourier transform gives

\[
\widehat f(\ell)
=
\det\!\left(\frac{2Y}{k}\right)^{-1/2}
\exp\!\left[
-\frac{\pi k}{2}
(\ell-Xp)^TY^{-1}(\ell-Xp)
\right].
\]

The shift

\[
a=k\left(t+\frac p2\right)
\]

contributes

\[
 e^{2\pi i k\ell^Tt+\pi i k p^T\ell}.
\]

Multiplying by the remaining factor

\[
 e^{-\pi k p^TYp/2}e^{2\pi i k p^Tx}
\]

and by the Bergman normalization \(\det(2kY)^{1/2}\), the determinants cancel as

\[
\det(2kY)^{1/2}
\det\!\left(\frac{2Y}{k}\right)^{-1/2}
=k^g.
\]

Using (2.2) yields (3.1). \(\square\)

---

## 4. Reality and the zero mode

The zero lattice vector \((p,\ell)=(0,0)\) contributes exactly

\[
k^g.
\]

The term indexed by \((-p,-\ell)\) is the complex conjugate of the term indexed by \((p,\ell)\), so the full sum is real, as required for a Bergman density.

Thus

\[
\boxed{
B_{g,k}(x,t;\Omega)
=
k^g+\text{nonzero normalized period-lattice modes}.
}
\tag{4.1}
\]

The phase

\[
e^{\pi i k p^T\ell}
\]

is convention-sensitive. It belongs to the specific theta trivialization used here and should not be quoted independently of these conventions.

---

## 5. Exponential bound

### Proposition 5.1 — fixed-\(\Omega\) exponential suppression

For every fixed \(\Omega\in\mathfrak H_g\),

\[
\boxed{
B_{g,k}(x,t;\Omega)
=
k^g\left[1+O_\Omega\!\left(e^{-\pi k\mu(\Omega)/2}\right)\right]
}
\tag{5.1}
\]

uniformly in \((x,t)\in[0,1)^{2g}\).

**Derived here.** This estimate is an elementary consequence of the exact formula and the positive-definite lattice Gaussian.

### Proof

From (3.1),

\[
\left|\frac{B_{g,k}}{k^g}-1\right|
\le
\sum_{(p,\ell)\ne0}
 e^{-\pi kQ_\Omega(p,\ell)/2}.
\]

For \(k\ge1\), split

\[
 e^{-\pi kQ/2}
=
 e^{-\pi (k-1)Q/2}e^{-\pi Q/2}
\le
 e^{-\pi (k-1)\mu(\Omega)/2}e^{-\pi Q/2}.
\]

Since \(Q_\Omega\) is positive definite,

\[
C(\Omega)
:=
\sum_{(p,\ell)\ne0}e^{-\pi Q_\Omega(p,\ell)/2}<\infty.
\]

Therefore

\[
\left|\frac{B_{g,k}}{k^g}-1\right|
\le
C(\Omega)
 e^{-\pi (k-1)\mu(\Omega)/2},
\]

which is equivalent to (5.1). \(\square\)

On a compact subset \(K\Subset\mathfrak H_g\), positive definiteness is uniform, so one likewise obtains

\[
B_{g,k}
=
k^g\left[1+O_K(e^{-c_Kk})\right]
\]

for some \(c_K>0\).

Near a degenerating boundary, the normalized shortest-vector scale can tend to zero, and uniform exponential suppression can fail. This is the higher-dimensional analogue of the elliptic cusp phenomenon.

---

## 6. Comparison with ordinary Bergman asymptotics

General Bergman asymptotics for positive line bundles have a local expansion of the form

\[
B_k(x)
\sim
k^g+a_1(x)k^{g-1}+a_2(x)k^{g-2}+\cdots,
\]

where the coefficients are local curvature polynomials [Zel98; Lu00; MM07].

For the translation-invariant flat metric on \(A_\Omega\), all positive-order local curvature invariants vanish. The exact formula (3.1) therefore refines the statement

\[
B_{g,k}=k^g+O(k^{-\infty})
\]

by resolving the beyond-all-orders remainder into explicit period-lattice Fourier modes.

**FCIG interpretation.** This motivates the decomposition

\[
\boxed{
\log B_{g,k}
=
g\log k
+
\underbrace{0+0/k+0/k^2+\cdots}_{\text{flat local curvature sector}}
+
\underbrace{O(e^{-k\mu(\Omega)})}_{\text{global lattice sector}}.
}
\tag{6.1}
\]

The phrase “global lattice sector” is FCIG terminology; the exact Fourier formula and exponential estimate are mathematical statements.

---

## 7. Genus-one reduction

For \(g=1\), put \(\Omega=\tau\), \(Y=\operatorname{Im}\tau\). Then

\[
Q_\tau(p,\ell)
=
\frac{|\ell-p\tau|^2}{Y},
\]

and (3.1) becomes

\[
\boxed{
B_k(x,t;\tau)
=
k\sum_{p,\ell\in\mathbf Z}
 e^{-\frac{\pi k}{2Y}|\ell-p\tau|^2}
 e^{2\pi i k(px+\ell t)+\pi i k p\ell},
}
\]

which is exactly the formula obtained in Explicit Model I.

Thus Gate E passes the reduction check.

---

## 8. Numerical non-diagonal genus-two check

The companion script `abelian-bergman.py` evaluates both sides independently for

\[
\Omega
=
\begin{pmatrix}
0.2+1.3i & 0.15+0.2i\\
0.15+0.2i & -0.1+1.1i
\end{pmatrix},
\]

whose imaginary part is positive definite.

At

\[
x=(0.13,0.29),
\qquad
t=(0.22,0.37),
\]

the truncated direct theta sum and truncated Poisson sum agree to near floating-point precision for \(k=2,3,4\) with the cutoffs stated in the script. The same script enumerates a finite window of the normalized period lattice to estimate \(\mu(\Omega)\).

The numerical test checks phases and normalization; Theorem 3.1 is analytic and does not depend on the numerical computation.

---

## 9. Gate E status

The original Gate E requirements are now met at the level of this explicit ppav model:

- exact multivariate Poisson-resummed formula: **passed**;
- convention-sensitive phase fixed: **passed**;
- shortest-vector invariant identified: **passed**;
- exponential bound for fixed \(\Omega\) and compact subsets: **passed**;
- non-diagonal genus-two numerical verifier: **passed**;
- degeneration mechanism identified through \(\mu(\Omega)\to0\): **passed qualitatively**; detailed boundary asymptotics remain a later problem.

The next independent v0.3 gate is therefore the global finite Weil/metaplectic descent of Issue #6.

---

## 10. Current FCIG decomposition on flat abelian fibers

Combining Explicit Models III and IIIb gives

\[
\boxed{
\begin{aligned}
\operatorname{rank}\mathcal H_k&=k^g,\\
F_{\det\mathcal H_k}&=-\frac{k^g}{2}F_{\lambda_H},\\
B_{g,k}&=k^g+O_\Omega(e^{-\pi k\mu(\Omega)/2}).
\end{aligned}
}
\]

Thus three mathematically distinct layers are simultaneously visible:

\[
\boxed{
\text{fiber capacity}
\oplus
\text{moduli determinant curvature}
\oplus
\text{nonperturbative period-lattice modes}.
}
\]

The fourth layer — residual global metaplectic holonomy after local curvature cancellation — is the subject of Gate D / Issue #6.

No gravitational field equation is inferred from this decomposition.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Mum83]** D. Mumford, *Tata Lectures on Theta I*, Birkhäuser (1983).
- **[BL04]** C. Birkenhake & H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer (2004).
- **[WY09]** X. Wang & H. P. Yu, “Theta function and Bergman metric on Abelian varieties,” *New York Journal of Mathematics* **15** (2009), 19–35.
- **[Han69]** J.-I. Hano, “On Theta Functions and Weil's Generalized Poisson Summation Formula,” *Transactions of the American Mathematical Society* **141** (1969), 195–210.
- **[Zel98]** S. Zelditch, “Szegő Kernels and a Theorem of Tian,” *IMRN* **1998**(6), 317–331.
- **[Lu00]** Z. Lu, “On the Lower Order Terms of the Asymptotic Expansion of Tian–Yau–Zelditch,” *American Journal of Mathematics* **122**(2) (2000), 235–273.
- **[MM07]** X. Ma & G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Birkhäuser (2007).
