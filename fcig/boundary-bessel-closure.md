# Boundary Bessel Closure

> **STATUS UPDATE (2026-09-10).** This derivation is complete. Its historical closing statement that `BC-A2` remained open is superseded by `lowest-k-hermite-closure.md`, where `BC-A2: PASS`. The consolidated current statement is `semiclassical-preprint.md` / `SAC-A: PASS`.

## BC-A1 — diagonal-endpoint double scaling

\[
\boxed{\textbf{BC-A1: PASS — the }q|\alpha-\beta|=O(1)\textbf{ boundary chart is Bessel.}}
\]

For \(n=m+k\), \(k\ge0\) fixed, the exact radial coefficient is

\[
M_{m,m+k}^{(q)}(t)=\mathcal N_{m,m+k}(q)\left(\cosh\frac t2\right)^{-2q}\left(\tanh\frac t2\right)^kP_m^{(k,2q-1)}\left(1-2\tanh^2\frac t2\right),
\]

\[
\mathcal N_{m,m+k}(q)=\left(\frac{m!\Gamma(2q+m+k)}{(m+k)!\Gamma(2q+m)}\right)^{1/2}.
\]

Using the terminating hypergeometric representation and the scaling

\[
\frac mq\to\alpha>0,\qquad k\text{ fixed},\qquad t=\frac{s}{q},
\]

one obtains the compact-set contraction

\[
{}_2F_1\left(-m,m+k+2q;k+1;r^2\right)\longrightarrow{}_0F_1\left(;k+1;-\frac{\alpha(\alpha+2)s^2}{4}\right),
\]

with \(r=\tanh(t/2)\). The normalization factors cancel against the standard \({}_0F_1\)-Bessel conversion, giving

\[
\boxed{M_{m,m+k}^{(q)}(s/q)\longrightarrow J_k\!\left(\sqrt{\alpha(\alpha+2)}\,s\right)}
\]

uniformly for bounded \(s\), up to the fixed unitary phase convention.

At the collapsing inner caustic,

\[
qt_-\to\frac{k}{\sqrt{\alpha(\alpha+2)}},
\]

hence the Bessel argument equals \(k\):

\[
\boxed{\sqrt{\alpha(\alpha+2)}\,qt_-=k.}
\]

This is the large-order Bessel turning scale and provides the overlap with the generic inner Airy chart.

## Gate status

\[
\boxed{\textbf{BC-A1: PASS.}}
\]

The sequel has now also been completed:

\[
\boxed{\textbf{BC-A2: PASS — lowest-K sheet merger is Hermite--Gaussian.}}
\]

See `lowest-k-hermite-closure.md`. Together,

\[
\boxed{\textbf{BC-A: PASS — both critical boundary charts are closed.}}
\]

## Claim firewall

- The Mehler--Heine/Bessel mechanism and large-order Bessel-to-Airy transition are classical.
- The FCIG scaling, Bessel argument, and its match to the inner caustic are the content derived in this notebook.
- This is a radial matrix-coefficient statement, not a character identity.
- `BC-A: PASS` is part of the leading semiclassical atlas and does not by itself prove unrestricted all-derivatives HC-Schwartz uniformity.

## References

1. NIST Digital Library of Mathematical Functions, §18.11(ii), Mehler--Heine type formulas for Jacobi polynomials.
2. NIST Digital Library of Mathematical Functions, §§10.19--10.20, large-order and Airy-uniform asymptotics for Bessel functions.
3. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975.
4. A. Gil, J. Segura, N. M. Temme, J. Math. Anal. Appl. **494** (2021), 124642.

## Cross-references

- `uniform-remainder-closure.md`
- `two-sheet-airy-normalization.md`
- `lowest-k-hermite-closure.md`
- `semiclassical-atlas-closure.md`
- `semiclassical-preprint.md`
