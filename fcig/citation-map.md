# FCIG Citation Map

**Purpose:** section-by-section provenance guide for the three existing FCIG notes.

Use this map when back-porting inline citations into the original prose. The rule is:

1. cite a source only for the statement it actually supports;
2. label calculations performed in the FCIG note as **derived here**;
3. label new terminology and physical interpretation as **FCIG interpretation/conjecture**.

Full entries: [`references.bib`](references.bib).  
Audited synthesis: [`cited-synthesis.md`](cited-synthesis.md).

---

## A. `research-note.md`

### Local Hermitian weights / line-bundle curvature

**Use:** [Bry93], optionally [ADH21] for differential refinement.

Supports:
- local weights \(\phi_i\);
- transition functions;
- global Chern curvature;
- bundles/connections as differential-cohomological objects.

**Do not cite these as proving:** “information potentials are gauge fields.” That phrase is FCIG interpretation.

### Differential cohomology / curvature vs holonomy

**Use:** [Bry93], [ADH21].

Supports:
- degree-two differential cohomology as a model for line-bundle-with-connection data;
- distinction between curvature and flat holonomy.

**FCIG interpretation:** “local anomaly” vs “global anomaly.”

### Geometric quantization

**Use:** [SW76].

Supports:
- prequantum Hermitian line bundles;
- holomorphic/polarized quantization by sections under standard hypotheses.

### Derived direct image / GRR

**Use:** [Stacks-GRR].

Supports exactly the relative formula

\[
\operatorname{ch}(R\pi_*E)
=
\pi_*(\operatorname{Td}(T_\pi)\operatorname{ch}(E))
\]

under the hypotheses stated there.

**FCIG interpretation:** degree 0 = capacity sector, degree 2 = anomaly sector.

### Determinant line / Quillen metric

**Use:** [Qui85], [BF86a], [BF86b].

- [Qui85]: determinant line/metric in the Cauchy–Riemann setting.
- [BF86a]: metrics and connections on determinant bundles, curvature.
- [BF86b]: Dirac operators, eta invariants, holonomy theorem.

### Bergman expansion

**Use:** [Zel98], [Lu00], [MM07].

- [Zel98]: diagonal Szegő/Bergman asymptotics / Tian theorem.
- [Lu00]: explicit lower-order coefficients and curvature polynomials.
- [MM07]: systematic Bergman-kernel expansion via heat/local-index methods.

**Important:** retain a normalization caveat. The coefficient written as \(1/2\) in some conventions should not be universalized without fixing \(\omega\), curvature, and \(2\pi\) conventions.

### Abelian varieties / theta groups / polarization type

**Use:** [BL04], [Mum83].

Supports:
- line bundles on complex tori;
- polarization type;
- theta/Heisenberg groups;
- dimensions of section spaces for ample line bundles.

The FCIG “single-bundle no-go” is a short consequence **derived in the note**, not a named theorem in [BL04].

### Families-index direction toward anomaly curvature

**Use:** [BF86a], [BF86b].

Supports the direction

\[
\text{geometric/gauge curvature}
\to
\text{determinant-line curvature/holonomy}.
\]

**Do not cite as supporting the inverse map** from determinant anomaly to spacetime curvature.

### Jacobson closure target

**Use:** [Jac95].

Supports:
- local Rindler horizons;
- Clausius relation \(\delta Q=T\delta S\);
- Einstein equation interpreted as an equation of state under the entropy-area assumption.

**Does not support:** an FCIG entropy functional. That remains open.

---

## B. `elliptic-model.md`

### Definition of \(E_\tau\), theta line, theta basis

**Use:** [Mum83], [BL04], [DLMF20].

Supports:
- classical theta series and quasi-periodicity;
- theta characteristics;
- line bundles/theta groups on elliptic/abelian varieties.

### \(\dim H^0(E_\tau,L^k)=k\)

**Use:** [BL04].

This is standard degree/Riemann–Roch theory on elliptic curves/abelian varieties.

### Exact \(L^2\) Gram matrix

\[
\langle s_j,s_m\rangle
=\delta_{jm}(2kY)^{-1/2}.
\]

**Citation:** **derived here**.

Do not attach [Mum83] or [BF86a] as though either source contains this exact normalization.

### Exact Poisson-resummed Bergman density

**Citation:** **derived here** from Poisson summation and the explicit theta basis.

For contextual comparison with the general asymptotic theory, cite [Zel98], [Lu00], [MM07] in the paragraph that contrasts the exact formula with local Bergman asymptotics.

### Exponentially small lattice sector

