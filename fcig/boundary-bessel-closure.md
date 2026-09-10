# Boundary Bessel Closure

## BC-A1 — diagonal-endpoint double scaling

**Status (2026-09-10).**

\[
\boxed{\textbf{BC-A1: PASS — the }q|\alpha-\beta|=O(1)\textbf{ boundary chart is Bessel.}}
\]

This note closes the first of the two boundary double scalings isolated in `uniform-remainder-closure.md`.

The regime

\[
q|\alpha-\beta|=O(1)
\]

is exactly the regime in which the two high \(K\)-type indices differ by a fixed integer while each index itself is proportional to \(q\).  The inner Airy fold then reaches the radial endpoint \(t=0\), so the separated-fold Airy coordinate is no longer uniform.  Starting from the exact Jacobi/hypergeometric matrix coefficient gives a Bessel canonical limit instead.

No literature-novelty claim is made.  The use of a Mehler--Heine/Bessel endpoint model is classical; the FCIG scaling and its match to the previously derived inner caustic are derived here.

---

## 1. Exact matrix coefficient

For \(n\ge m\), write

\[
k=n-m\ge0.
\]

Under the same radial and phase convention as the preceding FCIG notes,

\[
\boxed{
M_{m,m+k}^{(q)}(t)
=
\mathcal N_{m,m+k}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^k
P_m^{(k,2q-1)}
\left(1-2\tanh^2\frac t2\right),
}
\]

where

\[
\mathcal N_{m,m+k}(q)
=
\left(
\frac{m!\,\Gamma(2q+m+k)}
{(m+k)!\,\Gamma(2q+m)}
\right)^{1/2}.
\]

A fixed convention-dependent unitary phase can multiply this scalar coefficient; it does not alter the radial Bessel limit or absolute-value estimates.

Use the terminating hypergeometric representation

\[
P_m^{(k,2q-1)}(1-2r^2)
=
\frac{(k+1)_m}{m!}
{}_2F_1
\left(
-m,m+k+2q;k+1;r^2
\right),
\]

with

\[
r=\tanh\frac t2.
\]

---

## 2. Boundary scaling

Let

\[
\frac mq\to\alpha>0,
\qquad
k\ \text{fixed},
\qquad
t=\frac{s}{q},
\]

with \(s\) in a fixed compact subset of \(\mathbb C\) (or \(\mathbb R\) for the radial statement).

Then

\[
r
=
\tanh\frac{s}{2q}
=
\frac{s}{2q}+O(q^{-3}),
\]

and

\[
\left(\cosh\frac{s}{2q}\right)^{-2q}
=1+O(q^{-1}).
\]

The normalization has the fixed-difference limit

\[
\boxed{
\mathcal N_{m,m+k}(q)
\to
\left(\frac{\alpha+2}{\alpha}\right)^{k/2}.
}
\]

Also

\[
\frac{(k+1)_m}{m!}
=
\frac{\Gamma(m+k+1)}{\Gamma(k+1)\Gamma(m+1)}
\sim
\frac{(\alpha q)^k}{k!}.
\]

---

## 3. Hypergeometric contraction

For every fixed summation index \(j\),

\[
\frac{(-m)_j(m+k+2q)_j}{(k+1)_j\,j!}r^{2j}
\longrightarrow
\frac{(-1)^j}{(k+1)_j\,j!}
\left(
\frac{\alpha(\alpha+2)s^2}{4}
\right)^j.
\]

Because the limiting series is entire and the original series terminates, the standard compact-set dominated/finite-tail argument gives

\[
\boxed{
{}_2F_1
\left(
-m,m+k+2q;k+1;r^2
\right)
\longrightarrow
{}_0F_1
\left(
;k+1;
-\frac{\alpha(\alpha+2)s^2}{4}
\right)
}
\]

uniformly for bounded \(s\).

Let

\[
p_\alpha=\sqrt{\alpha(\alpha+2)}.
\]

The Bessel identity

\[
{}_0F_1
\left(;k+1;-\frac{x^2}{4}\right)
=
k!\left(\frac2x\right)^kJ_k(x)
\]

then yields the cancellation

\[
\left(\frac{\alpha+2}{\alpha}\right)^{k/2}
\left(\frac{s}{2q}\right)^k
\frac{(\alpha q)^k}{k!}
{}_0F_1
\left(;k+1;-\frac{p_\alpha^2s^2}{4}\right)
=
J_k(p_\alpha s)+o(1).
\]

Therefore

