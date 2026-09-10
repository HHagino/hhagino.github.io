# FCIG: Cyclic Fourier Profiles for Length Hessians and Bergman Orbitals

**Status:** exact mode decomposition in a fixed hyperbolic-cylinder convention  
**Date:** 2026-09-10  
**Depends on:** [`casimir-orbital-transmutation.md`](casimir-orbital-transmutation.md), [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md).  
**Bibliography:** [`casimir-orbital-transmutation.bib`](casimir-orbital-transmutation.bib).

> **Claim policy.** The Fourier decomposition below is a coordinate calculation on the cyclic cover. Axelsson--Schumacher's first/second length-variation formulae and Schumacher's resolvent field are established inputs [AS12; Sch; FRZ20]. The simultaneous diagonalization written below is **Derived here**. It is not a novelty certification.

---

## 0. Main result

Fix a primitive closed geodesic \(c\) of length \(\ell>0\). Conjugate its deck transformation on \(\mathbb H\) to

\[
z\longmapsto e^\ell z.
\]

Write

\[
z=e^w,
\qquad
w=t+i\theta,
\qquad
t\sim t+\ell,
\qquad
0<\theta<\pi.
\]

Then the hyperbolic metric is

\[
\boxed{
 ds^2=\frac{dt^2+d\theta^2}{\sin^2\theta}.
}
\tag{0.1}
\]

The closed geodesic is \(\theta=\pi/2\). With

\[
u=\cot\theta=\sinh r,\]

(0.1) becomes the Fermi-cylinder metric

\[
 ds^2=\frac{du^2}{1+u^2}+(1+u^2)dt^2.
\]

Let

\[
\Phi=\phi(w)dw^2
\]

be the holomorphic quadratic differential corresponding to a harmonic Beltrami direction. Since \(\phi(w+\ell)=\phi(w)\), choose the axis-normalized Fourier expansion

\[
\boxed{
\phi(t+i\theta)
=
\sum_{n\in\mathbb Z}
 b_n
 e^{i\nu_n t}
 e^{-\nu_n(\theta-\pi/2)},
\qquad
\nu_n=\frac{2\pi n}{\ell}.
}
\tag{0.2}
\]

Thus

\[
\phi(t+i\pi/2)=\sum_n b_ne^{i\nu_nt}.
\tag{0.3}
\]

For the hyperbolic density \(\rho=\sin^{-2}\theta\), the harmonic Beltrami coefficient is

\[
\mu=\rho^{-1}\overline\phi,
\]

so

\[
|\mu|^2
=\sin^4\theta\,|\phi|^2.
\tag{0.4}
\]

Longitudinal averaging kills the cross terms. Therefore

\[
\boxed{
\overline{|\mu|^2}(u)
=
\sum_{n\in\mathbb Z}|b_n|^2 A_{n,\ell}(u),
}
\tag{0.5}
\]

where

\[
\boxed{
A_{n,\ell}(u)
=
\frac{
\exp[-2\nu_n(\theta(u)-\pi/2)]
}{(1+u^2)^2},
\qquad
\theta(u)=\operatorname{arccot}u\in(0,\pi).
}
\tag{0.6}
\]

Let

\[
f_\mu=(1+\square_0)^{-1}|\mu|^2.
\]

Since \(\square_0\) commutes with the \(t\)-average,

\[
\boxed{
\overline f_\mu(u)
=
\sum_{n\in\mathbb Z}|b_n|^2F_{n,\ell}(u),
}
\tag{0.7}
\]

where \(F_{n,\ell}\) is the bounded solution of

\[
\boxed{
\left[
1-\frac12\partial_u((1+u^2)\partial_u)
\right]F_{n,\ell}
=A_{n,\ell}.
}
\tag{0.8}
\]

This gives a common mode basis for both geodesic-length geometry and the weighted Bergman orbital.

---

# Part I. Explicit zero-mode Green kernel

## 1. Radial resolvent

Define

\[
L_0
:=
1-\frac12\partial_u((1+u^2)\partial_u).
\]

The homogeneous equation \(L_0y=0\) has solutions

\[
y_+(u)=1+u\arctan u-\frac\pi2u,
\]

\[
y_-(u)=1+u\arctan u+\frac\pi2u.
\tag{1.1}
\]

Here \(y_+\) decays as \(u\to+\infty\), while \(y_-\) decays as \(u\to-\infty\). Their weighted Wronskian is

\[
(1+u^2)(y_-y_+'-y_-'y_+)=-\pi.
\tag{1.2}
\]

Hence the bounded Green kernel is

\[
\boxed{
G_0(u,v)
=
\frac2\pi
\begin{cases}
 y_-(u)y_+(v),&u\le v,\\
 y_-(v)y_+(u),&v<u.
\end{cases}
}
\tag{1.3}
\]

Indeed the derivative jump gives

\[
-\frac12(1+v^2)
\left[
\partial_uG_0(v^+,v)-\partial_uG_0(v^-,v)
\right]=1.
\]

