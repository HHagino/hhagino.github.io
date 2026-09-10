# Parameter-Uniform Discrete-Series Matrix-Coefficient Decay

## Status

This note attacks **UQ-B**, the missing pointwise ingredient after `uniform-q-schwartz-control.md`.

The full problem asks for Harish--Chandra-Schwartz estimates that are uniform as the holomorphic discrete-series parameter \(q	o\infty\), while also controlling the K-type indices. A complete all-\((m,n)\) estimate requires uniform Jacobi-function asymptotics in the three parameters \(q,m,n\).

The first nontrivial sector can nevertheless be closed exactly: for every fixed K-type window \(0\le m,n\le M\), all left/right derivatives satisfy Harish--Chandra-Schwartz bounds with only polynomial loss in \(q\).

We record this as **UQ-B1: PASS (fixed K-window)** and isolate the genuinely harder global K-type problem as UQ-B2.

---

## 1. Setup

Let

\[
G=SU(1,1)\simeq SL(2,\mathbb R)
\]

up to the usual finite-center convention, and let

\[
\pi_q=D^+_{2q-1},\qquad q>\frac12.
\]

Choose the standard orthonormal holomorphic K-type basis

\[
e_0,e_1,e_2,\ldots.
\]

Write

\[
m_{mn}^{(q)}(g)
:=
\langle e_m,\pi_q(g)e_n\rangle.
\]

The Cartan decomposition is

\[
g=k_1a_tk_2,
\qquad t\ge0.
\]

Since the K-actions contribute unit-modulus phases, radial decay is governed by

\[
m_{mn}^{(q)}(a_t).
\]

---

## 2. Explicit Jacobi structure

Holomorphic discrete-series matrix elements of \(SU(1,1)\) admit explicit Jacobi-polynomial formulas. In the standard parametrization

\[
\alpha=\cosh\frac t2,
\qquad
|\beta|=\sinh\frac t2,
\qquad
z=\beta\bar\alpha^{-1},
\]

one obtains, for \(n\ge m\), a formula of the schematic exact form

\[
\boxed{
 m_{mn}^{(q)}(a_t)
 =
 C_{mn}(q)
 \left(\cosh\frac t2\right)^{-2q}
 \left(\tanh\frac t2\right)^{n-m}
 P_m^{(n-m,\,2q-1)}\!\left(1-2\tanh^2\frac t2\right),
}
\]

up to the conventional equivalent redistribution of powers of \(\cosh(t/2)\) between the prefactor and Jacobi factor. The \(m>n\) formula follows by the corresponding symmetry/conjugation.

The crucial point for FCIG is invariant under those convention changes:

1. the Jacobi degree is \(\min(m,n)\);
2. its second parameter is affine in \(q\);
3. the radial coefficient contains the discrete-series exponential factor
   
   \[
   \left(\cosh\frac t2\right)^{-2q};
   \]
4. the remaining factors are finite-degree algebraic expressions when \(m,n\) are fixed.

---

## 3. Fixed K-window polynomial control

Fix \(M\ge0\) and restrict to

\[
0\le m,n\le M.
\]

For fixed Jacobi degree \(r\le M\), the polynomial

\[
P_r^{(\alpha,2q-1)}(x)
\]

is a finite sum whose coefficients are rational combinations of gamma/binomial factors with degree bounded only by \(M\). Consequently, uniformly for \(x\in[-1,1]\),

\[
\boxed{
\left|P_r^{(\alpha,2q-1)}(x)\right|
\le C_M(1+q)^M,
}
\]

for the finitely many \(\alpha=|m-n|\le M\).

The normalization factors \(C_{mn}(q)\) are ratios of gamma functions with shifts bounded by \(M\). Hence

\[
\boxed{
|C_{mn}(q)|\le C_M(1+q)^{M/2}
}
\]

is sufficient for the present purpose. No optimization of the exponent is needed.

Therefore there exists \(A_M\) such that

