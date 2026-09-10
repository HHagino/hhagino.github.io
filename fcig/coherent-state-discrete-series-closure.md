# FCIG: Coherent-State Discrete-Series Closure

**Status:** exact coherent-state identification + DS-A geometric/matrix-coefficient pass  
**Date:** 2026-09-10  
**Depends on:** [`disk-transported-bergman.md`](disk-transported-bergman.md), [`cyclic-relative-trace.md`](cyclic-relative-trace.md), [`k-type-group-lift.md`](k-type-group-lift.md), [`character-trace-firewall.md`](character-trace-firewall.md).

> **Claim firewall.** The object identified below is a coherent-state matrix coefficient of the holomorphic discrete series, not the Harish--Chandra character and not an ordinary trace of a single hyperbolic group element. The cyclic FCIG trace is obtained only after integrating these matrix coefficients over the primitive centralizer quotient.

---

## 0. Main theorem

Let `G=SU(1,1)` (or equivalently `PSL(2,R)` after the usual identification) and let `pi_q` be the scalar holomorphic discrete series realized on the weighted Bergman space corresponding to holomorphic `q`-differentials. Let `e_0` denote the normalized lowest-`K`-type vector and for `x=gK in G/K` define the normalized coherent state

\[
e_x:=\pi_q(g)e_0,
\]

understood up to the canonical unitary phase of the line bundle.

Then the normalized Bergman coherent overlap is

\[
\langle e_x,e_y\rangle
=\left[
\frac{\sqrt{(1-|z_x|^2)(1-|z_y|^2)}}{1-z_x\overline{z_y}}
\right]^{2q}
\]

in the disk realization.

For the positive hyperbolic translation `a_L` and the normal geodesic point `x_u`, with `u=sinh r`, the canonical `q`-canonical unitary transport phase gives

\[
\boxed{
\langle e_{x_u},\pi_q(a_L)e_{x_u}\rangle_{\rm transported}
=\kappa_{q,L}(u)
=\left(\cosh\frac L2-i\sinh\frac L2\,u\right)^{-2q}.
}
\tag{0.1}
\]

Consequently the transported Bergman diagonal is

\[
\boxed{
\mathcal K_q(a_L;x_u,x_u)
=C_q\langle e_{x_u},\pi_q(a_L)e_{x_u}\rangle_{\rm transported}
=C_q\kappa_{q,L}(u),
\qquad
C_q=\frac{2q-1}{4\pi}.
}
\tag{0.2}
\]

Thus Sun's exact hyperbolic cylinder kernel is precisely a family of coherent-state matrix coefficients of the holomorphic discrete series, parametrized by the transverse orbit `A\backslash G/K`.

---

# Part I. Lowest `K`-type coefficient

## 1. Disk realization

The scalar holomorphic discrete series is realized on the weighted Bergman space with group action of the standard form

\[
(\pi_q(g)f)(z)=j(g^{-1},z)^{-2q}f(g^{-1}z),
\]

up to the equivalent convention obtained by moving the inverse between `g` and the automorphy factor.

The lowest `K`-type vector is represented by the constant function. At the disk origin the hyperbolic element

\[
a_L(z)=\frac{Cz+S}{Sz+C},
\qquad
C=\cosh\frac L2,
\quad
S=\sinh\frac L2,
\]

therefore has lowest-`K`-type matrix coefficient

\[
\boxed{
\langle e_0,\pi_q(a_L)e_0\rangle
=C^{-2q}
=\cosh^{-2q}\frac L2.
}
\tag{1.1}
\]

This is the `u=0` specialization of the FCIG/Sun kernel.

The distinction is important:

\[
\boxed{
\text{lowest-`K` coefficient} = \kappa_{q,L}(0),
\qquad
\text{full cylinder kernel} = \text{its coherent-state translate over }G/K.
}
\tag{1.2}
\]

---

# Part II. Coherent-state translation

## 2. Covariance

For `x=g_xK`, unitarity gives

\[
\langle e_x,\pi_q(a_L)e_x\rangle
=
\langle e_0,\pi_q(g_x^{-1}a_Lg_x)e_0\rangle,
\tag{2.1}
\]

