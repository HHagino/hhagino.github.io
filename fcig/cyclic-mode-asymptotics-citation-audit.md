# Cyclic-Mode Asymptotics — Citation Audit

**Date:** 2026-09-10  
**Note:** [`cyclic-mode-asymptotics.md`](cyclic-mode-asymptotics.md)

| Claim | Status | Source(s) | Boundary |
| --- | --- | --- | --- |
| First length variation is one half of the geodesic integral | **Established** | [AS12; FRZ20] | Used to identify \(|b_0|^2=4|\partial\log L|^2\). |
| FRZ Selberg Hessian contains \(|\partial\log\ell(\gamma)|^2\) with explicit scalar local-zeta multipliers | **Established** | [FRZ20] | Supports comparison of deformation invariants and asymptotic scale. |
| Kummer \(U(a,b,z)\sim z^{-a}\) at large \(z\) | **Established special-function asymptotic** | [DLMF13] | Used only after the exact Fourier-transform calculation. |
| \(F_0(u)=1/[2(1+u^2)]\) solves the zero-mode resolvent | **Derived here, exact** | — | Direct differentiation. |
| \(\mathcal J_{q,L}[F_0]=(\pi/2)e^{-qL}\) | **Derived here, exact** | — | Exact Fourier transform + Gamma integral + \(\cosh(L/2)(1+\tanh(L/2))=e^{L/2}\). |
| \(\mathcal J_{q,L}[W_{q,0}]=(\pi/2)(3q-1-qe^{-L})e^{-qL}\) | **Derived here, exact** | — | Algebra from the exact transforms of \(A_0,F_0\). |
| Zero-mode profile contribution is proportional to \(|\partial\log L|^2\) | **Derived here from established first variation** | [AS12; FRZ20] | This is the normalized profile orbital, not yet the fully unfolded conjugacy-class coefficient. |
| Exact transform of \(A_\nu\) in terms of Kummer \(U\) | **Derived here, exact for \(\xi>0\)** | standard Gamma integrals | Numerically cross-checked during derivation; publication proof should record the Fubini conditions. |
| Fourier resolvent ODE Eq. (5.1) | **Derived here, exact** | — | Fourier transform of the radial hyperbolic operator. |
| \(\widehat F_\nu=d_\nu e^{-\xi}\xi^{i\nu}(1+O(\xi^{-1}))\) | **Derived asymptotic / theorem candidate** | input [DLMF13] | Dominant-balance derivation; rigorous error control for the bounded resolvent solution remains a proof obligation. |
| Fixed-mode weighted orbital is \(q e^{-qL}\) at profile level | **Derived asymptotic / theorem candidate** | — | Follows from the previous row and Gamma-ratio asymptotics; fixed \(L,\nu\). |
| Full unfolded Bergman fixed-mode scale is naturally \(q^2e^{-qL}\) | **Structural consequence with normalization caveat** | Sun prefactor; [FRZ20] comparison | External Bergman density is \(O(q)\), but exact centralizer/orientation coefficient still needs the Sun-unfolding audit. |
| Bergman and Selberg total coefficients are equal or cancel | **Not claimed** | — | Same scale is established/derived; numerical coefficient comparison remains open. |

## Exact zero-mode firewall

The strongest result in this note is the zero mode. It does not use a large-\(q\) approximation:

\[
\mathcal J_{q,L}[F_0]=\frac\pi2e^{-qL},
\]

\[
\mathcal J_{q,L}[W_{q,0}]
=\frac\pi2(3q-1-qe^{-L})e^{-qL}.
\]

Thus the recovery of the Selberg exponential scale is already exact in the length-variation zero mode.

## Fixed-mode asymptotic firewall

The general \(\nu\)-mode expansion assumes \(L>0\) and \(\nu\) fixed while \(q\to\infty\). It is not asserted to be uniform in \(|n|\), in degenerating collars \(L\to0\), or after summing all cyclic Fourier modes. Those are separate analysis problems.

## Unfolding firewall

No formula in this note silently inserts the missing Selberg/Sun centralizer multiplicities. A profile orbital \(\mathcal J_{q,L}\) becomes a geometric conjugacy-class contribution only after the orientation, primitive-power, longitudinal-volume, and Bergman-prefactor conventions are fixed.
