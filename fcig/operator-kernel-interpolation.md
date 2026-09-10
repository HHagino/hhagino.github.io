# Operator Kernel Interpolation: Matrix-Coefficient Corrections in the Hyperbolic Orbital Kernel

## Status

**OKI-A1: PASS.**  
**OKI-A2: PASS in the finite-rank, smooth K-finite sector.**  
**Universal Schwartz completion: OPEN; see SC-A in `cuspidal-projection-closure.md`.**

This note records the operator-valued interpolation needed to merge the FCIG Toeplitz/Fourier branch with the hyperbolic orbital branch. The earlier conditional status has now been superseded by `cuspidal-projection-closure.md`: discrete-series K-finite matrix coefficients are themselves Harish--Chandra cusp forms, so the finite-rank Fourier interpolants already lie in the regular split-hyperbolic orbital kernel.

## 1. Setup

Let

\[
G=PSL(2,\mathbb R),\qquad \pi_q=D^+_{2q-1},
\]

with formal degree \(d_q\), and use

\[
\widehat f(\pi)=\int_G f(g)\pi(g^{-1})\,dg.
\]

For smooth K-finite \(u,v\in\mathcal H_{\pi_q}\), put

\[
m_{u,v}(g)=\langle u,\pi_q(g)v\rangle.
\]

Schur orthogonality gives, with the FCIG rank-one convention,

\[
\boxed{
\widehat{m_{u,v}}(\pi_q)=d_q^{-1}|v\rangle\langle u|.
}
\]

Hence

\[
\boxed{
h_{u,v}:=d_qm_{u,v}
\quad\Longrightarrow\quad
\widehat h_{u,v}(\pi_q)=|v\rangle\langle u|.
}
\]

## 2. Finite-rank interpolation

For

\[
A=\sum_{j=1}^N c_j|v_j\rangle\langle u_j|
\]

with smooth K-finite vectors, define

\[
\boxed{
h_A(g)=d_q\sum_{j=1}^Nc_jm_{u_j,v_j}(g).}
\]

Then exactly

\[
\boxed{\widehat h_A(\pi_q)=A.}
\]

Therefore the discrete-series matrix-coefficient space is Fourier-surjective onto finite-rank K-finite operators.

## 3. Cuspidality closes the orbital condition

Harish--Chandra's cusp-form theorem identifies the group cuspidal Schwartz space with the closed span of K-finite discrete-series matrix coefficients. Thus every summand \(m_{u_j,v_j}\), and hence \(h_A\), is cuspidal.

For rank-one \(PSL(2,\mathbb R)\), the regular split semisimple classes are represented by \(a_L\), \(L\ne0\), and the cuspidal/discrete-series sector has vanishing split-hyperbolic orbital transform. Therefore

\[
\boxed{
O_{a_L}(h_A)=0,
\qquad
\widehat h_A(\pi_q)=A.
}
\]

This is the simultaneous operator interpolation required by OKI-A2.

## 4. FCIG merger

Let

\[
f_0=\mathcal L_q^{\rm orb}W
\]

be an orbital lift satisfying

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\]

Define

\[
\boxed{
A_W=d_q^{-1}T_W^{(q)}-\widehat f_0(\pi_q).
}
\]

Whenever \(A_W\) lies in the finite-rank smooth K-finite sector, put

\[
\boxed{f_{q,W}=f_0+h_{A_W}.}
\]

Then

\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W]
}
\]

and simultaneously

\[
\boxed{
\widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
}
\]

Thus the orbital and Toeplitz/Fourier branches are represented by one group test kernel in the finite-rank K-finite sector.

## 5. Remaining completion issue

The unresolved point is no longer algebraic interpolation. It is topological completion: extend

\[
A\mapsto h_A
\]

continuously from finite-rank K-finite operators to an appropriate smoothing operator ideal while retaining convergence in Harish--Chandra's cuspidal Schwartz topology.

For fixed \(q\) on a compact Riemann surface, the geometric Toeplitz space \(H^0(X,K_X^q)\) is finite-dimensional, so the finite-rank statement already covers the compact fixed-q FCIG block. A universal-cover or uniform \(q\to\infty\) theorem requires the stronger completion.

## 6. Gate status

\[
\boxed{\textbf{OKI-A1: PASS.}}
\]

\[
\boxed{\textbf{OKI-A2: PASS (finite-rank smooth K-finite).}}
\]

Next:

\[
\boxed{\textbf{SC-A — Schwartz Completion of Operator Interpolation: OPEN.}}
\]

## 7. Claim firewall

- Matrix coefficient \(\neq\) character \(\neq\) pseudo-coefficient \(\neq\) orbital integral.
- Schur orthogonality supplies the prescribed Fourier operator block.
- Cuspidality, not Schur orthogonality alone, supplies regular split-hyperbolic orbital vanishing.
- The full infinite-rank Schwartz completion is not claimed here.
- No literature-novelty claim is made.

## References

- Harish--Chandra, work on cusp forms, discrete series, orbital integrals, and Schwartz harmonic analysis.
- Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988, Chapter 7.
- A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
- James Arthur, *The characters of discrete series as orbital integrals*, Invent. Math. 32 (1976), 205--261.

## FCIG cross-references

- `cuspidal-projection-closure.md`
- `k-type-orbital-interpolation.md`
- `orbital-lift-closure.md`
- `discrete-series-invariant-inversion.md`
- `coherent-state-discrete-series-closure.md`
