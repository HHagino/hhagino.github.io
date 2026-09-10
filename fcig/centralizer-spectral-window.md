# FCIG: Centralizer Fourier Modes and the Exact Sun Spectral Window

**Status:** exact Fourier-transform theorem + partial closure of TOI-C  
**Date:** 2026-09-10  
**Depends on:** [`cyclic-fourier-profile.md`](cyclic-fourier-profile.md), [`disk-transported-bergman.md`](disk-transported-bergman.md), [`toeplitz-orbital-insertion.md`](toeplitz-orbital-insertion.md), [`character-trace-firewall.md`](character-trace-firewall.md).

> **Claim firewall.** The integer mode `n` below is the Pontryagin-dual mode of the compact longitudinal quotient `A/<a_ell> ~= R/ell Z`. It is **not** the Harish--Chandra spectral parameter of `G=PSL(2,R)`. The exact transform derived here is a transverse Fourier transform of the Sun/Bergman orbital kernel. The global Harish--Chandra/Selberg transform is a second, distinct step.

---

## 0. Result in one page

Fix a primitive closed geodesic `c` of length `ell` and write

\[
\nu_n=\frac{2\pi n}{\ell},\qquad n\in\mathbb Z.
\]

These are exactly the characters of the closed split-Cartan orbit

\[
A/\langle a_\ell\rangle\simeq \mathbb R/\ell\mathbb Z.
\]

The deformation field has the exact cyclic decomposition

\[
\overline f_\mu(u)=\sum_{n\in\mathbb Z}|b_n|^2F_{n,\ell}(u),
\]

and the `m`-th hyperbolic orbital multiplier is

\[
\Lambda_n^{(q,m)}(\ell)
=\Re\int_{\mathbb R}F_{n,\ell}(u)\kappa_{q,m\ell}(u)\,du.
\tag{0.1}
\]

Put

\[
C_L=\cosh\frac L2,\qquad
\tau_L=\tanh\frac L2,
\]

so that

\[
\kappa_{q,L}(u)=C_L^{-2q}(1-i\tau_Lu)^{-2q}.
\tag{0.2}
\]

With Fourier convention

\[
\widehat h(\xi)=\int_{\mathbb R}h(u)e^{i\xi u}\,du,
\tag{0.3}
\]

the oriented kernel has the exact one-sided transform

\[
\boxed{
\widehat\kappa_{q,L}(\xi)
=
\frac{2\pi C_L^{-2q}}{\Gamma(2q)\tau_L}
\left(\frac{-\xi}{\tau_L}\right)^{2q-1}
 e^{\xi/\tau_L}\mathbf 1_{\xi<0}.
}
\tag{0.4}
\]

Consequently the real Sun orbital kernel has the positive even transform

\[
\boxed{
\widehat{\Re\kappa_{q,L}}(\xi)
=
\frac{\pi C_L^{-2q}}{\Gamma(2q)\tau_L}
\left(\frac{|\xi|}{\tau_L}\right)^{2q-1}
 e^{-|\xi|/\tau_L}.
}
\tag{0.5}
\]

Therefore

\[
\boxed{
\Lambda_n^{(q,m)}(\ell)
=
\frac{C_L^{-2q}}{2\Gamma(2q)\tau_L}
\int_{\mathbb R}
\Re\widehat F_{n,\ell}(\xi)
\left(\frac{|\xi|}{\tau_L}\right)^{2q-1}
 e^{-|\xi|/\tau_L}\,d\xi,
\quad L=m\ell.
}
\tag{0.6}
\]

Thus each FCIG orbital coefficient is an exact **Gamma-windowed transverse spectral moment** of the resolvent profile.

The two spectral indices must be kept separate:

\[
\boxed{
\begin{array}{rcl}
n &:& \text{longitudinal centralizer Fourier mode},\\
\xi &:& \text{transverse Fourier variable},\\
L &:& \text{hyperbolic conjugacy-length variable}.
\end{array}
}
\tag{0.7}
\]

The Harish--Chandra/Selberg transform acts only after the classwise object has been assembled in the `L`/conjugacy variable. Hence the correct architecture is

\[
\boxed{
\text{centralizer Fourier decomposition}
\to
\text{Gamma-windowed modewise orbital}
\to
\text{Harish--Chandra/Selberg transform}.
}
\tag{0.8}
\]

---

# Part I. Exact Fourier transform of the oriented kernel

## 1. Gamma representation

For integer `q>=1`,

\[
(1-i\tau u)^{-2q}
=\frac1{\Gamma(2q)}\int_0^\infty
s^{2q-1}e^{-s}e^{i\tau us}\,ds.
\tag{1.1}
\]

