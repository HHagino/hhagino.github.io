# Hermitian Born–Fisher Completion — Citation Audit

**Date:** 2026-09-10  
**Note:** [`hermitian-born-fisher.md`](hermitian-born-fisher.md)  
**Bibliography:** [`hermitian-born-fisher.bib`](hermitian-born-fisher.bib)

This audit distinguishes established amplitude/phase geometry from the elementary J-paired deduction and from the still-open moving-fiber transport step.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| Projective pure-state metric decomposes into one quarter of classical Fisher plus phase covariance | **Established** | [FKMMSV10] | Facchi et al. explicitly write the metric as `1/4 Fisher + Cov(d alpha)` and the symplectic part as an amplitude/phase term. |
| Classical Fisher of a fixed measurement is bounded by pure-state QFI | **Established** | [BC94] | Braunstein–Caves characterize quantum statistical distance through optimization over measurements. |
| Fixed measurement saturates QFI only under additional conditions | **Established context** | [BC94; TFD17] | Used only to prevent automatic identification of one Born measurement with QFI. |
| Madelung transform is a Kähler map relating wave-function/Fubini–Study and density/Fisher–Rao geometry | **Established** | [KMM19] | Broad amplitude/phase-to-information-geometric correspondence is prior art. |
| Under projective holomorphicity, `s_{JX}=-2 a_X` and `a_{JX}=s_X/2` | **Derived here** | input: [FKMMSV10] decomposition + Cauchy–Riemann hypothesis | Elementary real/imaginary-part calculation; no novelty claim. |
| `I(X,Y)+I(JX,JY)=4 g_FS(X,Y)` | **Derived here** | same inputs | J-paired completion follows immediately from the score identities. Dedicated terminology “Hermitian Born–Fisher” is FCIG terminology. |
| `Var(a_X)+Var(a_{JX})=g_FS(X,X)` | **Derived here** | same inputs | Immediate consequence of the score identities and established decomposition. |
| Uniform `Var(a_q)=o(q)` on every J-paired real direction is impossible when `g_FS,q` has positive order-q growth | **No-go derived here** | same inputs | This supersedes the earlier uniform phase-defect hope. A special real/Lagrangian slice may still have small phase variance. |
| Hyperbolic Chern/minimal-solution Grassmannian metric satisfies `g_Gr,q^C=(q-1)G_WP/(4pi)+O(1)` | **Derived in companion FCIG note** | see `grassmannian-quantum-information.md` | Depends on the FRZ/Wan–Zhang normalization audit already recorded there. |
| J-paired Bergman-DPP Fisher has normalized WP limit | **Conditional corollary** | companion FCIG result + J-paired identity | Requires the concrete position measurement frame to be parallel for the same connection. This transport compatibility is still open. |
| Cho–Yum Fisher/Bergman identity | **Established in bounded-domain kernel model** | [CY23] | Structural context only; does not prove the moving hyperbolic result. |
| Information geometry derives Born's rule | **Explicitly NOT claimed** | — | The note assumes a Born measurement and analyzes its differential geometry. |
| Full Quillen curvature equals J-paired Fisher | **Explicitly NOT claimed** | — | The FCIG notes already separate the order-q KS information sector from the larger full determinant response. |

## Primary-source checks

Metadata and claims were checked against publisher or primary/preprint pages on 2026-09-10:

- Facchi et al., *Physics Letters A* **374** (2010), 4801–4803, DOI `10.1016/j.physleta.2010.10.005`, arXiv:1009.5219.
- Khesin–Misiołek–Modin, *Archive for Rational Mechanics and Analysis* **234** (2019), 549–573, DOI `10.1007/s00205-019-01397-2`, arXiv:1807.07172.
- Braunstein–Caves, *Physical Review Letters* **72** (1994), 3439–3443, DOI `10.1103/PhysRevLett.72.3439`.
- Toscano–Bastos–de Matos Filho, *Physical Review A* **95** (2017), 042125, DOI `10.1103/PhysRevA.95.042125`.
- Cho–Yum, arXiv:2305.10207, current revised version consulted in 2026.

## Correction recorded by this note

The previous research target

\[
\operatorname{Var}(a_q)=o(q)
\]

was useful as a sufficient condition along a fixed real direction, but is **not** a viable uniform condition on a complex tangent plane if the state map is projectively holomorphic and the projective metric is order `q`. The exact sum rule forces at least one member of each `X,JX` pair to carry order-`q` phase information.

The replacement target is the transport theorem: determine whether the Kähler–Einstein/Chern horizontal identification makes the Bergman position measurement parallel for the minimal-solution Hilbert connection. Only after that step does the J-paired WP limit become intrinsic to the moving-fiber DPP.