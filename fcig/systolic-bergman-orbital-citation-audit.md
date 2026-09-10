# Systolic Bergman Orbital — Citation Audit

**Date:** 2026-09-10  
**Note:** [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md)  
**Bibliography:** [`systolic-bergman-orbital.bib`](systolic-bergman-orbital.bib)

This audit separates Sun's new exact Bergman-loop formula, classical Selberg/unfolding machinery, FRZ geodesic-length variation, and calculations derived in the FCIG note.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| Exact Bergman density as a sum over based geodesic loops with length factor and Chern-holonomy phase | **Established** | [Sun26] | Sun, Theorem 1.1; v3 revised 2026-04-11. |
| Sun explicitly points out the analogy with the Selberg trace formula | **Established author remark** | [Sun26] | Sun calls a deeper connection an interesting problem; FCIG does not attribute the bridge below to Sun. |
| Hyperbolic-cylinder formulas for based-loop length and Chern holonomy | **Established** | [Sun26] | Sun's cylinder model and holonomy computation. |
| For \(L=K_X\), holonomy on a simple closed geodesic itself is trivial | **Established** | [Sun26] | Used only for the central axis; nearby based loops have nontrivial curvature-induced phase. |
| Complex combination \(C^{-2q}(1-i\tau u)^{-2q}\) | **Derived here** | input: [Sun26] | Algebraic combination of Sun's length and phase formulas; orientation reversal gives complex conjugate. |
| \(\int_{\mathbb R}u^m(1-i\tau u)^{-2q}du=0\) for \(0\le m\le2q-2\) | **Derived here, exact** | — | Elementary contour argument: only pole is in lower half-plane and the upper arc vanishes. |
| A length-only positive Laplace saddle gives the signed orbital coefficient | **Withdrawn / false** | — | Chern phase is leading-order and annihilates the low transverse moments. |
| Selberg-style conjugacy-class unfolding to cyclic hyperbolic cylinders | **Established general machinery** | [McK72; Hejhal] | The exact adaptation to Sun's based-loop sum must retain his orientation and convergence conventions. |
| Every constant-weight nonidentity Bergman orbital vanishes and only the identity orbital gives the trace | **Conditional derived proposition** | [Sun26; McK72] | Algebraic cylinder orbital is zero exactly. Publication-level proof still needs an explicit absolute-convergence/termwise-integration and centralizer-unfolding lemma in Sun's conventions. |
| \(\dim H^0(X,K^q)=(2q-1)(g-1)\) | **Established** | classical Riemann--Roch | The formula is not novel. The proposed orbital route is an alternate derivation. |
| Fourier/Gamma transform of the weighted orbital | **Derived here, exact for Schwartz weights** | — | Direct Gamma integral and Fubini; extension to the actual geometric weight requires a functional-analytic justification. |
| Orbital transform samples \(\widehat a\) near frequency \(2q\tanh(L/2)\) | **Derived interpretation of exact formula** | — | Gamma(2q,1) has mean \(2q\) and variance \(2q\). |
| Quotient Bergman/Szegő kernel is a periodization of the universal-cover kernel | **Established** | [LZ16] | General Poincaré-series background supporting the orbital viewpoint. |
| Exponentially small constant-curvature Bergman errors | **Established** | [Ber12; MM15] | Supports the safe exponential bound; does not determine the signed first coefficient. |
| Selberg-zeta Hessian is controlled at leading order by systole variations | **Established** | [FRZ20] | If first systole variation is nonzero, leading scale is \(q^2e^{-q\ell_0}\); a different \(qe^{-q\ell_0}\) law holds on the kernel of first systole variation. |
| \(f_\mu=(1+\square_0)^{-1}|\mu|^2\) occurs in the second variation of geodesic length | **Established** | [AS12; FRZ20] | This is the structural overlap with the leading \(O(q)\) part of the FCIG weight \(W_q\). |
| Weighted Bergman orbital can already be written solely in terms of \(\partial\ell\) and \(ar\partial\partial\ell\) | **Open problem** | — | This is the next theorem target, not established here. |
| Canonical Bergman projector is exactly an Euler--Poincaré / holomorphic-discrete-series test function in the standard trace-formula sense | **Interpretation / open representation-theory identification** | background [Mar75; McK72] | A precise representation, test function and Harish-Chandra orbital normalization remain to be supplied. |

## Primary-source checks

The following metadata/results were checked against primary or publisher pages on 2026-09-10:

- Jingzhou Sun, *On the Bergman Kernel of Complex Hyperbolic Manifolds*, arXiv:2511.16240v3, revised 11 April 2026.
- Ksenia Fedosova, Julie Rowlett, Genkai Zhang, *Second Variation of Selberg Zeta Functions and Curvature Asymptotics*, Annals of Global Analysis and Geometry 57 (2020), 23--60, DOI `10.1007/s10455-019-09687-4`.
- Reynir Axelsson, Georg Schumacher, *Variation of Geodesic Length Functions in Families of Kähler--Einstein Manifolds and Applications to Teichmüller Space*, 37 (2012), 91--106, DOI `10.5186/aasfm.2012.3703`.
- H. P. McKean, *Selberg's Trace Formula as Applied to a Compact Riemann Surface*, Communications on Pure and Applied Mathematics 25 (1972), 225--246, DOI `10.1002/cpa.3160250302`.
- Zhiqin Lu, Steve Zelditch, *Szegő Kernels and Poincaré Series*, Journal d'Analyse Mathématique 130 (2016), 167--184, DOI `10.1007/s11854-016-0033-9`.
- Xiaonan Ma, George Marinescu, *Exponential Estimate for the Asymptotics of Bergman Kernels*, Mathematische Annalen 362 (2015), 1327--1347, DOI `10.1007/s00208-014-1137-0`.
- Susan Martens, *The Characters of the Holomorphic Discrete Series*, PNAS 72 (1975), 3275--3276, DOI `10.1073/pnas.72.9.3275`.

## Normalization firewall

The Sun formula is used in hyperbolic-area normalization with identity density

\[
C_q=\frac{2q-1}{4\pi}.
\]

The cyclic-cylinder coordinate is \(u=\sinh r\), so \(dA=dt\,du\). Orientation reversal changes \((1-i\tau u)^{-2q}\) to its complex conjugate and therefore does not change the real moment-zero statement.

## Unfolding firewall

The proposed orbital Riemann--Roch proof is not promoted beyond a conditional proposition until the following is written explicitly in one convention:

\[
\int_{\Gamma\backslash\mathbb H}
\sum_{\gamma\ne1}F_q(z,\gamma z)\,dA(z)
=
\sum_{[\gamma]\ne1}
\int_{\Gamma_\gamma\backslash\mathbb H}
F_q(z,\gamma z)\,dA(z).
\]

One must check absolute convergence, orientation counting, the primitive generator of each centralizer, and powers \(\delta^m\). The cylinder integral is already zero once this lemma is justified.

## Novelty firewall

Sun explicitly notes the similarity of his loop formula to Selberg's trace formula. Classical trace-formula and holomorphic-discrete-series literature is extensive. Targeted searching did not reveal the exact moment-annihilation/orbital-Riemann--Roch formulation written in the FCIG note, but this is **not** a novelty certification. A MathSciNet/zbMATH/reference-chain and expert audit is required before any originality claim.
