# Semiclassical Publication-Freeze Status Audit

**Audit date:** 2026-09-10  
**Authoritative entry points:** `semiclassical-preprint.md`, `semiclassical-atlas-closure.md`.

This file resolves status drift across the chronological JA/RF/UR/BC derivation notebooks. Older notes are intentionally retained as research history, but their earlier OPEN/provisional language is not the current gate state when a later closure note exists.

## Authoritative gate ledger

\[
\boxed{\textbf{JA-A1: PASS — fixed K-window.}}
\]

The former `JA-A2: OPEN` statement in `jacobi-asymptotic-closure.md` is **superseded** by the proportional-K sequence `proportional-k-type-rate-function.md` through `semiclassical-atlas-closure.md`.

\[
\boxed{\textbf{RF-B1: PASS — exact off-diagonal caustic surface.}}
\]

\[
\boxed{\textbf{RF-B2: PASS — two-sheet Airy normalization.}}
\]

\[
\boxed{\textbf{RF-C: PASS — global off-diagonal forbidden rates.}}
\]

\[
\boxed{\textbf{UR-A1: PASS — generic saddle/Airy uniform architecture.}}
\]

\[
\boxed{\textbf{UR-A2: PASS — boundary critical scales.}}
\]

The former `BC-A: OPEN` line in `uniform-remainder-closure.md` is **superseded** by the next two closure notes:

\[
\boxed{\textbf{BC-A1: PASS — Bessel identity-endpoint chart.}}
\]

\[
\boxed{\textbf{BC-A2: PASS — Hermite--Gaussian lowest-K merger chart.}}
\]

Accordingly, the sentence in `boundary-bessel-closure.md` that calls BC-A2 the remaining boundary problem is historical and **superseded by** `lowest-k-hermite-closure.md`.

Finally,

\[
\boxed{\textbf{SAC-A: PASS — leading proportional-K semiclassical atlas closed.}}
\]

## Corrected proportional-rate wording

The provisional inequality in the old JA note,

\[
\Re\Phi(\alpha,\beta,t)\ge \frac{t}{2q}+\cdots,
\]

should not be used. It mixes an \(O(1)\) rate function with the large parameter \(q\) awkwardly. For comparison with the rank-one Harish--Chandra factor one should instead formulate a bound at the exponent level, for example

\[
\boxed{
q\,\Re\Phi(\alpha,\beta,t)
\ge
\frac t2+N\log(1+t)-O(\log q),
}
\]

on whatever parameter domain is being used. The local semiclassical atlas derived in the RF/UR/BC chain does **not** by itself prove this global all-derivatives Harish--Chandra-Schwartz estimate.

## What remains open

The following items remain distinct from SAC-A and are not to be marked solved merely because the radial atlas is closed:

- **UQ-A2:** full pointwise Harish--Chandra-Schwartz control uniform in \(q\) and unrestricted K-type indices;
- one globally explicit all-orders remainder theorem with constants uniform across all strata;
- a globally fixed phase convention under \(m\leftrightarrow n\), orientation reversal, and covering conventions;
- any theorem identifying the transverse orbital Fourier variable with a Harish--Chandra spectral parameter.

## Citation audit

The classical asymptotic tools are typed as follows.

1. **CFU Airy reduction:** NIST DLMF §2.4(v), coalescing saddle points.
2. **Jacobi-to-Hermite limit relations:** NIST DLMF §18.7(iii).
3. **Large-parameter Jacobi/Hermite approximations:** NIST DLMF §18.15(vi).
4. **Fixed-parameter uniform Jacobi asymptotics with error bounds:** C. L. Frenzen and R. Wong, *Canadian Journal of Mathematics* 37 (1985), 979–1007, DOI 10.4153/CJM-1985-053-5.
5. **Large degree and large parameters:** A. Gil, J. Segura, N. M. Temme, *Journal of Mathematical Analysis and Applications* 494 (2021), 124642, DOI 10.1016/j.jmaa.2020.124642.

These sources support the classical asymptotic mechanisms. The FCIG-specific caustic formulas, branch choices, normalizations, double scalings, and chart matching are recorded as derivations in the FCIG notes, not as claims that those formulas already appear in the cited literature.

## Precedence rule

For the proportional-K semiclassical branch, use the following precedence order when status language conflicts:

\[
\boxed{
\texttt{semiclassical-preprint.md}
\;>\;
\texttt{semiclassical-atlas-closure.md}
\;>\;
\text{later RF/UR/BC closure notes}
\;>\;
\text{earlier chronological notebooks}.
}
\]

This keeps the derivation history intact while giving readers one unambiguous publication-freeze status.