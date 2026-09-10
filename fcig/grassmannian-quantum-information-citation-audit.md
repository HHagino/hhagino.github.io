# Grassmannian Quantum Information — Citation Audit

**Date:** 2026-09-10  
**Note:** [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md)  
**Bibliography:** [`grassmannian-quantum-information.bib`](grassmannian-quantum-information.bib)

The purpose of this file is to prevent an FCIG synthesis from being mistaken for a literature theorem. In particular, the 50–50 wording is a project deduction; the underlying identities and asymptotics come from the cited literature.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| Direct-image curvature contains a second-fundamental/minimal-solution mechanism | **Established** | [Bern09] | Berndtsson explicitly describes the second fundamental form as the norm of a minimal solution of a `dbar` equation in the Hilbert-subbundle picture. |
| On Teichmüller space, for `q`-differentials, `eta=-mu·u` and the minimal solution `chi` satisfy the exact source-minus-minimal-solution resolvent identity | **Established** | [FRZ20, Prop. 1 and proof] | FRZ equations corresponding to their (2.7) and proof give `||eta||^2-||chi||^2 = (q-1)/2 <(box''+(q-1)/2)^(-1)eta,eta>`. |
| FRZ and Wan–Zhang resolvent expressions use different norm/Laplacian normalizations but represent the same term | **Established** | [FRZ20, Remark 1] | FRZ explicitly notes the alternative `(q-1)<(Delta+q-1)^(-1)eta,eta>` form and attributes the discrepancy to norms. |
| `A_q=B_q+R_q` after tracing | **Derived here** | input [FRZ20] | Direct sum of the statewise exact identity; not a novelty claim. |
| `A_q = ∫ <mu,nu> B_q dA` | **Derived here / standard Bergman trace** | Bergman setup from prior FCIG notes | Follows by summing the pointwise contraction norm over an orthonormal basis. |
| `R_q=(q-1)G_WP/(4pi)+O(1)` | **Derived in previous FCIG note from established high-power expansion** | [WZ21], `kodaira-spencer-information.md` | Coefficient is convention-dependent; previous note defines the WP Hermitian pairing explicitly and carries a normalization firewall. |
| `B_q=(q-1)G_WP/(4pi)+O(1)` | **Derived here** | exact `A=B+R` + Bergman trace + previous `R` asymptotic | This is the new subtraction step. |
| 50–50 ratios `B/A -> 1/2`, `R/A -> 1/2` | **Derived here** | same inputs | Project name “50–50 Kodaira–Spencer law”; no claim that equivalent asymptotics are absent from literature. |
| Slater determinant rays form a Grassmannian/Plücker manifold | **Established** | [AS20] | Aoto–da Silva explicitly use the identification of single Slater determinants with a Grassmannian submanifold of projective Hilbert space. |
| Pullback Plücker/FS metric equals trace of second-fundamental energy | **Derived here / standard differential geometry** | supporting context [Bern09; AS20] | The note includes the elementary wedge-derivative proof. |
| FRZ minimal solution is the normal component in the **chosen Chern/minimal-solution Hilbert gauge** | **Working geometric identification, carefully scoped** | [Bern09; FRZ20] | We do not claim invariance under arbitrary parameter-dependent Hilbert trivializations. The connection/gauge is part of the definition. Publication version must globalize this construction. |
| Standard pure-state quantum Fisher equals four times Fubini–Study metric | **Established** | [BC94] | Braunstein–Caves supplies the operational quantum statistical metric; factor-four convention is stated explicitly. |
| `I_Q^C=(q-1)G_WP/pi+O(1)` | **Derived here** | `g_Gr=B`, 50–50 result, [BC94] factor four | Valid in the Chern/minimal-solution covariant convention adopted in the note. |
| For a position measurement, `I_Q = I_pos + 4 Var(a)` | **Derived here from pure-state formula** | background [BC94] | Direct amplitude/phase decomposition; exact for real tangent directions after projective centering. |
| Classical position Fisher saturates WP iff phase variance is `o(q)` | **Conditional corollary** | previous line + Grassmannian asymptotic | The condition is not proved. |
| Quantized finite-dimensional metrics can converge to WP on polarized Calabi–Yau moduli | **Established in a different setting** | [KL15] | Used only as structural precedent; it does not prove the hyperbolic-curve formula here. |
| Universal Teichmüller space has a holomorphic inclusion into a Segal–Wilson Grassmannian and carries WP geometry | **Established prior art** | [TT06] | This is highly relevant prior art for any broad “Grassmannian = WP” novelty claim. It does **not** by itself identify the finite-dimensional `H^0(K^q)` minimal-solution metric or prove the 50–50 high-power law. |
| DPPs can form curved exponential families | **Established in finite/discrete setting** | [HY24] | Context only; not used to prove continuous Bergman DPP statements. |
| Full Quillen curvature equals the quantum Fisher/Grassmannian KS metric | **Explicitly NOT claimed** | [FRZ20] shows total curvature scale | Full curvature is `O(q^2)` while the isolated KS normal/resolvent channels here are `O(q)`. |
| Lorentzian gravity follows | **Not claimed** | — | Outside this note. |

