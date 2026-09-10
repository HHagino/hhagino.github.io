# Logarithmic Spatial-Weight Refinement

## SR-B — from structural Schwartz closure to sharp spatial cost

**Status (2026-09-10).**

This note refines `sharp-schwartz-refinement.md` and `unrestricted-schwartz-closure.md`.

\[
\boxed{\textbf{SR-B0: PASS — recent all-parameter Jacobi bounds do not by themselves imply the desired }\Xi\textbf{-weighted spatial estimate.}}
\]

\[
\boxed{\textbf{SR-B1a: PASS — the logarithmic spatial cost is proved on the lowest-}K\textbf{ columns/rows.}}
\]

\[
\boxed{\textbf{SR-B1: OPEN — the same sharp logarithmic cost for unrestricted pairs }(m,n).}
\]

The point of the split is to distinguish a genuine theorem from a plausible extrapolation.

---

## 1. Target seminorm

For radial matrix coefficients

\[
M_{m,n}^{(q)}(t)=\langle e_m,\pi_q(a_t)e_n\rangle,
\]

define

\[
p_N(M)=\sup_{t\ge0}(1+t)^N\Xi(a_t)^{-1}|M(t)|.
\]

The conjectured sharp parameter dependence is

\[
\boxed{
p_N(M_{m,n}^{(q)})
\le C_N\left[1+T_{q,m,n}\right]^N,
}
\]

where

\[
T_{q,m,n}
=\operatorname{arcosh}\left(1+\frac mq\right)
+\operatorname{arcosh}\left(1+\frac nq\right).
\]

For derivatives of degrees \(r=\deg D\), \(s=\deg E\), SR-A1 then predicts only the additional sharp factors

\[
(1+q+m)^r(1+q+n)^s.
\]

---

## 2. A recent Jacobi estimate and what it actually gives

For \(n\ge m\), set

\[
a=n-m,\qquad b=2q-1,
\qquad x=1-2\tanh^2(t/2).
\]

A recent uniform Jacobi estimate of Bai--Li (2026) applies to orthonormal Jacobi polynomials with degree and parameters varying simultaneously.  Translating their weighted bound to the FCIG normalization produces a useful cancellation.

The Jacobi norm is

\[
h_m^{(a,b)}
=\frac{2^{a+b+1}}{2m+a+b+1}
\frac{\Gamma(m+a+1)\Gamma(m+b+1)}{m!\Gamma(m+a+b+1)}.
\]

With

\[
\mathcal N_{m,n}(q)^2
=\frac{m!\Gamma(2q+n)}{n!\Gamma(2q+m)},
\]

one gets exactly

\[
\boxed{
\mathcal N_{m,n}(q)^2 h_m^{(a,2q-1)}
=\frac{2^{a+2q}}{m+n+2q}.
}
\]

Because

\[
1-x=2r^2,
\qquad
1+x=2\operatorname{sech}^2(t/2),
\qquad r=\tanh(t/2),
\]

the weighted Jacobi estimate yields a global bound of the schematic form

\[
\boxed{
|M_{m,n}^{(q)}(t)|^2
\le
C\,
\frac{Q(q,m,n)}{(m+n+2q)\sinh(t/2)},
}
\]

where, for \(n\ge m\), one may take

\[
Q(q,m,n)
=\max\left\{
1,
(n-m+2q)^{1/3},
(n-m+2q)^{1/2}(m+1)^{-1/6}
\right\}.
\]

This estimate is genuinely uniform in degree and parameters.  However, at large \(t\) it gives only

\[
|M|\lesssim e^{-t/4}
\]

up to parameter factors, whereas

\[
\Xi(a_t)\asymp (1+t)e^{-t/2}.
\]

Therefore the recent Jacobi estimate alone is too coarse to prove the desired Harish--Chandra-Schwartz spatial weight.

\[
\boxed{\textbf{SR-B0: PASS — useful global Jacobi control, but not a substitute for discrete-series tail asymptotics.}}
\]

---

## 3. Exact lowest-K column

For \(m\ge0\), the lowest-vector coefficient satisfies