Therefore, distributionally,

\[
\begin{aligned}
\widehat\kappa_{q,L}(\xi)
&=\frac{C_L^{-2q}}{\Gamma(2q)}
\int_0^\infty s^{2q-1}e^{-s}
\int_{\mathbb R}e^{iu(\xi+\tau_Ls)}du\,ds\\
&=\frac{2\pi C_L^{-2q}}{\Gamma(2q)}
\int_0^\infty s^{2q-1}e^{-s}
\delta(\xi+\tau_Ls)\,ds.
\end{aligned}
\tag{1.2}
\]

The delta constraint has a positive solution exactly when `xi<0`, namely

\[
s=-\frac\xi{\tau_L}.
\]

Using the Jacobian `1/tau_L` gives (0.4).

This one-sided support is the Fourier-space expression of the oriented holomorphic/Chern phase. Orientation reversal replaces `kappa` by its complex conjugate and flips the half-line.

---

## 2. Real orbital kernel

Since

\[
\Re\kappa(u)=\frac12\left(\kappa(u)+\overline{\kappa(u)}\right),
\]

and

\[
\widehat{\overline\kappa}(\xi)
=\overline{\widehat\kappa(-\xi)},
\]

one obtains the even positive density (0.5).

This makes the Chern-holonomy cancellation and the weighted response look very different in Fourier space:

- the unweighted constant profile is concentrated at `xi=0`, while (0.5) vanishes to order `2q-1` at `xi=0`;
- a nonconstant deformation profile contributes through nonzero transverse frequencies;
- the spectral window is everywhere nonnegative after taking the real/orientation-paired orbital.

The exact unweighted cancellation

\[
\int_{\mathbb R}\Re\kappa_{q,L}(u)du=0
\]

is therefore simply

\[
\widehat{\Re\kappa}_{q,L}(0)=0.
\tag{2.1}
\]

---

# Part II. Exact Gamma spectral window

## 3. Parseval pairing

For sufficiently decaying real `F`,

\[
\int_{\mathbb R}F(u)\Re\kappa(u)du
=\frac1{2\pi}\int_{\mathbb R}
\widehat F(\xi)\widehat{\Re\kappa}(-\xi)d\xi.
\tag{3.1}
\]

Because (0.5) is real and even, the imaginary odd part of `hat F` drops out and (0.6) follows.

Define the normalized positive-frequency Gamma density

\[
p_{q,\tau}(\xi)
=\frac1{\Gamma(2q)\tau}
\left(\frac\xi\tau\right)^{2q-1}e^{-\xi/\tau},
\qquad \xi>0.
\tag{3.2}
\]

It satisfies

\[
\int_0^\infty p_{q,\tau}(\xi)d\xi=1,
\quad
\mathbb E\xi=2q\tau,
\quad
\operatorname{Var}(\xi)=2q\tau^2,
\tag{3.3}
\]

and has mode `(2q-1)tau` for `q>=1`.

Thus the orbital transform samples `Re hat F` in a window centered at transverse frequency of order

\[
\boxed{|\xi|\sim 2q\tanh(L/2).}
\tag{3.4}
\]

with relative width `1/sqrt(2q)`.

This gives an exact finite-`q` interpretation and an immediate semiclassical statement: at large `q`, the Sun/Bergman orbital is a sharply localized transverse spectral probe rather than a low-frequency average.

---

# Part III. The cyclic index is not the Harish--Chandra parameter

## 4. Source of the integer `n`

The quadratic differential is periodic along the cylinder:

\[
\phi(t+\ell+i\theta)=\phi(t+i\theta).
\]

Hence

\[
\phi(t+i\theta)
=\sum_n b_ne^{i\nu_nt}e^{-\nu_n(\theta-\pi/2)},
\qquad
\nu_n=\frac{2\pi n}{\ell}.
\tag{4.1}
\]

This is simply Fourier analysis on

\[
\mathbb R/\ell\mathbb Z.
\]

Equivalently, it is the character decomposition of the cyclic centralizer quotient of the primitive hyperbolic orbit.

Calling `nu_n` a Harish--Chandra parameter would conflate two distinct harmonic analyses:

1. Fourier analysis on the closed `A`-orbit / centralizer quotient;
2. invariant harmonic analysis on the noncompact group `G` and its conjugacy classes.

The second is where the Weyl/Harish--Chandra denominator and Selberg transform live.

---

## 5. Correct representation-theoretic typing of TOI-C

