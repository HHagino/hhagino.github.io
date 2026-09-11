# Schwartz Completion of Discrete-Series Operator Interpolation

## Status revision — 2026-09-11

This note proves a universal discrete-series statement on

\[
\mathcal H_q:=\mathcal H_{D^+_{2q-1}}.
\]

The result remains valid exactly as a Harish--Chandra-Schwartz/Fourier theorem. A previous paragraph incorrectly suggested that finite-dimensionality of \(H^0(X,K_X^q)\) was enough to apply this theorem directly to compact Toeplitz matrices. The later automorphic multiplicity audit shows that this is false: the compact Toeplitz operator lives on the automorphic multiplicity factor, not on \(\mathcal H_q\).

Thus

\[
\boxed{\textbf{SC-A: PASS — universal discrete-series Schwartz operator completion.}}
\]

with compact descent handled separately by `automorphic-multiplicity-firewall.md` and `automorphic-two-point-kernel-closure.md`.

---

## 1. Smooth operator ideal

Let \(d\pi_q\) be the derived representation. Define

\[
\boxed{
\mathscr S(\mathcal H_q)
:=
\left\{A:\mathcal H_q\to\mathcal H_q:
 d\pi_q(D_1)A\,d\pi_q(D_2)
 \text{ is trace class for all }D_1,D_2\in U(\mathfrak g_\mathbb C)
\right\}.
}
\]

With seminorms

\[
p_{D_1,D_2}(A)
=
\|d\pi_q(D_1)A\,d\pi_q(D_2)\|_1,
\]

this is the rapid/smoothing operator ideal for the universal discrete-series representation.

In the standard K-type basis \(e_0,e_1,\ldots\), it is equivalently described by rapid decay of the matrix entries:

\[
\boxed{
A\in\mathscr S(\mathcal H_q)
\iff
\forall N\ge0,
\quad
\sup_{m,n\ge0}(1+m+n)^N|A_{mn}|<\infty.
}
\]

Finite-rank K-finite matrices are dense.

---

## 2. Matrix-coefficient synthesis

For

\[
A=\sum_{m,n}A_{mn}|e_m\rangle\langle e_n|
\]

with rapid matrix decay, define

\[
\boxed{
h_A(g)=d_q\sum_{m,n\ge0}A_{mn}\,m_{n,m}^{(q)}(g),}
\]

where

\[
d_q=\frac{2q-1}{4\pi}.
\]

The series converges in the cuspidal Harish--Chandra-Schwartz topology. Schur orthogonality and continuity of the Fourier transform give

\[
\boxed{
\widehat h_A(\pi_q)=A.
}
\tag{2.1}
\]

Because the synthesis lies in the discrete-series cuspidal summand,

\[
\boxed{
O_{a_L}(h_A)=0,
\qquad L\ne0.
}
\tag{2.2}
\]

Therefore

\[
\boxed{
A\in\mathscr S(\mathcal H_q)
\Longrightarrow
\begin{cases}
\widehat h_A(\pi_q)=A,\\
O_{a_L}(h_A)=0.
\end{cases}}
\]

This is the universal Schwartz interpolation theorem.

---

## 3. Fourier-side identification

Let \(\mathcal C(G)_{\pi_q}\) be the \(\pi_q\)-isotypic discrete-series summand of the cuspidal Harish--Chandra-Schwartz algebra. Then

\[
\boxed{
\mathcal C(G)_{\pi_q}
\simeq
\mathscr S(\mathcal H_q),
}
\]

with

\[
A\mapsto h_A,
\qquad
f\mapsto\widehat f(\pi_q).
\]

This is a statement about the **universal representation factor**.

---

## 4. Universal FCIG interpolation

Let \(T_W^{\rm univ,q}\) denote the universal disk/Bergman Toeplitz operator acting on \(\mathcal H_q\), and let an orbital lift \(f_0\) satisfy

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\]

Set

\[
A_W
=
d_q^{-1}T_W^{\rm univ,q}
-
\widehat f_0(\pi_q).
\]

If \(A_W\in\mathscr S(\mathcal H_q)\), then

\[
\boxed{
f_{q,W}=f_0+h_{A_W}}
\]

satisfies

\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W]
}
\]

and

\[
\boxed{
\widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{\rm univ,q}.
}
\]

This is the correct scope of SC-A/OSB-B1.

---

## 5. Compact quotient correction

For

\[
X=\Gamma\backslash\mathbb H,
\]

automorphic multiplicity theory gives

\[
H^0(X,K_X^q)
\simeq
\mathcal M_q\otimes\ell_q^{\rm low}.
\]

A compact Toeplitz operator

\[
T_W^{X,q}
\in
\operatorname{End}(\mathcal M_q\otimes\ell_q^{\rm low})
\simeq
\operatorname{End}(\mathcal M_q)
\]

acts on the multiplicity factor.

By contrast a scalar group convolution acts on the \(\pi_q\)-isotypic summand as

\[
I_{\mathcal M_q}\otimes\pi_q(f).
\]

Thus finite rank of \(T_W^{X,q}\) does **not** put it inside the operator ideal \(\mathscr S(\mathcal H_q)\). The factors are different.

The previous claim that compact fixed-q Toeplitz matrices were automatically covered by finite-rank OKI is therefore withdrawn.

The correct compact object is the automorphic two-point kernel

\[
\mathbb K_W^{X,q}(x,y)
=
\int_XB_{X,q}(x,z)W(z)B_{X,q}(z,y)\,dA(z),
\]

which is treated in AM-B.

---

## 6. Gate status

\[
\boxed{\textbf{SC-A: PASS — universal smoothing operator completion.}}
\]

\[
\boxed{\textbf{OKI-A2: PASS — universal smoothing sector.}}
\]

\[
\boxed{\textbf{AM-A2: PASS — direct scalar-convolution realization of generic compact Toeplitz matrices is obstructed.}}
\]

\[
\boxed{\textbf{AM-B1/B2: PASS — compact two-point kernel and scalar trace descent.}}
\]

## Claim firewall

- \(\mathscr S(\mathcal H_q)\) is an operator ideal on the universal discrete-series Hilbert space.
- Compact automorphic Toeplitz matrices live on the multiplicity factor \(\mathcal M_q\), not on \(\mathcal H_q\).
- Finite dimensionality does not remove a tensor-factor mismatch.
- The universal interpolation theorem is not retracted; only its former compact-quotient extrapolation is retracted.
- No novelty claim is made for standard discrete-series Schwartz theory or automorphic multiplicity theory.

## References

1. Harish-Chandra, harmonic analysis, cusp forms, and the Schwartz algebra of real reductive groups.
2. A. W. Knapp, *Representation Theory of Semisimple Groups*.
3. N. R. Wallach, *Real Reductive Groups I/II*.
4. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*.
5. A. Borel and N. Wallach, *Continuous Cohomology, Discrete Subgroups, and Representations of Reductive Groups*.
6. FCIG notes `automorphic-multiplicity-firewall.md` and `automorphic-two-point-kernel-closure.md`.