\[
\boxed{
|m_{mn}^{(q)}(a_t)|
\le
C_M(1+q)^{A_M}
\left(\cosh\frac t2\right)^{-2q},
\qquad 0\le m,n\le M.
}
\]

This already displays the key semiclassical fact: the representation parameter improves radial decay exponentially, while the fixed K-type cost is only polynomial in \(q\).

---

## 4. Comparison with the Harish--Chandra majorant

For real rank one,

\[
\Xi(a_t)
\asymp
(1+t)e^{-t/2}
\]

up to normalization-equivalent polynomial factors.

For every \(q\ge1\),

\[
\left(\cosh\frac t2\right)^{-2q}
\le
C_qe^{-qt}
\]

for large \(t\), and in fact the ratio to

\[
\Xi(a_t)(1+t)^{-N}
\]

is bounded for every fixed \(N\). Since increasing \(q\) only strengthens the exponential radial decay, the supremum of the weighted ratio is attained in a bounded \(t\)-region and costs at most a polynomial factor already absorbed into the fixed-window constant.

Thus, for every \(N\ge0\),

\[
\boxed{
|m_{mn}^{(q)}(a_t)|
\le
C_{M,N}(1+q)^{A_{M,N}}
\Xi(a_t)(1+t)^{-N},
\qquad
m,n\le M.
}
\]

---

## 5. Left/right derivatives

Let \(D,E\in U(\mathfrak g_\mathbb C)\). Left and right differentiation act on matrix coefficients by derived-representation operators:

\[
L_D R_E m_{mn}^{(q)}(g)
=
\langle d\pi_q(D^*)e_m,\pi_q(g)d\pi_q(E)e_n\rangle
\]

up to the standard adjoint/sign convention.

In the positive discrete series,

\[
K_0e_n=(q+n)e_n,
\]

\[
K_+e_n=\sqrt{(n+1)(2q+n)}\,e_{n+1},
\]

\[
K_-e_n=\sqrt{n(2q+n-1)}\,e_{n-1}.
\]

For \(m,n\le M\), applying fixed \(D,E\) creates only finitely many nearby K-types and contributes a polynomial factor in \(q\). Combining this with the previous radial estimate yields

\[
\boxed{
|L_D R_E m_{mn}^{(q)}(g)|
\le
C_{D,E,M,N}
(1+q)^{B_{D,E,M,N}}
\Xi(g)(1+\sigma(g))^{-N},
}
\]

for all \(q\ge1\) and all \(0\le m,n\le M\).

This is the fixed-window parameter-uniform Harish--Chandra-Schwartz estimate required by FCIG.

---

## 6. Consequence for synthesized kernels

Let

\[
A_q=\sum_{m,n\le M}A_{mn}^{(q)}|e_m\rangle\langle e_n|
\]

and

\[
h_{A_q,q}(g)
=d_q\sum_{m,n\le M}A_{mn}^{(q)}m_{nm}^{(q)}(g).
\]

Since

\[
d_q=\frac{2q-1}{4\pi}=O(q),
\]

we get, for every Harish--Chandra-Schwartz seminorm \(p_{D,E,N}\),

\[
\boxed{
 p_{D,E,N}(h_{A_q,q})
 \le
 C_{D,E,M,N}
 (1+q)^{C_{D,E,M,N}}
 \|A_q\|_{\mathrm{mat}},
}
\]

where any fixed finite-dimensional matrix norm may be used.

Thus the synthesized cuspidal correction has at most polynomial \(q\)-growth on every fixed K-window.

---

## 7. Gate status

We record

\[
\boxed{\textbf{UQ-B1: PASS — fixed K-window parameter-uniform Schwartz decay.}}
\]

Together with `uniform-q-schwartz-control.md`, this upgrades UQ-A from merely \(L^2\)-Sobolev control to pointwise Harish--Chandra-Schwartz control on fixed K-type sectors.

The remaining problem is genuinely two-parameter/three-parameter asymptotics:

\[
\boxed{\textbf{UQ-B2: OPEN — global K-type window.}}
\]

One seeks a bound of the form