\[
\boxed{
M_{m,m+k}^{(q)}(s/q)
\longrightarrow
J_k\!\left(\sqrt{\alpha(\alpha+2)}\,s\right)
}
\]

uniformly for bounded \(s\), up to the fixed representation/line-bundle phase convention.

This is the FCIG boundary Bessel contraction.

---

## 4. Identity check

At \(s=0\),

\[
J_0(0)=1,
\qquad
J_k(0)=0\quad(k>0).
\]

Thus the limit gives

\[
M_{m,m}^{(q)}(0)\to1
\]

and

\[
M_{m,m+k}^{(q)}(0)\to0\qquad(k>0),
\]

exactly matching orthogonality of distinct \(K\)-types at the identity element.

---

## 5. Match to the collapsing inner caustic

From `uniform-remainder-closure.md`, when

\[
\delta=\frac{k}{q},
\]

the inner caustic satisfies

\[
t_-
=
\frac{\delta}{\sqrt{\alpha(\alpha+2)}}+O(\delta^2).
\]

Hence in the boundary radial coordinate \(s=qt\),

\[
\boxed{
s_-
=qt_-
\to
\frac{k}{p_\alpha}.
}
\]

The Bessel argument at this location is therefore

\[
\boxed{
p_\alpha s_-=k.}
\]

This is exactly the large-order Bessel transition scale: when \(k\) itself becomes large, \(J_k(x)\) changes from exponentially small to oscillatory through the turning region \(x\approx k\).

Thus the two descriptions match as

\[
\boxed{
\text{fixed }k\text{ boundary Bessel chart}
\quad\xrightarrow{k\to\infty}\quad
\text{generic inner Airy chart}.
}
\]

The DLMF large-order Bessel expansion gives the corresponding Airy uniformization near \(x=k+O(k^{1/3})\).

This is the desired overlap between BC-A1 and RF-B2/UR-A1.

---

## 6. Interpretation

The boundary law

\[
q|\alpha-\beta|=O(1)
\]

has a simple representation-theoretic meaning:

\[
\boxed{n-m=k=O(1).}
\]

Both \(K\)-type indices are large, but their difference is fixed.  Simultaneously,

\[
t=O(q^{-1}),
\]

so the hyperbolic group element approaches the identity.  The pair

\[
q\to\infty,
\qquad
t=s/q
\]

is therefore a local group-contraction scale, and the Bessel function is the canonical radial transition function.

The appearance of

\[
p_\alpha=\sqrt{\alpha(\alpha+2)}
\]

is also consistent with the exact caustic geometry because

\[
p_\alpha=\sinh u_\alpha,
\qquad
\alpha+1=\cosh u_\alpha.
\]

---

## 7. Gate status

We may now sharpen the boundary ledger:

\[
\boxed{\textbf{BC-A1: PASS — diagonal/endpoint crossover is Bessel.}}
\]

The only remaining proportional-\(K\) boundary chart is

\[
\boxed{
\textbf{BC-A2 — lowest-}K\textbf{ sheet-merger closure:}
\qquad q\beta=O(1).
}
\]

If

\[
\nu=q\beta
\]

is fixed, then one \(K\)-type index remains finite while the other is proportional to \(q\), and

\[
t_+-t_-=O(q^{-1/2}).
\]

The exact Jacobi representation then has fixed polynomial degree \(\nu\) and two large parameters.  Classical large-parameter Jacobi theory suggests a Hermite/parabolic-cylinder boundary model, but that identification is **not yet asserted**.  BC-A2 must be derived directly with

\[
t=u_\alpha+\frac{\tau}{\sqrt q}
\]

before the canonical function is named.

---

## References

1. NIST Digital Library of Mathematical Functions, §18.11(ii), Mehler--Heine type formulas for Jacobi polynomials.
2. NIST Digital Library of Mathematical Functions, §§10.19--10.20, large-order and Airy-uniform asymptotics for Bessel functions.
3. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975.
4. A. Gil, J. Segura, N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss-Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. **494** (2021), 124642.

## Claim firewall

- The classical Mehler--Heine principle and Bessel large-order Airy asymptotics are established literature.
- The displayed FCIG limit is derived from the exact FCIG hypergeometric coefficient with \(m/q\to\alpha\), fixed \(k=n-m\), and \(t=s/q\).
- The Bessel argument \(p_\alpha s\) and its match \(p_\alpha s_-=k\) to the collapsing inner caustic are derived here.
- BC-A1 does not solve the distinct \(q\beta=O(1)\) sheet-merger regime.
