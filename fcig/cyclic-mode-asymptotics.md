# FCIG: Cyclic-Mode Asymptotics and the Recovery of the Selberg Exponential Scale

**Status:** exact zero-mode theorem + fixed-mode asymptotic derivation  
**Date:** 2026-09-10  
**Depends on:** [`cyclic-fourier-profile.md`](cyclic-fourier-profile.md), [`casimir-orbital-transmutation.md`](casimir-orbital-transmutation.md).  
**Bibliography:** [`casimir-orbital-transmutation.bib`](casimir-orbital-transmutation.bib).

> **Correction sharpened.** Dropping the Chern phase suggests the slow factor \(\cosh^{-2q}(L/2)\). Exact moment cancellation shows that this does not give the signed orbital coefficient. The calculations below show how the surviving holomorphic/Fourier contribution acquires an additional factor that converts the exponential scale to \(e^{-qL}\), the same scale that appears in the Selberg expansion. The exact conjugacy-class coefficient still requires the Sun-unfolding normalization audit.

---

## 0. Setup

For one cyclic Fourier mode put

\[
\nu=\frac{2\pi n}{\ell}
\]

and

\[
\boxed{
A_\nu(u)
:=
\frac{e^{2\nu\arctan u}}{(1+u^2)^2}.
}
\tag{0.1}
\]

This is the contribution of \(|b_n|^2\) to the longitudinal average of \(|\mu|^2\) in the axis-normalized cyclic Fourier convention of the companion note.

Let

\[
L_0
=1-\frac12\partial_u((1+u^2)\partial_u)
\]

and let \(F_\nu\) be the bounded solution

\[
\boxed{L_0F_\nu=A_\nu.}
\tag{0.2}
\]

For a hyperbolic conjugacy-length parameter \(L>0\), let

\[
\kappa_{q,L}(u)
=
\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}
\]

and

\[
\mathcal J_{q,L}[a]
=\Re\int_{\mathbb R}a(u)\kappa_{q,L}(u)du.
\tag{0.3}
\]

The weighted profile for one mode is

\[
W_{q,\nu}=A_\nu+2(q-1)F_\nu.
\tag{0.4}
\]

---

# Part I. Exact zero mode

## 1. The radial resolvent closes elementarily

For \(\nu=0\),

\[
A_0(u)=\frac1{(1+u^2)^2}.
\]

A direct differentiation gives

\[
L_0\left(\frac1{1+u^2}\right)
=
\frac2{(1+u^2)^2}.
\]

Hence

\[
\boxed{
F_0(u)=\frac1{2(1+u^2)}.
}
\tag{1.1}
\]

**Derived here, exact.**

With Fourier convention

\[
\widehat a(\xi)=\int_{\mathbb R}a(u)e^{i\xi u}du,
\]

one has for \(\xi\ge0\)

\[
\widehat F_0(\xi)=\frac\pi2e^{-\xi},
\qquad
\widehat A_0(\xi)=\frac\pi2(1+\xi)e^{-\xi}.
\tag{1.2}
\]

---

## 2. Exact zero-mode orbital

Write

\[
C=\cosh\frac L2,
\qquad
\tau=\tanh\frac L2.
\]

The Gamma/Fourier representation gives

\[
\begin{aligned}
\mathcal J_{q,L}[F_0]
&=
\frac{C^{-2q}}{\Gamma(2q)}
\frac\pi2
\int_0^\infty s^{2q-1}e^{-(1+\tau)s}ds\\
&=
\frac\pi2
C^{-2q}(1+\tau)^{-2q}.
\end{aligned}
\]

But

\[
C(1+\tau)
=\cosh\frac L2+\sinh\frac L2
=e^{L/2}.
\]

Therefore

\[
\boxed{
\mathcal J_{q,L}[F_0]
=\frac\pi2e^{-qL}.
}
\tag{2.1}
\]

This is exact for every integer \(q\ge2\).

Similarly,

\[
\boxed{
\mathcal J_{q,L}[A_0]
=
\frac\pi2e^{-qL}
\left[1+q(1-e^{-L})\right].
}
\tag{2.2}
\]

Consequently

\[
\boxed{
\mathcal J_{q,L}[W_{q,0}]
=
\frac\pi2
\left(3q-1-qe^{-L}\right)e^{-qL}.
}
\tag{2.3}
\]

**Theorem ZM (Derived here, exact).** The cyclic zero mode of the weighted Bergman/Chern orbital lives exactly on the Selberg exponential scale \(e^{-qL}\), not on the slower absolute-value scale \(\cosh^{-2q}(L/2)\).

