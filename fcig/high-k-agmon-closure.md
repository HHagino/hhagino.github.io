# High-K Agmon Closure

## SR-B1b — unrestricted two-high-K outer tail

**Status (2026-09-10).**

This note closes the only remaining obstruction in `logarithmic-spatial-weight-closure.md`.

\[
\boxed{\textbf{SR-B1b: PASS — the unrestricted outer tail has a parameter-uniform exponential slope.}}
\]

Consequently the sharp logarithmic spatial-weight theorem SR-B1 is closed for all K-type pairs.

---

## 1. Exact radial ODE

Let

\[
F(t)=M_{m,n}^{(q)}(t)
\]

in the radial phase convention in which the Jacobi expression is real.  Put

\[
\mu=q+m,\qquad \nu=q+n.
\]

Starting from

\[
F(t)=\mathcal N_{m,n}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^{n-m}
P_m^{(n-m,2q-1)}\left(1-2\tanh^2\frac t2\right)
\]
for \(n\ge m\), and using the Jacobi differential equation, one obtains after direct conjugation

\[
\boxed{
F''(t)+\coth t\,F'(t)
-
\left[
q(q-1)+
\frac{\mu^2+\nu^2-2\mu\nu\cosh t}{\sinh^2t}
\right]F(t)=0.
}
\tag{1.1}
\]

The formula is symmetric in \(m,n\), as required by the radial conjugation symmetry.

---

## 2. Liouville conjugation

Set

\[
Y(t)=\sqrt{\sinh t}\,F(t).
\]

Then (1.1) becomes the one-dimensional equation

\[
\boxed{Y''(t)=W_{q,m,n}(t)Y(t),}
\tag{2.1}
\]

where

\[
\boxed{
W_{q,m,n}(t)
=\left(q-\frac12\right)^2
+
\frac{\mu^2+\nu^2-2\mu\nu\cosh t-\frac14}{\sinh^2t}.
}
\tag{2.2}
\]

This is the exact radial Schrödinger/Agmon form relevant to the outer forbidden region.

---

## 3. Exact principal factorization

Define

\[
A=1+\frac mq=\cosh u_m,
\qquad
B=1+\frac nq=\cosh u_n.
\]

Then

\[
T:=t_+=u_m+u_n,
\qquad
t_-=|u_m-u_n|.
\]

The principal semiclassical potential factorizes exactly:

\[
\boxed{
1+
\frac{A^2+B^2-2AB\cosh t}{\sinh^2t}
=
\frac{(\cosh t-\cosh T)(\cosh t-\cosh t_-)}{\sinh^2t}.
}
\tag{3.1}
\]

Thus the same two caustics derived from the coefficient-extraction discriminant are precisely the turning points of the radial ODE at principal semiclassical order.

This gives an independent structural check of the SAC caustic geometry.

---

## 4. Uniform positivity beyond the outer caustic

Let

\[
t=T+\delta,\qquad\delta>0.
\]

Since \(\cosh T\ge\cosh t_-\),

\[
\frac{(\cosh t-\cosh T)(\cosh t-\cosh t_-)}{\sinh^2t}
\ge
\left(
\frac{\cosh(T+\delta)-\cosh T}{\sinh(T+\delta)}
\right)^2.
\]

The elementary identity

\[
\cosh(T+\delta)-\cosh T
=2\sinh(\delta/2)\sinh(T+\delta/2)
\]
shows

\[
\boxed{
\frac{\cosh(T+\delta)-\cosh T}{\sinh(T+\delta)}
\ge\tanh(\delta/2).
}
\tag{4.1}
\]

Indeed, after cancellation this inequality is equivalent to \(\sinh T\ge0\).

Combining (2.2), (3.1), and (4.1),

\[
W_{q,m,n}(t)
\ge
q^2\tanh^2(\delta/2)-q+\frac14-rac1{4\sinh^2t}.
\tag{4.2}
\]

For

\[
q\ge2,
\qquad
\delta\ge2,
\]
we have \(t\ge2\), so

\[
\boxed{
W_{q,m,n}(t)
\ge
c_0q^2,
\qquad
c_0:=\tanh^2(1)-\frac12>0.
}
\tag{4.3}
\]

The harmless positive finite-\(q\) remainder in (4.2) only improves this bound.  Most importantly, \(c_0\) is independent of \(q,m,n\).

---

## 5. One-dimensional comparison lemma

On \([T+2,\infty)\), the radial Jacobi coefficient has a fixed phase times a real solution and decays at infinity.  Since \(W>0\), a nonzero decaying real solution of

\[
Y''=WY
\]

cannot have a zero in this interval: a zero with nonzero derivative would force the solution, by convexity on either sign component, away from zero rather than back toward the decaying boundary condition.

Choose the overall sign so that \(Y>0\).  Let

\[
\lambda=q\sqrt{c_0}.
\]

