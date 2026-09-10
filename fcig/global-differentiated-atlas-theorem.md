# Global Differentiated Semiclassical Atlas

## DA-B — finite-order global radial closure

**Status (2026-09-10).**

This note upgrades the local derivative chart ledger in `derivative-atlas-closure.md` using the exact radial ODE and the unrestricted outer Agmon estimate in `high-k-agmon-closure.md`.

The key distinction is between two statements:

1. a **finite-order global radial estimate**, which can now be closed by patching compact canonical charts to the Agmon exterior;
2. a **single all-orders canonical expansion with one explicit remainder formula valid uniformly through every degenerating overlap**, which remains stronger and is not claimed here.

We record

\[
\boxed{\textbf{DA-B1: PASS — global finite-order radial derivative control.}}
\]

\[
\boxed{\textbf{DA-B2: OPEN — one all-orders explicit canonical remainder formula across every degeneration.}}
\]

---

## 1. Exact radial equation

Let

\[
F(t)=M_{m,n}^{(q)}(t),\qquad \mu=q+m,\quad \nu=q+n.
\]

The Jacobi equation conjugates exactly to

\[
F''+\coth t\,F'-V_{q,m,n}(t)F=0,
\]

with

\[
V_{q,m,n}(t)=q(q-1)+
\frac{\mu^2+\nu^2-2\mu\nu\cosh t}{\sinh^2t}.
\tag{1.1}
\]

Hence every higher radial derivative can be reduced recursively to

\[
\boxed{
\partial_t^jF=A_j(t;q,m,n)F+B_j(t;q,m,n)F',
}
\tag{1.2}
\]

where `A_j,B_j` are obtained by differentiating (1.1). Away from `t=0`, they are rational functions of `sinh t, cosh t` with polynomial dependence on `q,m,n` of degree at most `j` after the natural representation weights are counted.

Thus only `F` and `F'` require independent asymptotic control.

---

## 2. Compact canonical region

Put

\[
u_j=\operatorname{arcosh}(1+j/q),\qquad
 t_-=|u_m-u_n|,\quad t_+=u_m+u_n.
\]

Fix a derivative order `J` and a bounded enlargement of the transition region

\[
0\le t\le t_++2.
\]

The previously closed SAC charts cover this region after the two boundary blow-ups are included:

- ordinary saddle charts away from folds;
- Airy charts near simple folds;
- Bessel chart when `q|m/q-n/q|=|m-n|=O(1)` at the identity merger;
- Hermite--Gaussian chart when `min(m,n)=O(1)` at the two-fold merger.

The local derivative scales are

\[
\boxed{
\begin{array}{ccl}
\text{ordinary saddle}&:&q^j,\\
\text{Airy fold}&:&q^{2j/3},\\
\text{Bessel boundary}&:&q^j,\\
\text{Hermite boundary}&:&q^{j/2}.
\end{array}}
\tag{2.1}
\]

For each fixed `J`, differentiated steepest descent / differentiated canonical-function expansions give uniform bounds through order `J` on compact sets in their rescaled variables. On chart overlaps the exact coefficient is the common object, so a partition of unity may be chosen in the parameter/radial blow-up space and the local estimates patched without asserting equality of truncated asymptotic series.

This yields a finite-order bound of the form

\[
\boxed{
|\partial_t^jM_{m,n}^{(q)}(t)|
\le C_J(1+q+m+n)^j\,\Xi(a_t),
\qquad 0\le t\le t_++2,
\quad j\le J,
}
\tag{2.2}
\]

with the sharper chart powers (2.1) available when the local canonical scale is resolved.

The purpose of (2.2) is global domination, not optimal local power counting.

---

## 3. Agmon exterior and derivative bootstrap

The outer-tail note gives, for

\[
Y(t)=\sqrt{\sinh t}\,F(t),
\]

an exact Schrödinger equation

\[
Y''=W_{q,m,n}(t)Y
\]

and a universal positive lower bound

\[
W_{q,m,n}(t)\ge c_0q^2,
\qquad t\ge t_++2,
\quad q\ge2,
\tag{3.1}
\]

with

\[
c_0=\tanh^2(1)-\frac12>0.
\]

The decaying solution therefore satisfies

\[
|F(t_++2+s)|\le C\,\Xi(a_{t_++2+s})e^{-c s}
\tag{3.2}
\]

for universal `c,C>0`.

