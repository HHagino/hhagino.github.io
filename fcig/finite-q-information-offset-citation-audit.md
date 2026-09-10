# Finite-q Information Offset — Citation Audit

**Date:** 2026-09-10  
**Note:** [`finite-q-information-offset.md`](finite-q-information-offset.md)  
**Bibliography:** [`finite-q-information-offset.bib`](finite-q-information-offset.bib)

This audit separates quoted literature from the FCIG subtraction/polarization that produces the finite-quantization offset.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| For `K_X \otimes L^k`, the Bergman kernel has the TYZ expansion with canonical-bundle coefficients `A_0=1`, `A_1=-rho/2`, and the stated `A_2` curvature polynomial | **Established** | [WZ21], background [Lu00; MM07] | Wan--Zhang Eq. (2.12)/Theorems 2.3--2.4. |
| In the hyperbolic curve specialization `L=K_X`, `k=q-1`, `rho=-1`, the `A_2` coefficient vanishes | **Derived here** | formula: [WZ21] | Uses constant scalar curvature and the complex-dimension-one curvature contractions. |
| `B_q=(2q-1)/(4 pi)+O(q^-2)` | **Derived here** | [WZ21] | Conservative consequence of the full TYZ expansion after `A_2=0`; fixed-fiber statement. |
| `A_q=(2q-1)/(4 pi) G_WP+O(q^-2)` | **Derived here** | previous row | Bergman trace identity and Hermitian polarization. |
| FRZ trace curvature splits as `Chern^(q)=I^(q)+II^(q)` with `I^(q)=(q-1) int f(mu) B_q` and the positive resolvent expression for `II^(q)` | **Established** | [FRZ20] | Proposition 1. |
| `f(mu)=(1+square_0)^(-1)|mu|^2` | **Established** | [FRZ20] | Their Eq. (2.5), based on the hyperbolic/Schumacher setup. |
| `int f(mu)=||mu||_WP^2` | **Derived here / elementary** | [FRZ20] for the equation defining `f` | Integrate `(1+square_0)f=|mu|^2` on the compact surface. |
| `I^(q)=((q-1)(2q-1))/(4 pi) G_WP+O(q^-1)` | **Derived here** | [FRZ20; WZ21] | Substitute the refined Bergman kernel into FRZ's first curvature summand. |
| `Chern^(q)= [6q(q-1)+1]/(12 pi) G_WP + O(q^2 exp(-q l_0))` | **Established** | [FRZ20] | FRZ curvature asymptotic on a fixed compact hyperbolic surface. |
| The FCIG intrinsic KS resolvent `K_q` equals FRZ `II^(q)` in the stated norm convention | **Typing identification** | [FRZ20] + companion FCIG note | Earlier note called the same channel `R_q`; the present note standardizes it as `K_q`. |
| `K_q=(3q-2)/(12 pi) G_WP+O(q^-1)` | **Derived here** | [FRZ20; WZ21] | Exact subtraction `Chern^(q)-I^(q)`. |
| Exact source decomposition `A_q=B_q+K_q` | **Established in companion FCIG derivation from FRZ minimal-solution identity** | [FRZ20] | The source/minimal-solution/resolvent identity is exact; notation fixed in `grassmannian-quantum-information.md`. |
| `B_q=(3q-1)/(12 pi) G_WP+O(q^-1)` | **Derived here** | preceding rows | Subtract `K_q` from `A_q`. |
| `B_q-K_q=1/(12 pi) G_WP+O(q^-1)` | **Derived here** | preceding rows | Main finite-q offset; no literature-novelty claim. |
| `I_HBF,q^KE=B_q` in the local KE/BLS realization | **Derived in companion FCIG notes** | background [Var24; Bern09] | Depends on the separately audited BLS position transport and Pluecker/second-fundamental identification. |
| `I_HBF,q^KE-K_q=1/(12 pi)G_WP+O(q^-1)` | **Derived here** | current result + companion BLS/HBF identity | Statistical form of the main offset. |
| `B_q/A_q=1/2+1/(12q)+O(q^-2)` and `K_q/A_q=1/2-1/(12q)+O(q^-2)` | **Derived here** | algebra from refined expansions | Refined 50--50 law on nonzero diagonal directions. |
| The coefficient `1/(12 pi)` has a Bernoulli/local-index interpretation | **Interpretation grounded in established index polynomial** | [TZ87; FRZ20] | `6q^2-6q+1` is the standard local-index coefficient; the analytic offset was proved independently by subtraction. |
| The remainder can already be replaced everywhere by an exponential one | **NOT claimed** | [Ber12] | Berman proves exponentially accurate constant-curvature Bergman asymptotics in a closely related canonical setting, but the exact normalization and desired family-uniform crosswalk is left open. |
| Full Quillen curvature equals the Fisher/KS offset | **NOT claimed** | — | The full determinant/direct-image curvature contains larger-order sectors. |

## Primary-source checks

Metadata and formulas were checked on 2026-09-10 against the publisher/primary pages for:

- Fedosova--Rowlett--Zhang, *Annals of Global Analysis and Geometry* **57** (2020), 23--60, DOI `10.1007/s10455-019-09687-4`.
- Wan--Zhang, *Geometriae Dedicata* **214** (2021), 489--517, DOI `10.1007/s10711-021-00625-y`.
- Berman, *International Mathematics Research Notices* **2012**(22), 5031--5062, DOI `10.1093/imrn/rnr229`.
- Zograf--Takhtajan, *Russian Mathematical Surveys* **42**(6) (1987), 169--190, DOI `10.1070/RM1987V042N06ABEH001501`.
- Lu, *American Journal of Mathematics* **122**(2) (2000), 235--273, DOI `10.1353/ajm.2000.0013`.

## Normalization firewall

The note uses the repository's Hermitian Weil--Petersson pairing

\[
G_{\rm WP}(\mu,\bar\nu)=\int_X\langle\mu,\nu\rangle dA.
\]

The coefficient `1/(12 pi)` is therefore a coefficient of this Hermitian quadratic form. It must not be copied directly into a first-Chern-form statement, where factors of `i`, `2 pi`, or a convention for `omega_WP` enter.

## Indexing firewall

FRZ use the exponent `m` for `K^m`. Wan--Zhang use `k` for the positive bundle in `K_X \otimes L^k`. To represent the same space `H^0(K_X^q)` in the Wan--Zhang formula one must set

\[
L=K_X,\qquad k=q-1.
\]

Failing to make this shift changes precisely the constant term being computed.

## Novelty firewall

The main coefficient follows by combining known, explicit formulas. Targeted searching did not reveal a paper presenting the same quantity specifically as a Fisher--Kodaira--Spencer finite-q information offset. This is not a novelty certification. Any submission should run a broader MathSciNet/zbMATH/reference-chain audit and obtain expert verification of the convention crosswalk.