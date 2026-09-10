# Cyclic Fourier Profile — Citation Audit

**Date:** 2026-09-10  
**Note:** [`cyclic-fourier-profile.md`](cyclic-fourier-profile.md)

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| First geodesic-length variation is one half of the geodesic integral of the harmonic Beltrami/Kodaira--Spencer tensor | **Established** | [AS12; FRZ20] | Axelsson--Schumacher theorem; FRZ also reproduce the upper-half-plane formula. |
| Second variation formula with \((1+\square_0)^{-1}|\mu|^2\) and \((-D_t^2+2)^{-1}\) | **Established** | [AS12; FRZ20] | Used exactly as quoted by FRZ Proposition 3. |
| Schumacher field \(f_\mu=(1+\square_0)^{-1}|\mu|^2\) | **Established** | [Sch; FRZ20] | FRZ explicitly attribute the geodesic-curvature identity to Schumacher. |
| Hyperbolic cyclic coordinate \(w=t+i\theta\), metric \((dt^2+d\theta^2)/\sin^2\theta\) | **Standard / derived coordinate change** | — | From \(z=e^w\) in the upper half-plane metric. |
| Periodic Fourier expansion of a holomorphic quadratic differential on the cyclic strip | **Standard complex analysis** | — | Axis-normalized coefficients \(b_n\) are a convention chosen in the note. |
| \(\overline{|\mu|^2}=\sum |b_n|^2A_{n,\ell}\) | **Derived here, exact** | input: harmonic Beltrami/quadratic-differential correspondence | Parseval/longitudinal averaging kills cross terms. |
| Explicit zero-mode Green kernel \(G_0\) for \(1-\frac12\partial_u((1+u^2)\partial_u)\) | **Derived here, exact** | — | Direct ODE solution and weighted-Wronskian jump. |
| First length variation reads only \(b_0\) | **Derived here from established first-variation theorem** | [AS12; FRZ20] | Equation is stated in modulus-squared form to avoid orientation/conjugation convention. |
| Longitudinal resolvent diagonalizes with multiplier \((\nu_n^2+2)^{-1}\) | **Derived here, exact in the chosen parallel axis frame** | [AS12; FRZ20] | Requires the coordinate frame to be parallel on the central geodesic; this is included as a proof obligation to audit tensor conventions. |
| Second length variation becomes Eq. (3.4), a diagonal quadratic form in \(|b_n|^2\) | **Derived here** | [AS12; FRZ20] | Algebraic substitution of the established formula and derived mode decompositions. |
| Weighted Bergman orbital diagonalizes in the same \(|b_n|^2\) with multipliers \(\Lambda_n^{(q,m)}\) | **Derived here** | companion COT theorem | Follows by linearity of the orbital functional and the zero-mode resolvent decomposition. |
| A single classwise first/second length variation determines all Bergman multipliers | **Rejected / not implied** | — | It provides only a small number of scalar contractions of the cyclic mode sequence. |
| Full marked-length data globally fails to determine the deformation | **Not claimed** | — | Global marked-length rigidity is a different and much stronger question. |

## Direct source check

FRZ explicitly give, for a closed geodesic \(\gamma\),

\[
\overline{\partial_\mu\ell(\gamma)}
=
\frac12\int_\gamma
\mu(z(t))\overline{\dot z(t)}^2\rho(z(t))dt,
\]

and quote Axelsson--Schumacher's second variation

\[
\bar\partial_\mu\partial_\mu\ell
=
\frac12\int_\gamma
\left[(\square_0+1)^{-1}|\mu|^2+(-D_t^2+2)^{-1}(\mu)\bar\mu\right]
+
\frac1\ell|\partial_\mu\ell|^2.
\]

These are the only literature inputs needed for the length-side diagonalization.

## Coordinate firewall

The Fourier coefficients \(b_n\) are defined on the cyclic cover associated with one primitive geodesic and in the conformal coordinate

\[
w=t+i\theta,\qquad t\sim t+\ell.
\]

They are not global Fourier coefficients on the compact surface. A different normalization of \(w\), the quadratic-differential frame, or the Beltrami tensor changes intermediate coefficient conventions. Invariant conclusions must be restated after that crosswalk.

## Novelty firewall

Cyclic/Fourier descriptions of automorphic forms and geodesic collars are classical. The note does not claim novelty for using Fourier coefficients. The possibly useful contribution is the **simultaneous explicit packaging** of the Schumacher resolvent profile, AS/FRZ length Hessian and the Chern-holonomy Bergman orbital in one mode basis. A broader literature audit is required before any originality claim.