Since \(W\ge\lambda^2\), comparison with the Dirichlet Green kernel of \(d^2/dt^2-\lambda^2\) gives

\[
\boxed{
Y(T+2+s)
\le
Y(T+2)e^{-\lambda s},
\qquad s\ge0.
}
\tag{5.1}
\]

Equivalently,

\[
\boxed{
|F(T+2+s)|
\le
|F(T+2)|
\left(\frac{\sinh(T+2)}{\sinh(T+2+s)}\right)^{1/2}
e^{-q\sqrt{c_0}s}.
}
\tag{5.2}
\]

---

## 6. Harish--Chandra normalization

Cowling--Haagerup--Howe gives

\[
|F(T+2)|\le\Xi(a_{T+2})
\]

for normalized one-dimensional K-types of the tempered holomorphic discrete series.

Use the rank-one two-sided estimate

\[
\Xi(a_t)\asymp(1+t)e^{-t/2}.
\]

Since \(T+2\ge2\),

\[
\left(\frac{\sinh(T+2)}{\sinh(T+2+s)}\right)^{1/2}
\le C e^{-s/2}.
\]

The factor \(e^{-s/2}\) cancels the inverse exponential growth coming from \(\Xi(a_{T+2})/\Xi(a_{T+2+s})\).  Therefore

\[
\boxed{
\frac{|M_{m,n}^{(q)}(T+2+s)|}{\Xi(a_{T+2+s})}
\le
C e^{-q\sqrt{c_0}s}
\le
C e^{-2\sqrt{c_0}s},
}
\tag{6.1}
\]

for all \(q\ge2\), all \(m,n\ge0\), and all \(s\ge0\).

This is exactly the unrestricted tail estimate required by SR-B1.

---

## 7. Global logarithmic spatial-weight theorem

Define

\[
T_{q,m,n}
=\operatorname{arcosh}\left(1+\frac mq\right)
+\operatorname{arcosh}\left(1+\frac nq\right).
\]

For

\[
0\le t\le T_{q,m,n}+2,
\]
CHH gives

\[
(1+t)^N\Xi(a_t)^{-1}|M_{m,n}^{(q)}(t)|
\le(3+T_{q,m,n})^N.
\]

For the outer tail, (6.1) absorbs arbitrary polynomial powers of \(s=t-T-2\).  Hence for every integer \(N\ge0\),

\[
\boxed{
\sup_{t\ge0}
(1+t)^N\Xi(a_t)^{-1}|M_{m,n}^{(q)}(t)|
\le
C_N(1+T_{q,m,n})^N,
}
\tag{7.1}
\]

uniformly for \(q\ge2\) and all \(m,n\ge0\).

Since

\[
\operatorname{arcosh}(1+x)=O(1+\log(1+x)),
\]
we obtain

\[
\boxed{
p_N(M_{m,n}^{(q)})
\le
C_N
\left[
1+\log\left(1+\frac mq\right)
+\log\left(1+\frac nq\right)
\right]^N.
}
\tag{7.2}
\]

Thus the spatial K-type cost is logarithmic, not polynomial.

\[
\boxed{\textbf{SR-B1: PASS — unrestricted logarithmic spatial cost.}}
\]

---

## 8. Derivatives

Combining (7.1) with the exact derived-representation estimates from SR-A1 gives, for fixed \(D,E\) of degrees \(r,s\),

\[
\boxed{
\begin{aligned}
p_{D,E,N}(M_{m,n}^{(q)})
\le{}&C_{D,E,N}
(1+q+m)^r(1+q+n)^s\\
&\times
\left[
1+\operatorname{arcosh}(1+m/q)
+\operatorname{arcosh}(1+n/q)
\right]^N.
\end{aligned}
}
\tag{8.1}
\]

This is the sharpened quantitative form of UQ-A2.

---

## 9. Gate ledger

\[
\boxed{\textbf{SR-B1b: PASS — unrestricted two-high-K outer tail.}}
\]

\[
\boxed{\textbf{SR-B1: PASS — unrestricted logarithmic spatial Schwartz cost.}}
\]

Together with SR-A1 and SR-A2, the only remaining refinement gate is the globally differentiated SAC-overlap/remainder theorem (SR-B2 / DA-A2), not the basic spatial seminorm bound.

---

## Claim firewall

- The ODE is derived from the exact Jacobi equation in the fixed FCIG radial convention.
- The turning points of the principal ODE potential agree with the SAC caustics; finite-q lower-order terms do not move this statement into an exact finite-q turning-point identity.
- The Agmon comparison is used only beyond the fixed buffer `t >= t_+ + 2`, where the potential has a universal positive lower bound.
- The logarithmic spatial cost is an upper-bound theorem.  Optimal lower constants in every Schwartz seminorm are not claimed.
- The result is for radial matrix coefficients; global K-phases have unit modulus, while invariant derivatives are handled separately through derived-representation weights.
- No novelty claim is made without a literature comparison specifically for this combined parameter-uniform formulation.
