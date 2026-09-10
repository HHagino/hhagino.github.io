# BLS Position Transport — Citation Audit

**Date:** 2026-09-10  
**Note:** [`bls-position-transport.md`](bls-position-transport.md)  
**Bibliography:** [`bls-position-transport.bib`](bls-position-transport.bib)

This audit separates source theorems from FCIG deductions. A nearby paper is not cited as proving an equation merely because its machinery is used in the derivation.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| Fiberwise \(L^2(X_t,K_{X_t}\otimes E_t)\) spaces admit the BLS analytic/Chern framework even when they are not an ordinary holomorphic Hilbert bundle | **Established** | [Var24] | Core purpose of Varolin's BLS fields. |
| One should not simply assume a natural ordinary holomorphic structure on the full ambient \(L^2\) field in a nontrivial fibration | **Established warning** | [Bern09; Var24] | Berndtsson discusses the obstruction; Varolin supplies the BLS replacement. |
| BLS ambient Chern connection is induced by twisted Lie derivatives along horizontal lifts and preserves the \(L^2\) metric for a metric coefficient connection | **Established** | [Var24] | Varolin's construction/propositions in the direct-image setting. |
| For a locally trivial holomorphic subfield, its Chern connection is the orthogonal projection of the ambient BLS Chern connection | **Established** | [Var24] | BLS Gauss/subfield formula. |
| Twisted Lie derivative obeys a scalar Leibniz rule | **Established / elementary consequence of definition** | [Var24] | Follows directly from the covariant Cartan formula. |
| \(\nabla_X^{End\,\mathscr L}M_\varphi=M_{V_X\varphi}\) | **Derived here** | machinery: [Var24] | Not attributed as a separately named theorem in Varolin. |
| Horizontally advected ambient multiplication observables and the corresponding position PVM are parallel | **Derived here** | machinery: [Var24] | Smooth differential identity plus finite horizontal-flow/unitary transport. |
| \(\nabla_X^{End\,\mathscr H}(PM_\varphi P)=PM_{V_X\varphi}P+\mathbb B_X^*QM_\varphi P+PM_\varphi Q\mathbb B_X\) | **Derived here** | background: [Var24] | Differentiated-compression/Gauss identity. |
| Compressed Bergman/Toeplitz position observable is generally not parallel even when ambient position is | **Derived here / no-go** | previous row | Exact obstruction is the off-diagonal second fundamental form. |
| The Hilbert--Schmidt square of the second fundamental form is the Grassmannian/Plücker metric of the moving subspace | **Established differential geometry / derived in companion note** | [Bern09; Var24] | Standard Grassmannian subbundle geometry; companion FCIG note fixes conventions. |
| Bergman projection DPP is the Born position law of the normalized Slater state | **Established algebraic/DPP fact** | [Ber08; HY24] | Uses \(|\det U|^2=\det(U^*U)\); reviewed in `born-slater-information.md`. |
| The actual DPP position measurement can be taken on the ambient antisymmetric many-body \(L^2\) space, rather than as a compressed one-particle Toeplitz POVM | **Derived typing clarification** | background: [Ber08] | This is a distinction of measurement levels, not a new DPP theorem. |
| KE horizontal lift yields the harmonic Kodaira--Spencer representative in a canonically polarized family | **Established** | [Sch12] | Schumacher's fiberwise Kähler--Einstein construction. |
| For hyperbolic \(q\)-differentials, the direct-image negative Gauss term is represented by an \(L^2\)-minimal solution / KS second-fundamental channel | **Established** | [Bern09; FRZ20] | Sign and Laplacian conventions must be tracked; the norm is convention-insensitive. |
| \(g_{Pl,q}^{KE}=\mathfrak B_q=(q-1)(4\pi)^{-1}G_{WP}+O(1)\) | **Derived in companion FCIG note** | inputs: [FRZ20; Bern09] | Uses the separately audited 50--50 asymptotic; not claimed as a quoted literature theorem. |
| \(I_q^{KE}(X,Y)+I_q^{KE}(JX,JY)=4g_{Pl,q}^{KE}(X,Y)\) | **Derived here using companion exact HBF theorem** | background: [FKMMSV10; BC94; Var24] | Exact locally once the ambient BLS measurement transport and projectively holomorphic determinant line are represented with the same BLS/Chern realization. |
| \(\pi(q-1)^{-1}(I_q^{KE}+J^*I_q^{KE})\to G_{WP}\) | **Derived here from audited inputs** | [Sch12; Var24; FRZ20] + companion calculations | This is the main FCIG synthesis; no literature-novelty certification. |
| \(I_{HBF,q}^{KE}-\mathfrak K_q=O(1)\) | **Derived here** | companion asymptotics | Both sides have the same audited leading \((q-1)/(4\pi)G_{WP}\) coefficient. |
| Full Quillen/direct-image curvature equals Fisher information | **Explicitly NOT claimed** | — | Full curvature contains different/larger asymptotic sectors. |
| The theorem derives Born's rule from thermodynamics | **Explicitly NOT claimed** | — | Born reconstruction remains a separate FCIG gate. |