Let `T_f^(q)=P_q M_f P_q`. After cyclic unfolding, the symbol `f` decomposes into centralizer Fourier sectors. The FCIG quantity is therefore best typed as a family of modewise relative/orbital matrix functionals

\[
\boxed{
\mathscr M_{q,L,n}[f]
:=
\operatorname{Tr}^{\rm orb}_{L,n}
\bigl(T_f^{(q)}\pi_q(a_{L/2})\bigr),
}
\tag{5.1}
\]

where `Tr^orb_{L,n}` means: centralizer-normalize the hyperbolic cylinder and project the longitudinal dependence to the character `e^{i nu_n t}` before evaluating the transported Bergman diagonal.

For the quadratic information symbol, longitudinal averaging of `|mu|^2` makes the response diagonal in `|b_n|^2`; hence the geometrically computed multiplier is

\[
\boxed{
\mathscr M_{q,L,n}[f_\mu]
\propto
\Lambda_n^{(q,m)}(\ell),
\qquad L=m\ell,
}
\tag{5.2}
\]

with the proportionality normalization already fixed by the exact Sun--Selberg unfolding and disk-kernel crosswalk.

Equation (5.2) is now an operator-typing statement with an explicit scalar target, but an invariant definition of the mode-projected relative trace is still required for a full TOI-B/TOI-C theorem.

---

# Part IV. Reflection symmetry and mode pairing

## 6. Exact `n <-> -n` symmetry

The cylinder coordinate obeys

\[
\theta(-u)=\pi-\theta(u).
\]

Therefore the source profiles satisfy

\[
\boxed{A_{-n,\ell}(u)=A_{n,\ell}(-u).}
\tag{6.1}
\]

The radial resolvent operator

\[
1-\frac12\partial_u((1+u^2)\partial_u)
\]

commutes with `u -> -u`. Hence bounded uniqueness gives

\[
\boxed{F_{-n,\ell}(u)=F_{n,\ell}(-u).}
\tag{6.2}
\]

Since `Re kappa` is even,

\[
\boxed{
\Lambda_{-n}^{(q,m)}(\ell)=\Lambda_n^{(q,m)}(\ell).
}
\tag{6.3}
\]

Thus the classwise information orbital depends on the longitudinal mode data through

\[
|b_0|^2\Lambda_0
+\sum_{n\ge1}
\bigl(|b_n|^2+|b_{-n}|^2\bigr)\Lambda_n.
\tag{6.4}
\]

This is an exact reduction of the cyclic data relevant to the real FCIG response.

---

# Part V. What TOI-C now says

## 7. Partial closure

The previous open gate asked to identify the relation between the Toeplitz insertion and the explicit `Lambda_n` multipliers. The following parts are now exact:

1. the transported Bergman kernel is exactly `C_q kappa_{q,L}` in the disk convention;
2. centralizer unfolding gives the primitive-length normalization;
3. the deformation symbol is diagonal after longitudinal averaging in the centralizer characters `nu_n`;
4. each diagonal multiplier is an exact Gamma-windowed transverse spectral moment (0.6);
5. opposite centralizer modes pair exactly as in (6.3).

Accordingly:

\[
\boxed{
\textbf{TOI-C: PARTIAL PASS.}
}
\]

The remaining non-formal step is not another scalar integral. It is to construct the mode-projected relative trace (5.1) invariantly inside the restriction of the holomorphic discrete series to the split Cartan/centralizer geometry, and then prove that its geometric unfolding is exactly (0.6).

---

## 8. Revised TOI-D target

The old suggestion that

\[
\frac{e^{-qL}}{1-e^{-L}}
=\sum_{k\ge0}e^{-(q+k)L}
\]

should arise as a literal Hilbert-space ladder trace is rejected by the character-trace firewall.

The correct next target is:

\[
\boxed{
\textbf{Centralizer-to-Harish--Chandra Closure:}
}
\]

construct a test function/operator-valued distribution `h_{q,mu}` whose hyperbolic orbital integral is the FCIG class response and whose invariant group Fourier transform pairs with the discrete-series distribution character. The factor `(1-e^{-L})^{-1}` must then appear through the standard Weyl/Harish--Chandra/Selberg hyperbolic Jacobian/character machinery, not by summing alleged eigenvalues of `pi_q(a_L)`.

This separates three structures that had previously been conflated:

\[
\boxed{
\text{cyclic mode }n
\;\neq\;
\text{transverse frequency }\xi
\;\neq\;
\text{Harish--Chandra spectral variable}.
}
\tag{8.1}
\]

That separation is the main conceptual closure of this note.