with the line-bundle phase fixed by canonical unitary transport.

On the disk choose the normal geodesic point

\[
z_x=ix,
\qquad
x=\tanh\frac r2,
\qquad
u:=\sinh r=\frac{2x}{1-x^2}.
\]

The exact disk computation proves

\[
\rho_L(x)^{2q}
\left[
\frac{\sqrt{(1-x^2)(1-|a_L(ix)|^2)}}
{1-ix\,\overline{a_L(ix)}}
\right]^{2q}
=
(C-iS\nu)^{-2q},
\]

where `rho_L(x)` is the unit-modulus `q`-canonical transport phase. Therefore (0.1) follows exactly.

No large-`q` limit or stationary-phase approximation is used.

---

# Part III. Toeplitz operators as coherent-projector integrals

## 3. Resolution of the Bergman projector

Let

\[
\Pi_x:=|e_x\rangle\langle e_x|
\]

be the rank-one coherent projector. With the FCIG normalization, the Bergman density is constant on the universal hyperbolic disk and equals

\[
C_q=\frac{2q-1}{4\pi}.
\]

Equivalently, in the weak operator sense the identity/Bergman projector admits the coherent-state resolution

\[
\boxed{
I_{\mathcal H_q}
=C_q\int_{G/K}\Pi_x\,dA(x),
}
\tag{3.1}
\]

with the measure convention inherited from the curvature `-1` metric.

Therefore a sufficiently integrable symbol `W` has Toeplitz operator

\[
\boxed{
T_W^{(q)}
=C_q\int_{G/K}W(x)\Pi_x\,dA(x)
}
\tag{3.2}
\]

in the weak sense.

Pairing with a group element gives

\[
\boxed{
\operatorname{Tr}(T_W^{(q)}\pi_q(g))
=C_q\int_{G/K}
W(x)\langle e_x,\pi_q(g)e_x\rangle dA(x)
}
\tag{3.3}
\]

whenever the operator is trace class. For periodic FCIG symbols on the universal cylinder, (3.3) is **not** taken as an absolute trace; the same integrand is instead integrated over one primitive centralizer fundamental domain.

Thus the Toeplitz and orbital pictures are literally the same coherent-state matrix-coefficient integral with different global integration domains.

---

# Part IV. Cyclic trace as a relative coherent-state trace

## 4. Primitive centralizer quotient

Let `delta` be primitive of length `ell`, `L=m ell`, and

\[
Y_\delta=\langle\delta\rangle\backslash G/K.
\]

The cyclic relative trace becomes

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_W^{(q)}U_{\delta^m}^{(q)}]
=
C_q\Re\int_{Y_\delta}
W(x)\langle e_x,\pi_q(\delta^m)e_x\rangle dA(x).
}
\tag{4.1}
\]

In Fermi coordinates this is

\[
C_q\Re\int_0^\ell\int_{\mathbb R}
W(t,u)\kappa_{q,L}(u)\,du\,dt,
\]

hence

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_W^{(q)}U_{\delta^m}^{(q)}]
=C_q\ell\mathcal J_{q,L}[W].
}
\tag{4.2}
\]

This proves that the FCIG cyclic functional is a **centralizer-reduced coherent-state trace** of the holomorphic discrete series.

---

# Part V. What the discrete-series Fourier block really is

## 5. Matrix coefficient versus character

The coherent-state coefficient

\[
m_{q,x}(g):=\langle e_x,\pi_q(g)e_x\rangle
\]

is a genuine matrix coefficient. By contrast, the Harish--Chandra character `Theta_q` is a conjugation-invariant distribution.

They are related through harmonic analysis but are not the same typed object:

\[
\boxed{
m_{q,x}(g)\neq\Theta_q(g).}
\tag{5.1}
\]

Likewise

\[
\boxed{
\int_{Y_\delta}W(x)m_{q,x}(\delta^m)dA(x)
\neq
\Theta_q(\delta^m)
}
\tag{5.2}
\]

without an explicit invariant transform.

The correct group Fourier statement is instead that the kernel `m_{q,x}` lives entirely inside the `pi_q` discrete-series block: it is one of the defining matrix coefficients of that irreducible representation.

