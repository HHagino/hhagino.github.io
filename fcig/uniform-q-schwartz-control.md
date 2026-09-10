# Uniform-q Schwartz Control: Sobolev Transfer for the Discrete-Series FCIG Kernel

## Status

This note begins the semiclassical return from the fixed-`q` representation-theoretic closure to the `q -> infinity` regime.

The strongest statement that follows directly and exactly from Schur orthogonality is an `L^2`-Sobolev transfer principle: left/right derivatives of the group kernel correspond to left/right derived-representation weights on the operator Fourier block. This gives explicit polynomial `q`-control. A fully uniform family of pointwise Harish--Chandra-Schwartz seminorms requires one further weighted estimate and is therefore kept open.

Accordingly the gate is split into:

\[
\boxed{\textbf{UQ-A1: PASS -- exact }L^2\textbf{-Sobolev transfer with explicit }q\textbf{-growth.}}
\]

\[
\boxed{\textbf{UQ-A2: OPEN -- full uniform Harish--Chandra-Schwartz seminorm control.}}
\]

---

## 1. Discrete-series parameter and formal degree

Let

\[
\pi_q=D^+_{2q-1}
\]

be the holomorphic discrete-series representation used throughout the FCIG hyperbolic track. In the FCIG curvature `-1` normalization,

\[
\boxed{
d_q=C_q=\frac{2q-1}{4\pi}.
}
\]

Hence

\[
\boxed{
d_q\sim \frac{q}{2\pi},
\qquad
\sqrt{d_q}\sim \sqrt{\frac{q}{2\pi}}.
}
\]

The exact equality depends on the fixed Haar normalization already used in `coherent-state-discrete-series-closure.md`; only the linear asymptotic is normalization-independent up to the overall Haar constant.

---

## 2. Matrix-coefficient synthesis

For a smoothing operator `A` on `H_q`, let

\[
h_{A,q}(g)
=
d_q\sum_{m,n\ge0}A_{mn}\,m_{n,m}^{(q)}(g),
\]

where

\[
m_{n,m}^{(q)}(g)
=
\langle e_n,\pi_q(g)e_m\rangle
\]

and the rank-one convention is chosen so that

\[
\boxed{\widehat h_{A,q}(\pi_q)=A.}
\]

Schur orthogonality gives pairwise orthogonality of matrix coefficients and therefore the exact Plancherel identity

\[
\boxed{
\|h_{A,q}\|_{L^2(G)}^2
=
d_q\,\|A\|_{\mathrm{HS}}^2.
}
\tag{2.1}
\]

Equivalently,

\[
\boxed{
\|h_{A,q}\|_2
=
\sqrt{d_q}\,\|A\|_{\mathrm{HS}}.
}
\tag{2.2}
\]

Thus the unavoidable zeroth-order semiclassical growth of the synthesis map is only `q^{1/2}`.

---

## 3. Exact derivative transfer

Let `D,E` lie in the universal enveloping algebra `U(g_C)`. Under the Fourier convention

\[
\widehat f(\pi)=\int_Gf(g)\pi(g^{-1})\,dg,
\]

left and right invariant differential operators act on the Fourier block by the derived representation on opposite sides, up to the standard sign/anti-involution convention. Suppressing that harmless convention in the norm identity,

\[
\boxed{
\widehat{L_D R_E h_{A,q}}(\pi_q)
=
d\pi_q(D)\,A\,d\pi_q(E).
}
\]

Since `h_{A,q}` is supported in the single discrete-series Plancherel block, Schur orthogonality gives

\[
\boxed{
\|L_D R_E h_{A,q}\|_2^2
=
d_q\,
\|d\pi_q(D)A\,d\pi_q(E)\|_{\mathrm{HS}}^2.
}
\tag{3.1}
\]

This is the basic uniform-`q` identity.

Define operator Sobolev seminorms

\[
\boxed{
\mathfrak a_{D,E}^{(q)}(A)
:=
\|d\pi_q(D)A\,d\pi_q(E)\|_{\mathrm{HS}}.
}
\]

Then exactly

\[
\boxed{
\|L_D R_E h_{A,q}\|_2
=
\sqrt{d_q}\,\mathfrak a_{D,E}^{(q)}(A).
}
\tag{3.2}
\]

Therefore the renormalized synthesis map