## Primary-source metadata checked

The following bibliographic metadata were checked against publisher or primary preprint pages on 2026-09-10:

- Dror Varolin, *Advances in Mathematics* **446** (2024), 109675, DOI `10.1016/j.aim.2024.109675`, arXiv:2201.12802.
- Bo Berndtsson, *Annals of Mathematics* **169** (2009), 531--560, DOI `10.4007/annals.2009.169.531`.
- Georg Schumacher, *Inventiones Mathematicae* **190** (2012), 1--56, DOI `10.1007/s00222-012-0374-7`, arXiv:1201.2930.
- Ksenia Fedosova, Julie Rowlett and Genkai Zhang, *Annals of Global Analysis and Geometry* **57** (2020), 23--60, DOI `10.1007/s10455-019-09687-4`.
- Paolo Facchi et al., *Physics Letters A* **374** (2010), 4801--4803, DOI `10.1016/j.physleta.2010.10.005`, arXiv:1009.5219.
- Samuel L. Braunstein and Carlton M. Caves, *Physical Review Letters* **72** (1994), 3439--3443, DOI `10.1103/PhysRevLett.72.3439`.

## Type firewall

Three levels must remain distinct:

1. **Ambient one-particle \(L^2\) field** \(\mathscr L\): BLS field, not automatically an ordinary holomorphic Hilbert bundle.
2. **Holomorphic Bergman/direct-image subbundle** \(\mathscr H\subset\mathscr L\): finite-dimensional in the hyperbolic \(q\ge2\) application.
3. **Ambient antisymmetric many-body field** \(\bigwedge^N\mathscr L\): the level on which the ordinary position PVM acts and the Slater Born density becomes the DPP.

The compressed observable \(PM_\varphi P\) belongs to level 2. The actual \(N\)-particle position measurement used to obtain the DPP belongs to level 3. Confusing these two is exactly what made the earlier parallelism condition look problematic.

## Normalization firewall

The main asymptotic uses

\[
g_{Pl,q}^{KE}
=\frac{q-1}{4\pi}G_{WP}+O(1).
\]

Hence the raw J-paired classical Fisher is

\[
I_q^{KE}+J^*I_q^{KE}
=\frac{q-1}{\pi}G_{WP}+O(1),
\]

while the Hermitianized quarter-Fisher is

\[
I_{HBF,q}^{KE}
=\frac14(I_q^{KE}+J^*I_q^{KE})
=\frac{q-1}{4\pi}G_{WP}+O(1).
\]

Do not compare these coefficients without preserving the factor \(1/4\).

## Novelty firewall

Targeted searches found nearby literature on:

- BLS deformation/curvature of Bergman spaces;
- direct-image and Kodaira--Spencer curvature;
- Slater/Bergman determinantal processes;
- Fisher/phase decomposition of projective quantum geometry;
- Grassmannian and Weil--Petersson geometry.

No directly matching source was found for the complete BLS-position-transport + compression-defect + J-paired DPP/WP chain. This is **not** proof of novelty. A submission version requires a broader citation-chain, MathSciNet/zbMATH and expert-level audit.
