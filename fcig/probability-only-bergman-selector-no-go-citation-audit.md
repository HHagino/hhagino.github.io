# Probability-Only Bergman Selector — Citation Audit

**Date:** 2026-09-12

**Primary note:** [`probability-only-bergman-selector-no-go.md`](probability-only-bergman-selector-no-go.md)

| Claim | Status | Source / proof boundary |
|---|---|---|
| Projection DPP particle count is the sum of Bernoulli variables with kernel eigenvalues; rank-\(N\) projection gives exactly \(N\) points | **Established** | [HKPV06] |
| Positive Hermitian line bundles and their Bergman kernels define complex-geometric DPP/free-fermion models | **Established** | [Ber08] |
| Standard atomless probability models admit strongly mixing automorphisms, e.g. by transport of a Bernoulli shift | **Classical background** | [Hal56]; the needed mixing implication is restated in the note |
| A strongly mixing Koopman operator has no nonzero finite-dimensional invariant subspace in \(L^2_0\) | **Derived here / elementary** | Compactness of the finite-dimensional unitary group contradicts decay of matrix coefficients; full proof included |
| Full probability-space automorphism invariance leaves only the constant finite-dimensional sector | **Derived here** | Theorem 3.1; apply the preceding lemma to one mixing automorphism |
| A probability-only natural finite-rank projection DPP has rank at most one | **Derived here** | Corollaries 3.2–3.3 plus [HKPV06] |
| Polarized Hermitian complex data select the Dolbeault operator, Bergman projection and DPP naturally | **Established constructions + derived assembly** | Standard Dolbeault/Bergman functoriality; DPP endpoint [Ber08] |
| No conceivable rule \(p\mapsto D_p\) exists | **Not claimed** | The theorem only excludes nontrivial finite-rank projection selectors natural under all measure-preserving isomorphisms on the stated atomless category |
| Statistical axioms reconstruct a complex polarization | **Open** | This is the successor problem, not a theorem |

## Bibliographic checks

- Hough–Krishnapur–Peres–Virág: *Probability Surveys* **3** (2006), 206–229, DOI `10.1214/154957806000000078`, arXiv `math/0503110`.
- Berman: arXiv `0811.3341`, submitted 20 November 2008; the note uses only its Bergman-DPP/free-fermion construction, not its asymptotic theorems.
- Halmos: *Lectures on Ergodic Theory*, Chelsea Publishing Company, 1956. It is background for classical mixing/Koopman language; the new no-go deduction is proved in full and is not attributed to Halmos.

## Novelty firewall

No literature-newness claim is made merely because the short symmetry proof was not located verbatim in the targeted search. The publishable content, if pursued, is the categorical classification of FCIG selectors and the enriched reconstruction problem; a dedicated MathSciNet/zbMATH citation search remains necessary before submission.
