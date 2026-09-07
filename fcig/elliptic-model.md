# FCIG Explicit Model I: Elliptic Curves, Theta States, and Moduli Curvature

**Status:** worked research note / exact toy model  
**Date:** 2026-09-08

> The purpose of this note is to turn the abstract FCIG architecture into one model where essentially every object can be written down explicitly.
>
> The central phenomenon is a three-way split:
>
> \[
> \boxed{
> \text{fiber state counting}
> \;\oplus\;
> \text{global lattice/holonomy corrections}
> \;\oplus\;
> \text{moduli curvature}.
> }
> \]
>
> On a flat elliptic fiber, all local curvature coefficients in the Bergman expansion vanish, yet the exact Bergman density retains exponentially small lattice terms. Meanwhile the Hodge line over the moduli parameter \(\tau\) has nonzero hyperbolic curvature. This gives an explicit laboratory for separating local geometry from global and modular data.

---

## 1. The elliptic family

Let

\[
\tau=u+iY\in\mathbb H,
\qquad Y=\operatorname{Im}\tau>0,
\]

and define

\[
E_\tau
=
\mathbf C/(\mathbf Z+\tau\mathbf Z).
\]

Write points as

\[
z=x+\tau t,
\qquad x,t\in[0,1).
\]

The normalized flat Kähler form is

\[
\boxed{
\omega_\tau
=
\frac{i}{2Y}\,dz\wedge d\bar z,
\qquad
\int_{E_\tau}\omega_\tau=1.
}
\]

The scalar curvature is identically zero:

\[
\operatorname{Scal}_{\omega_\tau}=0.
\]

This will let us separate local curvature corrections from genuinely global effects.

---

## 2. The degree-one theta line

Take the classical degree-one theta line \(L\to E_\tau\). In the universal cover \(\mathbf C\), a holomorphic section is represented by a function satisfying

\[
f(z+1)=f(z),
\]

\[
f(z+\tau)
=
 e^{-\pi i\tau-2\pi iz}f(z).
\]

The Jacobi theta function

\[
\vartheta(z\mid\tau)
=
\sum_{n\in\mathbf Z}
\exp\left(
\pi i\tau n^2+2\pi inz
\right)
\]

is such a section.

For \(L^k\), define level-\(k\) theta sections

\[
\boxed{
s_j^{(k)}(z,\tau)
=
\vartheta
\begin{bmatrix}
 j/k\\0
\end{bmatrix}
(kz\mid k\tau),
\qquad
j=0,\ldots,k-1.
}
\]

Explicitly,

\[
s_j^{(k)}(z,\tau)
=
\sum_{n\in\mathbf Z}
\exp\left[
\pi i k\tau\left(n+\frac jk\right)^2
+
2\pi i k\left(n+\frac jk\right)z
\right].
\]

These obey

\[
s_j^{(k)}(z+1)=s_j^{(k)}(z),
\]

\[
s_j^{(k)}(z+\tau)
=
 e^{-\pi i k\tau-2\pi ikz}s_j^{(k)}(z),
\]

and form a basis of

\[
H^0(E_\tau,L^k),
\qquad
\dim H^0(E_\tau,L^k)=k.
\]

Thus the FCIG capacity entropy in this model is exactly

\[
\boxed{
S_k^{\mathrm{cap}}=\log k.
}
\]

No asymptotic Riemann–Roch approximation is needed here.

---

## 3. Hermitian metric and curvature

Use the standard translation-invariant curvature metric on the pullback of \(L^k\):

\[
\boxed{
\|f(z)\|_{h_k}^2
=
|f(z)|^2
\exp\left(
-\frac{2\pi k(\operatorname{Im}z)^2}{Y}
\right).
}
\]

The automorphy factor of \(f\) is cancelled by the Gaussian weight, so the norm descends to \(E_\tau\).

If

\[
\phi_k(z)=\frac{2\pi k(\operatorname{Im}z)^2}{Y},
\]

then, with the convention

\[
c_1(L^k,h_k)
=
\frac{i}{2\pi}F_{h_k},
\qquad
F_{h_k}=-\partial\bar\partial\log h_k,
\]

we obtain

\[
\boxed{
c_1(L^k,h_k)=k\omega_\tau.}
\]

Hence

\[
\deg L^k=k.
\]

This is the fiber quantization sector.

---

## 4. Exact \(L^2\) Gram matrix of the theta basis

Use the normalized fiber measure \(\omega_\tau\). Define

\[
\langle s,r\rangle_{L^2}
=
\int_{E_\tau}
 h_k(s,r)\,\omega_\tau.
\]

