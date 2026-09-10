# Semiclassical Atlas Closure

## Master theorem for the proportional-K discrete-series sector

**Status (2026-09-10).**

The sequence JA → RF → UR → BC now closes the leading canonical asymptotic atlas for radial holomorphic-discrete-series matrix coefficients in the FCIG normalization.

\[
\boxed{\textbf{SAC-A: PASS — leading proportional-K semiclassical atlas closed.}}
\]

This is an assembly theorem from the preceding FCIG notes.  It is not a claim that every publication-level uniform remainder constant has already been optimized.

---

## 1. Exact starting point

For the holomorphic discrete series corresponding to q-differentials, radial K-type matrix coefficients admit an exact Jacobi representation.  In the proportional regime

\[
m=\alpha q+o(q),\qquad n=\beta q+o(q),
\]

the coefficient-extraction phase has saddle discriminant

\[
\Delta_{\rm sad}
=(\alpha+\beta+2)^2(r^2-r_-^2)(r^2-r_+^2),
\qquad r=\tanh(t/2),
\]

where, with

\[
\alpha+1=\cosh u_\alpha,\qquad
\beta+1=\cosh u_\beta,
\]

\[
\boxed{t_-=|u_\alpha-u_\beta|,\qquad t_+=u_\alpha+u_\beta.}
\]

Hence the generic phase diagram is

\[
0<t<t_-:\ \text{inner forbidden},\qquad
t_-<t<t_+:\ \text{oscillatory},\qquad
t>t_+:\ \text{outer forbidden}.
\]

---

## 2. Generic bulk and folds

Away from the caustics, ordinary steepest descent gives the oscillatory or exponentially decaying leading forms.  In the forbidden chambers the explicit global rates \(\Phi_-\) and \(\Phi_+\) are those of `global-off-diagonal-rate-closure.md`.

At either simple caustic the two saddles coalesce.  The local normal form is Airy with

\[
z-z_*=O(q^{-1/3}),\qquad t-t_\pm=O(q^{-2/3}).
\]

The same coalescing projective saddle occurs on both sheets, while the cubic orientation changes sign.  The Airy coordinates can be chosen so that the forbidden side is positive on both sheets.

---

## 3. Boundary chart I — diagonal/identity collapse

When

\[
q|\alpha-\beta|=O(1),
\]

the inner fold reaches the identity endpoint.  Writing

\[
n-m=k=O(1),\qquad t=s/q,
\]

the exact hypergeometric coefficient contracts to

\[
\boxed{
M_{m,m+k}^{(q)}(s/q)
\to
J_k(\sqrt{\alpha(\alpha+2)}\,s).
}
\]

For large k, the Bessel turning point matches the generic inner Airy fold.

---

## 4. Boundary chart II — lowest-K sheet merger

When

\[
q\beta=O(1),
\]

write

\[
n=\nu\ \text{fixed},\qquad m/q\to\alpha>0,
\qquad t=u_\alpha+\tau/\sqrt q.
\]

Then

\[
\boxed{
q^{1/4}M_{\nu,m}^{(q)}
\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\to
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}.
}
\]

Equivalently the canonical function is the integer-order parabolic-cylinder function

\[
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{D_\nu(-\sqrt2\tau)}{\sqrt{\nu!}}.
\]

The two generic caustics become

\[
\tau_\pm\to\pm\sqrt{2\nu},
\]

which are precisely the large-order Hermite turning scales.  Their Airy limits recover the two generic folds.

---

## 5. Atlas statement

The leading canonical charts are therefore

\[
\boxed{
\begin{array}{ccl}
\text{generic forbidden bulk}&:&\text{real saddle + }e^{-q\Phi_\pm},\\
\text{generic allowed bulk}&:&\text{conjugate saddles / oscillation},\\
\text{simple caustic}&:&\text{Airy},\\
q|\alpha-\beta|=O(1)&:&\text{Bessel},\\
q\beta=O(1)&:&\text{Hermite--Gaussian / parabolic cylinder}.
\end{array}}
\]

The overlaps are compatible:

\[
\boxed{
\text{Bessel}\xrightarrow{k\to\infty}\text{Airy},
\qquad
\text{Hermite}\xrightarrow{\nu\to\infty}\text{two Airy folds}.
}
\]

Thus no additional leading canonical regime is presently missing from the radial proportional-K phase diagram with \(\alpha,\beta\ge0\), modulo exchange symmetry of the two K-type labels.

---

## 6. Relation to the FCIG orbital side

The representation-side atlas is controlled by the same hyperbolic disk coordinate

\[
r=\tanh(t/2)
\]

that appears in the exact Sun/Bergman orbital kernel.  The orbital transverse Fourier Gamma window localizes at

\[
|\xi|\sim2q\tanh(L/2).
\]

This establishes a quantitative compatibility of semiclassical scales, but not an identification of variables:

\[
\boxed{\xi\neq t\neq n\neq\text{Harish--Chandra spectral parameter}.}
\]

Any stronger identification still requires an explicit transform theorem.

---

## 7. What remains before publication-style freeze

The leading canonical mathematics is closed.  Remaining work is primarily theorem packaging and audit:

1. state compact parameter domains for each uniform remainder estimate;
2. make phase conventions globally consistent under m↔n and orientation reversal;
3. audit every external asymptotic citation against the exact parameter hypotheses;
4. consolidate the gate ledger and remove superseded provisional language;
5. add a concise master abstract/README explaining the result without overstating novelty.

These are real tasks, but they are no longer missing asymptotic regimes.

---

## Gate ledger

\[
\boxed{
\begin{array}{ll}
\text{JA-A1} & \text{PASS},\\
\text{RF-B1/B2/C} & \text{PASS},\\
\text{UR-A1/A2} & \text{PASS at leading uniform architecture},\\
\text{BC-A1} & \text{PASS (Bessel)},\\
\text{BC-A2} & \text{PASS (Hermite--Gaussian)},\\
\text{SAC-A} & \textbf{PASS (master leading atlas)}.
\end{array}}
\]

The stronger full Harish--Chandra pointwise Schwartz uniformity gate UQ-A2 remains logically distinct and is not claimed solved by this local radial atlas.

---

## References

See the detailed references in `jacobi-asymptotic-closure.md`, `uniform-remainder-closure.md`, `boundary-bessel-closure.md`, and `lowest-k-hermite-closure.md`.  Core classical sources include DLMF Chapter 18, Szegő's *Orthogonal Polynomials*, Chester--Friedman--Ursell coalescing-saddle theory, and the cited large-parameter Jacobi literature.

## Claim firewall

- SAC-A assembles derived FCIG formulas and established asymptotic methods; no literature-novelty claim is made.
- The theorem concerns radial matrix coefficients, not Harish--Chandra characters or ordinary traces.
- Leading atlas closure is weaker than a single globally uniform all-derivatives remainder theorem.
- UQ-A2 remains open until pointwise Harish--Chandra Schwartz seminorms are controlled uniformly in q and unrestricted K-type.