# Casimir Orbital Transmutation — Citation Audit

**Date:** 2026-09-10  
**Note:** [`casimir-orbital-transmutation.md`](casimir-orbital-transmutation.md)  
**Bibliography:** [`casimir-orbital-transmutation.bib`](casimir-orbital-transmutation.bib)

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| Exact canonical Bergman loop kernel with geodesic length and Chern-holonomy phase | **Established** | [Sun26] | Sun supplies the geometric loop formula; the differential identities below are not attributed to Sun. |
| FRZ convention \(\square_0=2\bar\partial^*\bar\partial=\Delta_0/2\) on functions | **Established** | [FRZ20] | Needed to fix the factor and sign in the cylinder Laplacian. |
| \(f_\mu=(1+\square_0)^{-1}|\mu|^2\) | **Established** | [FRZ20; AS12] | Schumacher/FRZ geodesic-curvature/resolvent field. |
| Axelsson--Schumacher closed-geodesic second-variation formula | **Established** | [AS12; FRZ20] | Contains the axis integral of \(f_\mu\), the longitudinal resolvent \((-D_t^2+2)^{-1}\), and the first-length-variation square. |
| \(\square_0\kappa_{q,L}=[q(q-1)(\cosh L-1)-\mathscr C_L]\kappa_{q,L}\) | **Derived here, exact** | input: [Sun26; FRZ20] | Direct differentiation plus the FRZ Laplacian normalization. No literature novelty claim. |
| \(\mathcal J_{q,L}[W_q]=\mathscr D_{q,L}\mathcal J_{q,L}[f_\mu]\) | **Derived here, exact under stated boundary conditions** | input: [FRZ20] | Integration by parts after longitudinal averaging. \(L\)-derivatives act on the kernel parameter while the lifted weight is held fixed. |
| Gamma/Fourier representation of \(\mathcal J_{q,L}\) | **Derived here / inherited from SBO** | — | Elementary Gamma integral and Fubini for Schwartz profiles. |
| Bergman orbital samples transverse Fourier frequencies near \(2q\tanh(L/2)\) | **Derived interpretation** | — | Gamma(2q,1) mean and variance. |
| Ordinary length Hessian and weighted Bergman orbital are the same functional of \(f_\mu\) | **False / rejected** | — | Length Hessian uses the axis trace plus longitudinal resolvent; Bergman orbital uses a high-frequency transverse transform. |
| Axis value or any finite transverse jet determines the weighted orbital on all Schwartz profiles | **No-go, exact for unrestricted profiles** | — | Evaluation/finite-jet distributions are supported at \(u=0\); the orbital functional is represented by a smooth nonlocal kernel. |
| The same no-go is already proved on the finite-dimensional space of actual harmonic-Beltrami profiles on a fixed surface | **Not claimed** | — | Harmonicity and automorphy may impose additional relations; this is a geometric restriction problem. |
| FRZ Selberg Hessian is a scalar marked-length-spectrum expansion | **Established** | [FRZ20] | Their Theorem 1 expresses the Hessian using first and second variations of primitive geodesic lengths with explicit \(A_\gamma,B_\gamma\). |
| \(q(q-1)\) is a holomorphic-discrete-series Casimir scale | **Established up to normalization** | [BW; DS] | Casimir conventions vary by signs/factors. The note does not identify the displayed \(\mathscr C_L\) with a standard radial Casimir without a convention crosswalk. |
| Discrete-series pseudo-coefficients can have vanishing non-elliptic orbital integrals | **Established representation-theory background** | [Lab] | Supports the analogy with SBO cancellation, not an equality with Sun's kernel. |
| Sun's Bergman kernel is exactly an Euler--Poincare pseudo-coefficient | **Open / not claimed** | — | Requires an explicit test-function and orbital-normalization identification. |

## Primary-source checks

The following statements were checked directly against the publisher/full-text presentation of Fedosova--Rowlett--Zhang on 2026-09-10:

- their Eq. (2.5) defines \(f(\mu)=(1+\square_0)^{-1}|\mu|^2\) and states \(\square_0=2\bar\partial^*\bar\partial\);
- their discussion of scalar Laplacian conventions gives \(\Delta_0=2\square_0\);
- their Proposition 3 quotes the Axelsson--Schumacher formula
  \[
  \bar\partial_\mu\partial_\mu\ell
  =\frac12\int_\gamma\left[f_\mu+(-D_t^2+2)^{-1}(\mu)\bar\mu\right]dt
  +\ell^{-1}|\partial_\mu\ell|^2;
  \]
- their Theorem 1 writes \(\bar\partial\partial\log Z(s)\) as a sum over primitive geodesics of scalar first/second length variations with explicit \(A_\gamma(s),B_\gamma(s)\).

## Normalization firewall

On the cyclic cylinder

\[
ds^2=(1+u^2)^{-1}du^2+(1+u^2)dt^2,
\]

we use the positive scalar Laplacian

\[
\Delta_0=-\left[\partial_u((1+u^2)\partial_u)+(1+u^2)^{-1}\partial_t^2\right]
\]

and therefore \(\square_0=\Delta_0/2\). Changing to a negative Laplacian convention flips the differential identity and must not be mixed with FRZ's formulas.

## Parameter-derivative firewall

The derivative \(\partial_L\) in \(\mathscr C_L\) differentiates

\[
\kappa_{q,L}(u)
=\left(\cosh(L/2)-iu\sinh(L/2)\right)^{-2q}
\]

with the profile \(\overline f_\mu(u)\) held fixed. It is a conjugacy-parameter derivative inside the model kernel, not a Teichmüller derivative \(\partial_\mu\ell(\gamma)\). The two must not be identified without a further chain-rule/deformation argument.

## Novelty firewall

Targeted searches found extensive literature on Selberg orbital integrals, Bergman/discrete-series realizations, radial Casimir operators, and pseudo-coefficients. We did not find the precise identities labeled Theorem A/B in the FCIG note, but this is **not** a novelty certification. Before publication, check MathSciNet/zbMATH and the reference chains around Sun, Berndtsson/Schumacher, trace-formula radial parts, and discrete-series matrix coefficients.
