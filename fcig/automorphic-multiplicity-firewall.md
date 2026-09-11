# Automorphic Multiplicity Firewall

## AM-A — compact holomorphic q-differentials versus the universal discrete series

**Status (2026-09-11).**

This note corrects a type ambiguity that becomes visible only after the compact quotient is inserted explicitly.

Let

\[
X=\Gamma\backslash\mathbb H,
\qquad
G=PSL(2,\mathbb R),
\qquad
\pi_q=D^+_{2q-1}.
\]

The universal holomorphic discrete-series Hilbert space \(\mathcal H_{\pi_q}\) and the compact vector space \(H^0(X,K_X^q)\) are **not the same representation space**. The compact space is the automorphic multiplicity space, tensored with the one-dimensional lowest-\(K\)-type line.

We record

\[
\boxed{\textbf{AM-A1: PASS — automorphic multiplicity identification.}}
\]

and a structural obstruction:

\[
\boxed{\textbf{AM-A2: PASS — scalar group convolution cannot realize a generic compact Toeplitz matrix on the multiplicity factor.}}
\]

---

## 1. Automorphic decomposition

Because \(\Gamma\backslash G\) is compact, the right regular representation decomposes discretely:

\[
\boxed{
L^2(\Gamma\backslash G)
\simeq
\widehat\bigoplus_{\pi\in\widehat G}
\mathcal M_\pi\widehat\otimes\mathcal H_\pi,
}
\tag{1.1}
\]

where

\[
\mathcal M_\pi:=\operatorname{Hom}_G(\mathcal H_\pi,L^2(\Gamma\backslash G))
\]

is finite-dimensional.

For the holomorphic discrete series \(\pi_q\), let

\[
\ell_q^{\rm low}\subset\mathcal H_{\pi_q}
\]

be its one-dimensional lowest-\(K\)-type line. With the FCIG convention, this is the \(K\)-weight corresponding to holomorphic \(q\)-differentials; reversing holomorphic/antiholomorphic conventions replaces \(\pi_q\) by its contragredient.

The automorphic realization of holomorphic \(q\)-differentials is

\[
\boxed{
H^0(X,K_X^q)
\simeq
\mathcal M_q\otimes\ell_q^{\rm low},
\qquad
\mathcal M_q:=\mathcal M_{\pi_q}.
}
\tag{1.2}
\]

After choosing a unit vector in \(\ell_q^{\rm low}\), this gives a noncanonical scalar trivialization

\[
H^0(X,K_X^q)\simeq\mathcal M_q.
\tag{1.3}
\]

The invariant content is (1.2), not the chosen trivialization.

---

## 2. Multiplicity dimension

For a compact Riemann surface of genus \(g\ge2\), Riemann--Roch gives

\[
\boxed{
\dim H^0(X,K_X)=g,
}
\tag{2.1}
\]

and for \(q\ge2\), since \(\deg K_X^q=2q(g-1)>2g-2\),

\[
H^1(X,K_X^q)=0
\]

and therefore

\[
\boxed{
\dim H^0(X,K_X^q)
=(2q-1)(g-1).
}
\tag{2.2}
\]

Consequently

\[
\boxed{
\dim\mathcal M_q=
\begin{cases}
g,&q=1,\\
(2q-1)(g-1),&q\ge2.
\end{cases}}
\tag{2.3}
\]

Thus the compact holomorphic dimension is the automorphic multiplicity of the relevant holomorphic discrete series, not the dimension of \(\mathcal H_{\pi_q}\), which is infinite.

---

## 3. Where compact Toeplitz operators live

Let

\[
P_{X,q}:L^2(X,K_X^q)\to H^0(X,K_X^q)
\]

be the compact Bergman projection and

\[
T^{X,q}_W=P_{X,q}M_WP_{X,q}.
\]

Under (1.2),

\[
\boxed{
T^{X,q}_W
\in
\operatorname{End}(\mathcal M_q\otimes\ell_q^{\rm low})
\simeq
\operatorname{End}(\mathcal M_q).
}
\tag{3.1}
\]

So a generic compact Toeplitz operator moves the **multiplicity coordinate**.

This is categorically different from the universal-cover Toeplitz operator

\[
T^{\rm univ,q}_W
\in\operatorname{End}(\mathcal H_{\pi_q}),
\]

constructed from the disk Bergman space. The two symbols may be related by periodization/descent, but the operators act on different factors.

---

## 4. Convolution acts on the opposite tensor factor

Let \(R(f)\) denote right convolution by a group test function \(f\). On the \(\pi_q\)-isotypic summand,

\[
\boxed{
R(f)|_{\mathcal M_q\otimes\mathcal H_{\pi_q}}
=
I_{\mathcal M_q}\otimes\pi_q(f),
}
\tag{4.1}
\]

