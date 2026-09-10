# Jacobi Asymptotic Closure for the Holomorphic Discrete Series

## Status

The previous note `parameter-uniform-matrix-decay.md` reduced full uniform Harish--Chandra-Schwartz control to parameter-uniform estimates for the Jacobi-polynomial formula of the holomorphic discrete-series matrix coefficients.

This note closes the **fixed K-window** regime exactly and isolates the genuine remaining problem when the K-type indices scale with the representation parameter.

We distinguish carefully:

\[
\boxed{\textbf{JA-A1: PASS — fixed K-window, uniform in }q.}
\]

and

\[
\boxed{\textbf{JA-A2: OPEN — proportional regime }m,n=O(q).}
\]

The latter requires Jacobi asymptotics with degree and parameters simultaneously varying.

---

## 1. Explicit discrete-series matrix coefficient

Let

\[
G=SU(1,1)\simeq SL(2,\mathbb R)
\]

up to the usual finite covering conventions, and let \(D_q^+\) denote the holomorphic discrete series in the weighted Bergman realization with lowest weight parameter \(q>1/2\). In the normalized monomial K-type basis \(e_n\), the matrix coefficients admit an explicit Jacobi-polynomial form.

For \(n\ge m\), suppressing harmless phase factors from the two compact K-variables, the radial coefficient along the positive Cartan \(a_t\) has the form

\[
\boxed{
M_{m,n}^{(q)}(t)
=
\mathcal N_{m,n}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^{n-m}
P_m^{(n-m,\,2q-1)}
\!\left(1-2\tanh^2\frac t2\right),
}
\]

with

\[
\mathcal N_{m,n}(q)
=
\left(
\frac{m!\,\Gamma(2q+n)}{n!\,\Gamma(2q+m)}
\right)^{1/2}
\]

under one standard normalization. The \(m\ge n\) case follows by symmetry/conjugation.

The exact phase depends on the chosen SU(1,1)/SL(2,R) coordinates, but the radial absolute-value estimates below do not.

This Jacobi-polynomial expression is standard for holomorphic discrete-series matrix coefficients.

---

## 2. Fixed K-window: normalization is polynomial in q

Fix

\[
0\le m,n\le M.
\]

Then the gamma ratio in \(\mathcal N_{m,n}(q)\) is a finite product. For example, if \(n\ge m\),

\[
\frac{\Gamma(2q+n)}{\Gamma(2q+m)}
=
\prod_{j=m}^{n-1}(2q+j).
\]

Hence

\[
\boxed{
\mathcal N_{m,n}(q)
\le C_M(1+q)^{|m-n|/2}
\le C_M(1+q)^{M/2}.
}
\]

No exponential growth in \(q\) appears in the normalization for fixed \(M\).

---

## 3. Fixed-degree Jacobi polynomial is polynomial in q

For fixed degree \(m\le M\), use the finite hypergeometric expansion

\[
P_m^{(\alpha,\beta)}(x)
=
\frac{(\alpha+1)_m}{m!}
{}_2F_1
\left(
-m,\,m+\alpha+\beta+1;\,\alpha+1;\,\frac{1-x}{2}
\right).
\]

Here

\[
\alpha=n-m,
\qquad
\beta=2q-1.
\]

Because the first upper parameter is \(-m\), the hypergeometric series terminates after \(m\le M\) terms. Each coefficient is polynomial in \(q\) of degree at most \(m\), uniformly for

\[
x\in[-1,1].
\]

Therefore

\[
\boxed{
\sup_{x\in[-1,1]}
\left|P_m^{(n-m,2q-1)}(x)\right|
\le
C_M(1+q)^M.
}
\]

Combining with the normalization factor and

\[
0\le \tanh(t/2)^{|m-n|}\le1,
\]

gives

\[
\boxed{
|M_{m,n}^{(q)}(t)|
\le
C_M(1+q)^{3M/2}
\left(\cosh\frac t2\right)^{-2q}.
}
\]

The exponent \(3M/2\) is deliberately crude; only polynomial dependence matters for the gate.

---

## 4. Radial exponential localization

For \(t\ge0\),

\[
\cosh\frac t2\ge \frac12 e^{t/2},
\]

so