\[
\boxed{
|L_D R_E m_{mn}^{(q)}(g)|
\le
C_{D,E,N}
P_{D,E,N}(q,m,n)
\Xi(g)(1+\sigma(g))^{-N},
}
\]

with a single explicit polynomial \(P\) valid for unbounded \(m,n\).

---

## 8. What is actually difficult in UQ-B2

When \(m,n\) grow with \(q\), the Jacobi polynomial degree and its parameters grow simultaneously. The elementary finite-degree argument above is no longer uniform.

The problem becomes one of simultaneous asymptotics for

\[
P_{\min(m,n)}^{(|m-n|,\,2q-1)}(x),
\]

including transition regions where

\[
m\sim q,\qquad n\sim q,
\]

or much larger.

A crude use of the unitary bound

\[
|m_{mn}^{(q)}(g)|\le1
\]

loses the required Harish--Chandra radial decay. Conversely, fixed-parameter Jacobi asymptotics do not control the growing-degree regime.

Thus the next correct gate is not another abstract representation-theoretic existence theorem. It is an explicit special-function estimate.

Define

\[
\boxed{\textbf{JA-A — Uniform Jacobi Asymptotic Closure}.}
\]

Target: derive a polynomially parameter-controlled bound for the above Jacobi family over the whole Cartan range \(t\ge0\), preferably split into semiclassical regions.

---

## 9. Relation to FCIG orbital localization

The orbital branch already has the Gamma spectral window

\[
p_{q,\tau}(\xi)
=\frac1{\Gamma(2q)\tau}
\left(\frac\xi\tau\right)^{2q-1}e^{-\xi/\tau},
\]

localized at

\[
\xi\sim2q\tanh\frac L2
\]

with relative width \(O(q^{-1/2})\).

UQ-B1 shows that, in fixed K-type sectors, the group-side matrix coefficients simultaneously concentrate spatially through

\[
\left(\cosh\frac t2\right)^{-2q}.
\]

These are different spectral/spatial variables and must not be identified. What is now established is the common semiclassical scale \(q\):

\[
\boxed{
\text{orbital Fourier localization scale }O(q)
\quad\text{and}\quad
\text{discrete-series radial localization scale }O(q)
}
\]

arise in the two transforms of the same FCIG operator-kernel architecture.

---

## 10. Claim firewall

- The Jacobi-polynomial formula is an explicit matrix-coefficient formula, not a character formula.
- UQ-B1 is uniform in \(q\) only after fixing a finite K-type window \(m,n\le M\).
- No all-\((m,n)\) polynomial bound is claimed yet.
- The estimate \,\Xi(a_t)\asymp(1+t)e^{-t/2}\, is used only up to normalization-equivalent rank-one Harish--Chandra estimates.
- The variables \(t\), longitudinal FCIG mode \(n\), transverse Fourier variable \(\xi\), and Harish--Chandra spectral variables remain distinct.
- No novelty claim is made.

---

## References

1. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393. In particular: discrete series, Schwartz spaces, asymptotic approximation, and explicit asymptotic coefficients.
2. P. J. Sally Jr., *Intertwining operators and the representations of SL(2,R)*, J. Functional Analysis **6** (1970), 441--453; discrete series and Jacobi-polynomial generating-function methods.
3. J.-P. Gazeau, M. A. del Olmo, H. Pejhan, *Holomorphic Discrete Series of SU(1,1): Orthogonality Relations, Character Formulas, and Multiplicities in Tensor Product Decompositions*, arXiv:2504.03901 (2025); explicit weighted-Bergman realization and Jacobi-polynomial matrix elements.
4. Harish-Chandra, foundational work on estimates of matrix coefficients and Schwartz spaces for real reductive groups.
5. G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications; classical Jacobi polynomial formulas and estimates.

## FCIG cross-references

- `uniform-q-schwartz-control.md`
- `schwartz-completion.md`
- `operator-kernel-interpolation.md`
- `centralizer-spectral-window.md`
- `coherent-state-discrete-series-closure.md`