---

## 3. Direct conversion to first length variation

For the primitive geodesic, the Axelsson--Schumacher/FRZ first variation gives, in the cyclic convention of the companion note,

\[
|\partial_\mu\ell|^2
=\frac{\ell^2}{4}|b_0|^2.
\]

For a power with \(L=m\ell\),

\[
\partial_\mu\log L
=\partial_\mu\log\ell,
\]

so

\[
|b_0|^2=4|\partial_\mu\log L|^2.
\tag{3.1}
\]

The zero-mode contribution to the **profile orbital** is therefore

\[
\boxed{
|b_0|^2\mathcal J_{q,L}[W_{q,0}]
=
2\pi
(3q-1-qe^{-L})e^{-qL}
|\partial_\mu\log L|^2.
}
\tag{3.2}
\]

This is the same deformation invariant \(|\partial\log\ell|^2\) that appears explicitly in the FRZ Selberg-zeta Hessian [FRZ20].

**Normalization firewall.** Equation (3.2) is the normalized one-dimensional profile orbital. The full conjugacy-class contribution to the surface integral still carries Sun's Bergman prefactor, the centralizer/cylinder longitudinal factor, and the oriented/unoriented counting convention. Those factors must be fixed before comparing the numerical coefficient directly with FRZ's \(A_\gamma+B_\gamma\).

---

# Part II. Exact Fourier transform of a general cyclic mode

## 4. Beta/Kummer form

Using

\[
\arctan u
=\frac1{2i}\log\frac{1+iu}{1-iu},
\]

we have

\[
\boxed{
A_\nu(u)
=(1+iu)^{-(2+i\nu)}
(1-iu)^{-(2-i\nu)}.
}
\tag{4.1}
\]

For \(\xi>0\), two Gamma integral representations and the \(u\)-Fourier integral give

\[
\boxed{
\widehat A_\nu(\xi)
=
\frac{2\pi e^{-\xi}\xi^3}{\Gamma(2+i\nu)}
U(2-i\nu,4,2\xi),
}
\tag{4.2}
\]

where \(U\) is Kummer's confluent hypergeometric function.

**Derived here, exact for \(\xi>0\).** Since \(A_\nu\) is real,

\[
\widehat A_\nu(-\xi)
=\overline{\widehat A_\nu(\xi)}.
\]

The standard Kummer asymptotic \(U(a,b,z)\sim z^{-a}\) gives

\[
\boxed{
\widehat A_\nu(\xi)
=
c_\nu e^{-\xi}\xi^{1+i\nu}
\left(1+O(\xi^{-1})\right),
}
\tag{4.3}
\]

with

\[
\boxed{
c_\nu
=\frac\pi2\frac{2^{i\nu}}{\Gamma(2+i\nu)}.
}
\tag{4.4}
\]

The Kummer asymptotic is standard [DLMF13].

---

# Part III. Fourier-space resolvent equation

## 5. Hyperbolic radial resolvent becomes an ODE in frequency

Fourier transformation of

\[
L_0F_\nu=A_\nu
\]

gives

\[
\boxed{
\left[
1+\frac{\xi^2}{2}
-\xi\partial_\xi
-\frac{\xi^2}{2}\partial_\xi^2
\right]
\widehat F_\nu(\xi)
=
\widehat A_\nu(\xi).
}
\tag{5.1}
\]

For a trial term

\[
e^{-\xi}\xi^p,
\]

the operator on the left multiplies it by

\[
(p+1)\xi
+1-\frac{p(p+1)}2.
\tag{5.2}
\]

Combining (4.3) with dominant balance in (5.1) yields

\[
\boxed{
\widehat F_\nu(\xi)
=
d_\nu e^{-\xi}\xi^{i\nu}
\left(1+O(\xi^{-1})\right),
}
\tag{5.3}
\]

where

\[
\boxed{
d_\nu
=\frac{c_\nu}{1+i\nu}
=\frac\pi2
\frac{2^{i\nu}}{(1+i\nu)\Gamma(2+i\nu)}.
}
\tag{5.4}
\]

**Status:** derived fixed-mode asymptotic. A publication proof should turn the dominant-balance argument into an error estimate for the bounded resolvent solution; the \(\nu=0\) case is already exact by Part I.

---

# Part IV. Fixed-mode nonperturbative asymptotic

