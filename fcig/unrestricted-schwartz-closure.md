# Unrestricted Harish--Chandra Schwartz Closure

## UQ-A2 / UQ-B2 — all K-types with polynomial parameter loss

**Status (2026-09-10).**

\[
\boxed{\textbf{UQ-A2: PASS — polynomially weighted pointwise Harish--Chandra--Schwartz control for all }q,m,n.}
\]

\[
\boxed{\textbf{UQ-B2: PASS — the global K-type window closes through the discrete-series Schwartz Fourier block.}}
\]

This note closes the pointwise gate left open in `uniform-q-schwartz-control.md` and `parameter-uniform-matrix-decay.md`. The key correction is conceptual: one does not need to extend a single Jacobi steepest-descent chart uniformly through arbitrarily large ratios `m/q,n/q`. The unrestricted statement is a consequence of the Harish--Chandra Schwartz Fourier theory for the discrete-series part, together with explicit polynomial Sobolev growth of the one-dimensional K-types of the holomorphic discrete series.

No novelty claim is made for the general Schwartz Fourier theorem. The FCIG contribution here is the normalization/crosswalk with the previously derived operator synthesis and semiclassical atlas.

---

## 1. Setup

Let

\[
G=SU(1,1)\simeq SL(2,\mathbb R)
\]

up to the fixed finite-cover convention and let

\[
\pi_q=D^+_{2q-1},\qquad q\ge1.
\]

Write

\[
m_{mn}^{(q)}(g)=\langle e_m,\pi_q(g)e_n\rangle
\]

for normalized K-type vectors. Harish--Chandra's Schwartz seminorms are

\[
p_{D,E,N}(f)
=
\sup_{g\in G}(1+\sigma(g))^N\Xi(g)^{-1}
|L_D R_E f(g)|.
\]

The target is a polynomial `P` such that

\[
p_{D,E,N}(m_{mn}^{(q)})
\le C_{D,E,N}P_{D,E,N}(q,m,n)
\]

uniformly in all `q,m,n`.

---

## 2. Zeroth-order uniform majorant

Every discrete-series representation is tempered. The Cowling--Haagerup--Howe estimate for a tempered unitary representation gives, for K-finite vectors,

\[
|\langle\pi(g)v,w\rangle|
\le
\Xi(g)\,\|v\|\,\|w\|
\sqrt{\dim\langle Kv\rangle\dim\langle Kw\rangle}.
\]

For the holomorphic discrete series of `SU(1,1)`, each K-type is one-dimensional. Hence for normalized basis vectors

\[
\boxed{|m_{mn}^{(q)}(g)|\le\Xi(g)}
\]

with a constant independent of `q,m,n`.

This is stronger than the fixed-window estimate at Harish--Chandra weight `N=0`.

---

## 3. Derived-representation cost is polynomial

The standard generators act by

\[
K_0e_j=(q+j)e_j,
\]

\[
K_+e_j=\sqrt{(j+1)(2q+j)}\,e_{j+1},
\]

\[
K_-e_j=\sqrt{j(2q+j-1)}\,e_{j-1}.
\]

Therefore, for every fixed `D` in the enveloping algebra of degree `r`,

\[
\boxed{
\|d\pi_q(D)e_j\|
\le C_D(1+q+j)^r.
}
\]

The same holds on the right. Applying the Cowling--Haagerup--Howe estimate after differentiation gives

\[
\boxed{
|L_D R_E m_{mn}^{(q)}(g)|
\le
C_{D,E}(1+q+m)^{\deg D}(1+q+n)^{\deg E}\Xi(g).
}
\]

Thus the only remaining issue is insertion of arbitrary powers of the proper-length weight `(1+sigma)^N`.

---

## 4. Discrete-series Schwartz Fourier theorem

Harish--Chandra's Schwartz theory identifies the cuspidal/discrete-series part of `\mathcal C(G)` with a rapidly decreasing family of smoothing operator Fourier blocks. In rank one this is also the framework used in the `SL(2,R)` Schwartz Fourier theory of Harish--Chandra, Arthur, Stanton--Tomas, and related treatments.

For the discrete spectrum, the inverse Fourier transform of a rank-one K-finite block is a K-finite discrete-series matrix coefficient (up to the formal-degree normalization). Continuity of the inverse Schwartz Fourier transform means that every group-side seminorm is controlled by finitely many operator-side Schwartz seminorms.

Specializing this continuity to the rank-one block

\[
A_{mn}^{(q)}=|e_n\rangle\langle e_m|
\]

gives integers `a,b,c` (depending only on `D,E,N`) and a constant independent of `q,m,n` such that

\[
\boxed{
 p_{D,E,N}(m_{mn}^{(q)})
 \le
 C_{D,E,N}
 (1+q)^a(1+q+m)^b(1+q+n)^c.
}
\]

