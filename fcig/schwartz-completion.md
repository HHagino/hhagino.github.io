# Schwartz Completion of Discrete-Series Operator Interpolation

## Status

The finite-rank, K-finite interpolation problem is closed in `cuspidal-projection-closure.md`: for
\(\pi_q=D^+_{2q-1}\), finite sums of discrete-series matrix coefficients simultaneously realize prescribed finite-rank Fourier blocks and vanish on the regular split-hyperbolic orbital side.

This note identifies the natural completion. The correct operator space is not merely trace class or Hilbert--Schmidt: it is the **smooth/rapid operator ideal** for the derived representation. In a K-type basis this is equivalent to rapid decay of matrix entries. Under the discrete-series Fourier transform this space is topologically equivalent to the \(\pi_q\)-isotypic cuspidal Harish--Chandra-Schwartz space.

Within this standard Schwartz-space formulation, the finite-rank interpolation extends continuously.

---

## 1. Representation and smooth operator ideal

Let

\[
G=PSL(2,\mathbb R),\qquad \pi_q=D^+_{2q-1}
\]

with Hilbert space \(\mathcal H_q\). Let \(\mathcal H_q^\infty\) be the smooth vectors and \(d\pi_q\) the derived representation of \(U(\mathfrak g_\mathbb C)\).

Define the rapid/smoothing operator space

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

Equip it with seminorms

\[
p_{D_1,D_2}(A)
=
\|d\pi_q(D_1)A\,d\pi_q(D_2)\|_1.
\]

This is stronger than bare trace class. It records rapid regularity in both representation variables.

---

## 2. K-type matrix characterization

Choose the standard orthonormal K-type basis

\[
e_0,e_1,e_2,\ldots
\]

of the holomorphic discrete series, with K-weights increasing linearly with \(n\). Write

\[
A_{mn}=\langle e_m,Ae_n\rangle.
\]

The compact generator acts diagonally with eigenvalues affine in \(n\), while the raising and lowering operators change \(n\) by one with coefficients of polynomial growth. Consequently the derived-representation seminorms above are equivalent to rapid matrix decay:

\[
\boxed{
A\in\mathscr S(\mathcal H_q)
\iff
\forall N\ge0,
\quad
\sup_{m,n\ge0}(1+m+n)^N|A_{mn}|<\infty.
}
\]

One may equivalently use weighted \(\ell^1\) or Hilbert--Schmidt seminorms; for rapidly decreasing matrices these define the same nuclear Fréchet topology.

Thus finite-rank K-finite matrices are dense in \(\mathscr S(\mathcal H_q)\).

Let

\[
A^{(N)}=P_NAP_N,
\qquad
P_N=\sum_{n=0}^N|e_n\rangle\langle e_n|.
\]

Then

\[
\boxed{
A^{(N)}\longrightarrow A
\quad\text{in }\mathscr S(\mathcal H_q).
}
\]

---

## 3. Matrix-coefficient synthesis

For a finite matrix \(A^{(N)}\), CP-A gave

\[
h_{A^{(N)}}(g)
=
d_q\sum_{m,n\le N}A_{mn}\,m_{n,m}(g),
\]

with convention chosen so that

\[
\widehat{h_{A^{(N)}}}(\pi_q)=A^{(N)}.
\]

For \(A\in\mathscr S(\mathcal H_q)\), define formally

\[
\boxed{
h_A(g)
:=
d_q\sum_{m,n\ge0}A_{mn}\,m_{n,m}(g).}
\]

The rapid decay of \(A_{mn}\), together with the standard Harish--Chandra-Schwartz estimates for K-finite discrete-series matrix coefficients and their left/right derivatives, gives convergence in the cuspidal Harish--Chandra-Schwartz topology.

Hence

\[
\boxed{
h_{A^{(N)}}\to h_A
\quad\text{in }\mathcal C(G)_{\mathrm{cusp}}.}
\]

---

## 4. Fourier inversion on the discrete-series block

Continuity of the group Fourier transform on Harish--Chandra's Schwartz algebra and Schur orthogonality imply

\[
\widehat h_A(\pi_q)
=
\lim_{N\to\infty}\widehat h_{A^{(N)}}(\pi_q)
=
\lim_{N\to\infty}A^{(N)}
=A.
\]

Therefore

\[
\boxed{
\widehat h_A(\pi_q)=A
\qquad(A\in\mathscr S(\mathcal H_q)).
}
\]

This is the continuous extension of OKI-A1.

---

## 5. Hyperbolic orbital nullity survives completion

Each finite partial sum belongs to the discrete-series cuspidal Schwartz sector and satisfies

\[
O_{a_L}(h_{A^{(N)}})=0,
\qquad L\ne0.
\]

Regular orbital integrals are continuous distributions on the Harish--Chandra-Schwartz space. Passing to the limit gives

\[
\boxed{
O_{a_L}(h_A)=0,
\qquad L\ne0.
}
\]