## 6. Chern phase converts the exponent to \(e^{-qL}\)

Set

\[
X_{q,L}:=q(1-e^{-L}).
\tag{6.1}
\]

Insert (5.3) into the Gamma/Fourier orbital formula. For fixed \(L>0\) and fixed \(\nu\), the Gamma-ratio asymptotic gives

\[
\boxed{
\mathcal J_{q,L}[F_\nu]
=
e^{-qL}
\Re\left[d_\nu X_{q,L}^{i\nu}\right]
+O(q^{-1}e^{-qL}).
}
\tag{6.2}
\]

Likewise, using (4.3),

\[
\mathcal J_{q,L}[A_\nu]
=
q e^{-qL}
\Re\left[
 c_\nu(1-e^{-L})X_{q,L}^{i\nu}
\right]
+O(e^{-qL}).
\tag{6.3}
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal J_{q,L}[W_{q,\nu}]
={}&q e^{-qL}
\Re\Bigl[
 d_\nu X_{q,L}^{i\nu}
\\
&\qquad\times
\bigl(
3-e^{-L}+i\nu(1-e^{-L})
\bigr)
\Bigr]
+O(e^{-qL}).
\end{aligned}
}
\tag{6.4}
\]

For \(\nu=0\), (6.4) agrees with the leading term of the exact formula (2.3).

**Derived fixed-mode asymptotic.** Equation (6.4) explains the exponential scale mechanically:

\[
\boxed{
\cosh^{-2q}(L/2)
(1+\tanh(L/2))^{-2q}
=e^{-qL}.
}
\tag{6.5}
\]

The extra factor comes from the \(e^{-\xi}\) high-frequency decay of the holomorphic cyclic profile. Thus the Chern phase first annihilates the local polynomial saddle and then forces the surviving analytic contribution onto the Selberg exponent.

---

## 7. Scale match with Selberg zeta

The diagonal Bergman density carries an additional prefactor of order \(q\), namely

\[
\frac{2q-1}{4\pi}.
\]

Hence a fixed cyclic mode in the fully unfolded weighted Bergman term is naturally of size

\[
\boxed{q^2e^{-qL}}
\tag{7.1}
\]

up to centralizer/orientation constants and the fixed mode coefficient \(|b_n|^2\).

FRZ's generic leading Selberg Hessian for a shortest geodesic is also of order

\[
\boxed{q^2e^{-q\ell_0}}
\tag{7.2}
\]

when the first systole variation is nonzero [FRZ20].

Thus the two channels are not merely both exponentially small: after Chern-holonomy cancellation they land on the **same semiclassical exponential and polynomial scale**.

This is a stronger structural match than the earlier absolute-value estimate.

---

# Part V. What remains before a total coefficient

## 8. Remaining normalization problem

To turn (3.2) and (6.4) into the exact coefficient of the total FCIG remainder

\[
D_q
=I_{{\rm HBF},q}^{KE}-\mathfrak K_q-rac1{12\pi}G_{\rm WP},
\]

one still must fix, in one convention:

1. whether Sun's loop sum already pairs the two orientations or the real part in \(\kappa\) does so;
2. the longitudinal volume of \(\Gamma_\gamma\backslash\mathbb H\) for \(\gamma=\delta^m\);
3. the primitive-versus-power multiplicity;
4. the external Bergman density factor \((2q-1)/(4\pi)\);
5. the chain-rule relation between the conjugacy parameter \(L=m\ell\) and Teichmüller variation;
6. the matching of FRZ's local Selberg \(A_\gamma(q),B_\gamma(q)\) convention.

Until those are audited, no cancellation/addition claim is made for the **numerical total** coefficient.

---

## 9. Main conceptual result

The nonperturbative picture has now sharpened to

\[
\boxed{
\begin{array}{c}
\text{Todd/GRR local term}\quad \dfrac1{12\pi}G_{\rm WP}
\\[2mm]
+\\[-1mm]
\text{Chern-holonomy cancellation of local hyperbolic moments}
\\[2mm]
+\\[-1mm]
\text{cyclic Fourier singularity at }|\operatorname{Im}u|=1
\\[2mm]
\Downarrow\\[1mm]
q^2e^{-q\ell}\text{-scale conjugacy-class corrections}.
\end{array}
}
\tag{9.1}
\]

The appearance of the Selberg exponent is therefore tied simultaneously to holomorphicity, Chern phase and the hyperbolic length parameter.

This is the correct target for the final conjugacy-class coefficient calculation.