\[
\boxed{
|M_{0,m}^{(q)}(t)|^2
=
\frac{\Gamma(2q+m)}{m!\Gamma(2q)}
\operatorname{sech}^{4q}\frac t2
\tanh^{2m}\frac t2.
}
\]

Let

\[
f_{q,m}(t)=\log|M_{0,m}^{(q)}(t)|.
\]

Differentiation gives

\[
f_{q,m}'(t)
=-q\tanh\frac t2+\frac{m}{\sinh t}.
\]

The unique maximum occurs at

\[
\boxed{
T_{q,m}=\operatorname{arcosh}\left(1+\frac mq\right),
}
\]

because

\[
m=q(\cosh T_{q,m}-1).
\]

Substituting this identity into the derivative gives the exact formula

\[
\boxed{
f_{q,m}'(t)
=-q\frac{\cosh t-\cosh T_{q,m}}{\sinh t}.}
\]

---

## 4. Uniform tail slope

For \(t=T_{q,m}+s\), \(s\ge1\),

\[
\frac{\cosh t-\cosh T_{q,m}}{\sinh t}
\ge \tanh\frac{s}{2}
\ge \tanh\frac12.
\]

Hence

\[
\boxed{
f_{q,m}'(t)\le-q\tanh(1/2),
\qquad t\ge T_{q,m}+1.}
\]

For \(q\ge2\), this decay is strictly stronger than the exponential part of the rank-one Harish--Chandra majorant

\[
\Xi(a_t)\asymp(1+t)e^{-t/2}.
\]

Cowling--Haagerup--Howe gives

\[
|M_{0,m}^{(q)}(t)|\le\Xi(a_t)
\]

because the holomorphic discrete series is tempered and each \(SO(2)\)-type is one-dimensional.

Split the supremum defining \(p_N\) into

\[
0\le t\le T_{q,m}+1
\]

and

\[
t\ge T_{q,m}+1.
\]

On the first interval, CHH immediately gives

\[
(1+t)^N\Xi(a_t)^{-1}|M(t)|
\le (2+T_{q,m})^N.
\]

On the tail, use the exact slope estimate and the two-sided rank-one estimate for \(\Xi\).  Writing

\[
t=T_{q,m}+1+s,
\qquad s\ge0,
\]

one obtains

\[
\Xi(t)^{-1}|M(t)|
\le
C\frac{T_{q,m}+2}{T_{q,m}+2+s}
\exp\left[-\left(q\tanh\frac12-\frac12\right)s\right].
\]

Since \(q\ge2\), the exponential rate on the right is bounded below by the positive universal constant

\[
2\tanh(1/2)-1/2>0.
\]

Therefore for every integer \(N\ge0\),

\[
\boxed{
\sup_{t\ge0}(1+t)^N\Xi(a_t)^{-1}|M_{0,m}^{(q)}(t)|
\le
C_N\left[1+T_{q,m}\right]^N,
\qquad q\ge2.
}
\]

By conjugation the same estimate holds for \(M_{m,0}^{(q)}\).

Since

\[
T_{q,m}
=\operatorname{arcosh}\left(1+\frac mq\right)
=\log\left(2\frac mq\right)+O(q/m)
\]

when \(m/q\to\infty\), the spatial cost is logarithmic in the distant K-type label.

\[
\boxed{\textbf{SR-B1a: PASS.}}
\]

---

## 5. Sharpness of the spatial scale

The logarithmic radius is not an artifact of the proof.  The coefficient has its actual maximum at

\[
t=T_{q,m}.
\]

Thus any uniform spatial-weight estimate must account for mass transported to radial distance

\[
\operatorname{arcosh}(1+m/q)\sim\log(1+m/q).
\]

What is not proved here is that the exact exponent \(N\) on \((1+T)^N\) is a lower bound for every \(N\), because the ratio \(|M|/\Xi\) at the peak also depends on \(q,m\).  The sharp statement proved here concerns the location scale and the upper-bound exponent.

---

## 6. General pair and the remaining obstacle

For general \((m,n)\), the SAC caustic geometry identifies

\[
t_+=
\operatorname{arcosh}\left(1+\frac mq\right)
+
\operatorname{arcosh}\left(1+\frac nq\right)
\]

as the outer transition scale.