up to the harmless convention swap between left/right regular actions.

Compressing to the lowest-\(K\)-type line gives

\[
\boxed{
(I\otimes p_{\rm low})R(f)(I\otimes p_{\rm low})
=
\langle e_0,\pi_q(f)e_0\rangle
I_{\mathcal M_q}\otimes p_{\rm low}.
}
\tag{4.2}
\]

Therefore a scalar convolution kernel can induce only a scalar multiple of the identity on the compact multiplicity space.

For generic \(W\),

\[
T^{X,q}_W\notin\mathbb C\,I_{\mathcal M_q}.
\]

Hence

\[
\boxed{
\text{generic compact }T^{X,q}_W
\text{ cannot equal the lowest-K compression of }\pi_q(f)
\text{ for a scalar group convolution kernel }f.
}
\tag{4.3}
\]

This is a representation-theoretic obstruction, not a lack of a clever choice of \(f\).

---

## 5. Correction to earlier FCIG wording

Earlier universal-cover notes proved a valid statement of the form

\[
\widehat f(\pi_q)=A
\]

for smoothing operators \(A\in\operatorname{End}(\mathcal H_{\pi_q})\), together with prescribed regular hyperbolic orbital data.

That theorem remains valid **on the universal discrete-series factor**.

What must not be inferred is

\[
A=T_W^{X,q}
\]

for a compact quotient Toeplitz operator merely because \(T_W^{X,q}\) is finite-dimensional.

Finite rank does not fix the tensor-factor mismatch.

Thus the statement

> “fixed \(q\) compact Toeplitz is finite rank, hence it is automatically covered by the universal finite-rank interpolation theorem”

is withdrawn unless an additional automorphic kernel identifies the multiplicity operator with the relevant two-point quotient kernel.

---

## 6. Correct next object: an automorphic two-point kernel

A general operator on \(L^2(\Gamma\backslash G)\) is represented by a kernel

\[
\mathbb K(\Gamma g,\Gamma h),
\]

not necessarily by convolution \(k(g^{-1}h)\).

For the compact Toeplitz operator, its exact kernel is

\[
\boxed{
\mathbb K^{X,q}_W(x,y)
=
\int_X B_{X,q}(x,z)\,W(z)\,B_{X,q}(z,y)\,dA(z),
}
\tag{6.1}
\]

where \(B_{X,q}\) is the compact Bergman kernel.

This two-point kernel can act nontrivially on \(\mathcal M_q\). It is therefore the correct category in which to seek simultaneous compact Toeplitz and closed-geodesic/Selberg information.

The new gate is

\[
\boxed{
\textbf{AM-B — Automorphic Two-Point Kernel Closure.}
}
\]

Construct the lifted \(\Gamma\times\Gamma\)-equivariant kernel, decompose its diagonal by conjugacy classes, and identify its \(\pi_q\)-isotypic multiplicity block with \(T_W^{X,q}\).

---

## 7. Gate ledger

\[
\boxed{\textbf{AM-A1: PASS — }H^0(X,K^q)\textbf{ is the lowest-K automorphic multiplicity space.}}
\]

\[
\boxed{\textbf{AM-A2: PASS — scalar convolution has the wrong tensor-factor action for generic compact Toeplitz operators.}}
\]

\[
\boxed{\textbf{AM-B: OPEN — automorphic two-point kernel / Selberg descent.}}
\]

## Claim firewall

- \(H^0(X,K_X^q)\neq\mathcal H_{\pi_q}\).
- The equality is with the lowest-\(K\)-type part of the automorphic multiplicity summand, not with the universal representation Hilbert space.
- Group convolution and multiplication/Toeplitz compression act in different operator categories.
- The universal smoothing interpolation theorem remains correct on \(\mathcal H_{\pi_q}\); its direct application to compact Toeplitz matrices is what is rejected.
- Holomorphic versus antiholomorphic discrete-series notation depends on the chosen right/left action convention; only the lowest-\(K\)-type statement is invariant here.
- No novelty claim is made for the standard automorphic decomposition or Riemann--Roch dimension formula.

## References

1. Standard automorphic spectral decomposition for cocompact lattices in \(PSL(2,\mathbb R)\).
2. A. Borel and N. Wallach, *Continuous Cohomology, Discrete Subgroups, and Representations of Reductive Groups*.
3. A. W. Knapp, *Representation Theory of Semisimple Groups* — holomorphic discrete series and lowest \(K\)-types.
4. Standard Riemann--Roch theorem for compact Riemann surfaces.
5. FCIG notes `typed-orbital-fourier-closure.md`, `schwartz-completion.md`, and `disk-transported-bergman.md`.