### Proposition 4.1 — exact orthogonality

For \(j,m\in\{0,\ldots,k-1\}\),

\[
\boxed{
\left\langle
s_j^{(k)},s_m^{(k)}
\right\rangle_{L^2}
=
\delta_{jm}\frac{1}{\sqrt{2kY}}.
}
\]

### Calculation

Write

\[
z=x+\tau t,
\qquad x,t\in[0,1).
\]

For fixed \(j\), put

\[
a_n=n+\frac jk.
\]

The \(x\)-integration kills all off-diagonal Fourier terms:

\[
\int_0^1
 e^{2\pi ik(a_n-a_m)x}\,dx
=
\delta_{nm}.
\]

The remaining Gaussian is

\[
\sum_{n\in\mathbf Z}
\int_0^1
\exp\left[
-2\pi kY(a_n+t)^2
\right]dt.
\]

The intervals

\[
\left[n+\frac jk,n+\frac jk+1\right]
\]

partition \(\mathbf R\), so

\[
\sum_n\int_0^1 e^{-2\pi kY(a_n+t)^2}dt
=
\int_{\mathbf R}e^{-2\pi kYq^2}dq
=
\frac1{\sqrt{2kY}}.
\]

Therefore the orthonormal basis is

\[
\boxed{
\widehat s_j^{(k)}
=
(2kY)^{1/4}s_j^{(k)}.
}
\]

This explicit normalization will control both the Bergman density and the determinant-line curvature.

---

## 5. Exact Bergman density

Define

\[
B_k(z;\tau)
=
\sum_{j=0}^{k-1}
\left\|
\widehat s_j^{(k)}(z,\tau)
\right\|_{h_k}^2.
\]

Equivalently,

\[
\boxed{
B_k(z;\tau)
=
\sqrt{2kY}\,
 e^{-2\pi k(\operatorname{Im}z)^2/Y}
\sum_{j=0}^{k-1}
\left|
\vartheta
\begin{bmatrix}j/k\\0\end{bmatrix}
(kz\mid k\tau)
\right|^2.
}
\]

By construction,

\[
\int_{E_\tau}B_k\,\omega_\tau=k.
\]

For \(k=1\), \(B_1\) cannot be constant because the unique theta section has a zero. Thus flat fiber geometry does **not** imply an exactly constant finite-\(k\) density.

What is true is subtler.

---

## 6. Poisson-resummed Bergman formula

Write

\[
\tau=u+iY,
\qquad
z=x+\tau t.
\]

A direct expansion of the theta sum, followed by Poisson summation, gives the exact Fourier formula

\[
\boxed{
\begin{aligned}
B_k(x,t;\tau)
=
 k
\sum_{(p,\ell)\in\mathbf Z^2}
&\exp\left[
-\frac{\pi k}{2Y}
|\ell-p\tau|^2
\right]\\
&\times
\exp\left[
2\pi ik(px+\ell t)
+\pi ikp\ell
\right].
\end{aligned}
}
\tag{6.1}
\]

The \((p,\ell)=(0,0)\) term is exactly \(k\). All other terms are nonzero Fourier modes controlled by the normalized lattice lengths

\[
\frac{|\ell-p\tau|^2}{Y}.
\]

Define the normalized systolic quantity

\[
\boxed{
\mu(\tau)
=
\min_{(p,\ell)\neq(0,0)}
\frac{|\ell-p\tau|^2}{Y}.
}
\]

For fixed \(\tau\), equation (6.1) implies

\[
\boxed{
B_k(z;\tau)
=
k\left[
1+O_\tau\left(e^{-\pi k\mu(\tau)/2}\right)
\right].
}
\tag{6.2}
\]

The estimate is uniform on compact subsets of moduli where \(\mu(\tau)\) is bounded away from zero.

---

## 7. Local curvature versus global lattice memory

The flat metric has

\[
\operatorname{Scal}=0,
\qquad
\operatorname{Ric}=0,
\qquad
\nabla^rR=0.
\]

Therefore every positive-power local curvature coefficient in the usual Tian–Catlin–Zelditch expansion vanishes.

In other words, at the level of the formal semiclassical expansion,

\[
B_k\sim k.
\]

But equation (6.1) shows that the **exact** answer is

\[
B_k
=
k
+
\text{exponentially small lattice Fourier modes}.
\]

Hence the finite-\(k\) local state density contains information invisible to every order of the local \(1/k\)-curvature expansion.

This motivates the FCIG split