Equivalently, there is a single polynomial `P_{D,E,N}` with

\[
\boxed{
|L_D R_E m_{mn}^{(q)}(g)|
\le
C_{D,E,N}P_{D,E,N}(q,m,n)
\Xi(g)(1+\sigma(g))^{-N}
}
\]

for all `g,q,m,n`.

This is exactly the UQ-B2 target formulated in `parameter-uniform-matrix-decay.md`.

The theorem is qualitative with respect to the optimal polynomial exponents: the Schwartz-space continuity guarantees finite polynomial loss, while the explicit generator formulas make the K-type/representation dependence polynomial. Optimizing `a,b,c` is not required for closure.

---

## 5. Why this does not conflict with the semiclassical atlas

The SAC atlas gives sharp local canonical behavior in the simultaneous scaling `m/q -> alpha`, `n/q -> beta`: forbidden rates, oscillatory chamber, Airy folds, and Bessel/Hermite boundary charts.

UQ-A2 asks a different question: whether all K-finite coefficients, including `m/q` or `n/q` unbounded, have Harish--Chandra Schwartz seminorms with only polynomial parameter cost.

The Schwartz Fourier theorem answers the global topological question; the Jacobi/SAC atlas answers the sharp local asymptotic question. Neither replaces the other.

Thus

\[
\boxed{
\text{global Schwartz topology}
\quad+\quad
\text{local semiclassical atlas}
}
\]

is the correct two-level closure.

---

## 6. Consequence for FCIG operator synthesis

Recall

\[
h_{A,q}(g)
=d_q\sum_{m,n\ge0}A_{mn}m_{nm}^{(q)}(g),
\qquad
d_q=\frac{2q-1}{4\pi}.
\]

If the operator family is uniformly rapid in the weighted K-type sense, then the polynomial matrix-coefficient bound above makes the series absolutely convergent in every Harish--Chandra Schwartz seminorm. Therefore

\[
\boxed{
(A_q)_q\text{ uniformly rapid}
\Longrightarrow
(h_{A_q,q})_q\text{ polynomially controlled in }\mathcal C(G).
}
\]

Together with the exact `L^2`-Sobolev identity

\[
\|L_D R_Eh_{A,q}\|_2^2
=d_q\|d\pi_q(D)A d\pi_q(E)\|_{HS}^2,
\]

this closes both the Hilbert and pointwise Schwartz sides of the FCIG synthesis map.

---

## 7. Gate ledger

\[
\boxed{\textbf{UQ-A1: PASS — exact }L^2\textbf{-Sobolev transfer}.}
\]

\[
\boxed{\textbf{UQ-B1: PASS — fixed K-window pointwise control}.}
\]

\[
\boxed{\textbf{UQ-B2: PASS — unrestricted K-types with polynomial parameter weights}.}
\]

\[
\boxed{\textbf{UQ-A2: PASS — full pointwise Harish--Chandra Schwartz seminorm closure}.}
\]

The remaining refinements are quantitative rather than structural:

- optimize the polynomial exponents in `(q,m,n)`;
- write an explicit rank-one inverse-Schwartz-Fourier seminorm constant;
- compare those coarse global bounds with the sharp SAC rate functions in overlap regions.

None is a missing existence/closure gate.

---

## 8. Claim firewall

- Cowling--Haagerup--Howe gives the uniform `Xi` majorant for tempered representations; it does not by itself supply arbitrary spatial Schwartz weights.
- The arbitrary `(1+sigma)^N` weights enter through the discrete-series Harish--Chandra Schwartz Fourier theorem, not through CHH alone.
- The polynomial exponents are asserted to exist and be finite; they are not claimed optimal.
- The result concerns K-finite matrix coefficients and uniformly rapid operator synthesis, not arbitrary tempered matrix coefficients.
- `SAC-A` remains the source of sharp proportional-K asymptotics. `UQ-A2` is a global Schwartz-topology statement.
- No novelty claim is made for Harish--Chandra/Arthur/Stanton--Tomas Schwartz theory.

---

## References

1. M. Cowling, U. Haagerup, R. Howe, *Almost L^2 matrix coefficients*, J. Reine Angew. Math. **387** (1988), 97--110.
2. Harish--Chandra, foundational papers on discrete series and Schwartz spaces for real reductive groups.
3. R. J. Stanton, P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.
4. A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
5. N. R. Wallach, *Real Reductive Groups I/II*, Academic Press, 1988/1992.

## FCIG cross-references

- `uniform-q-schwartz-control.md`
- `parameter-uniform-matrix-decay.md`
- `schwartz-completion.md`
- `semiclassical-atlas-closure.md`
- `semiclassical-preprint.md`