\[
\left(\cosh\frac t2\right)^{-2q}
\le
2^{2q}e^{-qt}.
\]

That estimate is useful at large \(t\), but its prefactor is poor for uniform \(q\). A better two-region argument avoids this artifact.

### Region I: \(0\le t\le1\)

Since \(|M_{m,n}^{(q)}(t)|\le1\) for normalized unitary matrix coefficients,

\[
|M_{m,n}^{(q)}(t)|\le1.
\]

### Region II: \(t\ge1\)

Write

\[
\cosh\frac t2
=
\frac{e^{t/2}}2(1+e^{-t}).
\]

Hence

\[
\left(\cosh\frac t2\right)^{-2q}
=
4^q e^{-qt}(1+e^{-t})^{-2q}.
\]

For \(t\ge1\), the exponential \(e^{-qt}\) dominates every polynomial in both \(t\) and \(q\). More precisely, for every fixed \(N,A\) there exists \(C_{N,A}\) such that

\[
(1+q)^A(1+t)^N
\left(\cosh\frac t2\right)^{-2q}
\le
C_{N,A}e^{-t/2}
\]

for all integers \(q\ge1\) and \(t\ge1\).

Thus, with the rank-one Harish--Chandra estimate

\[
\Xi(a_t)\asymp (1+t)e^{-t/2},
\]

we obtain for every \(N\)

\[
\boxed{
|M_{m,n}^{(q)}(t)|
\le
C_{M,N}(1+q)^{A_M}
\Xi(a_t)(1+t)^{-N},
\qquad m,n\le M.
}
\]

The compact interval \(0\le t\le1\) is absorbed into the constant using unitarity.

---

## 5. Left/right derivatives

The positive discrete-series Lie algebra action is

\[
K_0e_n=(q+n)e_n,
\]

\[
K_+e_n
=
\sqrt{(n+1)(2q+n)}\,e_{n+1},
\]

\[
K_-e_n
=
\sqrt{n(2q+n-1)}\,e_{n-1}.
\]

For fixed \(m,n\le M\) and fixed

\[
D,E\in U(\mathfrak g_\mathbb C),
\]

a left/right derivative of the matrix coefficient is a finite linear combination of neighboring K-type coefficients. The coefficients are polynomially bounded in \(q\).

Therefore, for every \(N\),

\[
\boxed{
|L_D R_E m_{m,n}^{(q)}(g)|
\le
C_{D,E,M,N}
(1+q)^{B_{D,E,M}}
\Xi(g)(1+\sigma(g))^{-N}.
}
\]

This is the full Harish--Chandra-Schwartz estimate uniformly in \(q\) on each fixed K-window.

Thus

\[
\boxed{\textbf{JA-A1: PASS.}}
\]

Combined with `uniform-q-schwartz-control.md`, this upgrades the previous L2-Sobolev estimate to pointwise Schwartz control in the sector relevant to bounded K-type complexity.

---

## 6. Why the proportional regime is genuinely different

Suppose now

\[
m\sim \alpha q,
\qquad
n\sim \beta q
\]

with positive constants \(\alpha,\beta\). Then in

\[
P_m^{(n-m,2q-1)}(x)
\]

all of the following scale simultaneously:

- the degree \(m\);
- the first Jacobi parameter \(n-m\);
- the second Jacobi parameter \(2q-1\).

The terminating-series argument no longer yields a polynomial loss: it contains \(O(q)\) terms, and naive absolute-value bounds can be exponentially poor.

This is exactly the setting of **Jacobi polynomials with varying degree and parameters**, for which steepest-descent/Riemann--Hilbert and large-parameter methods are standard.

In particular, modern asymptotic analyses explicitly treat Jacobi polynomials when degree and parameters become large together. The asymptotics naturally separate into bulk, endpoint, and transition/turning-point regimes.

Consequently the remaining target is not a routine extension of JA-A1.

---

## 7. Correct proportional-scaling variables

Set

\[
\alpha_q=\frac mq,
\qquad
\beta_q=\frac nq,
\qquad
x(t)=1-2\tanh^2\frac t2.
\]

The matrix coefficient has logarithmic scale

\[
\frac1q\log|M_{m,n}^{(q)}(t)|.
\]

