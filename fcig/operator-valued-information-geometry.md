# Operator-Valued Information Geometry on the Automorphic Multiplicity Space

## OIG-A — before Fisher scalarization

**Status (2026-09-11).**

The compact automorphic closure reveals a structural refinement of FCIG: the scalar Bergman/Fisher density is not the primitive local datum. The primitive datum is the rank-one positive operator
\[
\varrho_q(x)=|\mathrm{ev}_x\rangle\langle\mathrm{ev}_x|
\in\operatorname{End}(\mathcal M_q).
\]
Its trace is the Bergman density, while integration against a symbol produces the full Toeplitz response.

We record
\[
\boxed{\textbf{OIG-A1: PASS — exact operator-valued local information density.}}
\]

---

## 1. Exact identities

Let \(\mathcal M_q\simeq H^0(X,K_X^q)\) and choose an orthonormal basis \(s_a\). Define the coherent/evaluation vector \(v_x\in\mathcal M_q\) by its coordinates
\[
(v_x)_a=s_a(x)
\]
with the fiber metric absorbed into the chosen local trivialization. Then
\[
\boxed{\varrho_q(x)=|v_x\rangle\langle v_x|.}
\tag{1.1}
\]
Its matrix entries are
\[
(\varrho_q(x))_{ab}=s_a(x)\overline{s_b(x)}.
\tag{1.2}
\]
Consequently
\[
\boxed{\operatorname{Tr}\varrho_q(x)=\sum_a|s_a(x)|^2=B_{X,q}(x,x).}
\tag{1.3}
\]
For a scalar symbol \(W\),
\[
\boxed{T_W=\int_XW(x)\varrho_q(x)dA(x).}
\tag{1.4}
\]
Thus the usual scalar trace response is
\[
\operatorname{Tr}T_W=\int_XW(x)\operatorname{Tr}\varrho_q(x)dA(x).
\tag{1.5}
\]

---

## 2. Normalized local state

Whenever \(B_{X,q}(x,x)>0\), define
\[
\boxed{\widehat\varrho_q(x):=\frac{\varrho_q(x)}{B_{X,q}(x,x)}.}
\tag{2.1}
\]
Then
\[
\operatorname{Tr}\widehat\varrho_q(x)=1,
\qquad
\widehat\varrho_q(x)^2=\widehat\varrho_q(x),
\tag{2.2}
\]
so \(\widehat\varrho_q(x)\) is a pure-state density matrix on the multiplicity Hilbert space.

This gives a canonical map
\[
\boxed{X\longrightarrow\mathbb P(\mathcal M_q),\qquad x\mapsto[v_x],}
\tag{2.3}
\]
which is the projective coherent-state/Kodaira map when the linear system is base-point free.

---

## 3. Fisher metric as a scalar shadow of projective quantum geometry

The normalized rank-one family carries the Fubini--Study metric. Infinitesimally, for a parameter coordinate \(\theta^i\), the pure-state quantum Fisher tensor is determined by derivatives of \([v_\theta]\). Its real symmetric part is the Fubini--Study metric (up to the conventional factor used in defining quantum Fisher information), while its imaginary antisymmetric part is the Berry curvature.

Thus FCIG has the hierarchy
\[
\boxed{
\text{operator-valued coherent state}
\longrightarrow
\begin{cases}
\text{Fubini--Study / quantum Fisher metric},\\
\text{Berry curvature},\\
\text{scalar Bergman density by trace}.
\end{cases}}
\tag{3.1}
\]
This is more precise than treating Fisher information as the sole primitive structure.

---

## 4. Entropy firewall

Because \(\widehat\varrho_q(x)\) is rank one,
\[
S_{\mathrm{vN}}(\widehat\varrho_q(x))=0.
\]
Therefore the pointwise von Neumann entropy of the normalized coherent state is **not** the FCIG entropy candidate. Nontrivial entropy appears only after coarse-graining, mixing, tracing over additional structure, or considering dimensions/determinants of global section spaces.

This cleanly separates three notions:
\[
\boxed{
\begin{array}{rcl}
\log\dim H^0(X,L^q)&:&\text{global state-counting entropy candidate},\\
\log B_q(x,x)&:&\text{local density/normalization potential},\\
S_{\rm vN}(\widehat\varrho_q(x))=0&:&\text{pure coherent-state entropy}.
\end{array}}
\tag{4.1}
\]
They must not be identified.

---

## 5. Mixed response states

For a nonnegative symbol \(W\ge0\), assuming \(\operatorname{Tr}T_W>0\), define
\[
\boxed{\rho_W:=\frac{T_W}{\operatorname{Tr}T_W}.}
\tag{5.1}
\]
Then \(\rho_W\) is a genuine mixed density operator whenever the weighted coherent-state ensemble is not rank one. It is exactly
\[
\rho_W
=\frac{\int_XW(x)B_q(x,x)\widehat\varrho_q(x)dA(x)}{\int_XW(x)B_q(x,x)dA(x)}.
\tag{5.2}
\]
Hence \(W(x)B_q(x,x)dA(x)\), after normalization, acts as the classical mixing measure over projective coherent states.

This supplies a mathematically clean bridge between FCIG's measure-normalization theme and quantum-information geometry:
\[
\boxed{\text{Radon weight}\to\text{normalized ensemble measure}\to\rho_W.}
\tag{5.3}
\]

---

## 6. Candidate information potentials

The exact structure suggests several distinct potentials, each with a different type:

\[
\Phi_{\rm Berg}(x)=\log B_q(x,x),
\]
\[
\Phi_{\rm det}(W)=\log\det(T_W+\varepsilon I),
\]
\[
S_{\rm mix}(W)=-\operatorname{Tr}(\rho_W\log\rho_W),
\]
\[
S_{\rm count}(q)=\log\dim H^0(X,K_X^q).
\]
No equality among these is asserted. A future FCIG variational principle must specify which space is being differentiated and which coarse-graining operation defines entropy.

---

## 7. Gate status

\[
\boxed{\textbf{OIG-A1: PASS — exact operator-valued coherent-state density.}}
\]
\[
\boxed{\textbf{OIG-A2: PASS — normalized pure-state/projective geometry and entropy firewall.}}
\]
\[
\boxed{\textbf{OIG-B1: OPEN — derive a canonical FCIG variational functional coupling }\rho_W\textbf{, Quillen/Bergman data, and automorphic orbital sectors.}}
\]

## Claim firewall

- The normalized local coherent state is pure, so its von Neumann entropy vanishes.
- Quantum Fisher/Fubini--Study normalization conventions differ by constant factors; no convention-dependent numerical equality is asserted here.
- \(\log\dim H^0\), \(\log B\), log determinant, and von Neumann entropy are distinct functionals.
- The operator-valued formulation is an exact repackaging of the Bergman/Toeplitz identities; physical interpretation beyond that requires a separately stated model.
- No novelty claim is made without a literature audit.