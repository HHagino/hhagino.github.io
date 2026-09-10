# Born–Slater Information Geometry — Citation Audit

**Date:** 2026-09-10  
**Note:** [`born-slater-information.md`](born-slater-information.md)  
**Bibliography:** [`born-slater-information.bib`](born-slater-information.bib)

This audit separates historical facts, established theorems, elementary deductions, FCIG interpretations, and open reconstruction claims.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| Born introduced the probabilistic amplitude-squared interpretation in scattering theory | **Established / historical** | [Bor26] | Historical origin of the Born probability interpretation; not an information-geometric derivation. |
| Pure quantum states are rays/projective Hilbert points with natural Kähler/Fubini–Study geometry | **Established** | [AS98] | Standard geometric quantum mechanics. |
| Hilbert-space angle and optimal statistical distinguishability of pure preparations are related | **Established** | [Woo81] | Wootters' statistical-distance result. |
| For pure states, quantum Fisher information is \(4g_{FS}\) in the standard convention, and fixed-measurement classical Fisher is bounded above by QFI | **Established** | [BC94] | Braunstein–Caves' measurement-optimization/statistical-distance result. |
| Born measurement map \(\mathcal B_M:\mathbb P(\mathcal H)\to\mathcal P(\Omega)\) is “information-contracting” | **FCIG interpretation of established inequality** | [BC94] | Precise statement is pullback Fisher \(\preceq I_Q\); “channel/shadow” is interpretive language. |
| \(4g_{FS}=I_M+4\operatorname{Var}(a)\) for a fixed pure-state measurement representation and real direction | **Derived here / companion-note identity** | background [BC94] | Direct amplitude/phase decomposition; no claim that BC94 states this exact formula in FCIG notation. |
| Gleason theorem gives \(\mu(P)=\operatorname{tr}(\rho P)\) under Hilbert-lattice probability assumptions in dimension at least three | **Established** | [Gle57] | Requires the Hilbert event structure and additivity/noncontextuality assumptions; not a derivation of Hilbert space. |
| For pure \(\rho\) and rank-one \(P_\phi\), Gleason form reduces to \(|\langle\phi|\psi\rangle|^2\) | **Established corollary** | [Gle57] | Algebraic specialization of the density-operator form. |
| POVM/effect version yielding density-operator states | **Established** | [Bus03] | Busch's Gleason-type effect formulation. |
| Single Slater determinants form a Grassmannian submanifold of projective many-body Hilbert space | **Established** | [AS20] | Aoto–da Silva state this identification explicitly. |
| Born image of normalized Slater determinant equals a projection DPP density | **Derived here from elementary linear algebra / standard DPP theory** | [HKPV09; Ber08] | Uses \(|\det U|^2=\det(U^*U)\); DPP interpretation is standard. |
| Bergman DPPs describe free fermionic systems in complex-geometric settings | **Established** | [Ber08] | Berman develops Bergman-kernel DPPs with free-fermion applications. |
| Slater determinant is “a common mother object” for Grassmannian quantum geometry and determinantal probability geometry | **FCIG interpretation** | [AS20; Ber08] | Synthesis, not a quoted literature theorem. |
| Chern-covariant Grassmannian metric of the hyperbolic \(H^0(K^q)\) family tends to WP after normalization | **Derived in companion FCIG note** | see `grassmannian-quantum-information.md` | Depends on the explicitly chosen minimal-solution/Chern connection model and prior FRZ/Wan–Zhang audit. |
| Thermodynamic/determinant structure alone derives Born's rule | **Explicitly NOT claimed** | — | Open reconstruction problem. |
| Thermodynamic/determinant structure alone derives complex Hilbert space or fermionic exterior powers | **Explicitly NOT claimed** | — | Open reconstruction problems R1 and R3. |

## Primary-source checks

Metadata checked against publisher/primary pages on 2026-09-10:

- Max Born, *Zeitschrift für Physik* **37** (1926), 863–867, DOI `10.1007/BF01397477`.
- Andrew M. Gleason, *Journal of Mathematics and Mechanics* **6** (1957), 885–893, DOI `10.1512/iumj.1957.6.56050`.
- W. K. Wootters, *Physical Review D* **23** (1981), 357–362, DOI `10.1103/PhysRevD.23.357`.
- Samuel L. Braunstein and Carlton M. Caves, *Physical Review Letters* **72** (1994), 3439–3443, DOI `10.1103/PhysRevLett.72.3439`.
- Paul Busch, *Physical Review Letters* **91** (2003), 120403, DOI `10.1103/PhysRevLett.91.120403`.
- Paolo Facchi et al., *Physics Letters A* **374** (2010), 4801–4803, DOI `10.1016/j.physleta.2010.10.005`.
- Yuri A. Aoto and Márcio F. da Silva, *Physical Review A* **102** (2020), 052803, DOI `10.1103/PhysRevA.102.052803`.

## Normalization firewall

Three metrics must not be conflated:

\[
I_M,
\qquad
I_Q,
\qquad
g_{FS}.
\]

For the standard pure-state convention used here,

\[
I_Q=4g_{FS},
\qquad
I_M\le I_Q.
\]

Therefore comparisons of classical Fisher with projective geometry must either use raw \(I_M\) versus \(4g_{FS}\), or quarter-Fisher \(I_M/4\) versus \(g_{FS}\). Dropping this factor is a normalization error.

## Reconstruction firewall

The note deliberately separates:

1. **Born as a postulate/measurement map**: \(p=\langle\psi|M|\psi\rangle\);
2. **Gleason-type reconstruction**: probability assignments on an already-given Hilbert event structure are constrained to density-operator form under stated assumptions;
3. **FCIG emergence program**: derive the projective Hilbert/event structure and/or justify those probability assumptions from independent thermodynamic, cohomological, or information principles.

Only item 2 is an established reconstruction theorem. Item 3 remains open.