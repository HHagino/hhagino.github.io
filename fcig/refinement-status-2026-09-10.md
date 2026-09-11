# FCIG Refinement Status — 2026-09-11

This file is the authoritative ledger for the post-SAC quantitative, transform-theoretic, and automorphic refinement.

## 1. Quantitative semiclassical closure

The following remain closed:

\[
\boxed{\textbf{SR-A1: PASS — sharp derivative polynomial degrees}}
\]
\[
\boxed{\textbf{SR-A2: PASS — exact formal-degree synthesis cost}}
\]
\[
\boxed{\textbf{SR-B1: PASS — unrestricted logarithmic spatial Schwartz cost}}
\]
\[
\boxed{\textbf{DA-A1: PASS — local derivative scales}}
\]
\[
\boxed{\textbf{DA-B1: PASS — global finite-order radial derivative theorem}}
\]
\[
\boxed{\textbf{SR-B2a: PASS — finite-order differentiated SAC--Schwartz stitching}}
\]

In particular,
\[
\boxed{\begin{aligned}
p_{D,E,N}(M_{m,n}^{(q)})
\le{}&C_{D,E,N}(1+q+m)^{\deg D}(1+q+n)^{\deg E}\\
&\times\left[1+\operatorname{arcosh}(1+m/q)+\operatorname{arcosh}(1+n/q)\right]^N.
\end{aligned}}
\]

The stronger all-orders resolved atlas remains optional refinement:

\[
\boxed{\textbf{DA-B2: OPEN — one polyhomogeneous all-orders remainder architecture.}}
\]

---

## 2. Universal representation-side transform closure

The exact local/universal chain remains valid on the holomorphic discrete-series Hilbert space

\[
\mathcal H_{\pi_q},\qquad \pi_q=D^+_{2q-1}.
\]

The following are closed in their natural universal domains:

\[
\text{DS-B1 PASS},\quad
\text{RI-A PASS},\quad
\text{RI-B PASS modulo orbital kernel},\quad
\text{OKI-A2 PASS in the universal smoothing sector},\quad
\text{SC-A PASS}.
\]

Hence

\[
\boxed{\textbf{OSB-B1: PASS — universal-factor typed orbital/Fourier interpolation.}}
\]

For the universal Toeplitz operator \(T_W^{\rm univ,q}\), one can choose a common Schwartz representative \(f_{q,W}\) with

\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W],
\qquad
\widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{\rm univ,q}.
}
\]

This theorem is **not** a compact-quotient Toeplitz theorem.

---

## 3. Automorphic multiplicity correction

Let

\[
X=\Gamma\backslash\mathbb H
\]

be compact. The right regular representation decomposes as

\[
L^2(\Gamma\backslash G)
\simeq
\widehat\bigoplus_\pi
\mathcal M_\pi\widehat\otimes\mathcal H_\pi.
\]

For the holomorphic discrete series,

\[
\boxed{
H^0(X,K_X^q)
\simeq
\mathcal M_q\otimes\ell_q^{\rm low}.
}
\]

Thus the compact Toeplitz matrix acts on the automorphic multiplicity factor:

\[
T_W^{X,q}\in\operatorname{End}(\mathcal M_q).
\]

By contrast, scalar group convolution acts as

\[
I_{\mathcal M_q}\otimes\pi_q(f).
\]

After lowest-K compression it is only a scalar multiple of \(I_{\mathcal M_q}\). Therefore a generic compact Toeplitz matrix cannot be identified with \(\widehat f(\pi_q)\).

Accordingly:

\[
\boxed{\textbf{AM-A1: PASS — automorphic multiplicity identification.}}
\]
\[
\boxed{\textbf{AM-A2: PASS — scalar-convolution/multiplicity no-go.}}
\]

The earlier sentence “compact fixed-q is finite rank, hence universal OKI applies directly” is withdrawn. Finite rank does not cure a tensor-factor mismatch.

For genus \(g\ge2\),

\[
\dim\mathcal M_q
=
\dim H^0(X,K_X^q)
=
\begin{cases}
g,&q=1,\\
(2q-1)(g-1),&q\ge2.
\end{cases}
\]

---

## 4. Compact two-point-kernel closure

The correct compact object is

\[
\boxed{
\mathbb K_W^{X,q}(x,y)
=
\int_XB_{X,q}(x,z)W(z)B_{X,q}(z,y)\,dA(z).
}
\]

It acts directly on \(H^0(X,K_X^q)\) and therefore retains the full multiplicity matrix.

At the scalar trace level,

\[
\operatorname{Tr}T_W^{X,q}
=
\int_XW(x)B_{X,q}(x,x)\,dA(x).
\]

For `q>=2`, periodizing the universal Bergman kernel and grouping nonidentity deck transformations by primitive conjugacy class gives the exact cyclic terms

\[
\boxed{
C_q\ell\,\mathcal J_{q,m\ell}[W]
=
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W].
}
\]

Hence

\[
\boxed{\textbf{AM-B1: PASS — exact compact Toeplitz two-point kernel.}}
\]
\[
\boxed{\textbf{AM-B2: PASS — weighted Bergman trace descends to cyclic closed-geodesic orbitals.}}
\]

This is the corrected compact FCIG bridge.

---

## 5. Two distinct but compatible closure diagrams

### Universal representation diagram

\[
\boxed{
\begin{array}{ccc}
&f_{q,W}\in\mathcal C(G)&\\
\swarrow &&\searrow\\
d_q\mathcal J_{q,L}[W]
&&d_q^{-1}T_W^{\rm univ,q}.
\end{array}}
\]

### Compact automorphic diagram

\[
\boxed{
\begin{array}{ccc}
&\mathbb K_W^{X,q}(x,y)&\\
\swarrow &&\searrow\\
T_W^{X,q}\in\operatorname{End}(\mathcal M_q)
&&\{C_q\ell\mathcal J_{q,m\ell}[W]\}_{[\delta],m}.
\end{array}}
\]

The common object across the two theories is the universal Bergman/discrete-series **local kernel**, not a literal identification of their operator spaces.

---

## 6. Current frontier

The genuinely stronger remaining compact problem is

\[
\boxed{\textbf{AM-C: OPEN — state-decorated / matrix-element relative trace formula.}}
\]

The scalar trace formula sees conjugacy-class scalar data. It does not reconstruct an arbitrary matrix in \(\operatorname{End}(\mathcal M_q)\). To recover matrix elements one must insert external automorphic states, producing a relative/pre-trace formula with state-decorated geometric terms.

The other optional refinement is

\[
\boxed{\textbf{DA-B2: OPEN — resolved all-orders semiclassical atlas.}}
\]

Thus the project frontier is now

\[
\boxed{
\text{state-decorated automorphic trace theory}
\quad\oplus\quad
\text{all-orders resolved semiclassical geometry}.
}
\]

---

## Claim firewall

- Universal \(T_W^{\rm univ,q}\) and compact \(T_W^{X,q}\) act on different tensor factors.
- OSB-B1 remains correct in the universal smoothing sector.
- AM-B is the compact quotient theorem.
- Scalar closed-geodesic trace data do not determine the full compact Toeplitz matrix.
- `q>=2` is the safe absolutely convergent automorphic Bergman-periodization regime used in AM-B; `q=1` requires separate low-weight convergence treatment.
- The transverse Fourier variable, cyclic deformation mode, K-type label, and Harish--Chandra spectral parameter remain distinct.
- No novelty claim is made without a separate literature audit.