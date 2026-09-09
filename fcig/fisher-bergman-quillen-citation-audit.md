# Fisher–Bergman–Quillen Citation Audit

**Date:** 2026-09-10  
**Purpose:** provenance audit for [`fisher-bergman-quillen.md`](fisher-bergman-quillen.md).  
**Bibliography:** [`fisher-bergman-quillen.bib`](fisher-bergman-quillen.bib).

The repository rule is strict: a citation supports only the mathematical statement present in the cited source. Equations marked **Derived here** are not attributed to a paper merely because the paper supplies surrounding machinery.

| Note claim | Status | Source(s) | What the source actually supports |
| --- | --- | --- | --- |
| Boolean event algebra / Stone spectrum | **Established** | [Sto36] | Stone representation/duality for Boolean algebras. |
| “Measured Stone scheme” | **FCIG interpretation** | — | Project terminology for Stone spectrum plus an additional probability valuation; not standard terminology. |
| Probability sheaves | **Established** | [Sim17] | Simpson's categorical probability-sheaf framework and Giry-monad extension. |
| Fisher metric / information geometry | **Established** | [Cen82; AN00] | Standard statistical/information-geometric structures and invariance framework. |
| Kernel probability embedding with Fisher pullback equal to Bergman metric | **Established in bounded-domain setting** | [CY23] | Cho–Yum's statistical Bergman embedding and exact Fisher/Bergman equality in their hypotheses. |
| General projection-DPP correlation/covariance identities | **Established** | [HKPV09] | Standard determinantal process identities. |
| DPP as curved exponential family | **Established in finite/discrete setting** | [HY24] | Hino–Yano's embedding structure and information geometry of DPPs. |
| Bergman DPP on polarized complex manifolds and fluctuations | **Established** | [Ber08] | Bergman kernels as DPP correlation kernels and bulk fluctuation/universality results. |
| Polarized-Kähler DPP partition-function asymptotics via Bergman and Quillen methods | **Established** | [Eum26] | Full asymptotic expansion and the two derivations stated in Eum's paper. |
| Exact score \(D_\psi\log q=\sum_a(\Delta-k)\psi(x_a)\) | **Derived here** | background: [Eum26] | The DPP setup is established; this exact score formula is derived in the FCIG conventions. |
| Exact Fisher off-diagonal Bergman energy (Eq. 6.2) | **Derived here from established DPP covariance** | [HKPV09] | Standard covariance identity plus the FCIG score yields the displayed formula. |
| Exact metric Hessian defect (Eqs. 7.4–7.6) | **Derived here** | background: [AN00; Eum26] | The expectation-differentiation calculation is carried out in the FCIG note; no novelty claim is made. |
| TYZ expansion / scalar curvature in subleading Bergman coefficients | **Established** | [Zel98; Lu00; MM07] | General Bergman-kernel asymptotics; coefficients are convention-sensitive. |
| Quillen determinant metric | **Established** | [Qui85] | Quillen determinant metric in the Cauchy–Riemann setting. |
| Holomorphic-family Quillen curvature/anomaly | **Established** | [BGS88] | Bismut–Gillet–Soulé family theorem. |
| High-power analytic-torsion asymptotics | **Established** | [BV89] | Bismut–Vasserot asymptotic analysis. |
| \(L^2\) direct-image positivity/curvature | **Established** | [Bern09] | Berndtsson's theorem for \(\pi_*(K_{X/B}\otimes L)\) with the \(L^2\) metric. |
| High-power \(L^2\) and Quillen curvature comparison; \(\partial\bar\partial\log\tau_k^2=o(k^{n-1})\) | **Established** | [WZ21] | Wan–Zhang's stated asymptotic result. |
| Quillen variation/moment-map asymptotics on compatible complex structures | **Established preprint result** | [Eum25] | Eum's determinant-line/Quillen moment-map construction. |
| Fibered Fisher = Quillen + metric + KS + torsion decomposition | **Conjecture** | motivation: [Bern09; WZ21; Eum25; Eum26] | No cited source is claimed to prove the FCIG decomposition. |
| Leading moving-complex-structure Fisher form is proportional to Weil–Petersson | **Open problem** | comparison background: [Bern09; WZ21] | Must be derived from a defined statistical transport; not attributed to the cited sources. |
| Any Lorentzian/gravitational consequence | **Not claimed** | — | Outside the scope of this note. |

## Bibliographic verification performed

The following metadata were checked against publisher/primary pages on 2026-09-10:

- Berndtsson, *Annals of Mathematics* 169 (2009), 531–560, DOI `10.4007/annals.2009.169.531`.
- Wan–Zhang, *Geometriae Dedicata* 214 (2021), 489–517, DOI `10.1007/s10711-021-00625-y`.
- Hino–Yano, *Information Geometry* 7 (2024), 523–542, DOI `10.1007/s41884-024-00156-x`.
- Eum, *Journal of Geometry and Physics* 221 (2026), 105744, DOI `10.1016/j.geomphys.2025.105744`.
- Simpson, CALCO 2017, DOI `10.4230/LIPIcs.CALCO.2017.1`.
- Stone, *Transactions AMS* 40 (1936), 37–111, DOI `10.1090/S0002-9947-1936-1501865-8`.
- Bismut–Vasserot, *Communications in Mathematical Physics* 125 (1989), 355–367, DOI `10.1007/BF01217912`.

## Deliberate non-claims

This note does not claim that:

- a sigma-algebra is automatically a scheme carrying countable additivity;
- null sets are scheme-theoretic nilpotents;
- every information manifold is globally dually flat;
- a continuous Bergman DPP is covered verbatim by the finite DPP theorem of Hino–Yano;
- Fisher curvature is literally Quillen curvature without metric, torsion, dualization and moving-family corrections;
- the Kodaira–Spencer part of Berndtsson curvature has already been identified with a statistical Fisher term;
- FCIG derives Lorentzian gravity.