\[
\boxed{
\log B_k
=
\underbrace{\log k}_{\text{global capacity}}
+
\underbrace{\sum_{r\ge1}a_rk^{-r}}_{\text{local curvature sector}}
+
\underbrace{O(e^{-k\mu})}_{\text{global lattice/holonomy sector}}.
}
\]

For the flat elliptic curve,

\[
a_r=0\quad\text{for all }r,
\]

while the nonperturbative sector need not vanish.

This is an explicit example where **global geometric information survives after all local curvature coefficients disappear**.

---

## 8. The cusp as loss of nonperturbative suppression

The quantity \(\mu(\tau)\) is controlled by the shortest vector of the normalized lattice.

When

\[
Y=\operatorname{Im}\tau\to\infty,
\]

one has, for example from \((p,\ell)=(0,1)\),

\[
\mu(\tau)\le\frac1Y\to0.
\]

Therefore the exponential suppression

\[
e^{-\pi k\mu(\tau)/2}
\]

is not uniform near the cusp.

So the degeneration of the elliptic curve has a state-density signature:

\[
\boxed{
\text{cusp degeneration}
\quad\Longrightarrow\quad
\text{nonperturbative lattice corrections become unsuppressed unless }k/Y\to\infty.
}
\]

This gives a clean double-scaling parameter

\[
\frac{k}{Y}.
\]

It is a natural quantity to examine in any attempt to connect semiclassical quantization with degeneration in moduli space.

---

## 9. Heat equation and the theta-state connection

The Jacobi theta function satisfies the classical heat equation

\[
4\pi i\,\partial_\tau\vartheta(z\mid\tau)
=
\partial_z^2\vartheta(z\mid\tau).
\]

For the level-\(k\) states

\[
s_j^{(k)}(z,\tau)
=
\vartheta\begin{bmatrix}j/k\\0\end{bmatrix}(kz\mid k\tau),
\]

the chain rule gives

\[
\boxed{
\left(
\partial_\tau
-
\frac{1}{4\pi ik}\partial_z^2
\right)
s_j^{(k)}
=0.
}
\tag{9.1}
\]

Thus variation in complex structure is governed by a heat operator.

This is the most explicit form, in this toy model, of a connection between

\[
\boxed{
\text{variation in moduli}
\longleftrightarrow
\text{evolution of quantum states}.
}
\]

The heat connection is naturally flat/projectively flat only after one keeps careful track of scalar normalizations and modular multipliers.

---

## 10. The Hodge line over \(\mathbb H\)

Let

\[
\lambda_H
=
\pi_*\Omega^1_{\mathcal E/\mathbb H}
\]

be the Hodge line of the universal elliptic family over the upper half-plane.

A holomorphic frame is

\[
\eta=dz.
\]

Give it the natural \(L^2\) metric

\[
\|dz\|_H^2
=
\frac{i}{2}
\int_{E_\tau}dz\wedge d\bar z
=
Y.
\]

Using the Chern-curvature convention

\[
F_h=-\partial\bar\partial\log h,
\]

we obtain

\[
\boxed{
F_{\lambda_H}
=
-\partial\bar\partial\log Y
=
\frac{1}{4Y^2}
 d\tau\wedge d\bar\tau.
}
\tag{10.1}
\]

Therefore

\[
c_1(\lambda_H,h_H)
=
\frac{i}{2\pi}F_{\lambda_H}
=
\frac{1}{4\pi}\omega_{\mathrm{hyp}},
\]

where

\[
\boxed{
\omega_{\mathrm{hyp}}
=
\frac{i}{2Y^2}
 d\tau\wedge d\bar\tau
}
\]

is the hyperbolic area form.

Since a standard fundamental domain for \(\mathrm{PSL}_2(\mathbf Z)\) has hyperbolic area \(\pi/3\), this normalization gives the familiar orbifold degree

\[
\int_{\mathcal M_{1,1}}c_1(\lambda_H)=\frac1{12}.
\]

Thus the fiber may be flat while the moduli Hodge line is positively curved.

---

## 11. Determinant of the theta-state bundle

Let

\[
\mathcal H_k\to\mathbb H
\]

be the rank-\(k\) bundle with fiber

\[
(\mathcal H_k)_\tau
=
H^0(E_\tau,L_\tau^k).
\]

Use the holomorphic frame

\[
(s_0^{(k)},\ldots,s_{k-1}^{(k)}).
\]

From Proposition 4.1 the Gram matrix is

\[
G_k(\tau)
=
\frac1{\sqrt{2kY}}I_k.
\]

Hence the determinant frame

\[
\Sigma_k
=
s_0^{(k)}\wedge\cdots\wedge s_{k-1}^{(k)}
\]

