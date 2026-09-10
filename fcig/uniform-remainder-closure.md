# Uniform Remainder Closure

> **STATUS UPDATE (2026-09-10).** This notebook identified the two critical boundary scales before their canonical models were derived. Its historical `BC-A: OPEN` status is superseded by `boundary-bessel-closure.md` and `lowest-k-hermite-closure.md`. Both boundary charts now pass, and the consolidated leading atlas is `SAC-A: PASS` in `semiclassical-preprint.md`.

## UR-A — generic proportional-K uniformity and boundary double scaling

\[
\boxed{\textbf{UR-A1: PASS — generic proportional sector admits uniform saddle/Airy asymptotics.}}
\]

\[
\boxed{\textbf{UR-A2: PASS — both boundary degenerations become critical at a }q^{-1}\textbf{ parameter scale.}}
\]

\[
\boxed{\textbf{BC-A: PASS — Bessel and Hermite--Gaussian boundary replacements derived downstream.}}
\]

For \(m=\alpha q\), \(n=\beta q\), \(\alpha\ge\beta>0\), and \(r=\tanh(t/2)\), the coefficient-extraction phase is

\[
\Psi_{\alpha,\beta,r}(z)=\beta\log(z+r)-(\beta+2)\log(1+rz)-\alpha\log z.
\]

Its saddle equation reduces to

\[
r(\alpha+2)z^2+Bz+\alpha r=0,
\qquad B=(\alpha-\beta)+(\alpha+\beta+2)r^2.
\]

With \(\alpha+1=\cosh u_\alpha\), \(\beta+1=\cosh u_\beta\), the two caustics are

\[
\boxed{t_-=u_\alpha-u_\beta,\qquad t_+=u_\alpha+u_\beta}
\]

for \(\alpha\ge\beta\). On compact generic parameter sets away from the boundary degenerations, the two-saddle Chester--Friedman--Ursell reduction gives Airy fold charts near \(t_\pm\), while ordinary steepest descent applies away from the folds. This is `UR-A1: PASS`.

## Diagonal boundary scale

Let \(\delta=\alpha-\beta\downarrow0\). Then

\[
t_-=\frac{\delta}{\sqrt{\alpha(\alpha+2)}}+O(\delta^2),
\]

and comparison of the inner Airy width with the distance to the radial endpoint gives

\[
\frac{\Delta t_-^{\rm Airy}}{t_-}\asymp(q\delta)^{-2/3}.
\]

Hence the separated Airy model fails when

\[
\boxed{q|\alpha-\beta|=O(1).}
\]

The direct double-scaled coefficient was subsequently evaluated in `boundary-bessel-closure.md` and gives

\[
M_{m,m+k}^{(q)}(s/q)\to J_k(\sqrt{\alpha(\alpha+2)}\,s).
\]

## Lowest-K boundary scale

As \(\beta\downarrow0\),

\[
t_+-t_-=2u_\beta=2\sqrt{2\beta}+O(\beta^{3/2}),
\]

and comparison with the Airy widths gives

\[
\boxed{q\beta=O(1).}
\]

The direct double scaling was subsequently evaluated in `lowest-k-hermite-closure.md`; for fixed \(\nu=q\beta\),

\[
q^{1/4}M_{\nu,m}^{(q)}\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\to[\pi\alpha(\alpha+2)]^{-1/4}\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}.
\]

Thus the formerly open boundary problem is closed.

## Unified boundary law

\[
\boxed{q\,d_{\rm bdry}\gg1\Longrightarrow\text{separated generic Airy folds},}
\qquad d_{\rm bdry}\in\{|\alpha-\beta|,\beta\},
\]

whereas

\[
\boxed{q\,d_{\rm bdry}=O(1)}
\]

requires a boundary canonical model. Those models are now

\[
\boxed{q|\alpha-\beta|=O(1)\Rightarrow\text{Bessel},}
\qquad
\boxed{q\beta=O(1)\Rightarrow\text{Hermite--Gaussian / parabolic cylinder}.}
\]

## Gate ledger

\[
\boxed{\textbf{UR-A1: PASS},\quad\textbf{UR-A2: PASS},\quad\textbf{BC-A1: PASS},\quad\textbf{BC-A2: PASS}.}
\]

Consequently

\[
\boxed{\textbf{SAC-A: PASS — leading semiclassical atlas closed.}}
\]

The remaining stronger problem is not another missing canonical chart: it is the global all-derivatives, unrestricted-K uniform remainder/Harish--Chandra-Schwartz problem `UQ-A2`.

## Claim firewall

- Generic CFU Airy uniformity is asserted only away from the two critical boundary degenerations.
- The Bessel and Hermite models are derived in downstream notes, not inferred merely by formal limits of Airy formulas.
- Leading atlas closure is weaker than a single global all-orders theorem with explicit constants across all strata.
- No novelty claim is made for classical canonical functions or coalescing-saddle machinery.

## References

1. NIST Digital Library of Mathematical Functions, §2.4(v) and Chapter 36, coalescing saddle points and canonical integrals.
2. NIST Digital Library of Mathematical Functions, §§10.19--10.20, Bessel large-order/Airy transitions.
3. NIST Digital Library of Mathematical Functions, §§18.7 and 18.15, Jacobi/Hermite limit and large-parameter asymptotics.
4. C. Chester, B. Friedman, and F. Ursell, *An extension of the method of steepest descents*, Proc. Cambridge Philos. Soc. **53** (1957), 599--611.

## Cross-references

- `two-sheet-airy-normalization.md`
- `boundary-bessel-closure.md`
- `lowest-k-hermite-closure.md`
- `semiclassical-atlas-closure.md`
- `semiclassical-preprint.md`