This is already stronger than merely knowing that the orbital kernel has the same asymptotic decay as a discrete-series character.

---

# Part VI. Formal degree and normalization

## 6. Why the constant `C_q` is representation-theoretic

Discrete-series matrix coefficients satisfy Schur orthogonality with a formal degree `d_q`:

\[
\int_G
|\langle\pi_q(g)v,w\rangle|^2dg
=d_q^{-1}\|v\|^2\|w\|^2
\]

under a fixed Haar normalization.

For scalar holomorphic discrete series, the coherent-state resolution constant is the corresponding formal-degree density after passing from `G` to `G/K` and fixing `\int_Kdk=1`.

In the curvature `-1` hyperbolic-area convention used throughout FCIG, this density is exactly

\[
\boxed{C_q=\frac{2q-1}{4\pi}.}
\tag{6.1}
\]

Hence the same constant appearing in Sun's identity term, the disk Bergman kernel, Toeplitz quantization, and the cyclic trace is not accidental: these are all manifestations of the same discrete-series reproducing-kernel normalization.

---

# Part VII. Gate status

## 7. DS-A

The previous gate asked to connect the FCIG hyperbolic kernel directly to the discrete-series `K`-type block.

The exact statement is now:

\[
\boxed{
\kappa_{q,L}(u)
=
\text{canonically transported coherent-state matrix coefficient of }D^+_{2q-1}.
}
\]

The lowest-`K`-type coefficient is the special case `u=0`, and the transverse cylinder variable moves that vector through its coherent-state `G/K` orbit.

Therefore

\[
\boxed{\textbf{DS-A: PASS at the matrix-coefficient level.}}
\]

This does **not** yet identify the cyclic integral with the Harish--Chandra character distribution.

---

## 8. DS-B — invariant inversion closure

The remaining problem is now precisely typed.

For a compactly supported or Schwartz-class deformation symbol, define the coherent-state Toeplitz kernel

\[
F_{q,W}(g)
:=
C_q\int_{G/K}W(x)m_{q,x}(g)dA(x).
\]

For periodic FCIG data replace the full `G/K` integral by the appropriate centralizer-reduced distribution.

The next target is to embed this object into a standard Harish--Chandra Schwartz/distribution space and prove its invariant Fourier inversion formula. One must then determine exactly how the `pi_q` block pairs with the hyperbolic orbital transform and how the Weyl denominator enters that passage.

So the new frontier is

\[
\boxed{
\textbf{DS-B: coherent matrix coefficient}
\to
\textbf{Harish--Chandra invariant inversion}.}
\]

---

# Part VIII. FCIG synthesis

The nonperturbative hyperbolic information channel now has the exact architecture

\[
\boxed{
\begin{aligned}
|\mu|^2
&\xrightarrow{(1+\square_0)^{-1}}
f_\mu\\
&\xrightarrow{\text{Toeplitz}}
C_q\int f_\mu(x)|e_x\rangle\langle e_x|dA(x)\\
&\xrightarrow{\text{hyperbolic insertion}}
C_q f_\mu(x)\langle e_x,\pi_q(a_L)e_x\rangle\\
&\xrightarrow{\text{centralizer quotient}}
C_q\ell\mathcal J_{q,L}[f_\mu]\\
&\xrightarrow{\text{Weyl normalization}}
\frac{C_q\ell}{2\sinh(L/2)}\widetilde{\mathcal J}_{q,L}[f_\mu]\\
&\xrightarrow{\text{DS-B}}
\text{Harish--Chandra/Selberg spectral block}.
\end{aligned}
}
\]

The first five arrows are now explicit. Only the last invariant-inversion arrow remains open.

## Sources

- Standard holomorphic-discrete-series weighted Bergman realization of `SU(1,1)` / `SL(2,R)`.
- Harish--Chandra discrete-series orthogonality/formal-degree theory.
- Jingzhou Sun, *On the Bergman Kernel of complex hyperbolic manifolds*, arXiv:2511.16240v3 (2026).
- See also the FCIG exact disk derivation in [`disk-transported-bergman.md`](disk-transported-bergman.md).