has squared norm

\[
\boxed{
\|\Sigma_k\|_{\det L^2}^2
=
\det G_k
=
(2kY)^{-k/2}.
}
\tag{11.1}
\]

Its Chern curvature is therefore

\[
\begin{aligned}
F_{\det\mathcal H_k}
&=
-\partial\bar\partial
\log(2kY)^{-k/2}\\
&=
-\frac{k}{2}
F_{\lambda_H}.
\end{aligned}
\]

Thus we obtain the exact local identity

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{k}{2}F_{\lambda_H}.
}
\tag{11.2}
\]

Equivalently,

\[
\boxed{
F_{\det\mathcal H_k}
+
\frac{k}{2}F_{\lambda_H}
=0.
}
\tag{11.3}
\]

This is the sharpest concrete FCIG relation in the elliptic model:

\[
\boxed{
\text{determinant curvature of the quantum-state family}
\longleftrightarrow
\text{Hodge curvature of moduli}.
}
\]

The factor \(k/2\) also signals the familiar half-integral-weight/metaplectic phenomenon of theta functions. Globally over a modular quotient, one must include the Weil/theta multiplier system; equation (11.2) is a local curvature statement on \(\mathbb H\), not by itself a complete global descent theorem.

---

## 12. Metric renormalization and residual holonomy

The natural \(L^2\) norm of each theta basis vector is

\[
\|s_j^{(k)}\|_{L^2}^2
=(2kY)^{-1/2}.
\]

Rescale the Hermitian inner product by

\[
\langle\cdot,\cdot\rangle_{\mathrm{heat}}
=
\sqrt{2kY}
\langle\cdot,\cdot\rangle_{L^2}.
\]

Then the holomorphic theta frame becomes orthonormal:

\[
\|s_j^{(k)}\|_{\mathrm{heat}}^2=1.
\]

Consequently the determinant metric is locally flat on \(\mathbb H\).

The curvature removed by this scalar renormalization is exactly

\[
\frac{k}{2}F_{\lambda_H}.
\]

This supports the following FCIG interpretation:

\[
\boxed{
\text{a scalar local counterterm can cancel curvature locally,
while modular multiplier/holonomy data can remain globally.}
}
\]

This sentence is an interpretation, not a new theorem about anomalies. The exact mathematical content is the metric rescaling and curvature identity above.

---

## 13. Flat fiber, curved moduli

We can now display the three sectors side by side.

### Fiber geometry

\[
\operatorname{Scal}(E_\tau)=0.
\]

### Fiber state capacity

\[
\dim H^0(E_\tau,L^k)=k,
\qquad
S_k^{\mathrm{cap}}=\log k.
\]

### Exact local state density

\[
B_k
=
k+O_\tau(e^{-\pi k\mu(\tau)/2}).
\]

The correction is global/lattice-sensitive rather than a local polynomial curvature term.

### Moduli curvature

\[
F_{\lambda_H}
=
\frac{1}{4Y^2}d\tau\wedge d\bar\tau
\neq0.
\]

### Quantum determinant versus moduli

\[
F_{\det\mathcal H_k}
=
-\frac{k}{2}F_{\lambda_H}.
\]

Hence

\[
\boxed{
\text{flat fiber}
\centernot\Rightarrow
\text{flat family over moduli}.
}
\]

This is the conceptual gain of passing from a single \((X,L)\) to a family \(\pi:(\mathcal X,\mathscr L)\to B\).

---

## 14. Refined FCIG decomposition suggested by the model

The elliptic calculation suggests replacing a single “entropy-curvature” relation with a transseries-like hierarchy:

\[
\boxed{
\log B_k
=
\underbrace{S_{\mathrm{capacity}}}_{\log k}
+
\underbrace{S_{\mathrm{local}}}_{\text{curvature }1/k\text{-series}}
+
\underbrace{S_{\mathrm{global}}}_{e^{-k\mu}\text{ lattice/holonomy}}
.
}
\]

Meanwhile the family direction carries an independent curvature sector

\[
\boxed{
F_{\mathrm{moduli}}
\sim
F_{\lambda_H}
\sim
-\frac{2}{k}F_{\det\mathcal H_k}.
}
\]

Thus FCIG should distinguish at least four information-geometric observables:

1. **capacity** — rank / state-space dimension;
2. **local density** — Bergman asymptotics and curvature invariants;
3. **global nonperturbative density** — lattice, topology, holonomy, tunneling-like exponential terms;
4. **family anomaly/moduli curvature** — determinant/Hodge geometry over parameter space.

