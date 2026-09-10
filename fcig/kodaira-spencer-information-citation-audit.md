# Kodaira--Spencer Information Citation Audit

**Date:** 2026-09-10  
**For:** [`kodaira-spencer-information.md`](kodaira-spencer-information.md)  
**Bibliography:** [`kodaira-spencer-information.bib`](kodaira-spencer-information.bib)

| Claim | Class | Source / derivation boundary |
| --- | --- | --- |
| Positivity and curvature formula for \(\pi_*(K_{\mathcal X/B}\otimes L)\) | **Established** | Berndtsson [Bern09]. |
| High-power formula with geodesic-curvature and KS resolvent summands | **Established** | Wan--Zhang [WZ21], especially their Berndtsson formula (2.7). |
| Resolvent expansion whose relevant leading term is \(1/(2m)\) | **Established** | Wan--Zhang [WZ21], Lemma 3.1 / equation (1.10). The shorthand in the FCIG note is a statement about the KS matrix-element/trace asymptotic used there, **not** a global operator-norm identity on the entire form space. |
| Bergman expansion \(B_m=(2\pi)^{-1}(m-\rho/2+\cdots)\) for curve fibers | **Established** | Wan--Zhang [WZ21] in their normalization; consistent with the exact hyperbolic local factor already used by FCIG. |
| WP metric as the \(L^2\) pairing of harmonic Kodaira--Spencer/Beltrami representatives | **Established** | Wolpert [Wol86]; Schumacher [Sch12] for the canonically polarized/KE family framework. |
| Definition of \(\mathfrak K_q\) as the trace of the KS resolvent summand | **Derived here / definition** | Direct trace of the established Berndtsson summand. |
| Basis independence and positivity of \(\mathfrak K_q\) | **Derived here** | Trace invariance and positivity of \((m+\Delta')^{-1}\). |
| \(\mathfrak K_q=(q-1)G_{WP}/(4\pi)+O(1)\) | **Derived here from established asymptotics** | Multiply the WZ KS coefficient \(1/2\) by the curve Bergman leading density \(m/(2\pi)\), then identify \(\int|\mu|^2\omega=G_{WP}\). No coefficient fitting. No claim of literature novelty. |
| Chern-normalized KS piece \((2\pi)^{-1}\mathfrak K_q=(q-1)G_{WP}/(8\pi^2)+O(1)\) | **Derived here** | Immediate normalization of the previous line using WZ's displayed \((-i)c_1=(2\pi)^{-1}\operatorname{Tr}\Theta\) convention. |
| Quillen/L2 torsion curvature is \(o(1)\) for curve fibers | **Established** | Wan--Zhang Corollary 1.3 with \(n=1\); their Remark 1.5 records exponential behavior in the compact Teichmüller canonical case. |
| Zograf--Takhtajan Quillen curvature is proportional to WP | **Established benchmark** | [ZT87]. Numerical cross-comparison with WZ is blocked until the conventions for the WP Kähler form versus Hermitian pairing, \(i\), and \(2\pi\) are explicitly crosswalked. |
| Score transformation \(S^{\tau'}=S^\tau+\operatorname{div}_{P}V\) under a change of moving-fiber transport | **Derived here** | Elementary differentiation of \(F_b^*P_b\) using the Lie derivative. |
| Classical moving-fiber Fisher is not invariant under arbitrary transport change | **Derived here / no-go** | Expansion of the transformed score covariance. |
| A KE/Chern horizontal transport makes classical DPP Fisher converge to WP | **Open** | Not claimed. This is the next test. |

## Metadata checks

- Berndtsson: *Annals of Mathematics* **169** (2009), 531--560, DOI `10.4007/annals.2009.169.531`.
- Wan--Zhang: *Geometriae Dedicata* **214** (2021), 489--517, DOI `10.1007/s10711-021-00625-y`.
- Wolpert: *Inventiones Mathematicae* **85** (1986), 119--145, DOI `10.1007/BF01388794`.
- Schumacher: *Inventiones Mathematicae* **190** (2012), 1--56, DOI `10.1007/s00222-012-0374-7`; published erratum: **192** (2013), 253--255, DOI `10.1007/s00222-013-0458-z`.
- Zograf--Takhtajan: *Russian Mathematical Surveys* **42**:6 (1987), 169--190, DOI `10.1070/RM1987V042N06ABEH001501`.
- Hino--Yano: *Information Geometry* **7** (2024), 523--542, DOI `10.1007/s41884-024-00156-x`.

## Explicit non-claims

This milestone does **not** claim that an arbitrary classical Fisher metric on moving configurations is canonical, that the isolated KS summand is itself the full Quillen curvature, that the numerical coefficient in one paper's \(\omega_{WP}\) convention can be copied into another without a convention audit, or that any Lorentzian/gravitational dynamics follows from the WP limit.