Therefore

\[
\boxed{
F_{n,\ell}(u)
=
\int_{\mathbb R}G_0(u,v)A_{n,\ell}(v)dv.
}
\tag{1.4}
\]

Equations (0.7) and (1.4) turn the abstract resolvent field into an explicit diagonal quadratic form in the cyclic Fourier coefficients \(|b_n|^2\).

**Derived here.** No asymptotic expansion is used.

---

# Part II. Length variations in the same Fourier basis

## 2. First variation reads only the zero Fourier mode

Axelsson--Schumacher prove that the first variation of a closed-geodesic length is one half of the geodesic integral of the harmonic Beltrami differential [AS12]. FRZ give the same formula in their upper-half-plane convention [FRZ20].

On the central geodesic \(\theta=\pi/2\), the conformal factor has zero normal derivative, so the coordinate frame is parallel along \(t\). Using (0.3), the nonzero Fourier modes integrate to zero. Up to the harmless conjugation convention used to identify a tangent vector with \(\Phi\),

\[
\boxed{
|\partial_\mu\ell|^2
=
\frac{\ell^2}{4}|b_0|^2.
}
\tag{2.1}
\]

Thus first marked-length variation sees precisely the cyclic zero mode.

---

## 3. Second variation is one diagonal quadratic form

FRZ quote the Axelsson--Schumacher formula

\[
\boxed{
\bar\partial_\mu\partial_\mu\ell
=
\frac12\int_c
\left[
 f_\mu
+
(-D_t^2+2)^{-1}(\mu)\bar\mu
\right]dt
+
\frac1\ell|\partial_\mu\ell|^2.
}
\tag{3.1}
\]

[AS12; FRZ20].

The first integral in (3.1) is

\[
\int_c f_\mu dt
=
\ell\,\overline f_\mu(0)
=
\ell\sum_n|b_n|^2F_{n,\ell}(0).
\tag{3.2}
\]

On the axis,

\[
\mu(t,0)
=
\sum_n\overline{b_n}e^{-i\nu_nt}
\]

in the parallel frame. Hence

\[
\boxed{
\int_c
(-D_t^2+2)^{-1}(\mu)\bar\mu\,dt
=
\ell
\sum_{n\in\mathbb Z}
\frac{|b_n|^2}{\nu_n^2+2}.
}
\tag{3.3}
\]

Combining (2.1)--(3.3),

\[
\boxed{
\bar\partial_\mu\partial_\mu\ell
=
\frac\ell2
\sum_{n\in\mathbb Z}|b_n|^2
\left[
F_{n,\ell}(0)+\frac1{\nu_n^2+2}
\right]
+
\frac\ell4|b_0|^2.
}
\tag{3.4}
\]

**Derived here from the established AS/FRZ formula.** Equation (3.4) is a simultaneous cyclic-Fourier diagonalization of the scalar length Hessian.

The important information-theoretic point is immediate:

\[
\boxed{
\partial\ell\text{ reads }b_0,
\qquad
\bar\partial\partial\ell\text{ reads one weighted sum of all }|b_n|^2.
}
\tag{3.5}
\]

---

# Part III. Bergman orbitals in the same Fourier basis

## 4. Mode multipliers

For the \(m\)-th power of the primitive conjugacy class, put

\[
L=m\ell.
\]

Let

\[
\kappa_{q,L}(u)
=
\left(
\cosh\frac L2-iu\sinh\frac L2
\right)^{-2q}.
\]

Define

\[
\boxed{
\Lambda_n^{(q,m)}(\ell)
:=
\Re\int_{\mathbb R}
F_{n,\ell}(u)\kappa_{q,m\ell}(u)du.
}
\tag{4.1}
\]

Then (0.7) gives the exact diagonal decomposition

\[
\boxed{
\mathcal J_{q,m\ell}[f_\mu]
=
\sum_{n\in\mathbb Z}
|b_n|^2\Lambda_n^{(q,m)}(\ell).
}
\tag{4.2}
\]

Under the Casimir-transmutation theorem of the companion note,

\[
\boxed{
\mathcal J_{q,m\ell}[W_q]
=
\sum_n|b_n|^2
\mathscr D_{q,L}
\Lambda_n^{(q,m)}(\ell)
\bigg|_{L=m\ell},
}
\tag{4.3}
\]

where \(\mathscr D_{q,L}\) differentiates the **orbital kernel parameter \(L\)** with \(F_{n,\ell}\) held fixed.

This is not a Teichmüller derivative of \(\ell\).

---

## 5. Gamma/Fourier form of each multiplier

Let

\[
\widehat F_{n,\ell}(\xi)
=
\int_{\mathbb R}F_{n,\ell}(u)e^{i\xi u}du.
\]

Then