The elliptic curve is the first example in which all four can be written explicitly.

---

## 15. What this model does not prove

This calculation does **not** show that

\[
F_{\lambda_H}
\]

is spacetime curvature, nor that

\[
F_{\det\mathcal H_k}
\]

generates gravity.

It does prove that, in a solvable quantized family,

- state capacity,
- exact local density,
- global lattice corrections,
- moduli curvature,
- determinant curvature,
- and a heat-equation connection

are simultaneously present and mathematically related.

The Lorentzian Gravity Closure Problem therefore becomes more specific:

\[
\boxed{
\text{Which combination of local Bergman data,
nonperturbative holonomy data,
and family determinant curvature
admits a causal thermodynamic interpretation?}
}
\]

---

## 16. Next calculations

The next exact targets are:

### A. Modular transformation law

Compute the \(S\) and \(T\) action on the level-\(k\) theta basis and identify the induced Weil representation

\[
\rho_k:\operatorname{Mp}_2(\mathbf Z)\to U(k).
\]

Then separate

\[
\text{determinant curvature}
\quad\text{from}\quad
\text{flat modular holonomy}.
\]

### B. Quillen determinant

Replace the elementary \(L^2\) determinant by a zeta-regularized determinant/Quillen metric and compare its curvature and multiplier with the Hodge line.

### C. Degeneration

Study the double-scaling regimes

\[
k\to\infty,
\qquad
Y\to\infty,
\qquad
k/Y=\text{fixed}.
\]

This is where the exponentially small lattice sector can cease to be negligible.

### D. Genus \(g\ge2\)

Move to compact hyperbolic Riemann surfaces, where the local curvature coefficients no longer vanish. Then compare

\[
\text{polynomial }1/k\text{ curvature data}
\]

against

\[
\text{exponentially small global geodesic/topological data}.
\]

This should reveal whether the elliptic transseries split survives beyond the flat case.

---

## References / checkpoints

- Classical theta functions and level-\(k\) bases for elliptic curves: standard theta-function theory; an explicit account is given in expository notes on mirror symmetry of elliptic curves.
- Wang, X. and Yu, H. P., **Theta function and Bergman metric on Abelian varieties**, *New York Journal of Mathematics* 15 (2009), 19–35.
- Classical theta heat equation:
  \[
  4\pi i\,\partial_\tau\vartheta=\partial_z^2\vartheta.
  \]
- Quillen, D., **Determinants of Cauchy–Riemann operators over a Riemann surface**, *Functional Analysis and Its Applications* 19 (1985).
- Freed, D. S., **Determinant Line Bundles Revisited**, arXiv:dg-ga/9505002.
- Ma, X. and Marinescu, G., **Holomorphic Morse Inequalities and Bergman Kernels**.
- Standard modular-form interpretation of the Hodge line: modular forms of weight \(m\) are sections of powers of the Hodge bundle.

---

## Summary formula sheet

\[
\boxed{
E_\tau=\mathbf C/(\mathbf Z+\tau\mathbf Z),
\qquad
\omega_\tau=\frac{i}{2Y}dz\wedge d\bar z.
}
\]

\[
\boxed{
\dim H^0(E_\tau,L^k)=k,
\qquad
S_k^{\mathrm{cap}}=\log k.
}
\]

\[
\boxed{
\langle s_j^{(k)},s_m^{(k)}\rangle
=\delta_{jm}(2kY)^{-1/2}.
}
\]

\[
\boxed{
B_k(x,t;\tau)
=
k\sum_{p,\ell\in\mathbf Z}
 e^{-\frac{\pi k}{2Y}|\ell-p\tau|^2}
 e^{2\pi ik(px+\ell t)+\pi ikp\ell}.
}
\]

\[
\boxed{
B_k
=
k\left[1+O_\tau(e^{-\pi k\mu(\tau)/2})\right].
}
\]

\[
\boxed{
\left(\partial_\tau-\frac1{4\pi ik}\partial_z^2\right)s_j^{(k)}=0.
}
\]

\[
\boxed{
F_{\lambda_H}
=\frac1{4Y^2}d\tau\wedge d\bar\tau,
\qquad
c_1(\lambda_H)=\frac1{4\pi}\omega_{\mathrm{hyp}}.
}
\]

\[
\boxed{
F_{\det\mathcal H_k}
=-\frac{k}{2}F_{\lambda_H}.
}
\]

The core lesson is therefore:

\[
\boxed{
\textbf{flat local geometry can coexist with nonperturbative state-density structure and curved moduli geometry.}
}
\]