Inside a bounded enlargement of this radius, CHH gives exactly the desired logarithmic spatial factor.  The missing step is therefore only the uniform tail statement

\[
\boxed{
\frac{|M_{m,n}^{(q)}(t)|}{\Xi(a_t)}
\le
C\exp[-c(t-t_+)]
\quad\text{for }t\ge t_++1,
}
\]

with \(c,C>0\) independent of \(q,m,n\) after the obvious derivative weights are removed.

The proportional-K SAC rate proves such a statement on compact ratio sets, while Stanton--Tomas/Barker-type asymptotic theory proves rapid decay for every fixed discrete-series block.  What is still required for the sharp unrestricted theorem is a tail estimate whose constants survive simultaneously as \(m/q\) and \(n/q\) become unbounded.

Thus

\[
\boxed{\textbf{SR-B1: OPEN only at the unrestricted two-high-K tail.}}
\]

---

## 7. Consequence for the SAC--Schwartz stitch

On any parameter region where the outer forbidden rate is valid uniformly,

\[
M_{m,n}^{(q)}(t)
\sim q^{-1/2}A(\alpha,\beta,t)e^{-q\Phi_+(\alpha,\beta,t)}.
\]

The switch from the sharp SAC approximation to the global Schwartz majorant occurs when

\[
\boxed{
q\Phi_+(\alpha,\beta,t)
\approx
\frac t2+N\log(1+t)
+\log P_{D,E}(q,m,n),
}
\]

where SR-A1 permits

\[
P_{D,E}(q,m,n)
=(1+q+m)^{\deg D}(1+q+n)^{\deg E}
\]

at zero spatial weight.

Near the outer fold,

\[
\Phi_+(t)\sim C_+(t-t_+)^{3/2},
\]

so the overlap thickness is

\[
\boxed{
\Delta t_{\rm stitch}
\asymp
\left[
\frac{
 t_+/2+N\log(1+t_+)+\log P_{D,E}
}{qC_+}
\right]^{2/3}.
}
\]

This formula is a derived matching law on regions where the SAC remainder theorem is uniform.  A globally uniform SR-B2 theorem still depends on closing SR-B1 for the unrestricted two-high-K tail.

---

## 8. Gate ledger

\[
\boxed{
\begin{array}{ll}
\text{SR-A1} & \text{PASS — sharp derivative degrees},\\
\text{SR-A2} & \text{PASS — exact formal-degree synthesis cost},\\
\text{SR-B0} & \text{PASS — all-parameter Jacobi bound translated; insufficient for }\Xi\text{-weight},\\
\text{SR-B1a} & \text{PASS — logarithmic spatial cost on lowest-K rows/columns},\\
\text{SR-B1} & \text{OPEN — unrestricted two-high-K tail},\\
\text{SR-B2} & \text{PARTIAL — quantitative stitch proved on uniform SAC sectors}.
\end{array}}
\]

---

## References

1. M. Cowling, U. Haagerup, R. Howe, *Almost L2 matrix coefficients*, J. reine angew. Math. **387** (1988), 97--110.
2. R. J. Stanton, P. A. Tomas, *Lp Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.
3. Viktor Losert, *On the asymptotics of matrix coefficients of representations of SL(2,R)*, J. Functional Analysis **287** (2024), 110476.
4. Qi-Feng Bai, Yu-Tian Li, *The Erdelyi--Magnus--Nevai and Krasikov Conjectures for Jacobi Polynomials*, arXiv:2608.30304 (2026).
5. FCIG notes `semiclassical-atlas-closure.md`, `sharp-schwartz-refinement.md`, and `unrestricted-schwartz-closure.md`.

## Claim firewall

- CHH supplies the uniform \(\Xi\) majorant; it does not by itself supply arbitrary spatial Schwartz weights.
- The Bai--Li bound is used only for the displayed all-parameter Jacobi estimate and is explicitly recorded as insufficient for the desired \(\Xi\)-weighted theorem.
- SR-B1a is a theorem for lowest-K rows/columns only.
- The unrestricted logarithmic cost remains open until the two-high-K tail is controlled with constants independent of all parameters.
- The SAC stitch law is uniform only on parameter regions where the SAC remainder construction is itself uniform.
- No novelty claim is made.