\[
\boxed{
\Lambda_n^{(q,m)}(\ell)
=
\frac{\cosh^{-2q}(m\ell/2)}{\Gamma(2q)}
\int_0^\infty
s^{2q-1}e^{-s}
\Re\widehat F_{n,\ell}
\left(
 s\tanh\frac{m\ell}{2}
\right)ds.
}
\tag{5.1}
\]

Thus the two geometric observables are diagonal in the **same** coefficients \(|b_n|^2\), but with different multipliers:

\[
\boxed{
\begin{array}{rcl}
\text{length Hessian} &:&
H_n(\ell)=\dfrac\ell2\left[F_{n,\ell}(0)+\dfrac1{\nu_n^2+2}\right]
+\dfrac\ell4\,\delta_{n0},\\[3mm]
\text{Bergman/Fisher orbital} &:&
B_n^{(q,m)}(\ell)=\mathscr D_{q,L}\Lambda_n^{(q,m)}(\ell)|_{L=m\ell}.
\end{array}
}
\tag{5.2}
\]

This is the desired common cyclic-Fourier basis.

---

# Part IV. What is and is not reconstructed by marked length data

## 6. One geodesic does not determine the Bergman profile

For a fixed primitive geodesic, \(\partial\ell\) and \(\bar\partial\partial\ell\) provide only finitely many scalar quadratic/linear functionals of the sequence \(\{b_n\}\). The Bergman orbital (4.3) uses a different \(q,m\)-dependent family of multipliers.

Therefore the classwise equality

\[
\mathcal J_{q,m\ell}[W_q]
=F(\partial\ell,\bar\partial\partial\ell)
\]

cannot be inferred from the AS scalar formula alone.

This is fully consistent with the general-profile no-go in the COT note.

---

## 7. The full marked spectrum may still reconstruct the deformation

The preceding statement is **classwise**, not global. The collection of all marked length functions on Teichmüller space is far more rigid than one length function. Thus it remains possible that the family

\[
\{\partial_\mu\ell(\gamma),
\bar\partial_\mu\partial_\mu\ell(\gamma)\}_{[\gamma]}
\]

across all conjugacy classes determines enough of \(\mu\) to reconstruct the Bergman profile globally.

The present calculation does not prove or disprove such a global reconstruction theorem.

What it does prove is the correct intermediate statement:

\[
\boxed{
\text{Selberg length response and Bergman/Fisher response are two distinct spectral filters of the same cyclic Fourier data.}
}
\tag{7.1}
\]

---

# Part V. Status of the previous COT gates

## 8. COT-2 — geometric profile theorem

**PASS in explicit cylinder coordinates, modulo standard convergence of the cyclic Fourier expansion.**

The resolvent profile is

\[
\boxed{
\overline f_\mu(u)
=
\sum_n|b_n|^2F_{n,\ell}(u),
}
\]

with explicit source (0.6) and Green representation (1.4).

Consequently

\[
\mathfrak F_{c,\mu}(\xi)
=
\sum_n|b_n|^2\widehat F_{n,\ell}(\xi).
\tag{8.1}
\]

---

## 9. COT-3 — same-mode comparison with length Hessian

**PASS as a mode decomposition; not as a scalar equality.**

Equations (3.4) and (5.2) put the length Hessian and weighted Bergman orbital in the same cyclic Fourier coefficients. They also identify precisely why the scalar length Hessian is insufficient class-by-class: it contracts those coefficients with one multiplier, while the Bergman family uses a different \((q,m)\)-dependent multiplier family.

---

## 10. Revised COT-4

The first total nonperturbative coefficient should now be attacked mode-by-mode:

\[
\boxed{
D_q(\mu)
=
\sum_{[c]}
\sum_{m\ge1}
\sum_{n\in\mathbb Z}
|b_{c,n}|^2
\left[
\text{Selberg}_{q,c,m,n}
+
\text{Bergman}_{q,c,m,n}
\right],
}
\tag{10.1}
\]

once all orientation/centralizer normalizations are fixed.

The Bergman multiplier is now explicit through (4.1)--(5.1); the Selberg multiplier follows from the AS/FRZ length-variation formulas after substituting the same Fourier coefficients.

This is a substantially smaller and more concrete problem than the original two-dimensional weighted surface integral.

---

# 11. Proof obligations

Before treating (0.5)--(5.2) as publication-ready globally:

1. audit the tensor normalization \(\mu=\rho^{-1}\overline\phi\) against the exact FRZ convention;
2. justify Fourier-series/longitudinal-average interchange up to the two ends of the cyclic cover;
3. verify boundedness conditions selecting the Green kernel (1.3) for the lift of the global resolvent field;
4. match orientation/conjugation in the first variation; equation (2.1) is insensitive to this choice;
5. audit the parallel trivialization along the central geodesic used to replace \(D_t\) by \(\partial_t\);
6. combine the mode multipliers with the exact Sun centralizer/orientation counting before summing conjugacy classes;
7. perform a literature novelty audit for cyclic-Fourier forms of the Schumacher/AS resolvent equations before originality claims.

The note is a calculation dossier, not a priority claim.
