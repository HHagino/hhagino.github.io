# Cuspidal Projection Closure: Discrete-Series Matrix Coefficients Already Supply the Required Kernel

## Status

**CP-A (finite-rank / K-finite sector): PASS.**

The previous note `operator-kernel-interpolation.md` introduced an apparently separate problem: starting from a matrix-coefficient correction with prescribed \(D^+_{2q-1}\) Fourier block, project it to Harish--Chandra's cuspidal Schwartz space without altering that block.

For the finite-rank \(K\)-finite sector this extra projection is unnecessary. Harish--Chandra's cusp-form theorem says that the \(K\)-finite matrix coefficients of the discrete series are themselves cusp forms, and the cuspidal Schwartz space is the closed discrete-series part of the Schwartz space. In real rank one the regular split-hyperbolic orbital integrals of this cuspidal sector vanish.

Thus the rank-one Fourier interpolants constructed in OKI already lie in the hyperbolic orbital kernel.

---

## 1. Setup

Let

\[
G=PSL(2,\mathbb R),\qquad \pi_q=D^+_{2q-1},
\]

with formal degree \(d_q\), and Fourier convention

\[
\widehat f(\pi)=\int_G f(g)\pi(g^{-1})\,dg.
\]

For smooth \(K\)-finite vectors \(u,v\in\mathcal H_{\pi_q}\), set

\[
m_{u,v}(g)=\langle u,\pi_q(g)v\rangle.
\]

Schur orthogonality gives

\[
\boxed{
\widehat{d_qm_{u,v}}(\pi_q)=|v\rangle\langle u|.
}
\tag{1.1}
\]

For a finite-rank \(K\)-finite operator

\[
A=\sum_{j=1}^N c_j|v_j\rangle\langle u_j|,
\]

define

\[
\boxed{
h_A(g)=d_q\sum_{j=1}^Nc_jm_{u_j,v_j}(g).}
\tag{1.2}
\]

Then

\[
\boxed{\widehat h_A(\pi_q)=A.}
\tag{1.3}
\]

---

## 2. Harish--Chandra cusp-form theorem

For a real reductive group, Harish--Chandra defines the cuspidal Schwartz space by vanishing of the constant terms along every proper parabolic. His fundamental result identifies this space with the closed span of the \(K\)-finite matrix coefficients of discrete-series representations:

\[
\boxed{
\mathcal C_{\rm cusp}(G)=\mathcal C_{\rm ds}(G).
}
\tag{2.1}
\]

In particular each \(m_{u,v}\) above is already cuspidal.

Consequently every finite sum \(h_A\) in (1.2) lies in

\[
\boxed{
h_A\in\mathcal C_{\rm cusp}(G).}
\tag{2.2}
\]

The previously proposed operation

\[
P_q^{\rm cusp}h_A
\]

therefore acts trivially on this finite-rank coefficient space: there is no need to manufacture a new projection merely to reach the cuspidal sector.

---

## 3. Split-hyperbolic orbital vanishing

For \(G=PSL(2,\mathbb R)\), the proper parabolic is the minimal split parabolic and the non-elliptic regular semisimple classes are represented by

\[
a_L,\qquad L\ne0.
\]

Harish--Chandra's rank-one orbital theory separates the cuspidal/discrete-series part from the split principal-series transform. In this sector the regular split-hyperbolic orbital integrals vanish:

\[
\boxed{
O_{a_L}(h)=0,
\qquad
h\in\mathcal C_{\rm cusp}(G),\quad L\ne0.
}
\tag{3.1}
\]

Hence the explicit operator interpolant (1.2) satisfies

\[
\boxed{
O_{a_L}(h_A)=0,
\qquad
\widehat h_A(\pi_q)=A.
}
\tag{3.2}
\]

This is exactly the simultaneous condition required in OKI-A2.

A useful consistency check is the familiar pseudo-coefficient statement: a discrete-series pseudo-coefficient has orbital integral zero on regular non-elliptic classes and retains elliptic discrete-series character data. The present statement is stronger in direction but narrower in topology: it treats arbitrary finite-rank \(K\)-finite Fourier blocks by finite sums of discrete-series matrix coefficients.

---

## 4. Finite-rank Operator Kernel Interpolation theorem

We may now state the FCIG result without a conditional clause.

> **Theorem (finite-rank operator kernel interpolation).**  
> Let \(A\) be a finite-rank operator on \(D^+_{2q-1}\) admitting a decomposition into rank-one operators built from smooth \(K\)-finite vectors. Then there exists an explicit Harish--Chandra cusp function
> \[
> h_A(g)=d_q\sum_jc_j\langle u_j,\pi_q(g)v_j\rangle
> \]
> such that
> \[
> \boxed{
> O_{a_L}(h_A)=0\quad(L\ne0),
> \qquad
> \widehat h_A(\pi_q)=A.
> }
> \]

