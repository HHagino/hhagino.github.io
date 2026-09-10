# Operator Kernel Interpolation: Matrix-Coefficient Corrections in the Hyperbolic Orbital Kernel

## Status

This note sharpens KOI-A2. The scalar pseudo-coefficient argument controls only the trace of the discrete-series Fourier block. For the full FCIG Toeplitz block one needs operator-valued corrections.

The key observation is that square-integrability of the discrete series gives such corrections explicitly at the level of finite-rank operators, while the hyperbolic-orbital-null condition requires a separate cuspidality input. Keeping these two ingredients typed separately prevents a false identification.

## 1. Setup

Let

\[
G=PSL(2,\mathbb R),\qquad \pi_q=D^+_{2q-1},
\]

and let \(d_q\) denote the formal degree in the Haar normalization used throughout the FCIG hyperbolic notes. Use the Fourier convention

\[
\widehat f(\pi)=\int_G f(g)\pi(g^{-1})\,dg.
\]

For \(u,v\in\mathcal H_{\pi_q}\), define the matrix coefficient

\[
m_{u,v}(g)=\langle u,\pi_q(g)v\rangle.
\]

For \(a,b\in\mathcal H_{\pi_q}\), Schur orthogonality for the square-integrable representation gives

\[
\int_G
\langle u,\pi_q(g)v\rangle
\overline{\langle a,\pi_q(g)b\rangle}\,dg
=
\frac1{d_q}\langle u,a\rangle\langle b,v\rangle,
\]

up to the harmless interchange of rank-one conventions induced by the chosen inner-product convention.

Equivalently, after fixing the convention once and for all,

\[
\boxed{
\widehat{m_{u,v}}(\pi_q)
=
\frac1{d_q}|v\rangle\langle u|.
}
\]

Thus

\[
\boxed{
h_{u,v}:=d_q m_{u,v}
\quad\Longrightarrow\quad
\widehat h_{u,v}(\pi_q)=|v\rangle\langle u|.
}
\]

This is the operator-valued analogue of the coherent-state computation in `discrete-series-invariant-inversion.md`.

## 2. Finite-rank Fourier interpolation

Let

\[
A=\sum_{j=1}^N c_j|v_j\rangle\langle u_j|
\]

be a finite-rank operator with smooth \(K\)-finite vectors. Define

\[
\boxed{
h_A(g)=d_q\sum_{j=1}^N c_jm_{u_j,v_j}(g).}
\]

Then exactly

\[
\boxed{
\widehat h_A(\pi_q)=A.
}
\]

Hence the group Fourier transform restricted to the discrete-series coefficient space is already surjective onto finite-rank \(K\)-finite operators.

This closes the purely operator-theoretic part of OKI-A.

## 3. Why this does not yet imply orbital nullity

It would be incorrect to infer from square-integrability alone that

\[
O_{a_L}(h_A)=0.
\]

A generic matrix coefficient is not automatically a pseudo-coefficient, and ordinary orbital integrals are not determined solely by the \(\pi_q\)-Fourier block.

The missing condition is **cuspidality / vanishing of the split constant term**.

For real rank one, a cuspidal test function has vanishing constant term along the proper parabolic. Standard trace-formula theory then forces its regular split-hyperbolic orbital integrals to vanish. Discrete-series pseudo-coefficients are the scalar example of this phenomenon.

Therefore the correct target is not the full coefficient space but a cuspidal matrix-coefficient completion

\[
\mathcal C_{q}^{\mathrm{cusp}}
\subset
\mathcal K_{\mathrm{hyp}}
:=
\{f:O_{a_L}(f)=0\text{ for every regular }L\ne0\}.
\]

## 4. The finite-rank cuspidal interpolation theorem target

The precise theorem needed by FCIG is:

> **OKI finite-rank theorem.** For every finite-rank \(K\)-finite operator \(A\) on \(D^+_{2q-1}\), there exists a cuspidal Harish--Chandra-Schwartz test function \(h_A\) such that
> \[
> O_{a_L}(h_A)=0\quad(L\ne0),
> \qquad
> \widehat h_A(\pi_q)=A.
> \]

The matrix-coefficient calculation above proves the second condition constructively. Standard cuspidal projection / discrete-series Paley--Wiener theory is the natural mechanism for imposing the first while preserving the chosen discrete-series block.

Accordingly:

\[
\boxed{\textbf{OKI-A1: PASS — finite-rank Fourier interpolation.}}
\]

The stronger simultaneous statement is recorded conservatively as

