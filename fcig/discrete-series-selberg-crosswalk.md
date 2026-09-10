# FCIG: Holomorphic Discrete-Series Character and the Selberg Denominator

**Status:** established character formula + derived normalization crosswalk  
**Date:** 2026-09-10  
**Depends on:** [`sun-selberg-unfolding.md`](sun-selberg-unfolding.md), [`cyclic-mode-asymptotics.md`](cyclic-mode-asymptotics.md).

## 1. The exact denominator match

For the holomorphic discrete series of \(SL(2,\mathbb R)\), use the standard parameter \(D_n^+\) for which the lowest \(K\)-type has weight \(n+1\). On a positive hyperbolic element

\[
a_t=\begin{pmatrix}e^t&0\\0&e^{-t}\end{pmatrix},\qquad t>0,
\]

the Harish--Chandra character is

\[
\boxed{
\Theta_n^+(a_t)=\frac{e^{-nt}}{e^t-e^{-t}}
}
\tag{1.1}
\]

(up to the standard central-sign convention when working in \(SL(2,\mathbb R)\) rather than \(PSL(2,\mathbb R)\)). This is classical discrete-series character theory.

Holomorphic \(q\)-differentials transform with lowest rotation weight \(2q\), so the matching discrete-series parameter is

\[
\boxed{n=2q-1.}
\tag{1.2}
\]

A hyperbolic element whose translation length on \(\mathbb H\) is \(L\) is conjugate to \(a_{L/2}\). Therefore

\[
\begin{aligned}
\Theta_{2q-1}^+(a_{L/2})
&=\frac{e^{-(2q-1)L/2}}{e^{L/2}-e^{-L/2}}\\
&=\boxed{\frac{e^{-qL}}{1-e^{-L}}}.
\end{aligned}
\tag{1.3}
\]

This is an exact algebraic crosswalk, not an asymptotic analogy.

## 2. Connection to the FRZ systole Hessian

Fedosova--Rowlett--Zhang prove that, when the first systole variation is nonzero,

\[
\bar\partial_\mu\partial_\mu\log Z(q)
\sim
-\frac{q^2e^{-qL}}{1-e^{-L}}
|\partial_\mu L|^2
\tag{2.1}
\]

for each shortest class at leading order. Using (1.3), the class coefficient can be written

\[
\boxed{
\bar\partial_\mu\partial_\mu\log Z(q)
\sim
-q^2\,\Theta_{2q-1}^+(a_{L/2})
|\partial_\mu L|^2.
}
\tag{2.2}
\]

**Derived crosswalk.** FRZ do not state their asymptotic in character notation; equation (2.2) is simply their established coefficient rewritten using the established \(SL(2,\mathbb R)\) discrete-series character formula.

## 3. Why this matters for the cyclic Fourier calculation

The Selberg local factor is

\[
Z_c(q)=\prod_{k=0}^{\infty}(1-e^{-(q+k)L}).
\tag{3.1}
\]

The geometric-series denominator in its large-\(q\) variation is

\[
\frac{e^{-qL}}{1-e^{-L}}
=\sum_{k=0}^{\infty}e^{-(q+k)L}.
\tag{3.2}
\]

Equation (1.3) shows that this ``descendant tower'' is exactly the hyperbolic character denominator of the holomorphic discrete series underlying canonical \(q\)-differential quantization.

The FCIG cyclic-cover calculation decomposes the deformation into longitudinal Fourier modes \(b_n\). The zero mode alone produces an \(e^{-qL}\) term but no \((1-e^{-L})^{-1}\) denominator. Thus the natural theorem target is now representation-theoretically precise:

\[
\boxed{
\text{identify the full cyclic-mode weighted Bergman transform with a character/matrix-coefficient transform of }D_{2q-1}^+.
}
\tag{3.3}
\]

This is stronger than the previous heuristic statement that ``the nonzero modes should supply the denominator'', but it is still an **open identification problem**: the ordinary Harish--Chandra character is a distributional trace of the representation, whereas the weighted Bergman orbital contains the deformation field \(f_\mu\). The correct object may therefore be a differentiated character, weighted orbital integral, or matrix-coefficient transform rather than \(\Theta\) itself.

## 4. Compatibility with the orbital-vanishing result

There is no contradiction between

\[
\Theta_{2q-1}^+(a_{L/2})\ne0
\]

and the earlier theorem that the **unweighted Sun Bergman orbital** vanishes. These are different operations:

- the Harish--Chandra character is the representation trace evaluated at a group element;
- the Sun/FCIG unweighted hyperbolic orbital is an orbital integral of the Bergman projector kernel with its Chern phase.

Discrete-series pseudo-coefficients can have vanishing nonelliptic orbital integrals even though the discrete-series character on the regular hyperbolic set is nonzero. The next representation-theory audit must keep these two transforms distinct.

## 5. New target

The remaining classwise problem is no longer merely to guess the exponential scale. It is to derive an exact formula of the form

\[
\sum_{n\in\mathbb Z}|b_n|^2\Lambda_{n}^{(q)}(L)
=\mathfrak T_{q,L}[\mu],
\tag{5.1}
\]

where \(\mathfrak T_{q,L}\) is expressed in the harmonic analysis of \(D_{2q-1}^+\), and then compare its leading variation channel with

\[
-q^2\Theta_{2q-1}^+(a_{L/2})|\partial_\mu L|^2.
\tag{5.2}
\]

The exact equality (1.3) makes this a concrete representation-theoretic crosswalk rather than a numerical coincidence.

## Sources

- Harish--Chandra, *Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters*, Acta Mathematica 116 (1966), 1--111.
- Standard \(SL(2,\mathbb R)\) Harish--Chandra module reference tables give \(\Theta_n^+(a_t)=e^{-n|t|}/|e^t-e^{-t}|\) on the positive split Cartan.
- Fedosova, Rowlett, Zhang, *Second Variation of Selberg Zeta Functions and Curvature Asymptotics*, Ann. Global Anal. Geom. 57 (2020), 23--60.
