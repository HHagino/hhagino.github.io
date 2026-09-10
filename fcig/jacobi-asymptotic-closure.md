# Jacobi Asymptotic Closure for the Holomorphic Discrete Series

> **STATUS UPDATE (2026-09-10).** This is a historical derivation notebook. Its former `JA-A2: OPEN` status has been superseded by `proportional-k-type-rate-function.md`, the RF/UR/BC closure sequence, and the consolidated `semiclassical-preprint.md`. The current branch status is `SAC-A: PASS` at the level of the leading semiclassical atlas. The stronger unrestricted all-derivatives Harish--Chandra--Schwartz problem remains the separate gate `UQ-A2`.

## Status

The previous note `parameter-uniform-matrix-decay.md` reduced full uniform Harish--Chandra-Schwartz control to parameter-uniform estimates for the Jacobi-polynomial formula of the holomorphic discrete-series matrix coefficients.

This note originally closed the **fixed K-window** regime and isolated the proportional regime as the next problem. That proportional problem has since been solved at the level of the leading saddle/Airy/Bessel/Hermite atlas; see `semiclassical-preprint.md` for the current theorem statement.

\[
\boxed{\textbf{JA-A1: PASS — fixed K-window, uniform in }q.}
\]

\[
\boxed{\textbf{JA-A2: SUPERSEDED — closed downstream at leading-atlas level by SAC-A.}}
\]

---

## 1. Explicit discrete-series matrix coefficient

Let \(G=SU(1,1)\simeq SL(2,\mathbb R)\) up to the usual finite-covering conventions. In the normalized monomial K-type basis, for \(n\ge m\), suppressing the fixed compact phase,

\[
M_{m,n}^{(q)}(t)=\mathcal N_{m,n}(q)\left(\cosh\frac t2\right)^{-2q}\left(\tanh\frac t2\right)^{n-m}P_m^{(n-m,2q-1)}\!\left(1-2\tanh^2\frac t2\right),
\]

\[
\mathcal N_{m,n}(q)=\left(\frac{m!\Gamma(2q+n)}{n!\Gamma(2q+m)}\right)^{1/2}.
\]

The \(m\ge n\) case is obtained by the adjoint symmetry once the phase convention is fixed.

## 2. Fixed K-window

For fixed \(0\le m,n\le M\), the gamma ratios and terminating Jacobi series have only polynomial dependence on \(q\). Together with unitarity on compact radial sets and exponential radial localization, this gives, for fixed left/right differential operators \(D,E\) and every \(N\),

\[
|L_D R_E m_{m,n}^{(q)}(g)|\le C_{D,E,M,N}(1+q)^{B_{D,E,M}}\Xi(g)(1+\sigma(g))^{-N}.
\]

Thus

\[
\boxed{\textbf{JA-A1: PASS.}}
\]

## 3. Historical proportional target and downstream resolution

The original open regime was

\[
m\sim\alpha q,\qquad n\sim\beta q,
\]

where degree and Jacobi parameters vary simultaneously. The correct coefficient-extraction phase was subsequently derived as

\[
\Psi_{\alpha,\beta,r}(z)=\beta\log(z+r)-(\beta+2)\log(1+rz)-\alpha\log z,
\qquad r=\tanh(t/2).
\]

The downstream notes then established:

- the exact two-sheet caustic surface \(t_\pm=|u_\alpha-u_\beta|,u_\alpha+u_\beta\);
- explicit real forbidden saddles and rate functions;
- Airy normal forms at simple folds;
- the Bessel chart when \(q|\alpha-\beta|=O(1)\);
- the Hermite--Gaussian chart when \(q\beta=O(1)\);
- overlap of those boundary charts with the generic Airy charts.

Therefore the old proportional gate is no longer open:

\[
\boxed{\textbf{JA-A2: SUPERSEDED by RF/UR/BC and SAC-A.}}
\]

The old provisional inequality involving \(\Re\Phi\ge t/(2q)+\cdots\) is withdrawn. A genuine unrestricted Harish--Chandra comparison is an exponent-level, all-derivatives uniformity problem and belongs to `UQ-A2`, not to the leading atlas theorem.

## 4. Current gate ledger

\[
\boxed{\textbf{JA-A1: PASS — fixed K-window.}}
\]

\[
\boxed{\textbf{JA-A2: SUPERSEDED — proportional leading atlas closed downstream.}}
\]

\[
\boxed{\textbf{SAC-A: PASS — master leading semiclassical atlas.}}
\]

\[
\boxed{\textbf{UQ-A2: OPEN — stronger unrestricted pointwise HC-Schwartz uniformity.}}
\]

## 5. Claim firewall

- The exact Jacobi formula is a radial matrix-coefficient formula, not a Harish--Chandra character formula.
- Fixed-K estimates do not imply unrestricted K-type estimates.
- `SAC-A: PASS` means closure of the leading canonical semiclassical atlas, not a single global all-orders remainder theorem.
- K-type labels, Cartan radius, transverse orbital Fourier frequency, and Harish--Chandra spectral variables remain distinct.
- No novelty claim is made for classical Jacobi/Airy/Bessel/Hermite asymptotic machinery.

## References

1. NIST Digital Library of Mathematical Functions, §15.9(i), Jacobi polynomials and Gauss hypergeometric functions.
2. C. L. Frenzen and R. Wong, *A Uniform Asymptotic Expansion of the Jacobi Polynomials with Error Bounds*, Canadian Journal of Mathematics **37** (1985), 979--1007.
3. A. Gil, J. Segura, and N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss--Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. **494** (2021), 124642.
4. NIST Digital Library of Mathematical Functions, Chapter 36 and §2.4(v), coalescing-saddle canonical asymptotics.

## FCIG cross-references

- `proportional-k-type-rate-function.md`
- `two-sheet-airy-normalization.md`
- `global-off-diagonal-rate-closure.md`
- `boundary-bessel-closure.md`
- `lowest-k-hermite-closure.md`
- `semiclassical-atlas-closure.md`
- `semiclassical-preprint.md`