Thus the two required conditions survive simultaneously:

\[
\boxed{
A\in\mathscr S(\mathcal H_q)
\Longrightarrow
\begin{cases}
\widehat h_A(\pi_q)=A,\\
O_{a_L}(h_A)=0\quad(L\ne0).
\end{cases}}
\]

---

## 6. Topological isomorphism statement

Let \(\mathcal C(G)_{\pi_q}\) denote the \(\pi_q\)-isotypic discrete-series summand of the cuspidal Harish--Chandra-Schwartz algebra. Then the preceding construction is the concrete rank-one realization of the standard Fourier-side identification

\[
\boxed{
\mathcal C(G)_{\pi_q}
\simeq
\mathscr S(\mathcal H_q).
}
\]

Under this correspondence,

\[
\boxed{
A\longmapsto h_A
}
\]

is continuous, and its inverse is

\[
\boxed{
f\longmapsto\widehat f(\pi_q).}
\]

Normalization by the formal degree \(d_q\) is fixed by Schur orthogonality.

This is the appropriate meaning of a discrete-series Schwartz Fourier block. It is stronger and cleaner than asking for an arbitrary trace-class completion.

---

## 7. FCIG operator-level merger

Let

\[
f_0=\mathcal L_q^{\rm orb}W
\]

satisfy

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\]

Define

\[
A_W
=
d_q^{-1}T_W^{(q)}-\widehat f_0(\pi_q).
\]

Whenever

\[
\boxed{A_W\in\mathscr S(\mathcal H_q),}
\]

define

\[
\boxed{
f_{q,W}:=f_0+h_{A_W}.}
\]

Then

\[
\boxed{
O_{a_L}(f_{q,W})
=d_q\mathcal J_{q,L}[W]
}
\]

because \(h_{A_W}\) is hyperbolic-orbital-null, while

\[
\boxed{
\widehat f_{q,W}(\pi_q)
=d_q^{-1}T_W^{(q)}.
}
\]

Therefore the orbital and Toeplitz/Fourier branches merge at operator level for every FCIG symbol whose defect lies in the smooth operator ideal.

---

## 8. Compact quotient consequence

For a compact hyperbolic surface \(X\),

\[
H^0(X,K_X^q)
\]

is finite-dimensional at each fixed \(q\). Hence the compact FCIG Toeplitz block is automatically finite rank. After identifying it with the relevant automorphic discrete-series multiplicity block, the finite-rank CP-A/OKI construction already applies.

The Schwartz completion is needed primarily for:

- the universal-cover representation model;
- uniform families as \(q\to\infty\);
- infinite-rank smoothing symbols;
- a genuine Plancherel/Harish--Chandra formulation independent of a finite-dimensional quotient.

---

## 9. Gate status

We record

\[
\boxed{\textbf{SC-A: PASS — discrete-series Schwartz operator completion.}}
\]

More precisely, the pass is in the standard smooth operator ideal

\[
\mathscr S(\mathcal H_q),
\]

not in the whole trace-class ideal.

Together with CP-A this gives

\[
\boxed{\textbf{OKI-A2: PASS in the Schwartz smoothing sector.}}
\]

The next nontrivial question is no longer existence of a common test kernel. It is **uniform semiclassical control in \(q\)**.

Define the next gate

\[
\boxed{\textbf{UQ-A — Uniform-}q\textbf{ Schwartz Control}.}
\]

The target is to estimate the seminorms of

\[
h_{A_W,q}
\]

uniformly or asymptotically as \(q\to\infty\), and compare them with the already derived Bergman/Toeplitz and Selberg-scale asymptotics.

---

## 10. Claim firewall

- SC-A concerns the rapid/smoothing operator ideal, not arbitrary bounded, Hilbert--Schmidt, or trace-class operators.
- The equivalence with rapidly decreasing K-type matrices is with respect to the smooth derived-representation topology.
- Hyperbolic orbital nullity follows from membership in the cuspidal discrete-series Schwartz summand plus continuity of regular orbital integrals; it is not a pointwise statement about arbitrary coefficients.
- Compact-quotient Toeplitz operators and the universal-cover discrete-series operator model remain distinct objects until an automorphic multiplicity identification is specified.
- No novelty claim is made.

---

## References

1. Harish-Chandra, foundational papers on harmonic analysis, cusp forms, and the Schwartz algebra of real reductive groups.
2. A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
3. N. R. Wallach, *Real Reductive Groups I/II*, Academic Press, 1988/1992.
4. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.
5. J. Dixmier, standard results on smooth vectors and operator ideals for unitary representations.
6. J.-P. Labesse, pseudo-coefficients and cuspidal test functions for discrete series.

## FCIG cross-references

- `operator-kernel-interpolation.md`
- `cuspidal-projection-closure.md`
- `k-type-orbital-interpolation.md`
- `orbital-lift-closure.md`
- `discrete-series-invariant-inversion.md`
- `coherent-state-discrete-series-closure.md`
