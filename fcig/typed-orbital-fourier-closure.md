# Typed Orbital/Fourier Closure — Universal-Factor Scope

## Status revision — 2026-09-11

The interpolation theorem proved in this note remains valid, but its **operator target is the universal holomorphic discrete-series Hilbert space**

\[
\mathcal H_{\pi_q},\qquad \pi_q=D^+_{2q-1},
\]

not the compact automorphic Toeplitz space \(H^0(X,K_X^q)\).

The later notes

- `automorphic-multiplicity-firewall.md`,
- `automorphic-two-point-kernel-closure.md`

supersede any reading that identifies these two operator spaces.

We retain

\[
\boxed{\textbf{OSB-B1: PASS — universal-factor typed orbital/Fourier interpolation in the smoothing sector.}}
\]

The compact quotient uses a different two-point-kernel theorem, AM-B.

---

## 1. Universal theorem

Let

\[
\pi_q=D^+_{2q-1},\qquad d_q=\frac{2q-1}{4\pi},
\]

and let \(T_W^{\rm univ,q}\) denote the universal disk/Bergman Toeplitz operator acting on \(\mathcal H_{\pi_q}\).

For admissible Weyl-normalized orbital data choose an orbital lift \(f_0\) satisfying

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\tag{1.1}
\]

Define the universal Fourier defect

\[
A_W
:=
d_q^{-1}T_W^{\rm univ,q}
-
\widehat f_0(\pi_q).
\tag{1.2}
\]

If

\[
A_W\in\mathscr S(\mathcal H_{\pi_q}),
\]

the discrete-series cuspidal Schwartz synthesis gives \(h_{A_W}\) with

\[
\widehat h_{A_W}(\pi_q)=A_W,
\qquad
O_{a_L}(h_{A_W})=0
\quad(L\ne0).
\tag{1.3}
\]

Hence

\[
\boxed{f_{q,W}:=f_0+h_{A_W}}
\tag{1.4}
\]

satisfies simultaneously

\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W],
}
\tag{1.5}
\]

and

\[
\boxed{
\widehat f_{q,W}(\pi_q)
=d_q^{-1}T_W^{\rm univ,q}.
}
\tag{1.6}
\]

This is the precise scope of OSB-B1.

---

## 2. Why compact descent is not obtained by finite rank

For

\[
X=\Gamma\backslash\mathbb H,
\]

the automorphic decomposition has

\[
L^2(\Gamma\backslash G)
\simeq
\widehat\bigoplus_\pi
\mathcal M_\pi\widehat\otimes\mathcal H_\pi.
\]

The compact holomorphic space is

\[
\boxed{
H^0(X,K_X^q)
\simeq
\mathcal M_q\otimes\ell_q^{\rm low},
}
\tag{2.1}
\]

not \(\mathcal H_{\pi_q}\).

A scalar group convolution acts on the \(\pi_q\)-isotypic summand as

\[
I_{\mathcal M_q}\otimes\pi_q(f).
\]

After compression to \(\ell_q^{\rm low}\), it is only a scalar multiple of the identity on \(\mathcal M_q\). A generic compact Toeplitz matrix

\[
T_W^{X,q}\in\operatorname{End}(\mathcal M_q)
\]

therefore cannot be obtained by simply declaring

\[
\widehat f(\pi_q)=T_W^{X,q}.
\]

Finite dimensionality does not remove this tensor-factor obstruction.

---

## 3. Correct compact replacement

The compact object is the two-point Toeplitz kernel

\[
\boxed{
\mathbb K_W^{X,q}(x,y)
=
\int_X
B_{X,q}(x,z)W(z)B_{X,q}(z,y)\,dA(z).
}
\tag{3.1}
\]

It retains the full operator

\[
T_W^{X,q}\in\operatorname{End}(H^0(X,K_X^q)),
\]

while its weighted diagonal/pre-trace expansion descends, after grouping deck transformations by conjugacy class, to the cyclic orbital terms

\[
C_q\ell\,\mathcal J_{q,m\ell}[W].
\]

That compact theorem is recorded as AM-B in `automorphic-two-point-kernel-closure.md`.

---

## 4. Two correct diagrams

### Universal representation diagram

\[
\boxed{
\begin{array}{ccc}
&f_{q,W}\in\mathcal C(G)&\\
\swarrow &&\searrow\\
d_q\mathcal J_{q,L}[W]
&&d_q^{-1}T_W^{\rm univ,q}\in\operatorname{End}(\mathcal H_{\pi_q}).
\end{array}}
\tag{4.1}
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
\tag{4.2}
\]

The first is a group-Fourier/orbital interpolation theorem. The second is an automorphic two-point-kernel/pre-trace theorem.

They share the same universal Bergman/discrete-series local building block but live in different operator categories.

---

## 5. Weyl and Gamma structures remain unchanged

The correction above does not alter the already-proved scalar hyperbolic structures:

\[
\Delta(L)=2\sinh(L/2),
\]

\[
\Theta_{2q-1}^{+}(a_{L/2})
=
\Delta(L)^{-1}e^{-(q-1/2)L},
\]

and

\[
\widehat{\Re\kappa}_{q,L}(\xi)
\propto
\left(\frac{|\xi|}{\tanh(L/2)}\right)^{2q-1}
 e^{-|\xi|/\tanh(L/2)}.
\]

Only the typing of the compact Toeplitz operator is changed.

---

## 6. Gate status

\[
\boxed{\textbf{OSB-B1: PASS — universal-factor smoothing interpolation.}}
\]

\[
\boxed{\textbf{AM-A1/A2: PASS — multiplicity identification and convolution no-go.}}
\]

\[
\boxed{\textbf{AM-B1/B2: PASS — compact two-point Toeplitz kernel and conjugacy-class trace descent.}}
\]

The remaining genuinely stronger compact question is

\[
\boxed{\textbf{AM-C: OPEN — state-decorated/matrix-element relative trace formula.}}
\]

## Claim firewall

- \(T_W^{\rm univ,q}\in\operatorname{End}(\mathcal H_{\pi_q})\) and \(T_W^{X,q}\in\operatorname{End}(\mathcal M_q)\) are different objects.
- OSB-B1 remains correct only with the universal operator target.
- AM-B, not OSB-B1, is the compact quotient theorem.
- Scalar conjugacy-class trace data do not reconstruct a generic compact Toeplitz matrix.
- No spectral variable identifications are introduced by this correction.
- No novelty claim is made for standard automorphic multiplicity theory or pre-trace formulas.