\[
\boxed{\textbf{OKI-A2: CONDITIONAL PASS — pending explicit cuspidal projection preserving the }\pi_q\textbf{ block.}}
\]

No claim is made here that an arbitrary raw matrix coefficient already has zero hyperbolic orbital integrals.

## 5. Application to the FCIG Toeplitz defect

Let

\[
f_0=\mathcal L_q^{\rm orb}W
\]

be an orbital lift with

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\]

Define the operator defect

\[
\boxed{
A_W
:=
 d_q^{-1}T_W^{(q)}-\widehat f_0(\pi_q).
}
\]

If \(A_W\) is finite rank, or is approximated in the relevant smoothing topology by finite-rank \(K\)-finite operators, the preceding construction gives Fourier corrections with the exact desired \(\pi_q\) block.

If the cuspidal projection can be chosen to preserve that block, then

\[
\boxed{
f_{q,W}=f_0+h_{A_W}}
\]

satisfies simultaneously

\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W]
}
\]

and

\[
\boxed{
\widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
}
\]

This is exactly the operator-level merger of the FCIG orbital and Toeplitz branches.

## 6. Smoothing completion

For the compact quotient relevant to FCIG, Toeplitz operators with smooth symbols are smoothing in the semiclassical finite-dimensional holomorphic space at fixed \(q\). On the universal discrete-series model, however, one must distinguish finite-rank, trace-class, Hilbert--Schmidt, and Harish--Chandra-Schwartz operator topologies.

Thus the infinite-rank completion should be formulated as continuity of

\[
A\longmapsto h_A
\]

from a specified smoothing operator class into the cuspidal Schwartz algebra. This is a topological Paley--Wiener question, not an algebraic consequence of the rank-one formula.

## 7. Updated architecture

We now have

\[
\boxed{
\begin{array}{rcl}
W
&\longmapsto&
T_W^{(q)},\\
W
&\longmapsto&
\mathcal J_{q,L}[W],\\
\mathcal L_q^{\rm orb}W
&\longmapsto&
O_{a_L}=d_q\mathcal J_{q,L}[W],\\
A
&\longmapsto&
h_A,
\quad \widehat h_A(\pi_q)=A.
\end{array}}
\]

The remaining compatibility condition is exactly

\[
\boxed{
h_A\in\ker O_{\rm hyp}}
\]

while preserving its prescribed \(\pi_q\)-Fourier block.

This isolates the final representation-theoretic obstruction much more sharply than the earlier scalar pseudo-coefficient formulation.

## 8. Next gate

Define

\[
\boxed{\textbf{CP-A — Cuspidal Projection Closure}.}
\]

Construct or cite an explicit continuous projection

\[
P_{q}^{\rm cusp}:\mathcal S(G)_{K\text{-finite}}
\longrightarrow
\mathcal S(G)_{\rm cusp}
\]

such that on the target discrete-series block

\[
\boxed{
\widehat{P_q^{\rm cusp}f}(\pi_q)=\widehat f(\pi_q)
}
\]

and

\[
\boxed{
O_{a_L}(P_q^{\rm cusp}f)=0.
}
\]

If CP-A passes, then OKI-A2 passes and the FCIG hyperbolic orbital and Toeplitz Fourier branches admit a single operator-valued test kernel.

## 9. Claim firewall

- Matrix coefficients, characters, pseudo-coefficients, and orbital integrals remain distinct typed objects.
- Schur orthogonality proves finite-rank Fourier interpolation; it does **not** by itself prove hyperbolic orbital vanishing.
- Pseudo-coefficients prove a scalar trace interpolation direction, not arbitrary operator interpolation.
- Cuspidal projection is the remaining mechanism to verify, not an assumption to hide.
- No novelty claim is made.

## References

1. Harish-Chandra, *Discrete series for semisimple Lie groups. II. Explicit determination of the characters*, Acta Math. **116** (1966), 1–111.
2. Harish-Chandra, foundational work on harmonic analysis and the Schwartz space of real reductive groups.
3. A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986 — square-integrable representations, formal degree, matrix coefficients, Plancherel theory.
4. J.-P. Labesse, work on pseudo-coefficients and the trace formula — cuspidal test functions isolating discrete series.
5. R. A. Herb, harmonic analysis and Fourier transforms of orbital/weighted orbital integrals on \(SL(2,\mathbb R)\).
6. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.

## FCIG cross-references

- `coherent-state-discrete-series-closure.md`
- `discrete-series-invariant-inversion.md`
- `relative-invariantization.md`
- `orbital-lift-closure.md`
- `k-type-orbital-interpolation.md`
- `character-trace-firewall.md`
