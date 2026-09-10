# FCIG: Character/Trace Firewall for the Hyperbolic Discrete Series

**Status:** exact operator-theoretic correction + revised representation-theory target  
**Date:** 2026-09-10  
**Depends on:** [`discrete-series-selberg-crosswalk.md`](discrete-series-selberg-crosswalk.md), [`orbital-character-closure.md`](orbital-character-closure.md), [`toeplitz-orbital-insertion.md`](toeplitz-orbital-insertion.md), [`disk-transported-bergman.md`](disk-transported-bergman.md).

---

## 0. Correction

The exact algebraic identity

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}}
=\sum_{k\ge0}e^{-(q+k)L}
\tag{0.1}
\]

must **not** be interpreted as an ordinary Hilbert-space trace of the unitary operator `pi_q(a_{L/2})` obtained by summing a literal discrete list of eigenvalues `e^{-(q+k)L}`.

The holomorphic discrete series is infinite-dimensional and unitary. Therefore `pi_q(a_{L/2})` is unitary. If it were trace class, all of its singular values would equal `1`, so the trace norm would be

\[
\sum_{j=1}^{\infty}1=\infty.
\]

Hence

\[
\boxed{
\pi_q(a_{L/2})\ \text{is not trace class.}
}
\tag{0.2}
\]

The Harish--Chandra character is instead a conjugation-invariant distribution on the group, represented by an analytic function on the regular set. Equation (0.1) is the value of that character function on the regular positive split Cartan in the chosen normalization.

So the slogan is

\[
\boxed{
\text{character value}\neq\text{ordinary operator trace at a single hyperbolic element}.
}
\tag{0.3}
\]

---

## 1. Consequence for the “descendant tower” language

The geometric-series rewrite

\[
\frac{1}{1-e^{-L}}=1+e^{-L}+e^{-2L}+\cdots
\]

is algebraically correct, but by itself it does not prove that the terms are eigenvalues of a hyperbolic translation acting on a `K`-type ladder.

For a hyperbolic element the correct representation-theoretic denominator is the split-Cartan/Weyl denominator appearing in the Harish--Chandra character formula. Therefore the previous phrase “nonzero cyclic modes should supply the descendant denominator” is only a heuristic until an actual transform identity is proved.

The corrected target is

\[
\boxed{
\text{cyclic Toeplitz orbital transform}
\longleftrightarrow
\text{Harish--Chandra/Weyl character denominator},
}
\tag{1.1}
\]

not a naive eigenvalue sum.

---

## 2. Why Toeplitz insertion can still make sense

The correction does **not** invalidate the local identity proved in `disk-transported-bergman.md`:

\[
\mathcal K_q(g_L;u)=C_q\kappa_{q,L}(u).
\]

Nor does it invalidate the geometric cyclic-cylinder functional

\[
C_q\ell_c\,\mathcal J_{q,m\ell_c}[W].
\]

It only forbids replacing that geometric orbital integral by the unsupported expression

\[
\operatorname{Tr}_{D^+_{2q-1}}
\left(T_W\pi_q(a_{L/2})\right)
\]

without first proving trace-class or specifying an appropriate regularized/relative/orbital functional.

A sufficiently smoothing insertion can in principle make a product with a unitary operator trace class, but the lifted periodic FCIG weight is not automatically of that type. The cyclic quotient must therefore remain the primary definition.

---

## 3. Correct Selberg-style architecture

The standard trace-formula architecture distinguishes three operations:

\[
\boxed{
\begin{array}{rcl}
\text{spectral side} &:& \Theta_\pi(f),\\
\text{geometric side} &:& O_\gamma(f),\\
\text{pointwise character} &:& \Theta_\pi(\gamma)\ \text{on regular }\gamma.
\end{array}
}
\tag{3.1}
\]

Here `f` is a suitable test function or kernel. These objects are related by harmonic analysis, but they are not interchangeable.

For FCIG the deformation weight `W_q` makes the kernel noncentral, so the natural object is closer to a deformation-dependent kernel/orbital pairing than to an ordinary central test function.

Thus the sharp question becomes:

\[
\boxed{
\text{Can the weighted kernel }W_q(u)\kappa_{q,L}(u)
\text{ be realized as the orbital transform of a deformation-dependent operator/kernel whose spectral transform is controlled by }D^+_{2q-1}?
}
\tag{3.2}
\]

---

## 4. Revised TOI-D

### Old heuristic

“Use an `sl_2` ladder recurrence to sum the nonzero modes into `(1-e^{-L})^{-1}`.”

### Corrected gate

**TOI-D — Harish--Chandra denominator closure — OPEN / FALSIFIABLE.**

Starting from the exact cyclic Toeplitz coefficients, construct the relevant group/kernel transform and test whether its split-Cartan spectral transform carries the same Weyl denominator as

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}}.
\]

A ladder computation is useful only if it is derived inside a legitimate realization of this transform; the geometric series alone is not evidence.

---

## 5. Stronger conceptual picture

The exact disk calculation and this firewall together separate the problem into two layers:

\[
\boxed{
\begin{array}{ll}
\text{local / kernel layer:}&
\kappa_{q,L}\ \text{is exactly the gauge-corrected Bergman matrix coefficient},\\[1mm]
\text{global / harmonic-analysis layer:}&
\text{determine the legitimate orbital-to-character transform and its Weyl denominator}.
\end{array}
}
\tag{5.1}
\]

This is stronger than a loose “Bergman looks like Selberg” analogy because the local kernel identification is already exact. What remains is a precise trace-formula problem.

## Sources

- Harish--Chandra, *Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters*, Acta Mathematica 116 (1966), 1--111.
- Dennis A. Hejhal, *The Selberg Trace Formula for PSL(2,R), Vol. I*.
- Jingzhou Sun, *On the Bergman Kernel of complex hyperbolic manifolds*, arXiv:2511.16240v3 (2026).