\[
\boxed{
A\longmapsto d_q^{-1/2}h_{A,q}
}
\]

is isometric at every `L^2`-Sobolev level once the same enveloping-algebra seminorm is used on the operator side.

---

## 4. Explicit q-cost in the K-type basis

Write the positive discrete series with Bargmann parameter `q` in the standard orthonormal basis `e_n`. The `su(1,1)` generators act as

\[
K_0e_n=(q+n)e_n,
\]

\[
K_+e_n=\sqrt{(n+1)(2q+n)}\,e_{n+1},
\]

\[
K_-e_n=\sqrt{n(2q+n-1)}\,e_{n-1}.
\]

Hence every monomial `D` of enveloping-algebra degree `r` obeys a weighted estimate of the form

\[
\boxed{
\|d\pi_q(D)v\|
\le
C_D\|(1+q+N)^r v\|,
}
\tag{4.1}
\]

where `N e_n=n e_n` and `C_D` is independent of `q`.

Consequently, if `deg D=r` and `deg E=s`,

\[
\boxed{
\mathfrak a_{D,E}^{(q)}(A)
\le
C_{D,E}
\|(1+q+N)^rA(1+q+N)^s\|_{\mathrm{HS}}.
}
\tag{4.2}
\]

Combining (3.2) and (4.2),

\[
\boxed{
\|L_D R_E h_{A,q}\|_2
\le
C_{D,E}\sqrt{d_q}
\|(1+q+N)^rA(1+q+N)^s\|_{\mathrm{HS}}.
}
\tag{4.3}
\]

This is a uniform estimate with all `q`-dependence visible on the operator side.

---

## 5. Fixed K-window consequence

Suppose `A_q` is supported on a fixed K-type window

\[
0\le m,n\le M
\]

with `M` independent of `q`. Then

\[
(1+q+N)^r\asymp_M (1+q)^r,
\]

so

\[
\boxed{
\|L_D R_E h_{A_q,q}\|_2
\le
C_{D,E,M}
q^{r+s+1/2}\|A_q\|_{\mathrm{HS}}.
}
\tag{5.1}
\]

Thus every fixed differential order has polynomial, not exponential, growth in the representation parameter.

For the lowest coherent state itself, the radial coefficient

\[
\langle e_0,\pi_q(a_L)e_0\rangle
=
\cosh^{-2q}(L/2)
\]

actually decays faster as `q` grows away from the identity. The polynomial powers in (5.1) arise from differentiation near the identity and from the formal-degree factor, not from loss of hyperbolic decay.

---

## 6. Uniform rapid operator class

The natural family space is therefore not obtained by demanding `A_q` itself be uniformly bounded in an unweighted norm. Define for integers `r,s >= 0`

\[
\boxed{
\alpha_{r,s}(A_q)
:=
\|(1+q+N)^rA_q(1+q+N)^s\|_{\mathrm{HS}}.
}
\]

A family `(A_q)_{q\ge q_0}` is **uniformly rapid** if, after whatever semiclassical normalization is natural for the FCIG observable, these seminorms have controlled polynomial growth in `q` for every `r,s`.

Then (4.3) turns operator estimates immediately into group-kernel Sobolev estimates.

This is the precise sense in which uniform-`q` control is an operator-side problem.

---

## 7. Application to the FCIG defect

Recall

\[
A_{W,q}
=
d_q^{-1}T_W^{(q)}
-
\widehat{\mathcal L_q^{\rm orb}W}(\pi_q),
\]

and

\[
f_{q,W}
=
\mathcal L_q^{\rm orb}W+h_{A_{W,q},q}.
\]

The correction term does not alter the split-hyperbolic orbital response:

\[
O_{a_L}(h_{A_{W,q},q})=0.
\]

Its Sobolev size is exactly governed by

\[
\boxed{
\|L_D R_E h_{A_{W,q},q}\|_2
=
\sqrt{d_q}
\|d\pi_q(D)A_{W,q}d\pi_q(E)\|_{\mathrm{HS}}.
}
\]

Therefore a uniform semiclassical FCIG theorem reduces to estimates on the operator defect `A_{W,q}`.

This is substantially sharper than trying to estimate the synthesized group function directly.

---

## 8. Match with the FCIG hyperbolic frequency scale

The previously derived Fourier transform of the Sun/coherent-state cylinder kernel is a Gamma window concentrated at