## Prior-art collision check

A broad claim that “Teichmüller/WP geometry embeds into a Grassmannian” would be old: Takhtajan–Teo prove a holomorphic inclusion of the Weil–Petersson component of universal Teichmüller space into the Segal–Wilson universal Grassmannian [TT06]. Keller–Lukic also prove convergence of a finite-dimensional quantized sequence of Kähler metrics to WP in polarized Calabi–Yau moduli [KL15].

Therefore the potentially distinctive FCIG statement must stay narrow:

\[
\boxed{
\text{for the }H^0(K^q)\text{ family, the FRZ minimal-solution energy and the Berndtsson resolvent energy split the KS source 50--50 at leading order.}
}
\]

The quantum-Fisher interpretation is then attached to the minimal-solution/Plücker channel with a specified connection and normalization. No novelty claim is made until a dedicated literature review checks equivalent formulations.

## Primary-source checks

Metadata and mathematical statements were checked against publisher or primary pages on 2026-09-10:

- Bo Berndtsson, *Annals of Mathematics* **169** (2009), 531–560, DOI `10.4007/annals.2009.169.531`.
- Ksenia Fedosova, Julie Rowlett, Genkai Zhang, *Annals of Global Analysis and Geometry* **57** (2020), 23–60, DOI `10.1007/s10455-019-09687-4`.
- Xueyuan Wan, Genkai Zhang, *Geometriae Dedicata* **214** (2021), 489–517, DOI `10.1007/s10711-021-00625-y`.
- Samuel L. Braunstein, Carlton M. Caves, *Physical Review Letters* **72** (1994), 3439–3443, DOI `10.1103/PhysRevLett.72.3439`.
- Yuri Alexandre Aoto, Marcio Fabiano da Silva, *Physical Review A* **102** (2020), 052803, DOI `10.1103/PhysRevA.102.052803`.
- Julien Keller, Sergio Lukic, *Journal of Geometry and Physics* **92** (2015), 252–270, DOI `10.1016/j.geomphys.2015.02.018`.
- Leon A. Takhtajan, Lee-Peng Teo, *Memoirs of the American Mathematical Society* **183** no. 861 (2006), 1–119, DOI `10.1090/memo/0861`.
- Hideitsu Hino, Keisuke Yano, *Information Geometry* **7** (2024), 523–542, DOI `10.1007/s41884-024-00156-x`.

## Normalization firewall

Three objects differing by conventional factors occur:

\[
I_{\rm cl}=\mathbb E[s^2],
\qquad
g_{FS},
\qquad
I_Q=4g_{FS}.
\]

The FCIG geometric comparison to the second-fundamental tensor uses

\[
\frac14 I_{\rm cl}\quad\text{versus}\quad g_{FS},
\]

not raw `I_cl` versus `g_FS`. Any future comparison that drops this factor must be treated as a regression.

Likewise, FRZ and Wan–Zhang explicitly use different form norms/Laplacian conventions. The project compares invariant geometric channels only after the cited FRZ normalization remark; raw operator coefficients are not transplanted silently.