\[
B_k=k(1+O_\tau(e^{-\pi k\mu(\tau)/2})).
\]

**Citation:** **derived here**.

The interpretation as “nonperturbative global data” is FCIG terminology.

### Theta heat equation

**Use:** [Mum83] plus [ThetaHeat] if an explicit modern equation reference is desired.

Supports

\[
4\pi i\,\partial_\tau\vartheta=\partial_z^2\vartheta.
\]

The level-\(k\) rescaling in the note is **derived here**.

### Hodge bundle / modular forms

**Use:** [Katz73].

Supports modular forms as sections of powers of the Hodge bundle in the moduli interpretation.

### Hodge curvature

\[
F_{\lambda_H}=-\partial\bar\partial\log Y.
\]

**Citation:** **derived here** from the chosen metric \(\|dz\|^2=Y\).

[Katz73] supports the Hodge-bundle setting, not this exact metric normalization.

### Elliptic determinant identity

\[
F_{\det\mathcal H_k}
=-\frac{k}{2}F_{\lambda_H}.
\]

**Citation:** **derived here** from the exact Gram determinant.

Context only: [Qui85], [BF86a].

This is the single most important place not to over-cite.

---

## C. `modular-holonomy.md`

### Classical \(S,T\) transformations

**Use:** [DLMF20], [Mum83].

DLMF §20.7(viii) is an especially safe reference for transformations of the lattice parameter and permutation of the classical Jacobi theta functions.

### Weil representation / eighth-root phase

**Use:** [Fri85].

Friedberg explicitly treats theta transformation formulas via the Weil representation and the eighth root of unity.

### Finite matrices in FCIG convention

\[
(U_S)_{j\ell}=k^{-1/2}e^{-2\pi i j\ell/k},
\qquad
(U_T)_{j\ell}=\delta_{j\ell}e^{\pi i j^2/k}.
\]

**Citation:** **derived here**, with [Fri85] cited for the general Weil/metaplectic framework.

Do not claim Friedberg uses exactly these normalization/sign conventions.

### Gauss phase

\[
(U_SU_T)^3=e^{\pi i/4}C.
\]

**Citation:** **derived here in the chosen convention**; [Fri85] supports the general eighth-root phenomenon.

### Odd \(k\) characteristic swap

**Use:** [DLMF20], [Mum83] for the classical characteristic-permutation phenomenon.

The exact level-\(k\) formulas and \(T^2\) closure in the note are **derived here**.

### Flat anomaly line

\[
\mathscr A_k
=\det\mathcal H_k\otimes\lambda_H^{k/2},
\qquad
F_{\mathscr A_k}=0.
\]

**Citation:** **derived here** from the preceding elliptic curvature identity.

Use [Bry93], [ADH21] only for the general principle that a flat connection can retain nontrivial holonomy.

The phrase “flat anomaly line” is FCIG terminology.

---

# D. Statements that should remain uncited except as FCIG proposals

These are not established by the references above:

- “Bayesian inference is literally a gauge theory.”
- “\(\log h^0\) is thermodynamic entropy without specifying an ensemble.”
- “determinant anomaly curvature generates spacetime curvature.”
- “Bergman density automatically gives Einstein gravity.”
- “metaplectic holonomy is a physical gravitational anomaly in the present model.”
- “FCIG derives Einstein's equation.”

When such statements are discussed, mark them as **interpretation**, **postulate**, **conjecture**, or **open problem**.

---

# Reference keys

- [ADH21] Amabel–Debray–Haine, differential cohomology.
- [BF86a] Bismut–Freed I, determinant metrics/connections/curvature.
- [BF86b] Bismut–Freed II, eta invariants/holonomy.
- [BL04] Birkenhake–Lange, complex abelian varieties.
- [Bry93] Brylinski, differential/Deligne geometry and quantization.
- [DLMF20] NIST DLMF, Chapter 20, especially §20.7(viii).
- [Fri85] Friedberg, theta transformations and Weil representation.
- [Jac95] Jacobson, thermodynamics of spacetime.
- [Katz73] Katz, modular schemes/forms and Hodge-bundle interpretation.
- [Lu00] Lu, lower coefficients of TYZ expansion.
- [MM07] Ma–Marinescu, Bergman kernels.
- [Mum83] Mumford, *Tata Lectures on Theta I*.
- [Qui85] Quillen, determinant of Cauchy–Riemann operators.
- [Stacks-GRR] Stacks Project Tag 02UO.
- [SW76] Simms–Woodhouse, geometric quantization.
- [Zel98] Zelditch, Szegő kernels/Tian theorem.