Therefore

\[
\boxed{\textbf{CP-A: PASS in the finite-rank }K\textbf{-finite sector.}}
\tag{4.1}
\]

and simultaneously

\[
\boxed{\textbf{OKI-A2: PASS in the same sector.}}
\tag{4.2}
\]

---

## 5. FCIG merger theorem

Let \(f_0=\mathcal L_q^{\rm orb}W\) be any orbital lift satisfying

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\]

Define the discrete-series Fourier defect

\[
\boxed{
A_W=d_q^{-1}T_W^{(q)}-\widehat f_0(\pi_q).
}
\tag{5.1}
\]

Assume first that \(A_W\) is finite-rank and \(K\)-finite. Take the explicit cuspidal interpolant \(h_{A_W}\) and put

\[
\boxed{
f_{q,W}=f_0+h_{A_W}.}
\tag{5.2}
\]

Then

\[
\boxed{
O_{a_L}(f_{q,W})
=d_q\mathcal J_{q,L}[W]
}
\tag{5.3}
\]

because the correction has zero regular split orbital integral, while

\[
\boxed{
\widehat f_{q,W}(\pi_q)
=d_q^{-1}T_W^{(q)}.
}
\tag{5.4}
\]

Thus, in this sector, a **single group test kernel simultaneously realizes the FCIG hyperbolic orbital response and the Toeplitz discrete-series Fourier block.**

This is the operator-level merger sought since `k-type-group-lift.md`.

---

## 6. What remains open

The finite-rank theorem does not automatically solve the topological completion required for arbitrary smoothing or trace-class operators on the universal discrete-series model.

The remaining question is whether

\[
A\mapsto h_A
\]

extends continuously from finite-rank \(K\)-finite operators to a natural smoothing operator ideal, with convergence in the Harish--Chandra cuspidal Schwartz topology.

For fixed \(q\) on a compact Riemann surface, \(H^0(X,K_X^q)\) is finite-dimensional, so the actual compact-quotient Toeplitz block is finite rank. Therefore this completion issue is not needed for the fixed-\(q\) compact FCIG application, but it matters for a universal-cover or simultaneous \(q\to\infty\) representation-theoretic formulation.

Define the next gate

\[
\boxed{\textbf{SC-A — Schwartz Completion of Operator Interpolation}.}
\]

---

## 7. Updated gate ledger

\[
\boxed{
\begin{array}{rcl}
\text{DS-A} &:& \text{PASS},\\
\text{DS-B1} &:& \text{PASS},\\
\text{RI-A} &:& \text{PASS},\\
\text{RI-B} &:& \text{PASS modulo orbital-transform kernel},\\
\text{KOI-A1} &:& \text{PASS},\\
\text{OKI-A1} &:& \text{PASS},\\
\text{CP-A} &:& \text{PASS (finite-rank }K\text{-finite)},\\
\text{OKI-A2} &:& \text{PASS (finite-rank }K\text{-finite)},\\
\text{SC-A} &:& \text{OPEN}.
\end{array}
}
\]

---

## 8. Claim firewall

1. A matrix coefficient is not a character.
2. A generic tempered matrix coefficient need not be cuspidal; the statement here uses **discrete-series** matrix coefficients.
3. The finite-rank correction is not an ordinary scalar pseudo-coefficient; it is a finite linear combination of off-diagonal discrete-series matrix coefficients.
4. The split-hyperbolic orbital vanishing belongs to Harish--Chandra's cuspidal/discrete-series harmonic analysis, not to Schur orthogonality alone.
5. The infinite-rank Schwartz completion remains open here.
6. No novelty claim is made for the underlying Harish--Chandra theorems; the FCIG contribution is the assembly with the previously derived orbital and Toeplitz objects.

---

## References

- Harish--Chandra, foundational papers on cusp forms, discrete series, orbital integrals, and harmonic analysis on real reductive groups.
- Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988, Chapter 7: cusp forms on \(G\), orbital integrals of cusp forms, and harmonic analysis on the cusp space.
- Erik P. van den Ban and Job J. Kuit, *Cusp forms for reductive symmetric spaces of split rank one*, for the standard summary of Harish--Chandra's group theorem \(\mathcal C_{\rm cusp}(G)=\mathcal C_{\rm ds}(G)\).
- A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
- James Arthur, *The characters of discrete series as orbital integrals*, Invent. Math. **32** (1976), 205--261.
- J.-P. Labesse / Clozel--Delorme pseudo-coefficient theory for the complementary scalar-trace formulation.

## FCIG cross-references

- `coherent-state-discrete-series-closure.md`
- `discrete-series-invariant-inversion.md`
- `orbital-lift-closure.md`
- `k-type-orbital-interpolation.md`
- `operator-kernel-interpolation.md`