\[
\boxed{
|\xi|\sim2q\tanh(L/2)
}
\]

with relative width `O(q^{-1/2})`.

On the representation side, the infinitesimal generators on low K-types have scale

\[
K_0\sim q,
\qquad
K_\pm\sim q^{1/2}
\]

and enveloping-algebra derivatives therefore carry polynomial powers of the same semiclassical parameter `q`.

Thus the two previously separate large-`q` observations are compatible:

\[
\boxed{
\text{orbital transverse frequency }\xi=O(q)
\quad\leftrightarrow\quad
\text{discrete-series infinitesimal scale }d\pi_q=O(q).
}
\]

This is a scale match, not an identification of `xi` with a Harish--Chandra spectral parameter.

---

## 9. What is still missing for full Schwartz uniformity

Harish--Chandra Schwartz seminorms involve not only invariant derivatives but also spatial weights, schematically

\[
p_{D,E,N}(f)
=
\sup_{g\in G}
(1+\sigma(g))^N\Xi(g)^{-1}
|L_D R_Ef(g)|.
\]

The exact `L^2` identities above control all derivatives but do not, by themselves, insert arbitrary powers of the proper length function `sigma(g)`.

For a single discrete-series coefficient those weights are harmless because of exponential decay. Uniformly in both `q` and unrestricted K-type indices `(m,n)`, however, one needs explicit asymptotic coefficient estimates or a parameter-uniform version of the discrete-series Schwartz isomorphism.

Stanton--Tomas develop precisely the discrete-series matrix-coefficient asymptotics and Schwartz-space Fourier transform for `SL(2,R)`, but extracting constants uniform in the changing lowest weight is a separate step.

Therefore we do **not** claim full pointwise uniform Schwartz bounds here.

---

## 10. Gate ledger

\[
\boxed{\textbf{UQ-A1: PASS}}
\]

with exact identity

\[
\|L_D R_E h_{A,q}\|_2^2
=
d_q\|d\pi_q(D)A d\pi_q(E)\|_{HS}^2.
\]

For fixed K-window,

\[
\boxed{
\|L_D R_Eh_{A_q,q}\|_2
=O(q^{\deg D+\deg E+1/2})\|A_q\|_{HS}.
}
\]

But

\[
\boxed{\textbf{UQ-A2: OPEN}}
\]

for the full family of weighted pointwise Harish--Chandra-Schwartz seminorms.

Define the next gate

\[
\boxed{\textbf{UQ-B -- Parameter-Uniform Matrix-Coefficient Decay}.}
\]

The target is an estimate of the form

\[
|L_D R_E m_{m,n}^{(q)}(g)|
\le
C_{D,E,N}\,P_{D,E,N}(q,m,n)
\Xi(g)(1+\sigma(g))^{-N},
\]

with an explicit polynomial `P` and constants independent of `q,m,n` after suitable weights. Such an estimate would promote UQ-A1 to full UQ-A2.

---

## 11. Claim firewall

- `q` is the holomorphic-discrete-series/Bergman semiclassical parameter; the exact label `D^+_{2q-1}` and Bargmann parameter conventions must not be conflated.
- The transverse Fourier variable `xi` is not the Harish--Chandra spectral parameter.
- `L^2`-Sobolev uniformity is proved here; full pointwise Harish--Chandra-Schwartz uniformity is not.
- Formal degree depends on Haar normalization; `d_q=(2q-1)/(4 pi)` is the FCIG normalization.
- Fixed-K-window polynomial estimates do not automatically imply uniform bounds for K-types growing with `q`.
- No novelty claim is made.

---

## References

1. Harish-Chandra, *Representations of Semisimple Lie Groups VI: Integrable and Square-Integrable Representations*, Amer. J. Math. **78** (1956), 564--628.
2. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.
3. A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
4. N. R. Wallach, *Real Reductive Groups I/II*, Academic Press, 1988/1992.
5. Recent work on Wehrl inequalities for holomorphic discrete-series matrix coefficients, including explicit formal-degree normalization and weighted Bergman realization.

## FCIG cross-references

- `schwartz-completion.md`
- `cuspidal-projection-closure.md`
- `operator-kernel-interpolation.md`
- `coherent-state-discrete-series-closure.md`
- `centralizer-spectral-window.md`
- `finite-q-information-offset.md`