After Stirling expansion of the gamma normalization and a varying-parameter Jacobi asymptotic, one expects a rate-function form

\[
\boxed{
M_{m,n}^{(q)}(t)
\sim
q^{-1/2}A(\alpha,\beta,t)
\exp\{-q\Phi(\alpha,\beta,t)\}
}
\]

away from turning points, with another local model at the transition set.

This formula is recorded as a target, not as a proved FCIG identity.

The key question for Harish--Chandra control becomes whether

\[
\boxed{
\Re\Phi(\alpha,\beta,t)\ge \frac{t}{2q}+\text{positive margin}
}
\]

in the admissible FCIG scaling region, or more naturally whether the exponential decay dominates the fixed rank-one Harish--Chandra factor

\[
\Xi(a_t)\sim(1+t)e^{-t/2}.
\]

---

## 8. Existing asymptotic literature and its exact use here

The literature provides several relevant but differently normalized regimes:

1. **Frenzen--Wong:** classical uniform Jacobi asymptotics with error bounds, especially for large degree and fixed parameters.
2. **Kuijlaars--Van Assche:** varying recurrence coefficients and asymptotic zero distributions, including varying Jacobi families.
3. **Gil--Segura--Temme:** asymptotic expansions when Jacobi degree and parameters are simultaneously large.
4. **Riemann--Hilbert/Deift--Zhou methods:** strong asymptotics for varying Jacobi parameters, with separate bulk/edge local models.

These results justify the analytic route, but they are not imported as an unverified theorem for the precise FCIG normalization.

---

## 9. Gate ledger

We therefore record

\[
\boxed{\textbf{JA-A1: PASS — fixed K-window.}}
\]

and

\[
\boxed{\textbf{JA-A2: OPEN — }m,n=O(q)\textbf{ varying-parameter regime.}}
\]

The next gate is

\[
\boxed{\textbf{JA-B — Proportional K-Type Rate Function}.}
\]

Its task is to derive the explicit exponent

\[
\Phi(\alpha,\beta,t)
\]

from the exact hypergeometric/Jacobi integral representation by saddle point, including:

- bulk saddles;
- saddle coalescence;
- endpoint transition;
- the Weyl-symmetric \(m\leftrightarrow n\) continuation.

Once \(\Phi\) is explicit, one can compare it directly with the FCIG orbital Gamma-window localization

\[
|\xi|\sim2q\tanh(L/2).
\]

That comparison is the first point where the representation-side and orbital-side semiclassical localizations can be matched quantitatively rather than only at the level of scale.

---

## 10. Claim firewall

- JA-A1 is a fixed-K-window theorem, not a theorem uniform for arbitrary \(m,n\).
- The polynomial exponents displayed above are intentionally non-optimal.
- The proportional-regime rate function \(\Phi\) is a target until derived in FCIG conventions.
- The transverse Fourier variable \(\xi\), the Cartan radius \(t\), K-type labels \(m,n\), and the Harish--Chandra spectral variable remain distinct.
- No novelty claim is made.

---

## References

1. Standard holomorphic discrete-series matrix coefficients of \(SU(1,1)\) in terms of Jacobi polynomials.
2. C. L. Frenzen and R. Wong, *A Uniform Asymptotic Expansion of the Jacobi Polynomials with Error Bounds*, Canadian Journal of Mathematics **37** (1985), 979--1007.
3. A. B. J. Kuijlaars and W. Van Assche, *The Asymptotic Zero Distribution of Orthogonal Polynomials with Varying Recurrence Coefficients*, Journal of Approximation Theory **99** (1999), 167--197.
4. A. Gil, J. Segura, and N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss--Jacobi quadrature for large degree and parameters in terms of elementary functions*, Journal of Mathematical Analysis and Applications **494** (2021), 124642.
5. A. B. J. Kuijlaars et al., Riemann--Hilbert strong asymptotics for Jacobi-type orthogonal polynomials.
6. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.

## FCIG cross-references

- `parameter-uniform-matrix-decay.md`
- `uniform-q-schwartz-control.md`
- `schwartz-completion.md`
- `coherent-state-discrete-series-closure.md`
- `centralizer-spectral-window.md`