Differentiate the exact ODE. Since on `t\ge t_++2` all derivatives of `coth t` and `sinh(t)^{-2}` are uniformly bounded and the parameter coefficients in (1.1) have the natural polynomial representation size, induction in (1.2) gives, for each fixed `J`,

\[
\boxed{
|\partial_t^jF(t_++2+s)|
\le
C_J(1+q+m+n)^j\,
\Xi(a_{t_++2+s})e^{-c_Js},
\quad j\le J.
}
\tag{3.3}
\]

The constants depend on `J`, but not on `q,m,n`.

This is precisely the derivative control missing from the purely leading SAC atlas in the unrestricted exterior.

---

## 4. Global finite-order theorem

Combining (2.2) and (3.3), and using

\[
t_+=\operatorname{arcosh}(1+m/q)+\operatorname{arcosh}(1+n/q),
\]

gives the following.

### Theorem DA-B1

For every pair of integers `J,N>=0` there is a constant `C_{J,N}` such that, for `q>=2`, `m,n>=0`, and `0<=j<=J`,

\[
\boxed{
\sup_{t\ge0}
(1+t)^N\Xi(a_t)^{-1}
|\partial_t^jM_{m,n}^{(q)}(t)|
\le
C_{J,N}
(1+q+m+n)^j
(1+t_+)^N.
}
\tag{4.1}
\]

Equivalently, because

\[
t_+=O\!\left(1+\log(1+m/q)+\log(1+n/q)\right),
\]

the spatial cost is logarithmic in the distant K-type labels, while finite radial differentiation costs only the natural polynomial representation weight.

Thus

\[
\boxed{\textbf{DA-B1: PASS.}}
\]

---

## 5. What DA-B1 does and does not close

DA-B1 is sufficient for the finite-order radial Harish--Chandra--Schwartz estimates needed in the semiclassical synthesis problem. It also supplies a rigorous global majorant against which the sharper saddle/Airy/Bessel/Hermite approximations may be stitched.

It does **not** claim a single formula

\[
M=\mathcal A_{\rm global}+R_K
\]

whose `R_K` has one explicit power of `q` simultaneously uniform through:

- separated simple folds;
- the diagonal Bessel degeneration;
- the lowest-K Hermite merger;
- all transitions between those blow-up faces;
- arbitrary derivative order with constants controlled as the order varies.

That stronger object is a polyhomogeneous/all-orders theorem on a resolved parameter space. It remains a worthwhile refinement, but it is no longer required for finite-order Schwartz closure.

We therefore rename the old `DA-A2` frontier:

\[
\boxed{
\textbf{DA-B2 — resolved all-orders atlas: OPEN.}
}
\]

---

## 6. Consequence for SR-B2

The previous stitch law near a simple outer fold was

\[
q\Phi_+(t)
\approx
\frac t2+N\log(1+t)+\log P_{D,E}
+\frac{2j}{3}\log q.
\]

DA-B1 supplies a global differentiated majorant on the far side of this overlap. Hence for every fixed derivative order the SAC-to-Schwartz patch is now legitimate: use the canonical approximation where its local remainder is smaller and the global DA-B1 majorant outside.

Accordingly we record

\[
\boxed{\textbf{SR-B2a: PASS — finite-order differentiated SAC--Schwartz stitching.}}
\]

The stronger single-formula all-orders version is exactly DA-B2.

---

## 7. Gate ledger

\[
\boxed{
\begin{array}{ll}
\text{DA-A1} & \text{PASS — local canonical derivative scales},\\
\text{DA-B1} & \text{PASS — global finite-order radial derivative theorem},\\
\text{SR-B2a} & \text{PASS — finite-order differentiated stitching},\\
\text{DA-B2} & \text{OPEN — resolved all-orders explicit remainder theorem}.
\end{array}}
\]

## Claim firewall

- The theorem is finite-order: `J` is fixed before the constants are chosen.
- Local canonical powers remain sharper than the global polynomial domination in (4.1).
- `DA-B1` is a radial theorem. General left/right enveloping-algebra derivatives use the separate exact K-type shift/weight estimates already proved in SR-A1.
- The existence of a finite chart cover plus exact ODE bootstrap is not a claim of a single global canonical normal form.
- No novelty claim is made for differentiated steepest descent, Airy/Bessel/Hermite differentiation, or one-dimensional Agmon comparison.