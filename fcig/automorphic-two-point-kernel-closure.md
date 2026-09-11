# Automorphic Two-Point Kernel Closure

## AM-B — compact Toeplitz multiplicity and closed-geodesic descent

**Status (2026-09-11).**

The automorphic multiplicity firewall shows that a scalar convolution kernel on `G` acts on the representation factor, whereas a generic compact Toeplitz operator acts on the automorphic multiplicity factor. The correct compact object is therefore a two-point automorphic kernel on the quotient.

Within that category the two FCIG outputs coexist exactly:

- the full compact Toeplitz matrix is the operator defined by the two-point kernel;
- the closed-geodesic/Selberg contribution is the conjugacy-class decomposition of its relevant diagonal trace density.

We record

\[
\boxed{\textbf{AM-B1: PASS — exact compact Toeplitz two-point kernel.}}
\]

\[
\boxed{\textbf{AM-B2: PASS — conjugacy-class descent of the weighted Bergman trace to cyclic relative orbitals.}}
\]

A scalar classwise orbital profile does not reconstruct the full multiplicity matrix; that information loss is expected and is not treated as an obstruction.

---

## 1. Compact Bergman projector

Let

\[
X=\Gamma\backslash\mathbb H
\]

be compact and torsion-free, and let

\[
P_{X,q}:L^2(X,K_X^q)\to H^0(X,K_X^q)
\]

be the Bergman projection. Write its integral kernel as

\[
B_{X,q}(x,y): (K_X^q)_y\to(K_X^q)_x.
\]

In a unitary frame the fiber contraction may be represented by a scalar kernel with the usual automorphy phases. On the universal cover, for `q>=2` the compact kernel is represented by the absolutely convergent automorphic/Poincare sum of the universal Bergman kernel; `q=1` requires the standard low-weight convergence care and is kept separate here.

Schematically,

\[
\boxed{
B_{X,q}(x,y)
=
\sum_{\gamma\in\Gamma}
B_{\mathbb H,q}(\tilde x,\gamma\tilde y)\,J_q(\gamma,\tilde y),
}
\tag{1.1}
\]

where the bundle automorphy factor `J_q` is fixed by the canonical `q`-differential action. The right-hand side is independent of the chosen lifts after the covariance factors are included.

---

## 2. Compact Toeplitz kernel

For a smooth scalar symbol `W` on `X`,

\[
T_W^{X,q}=P_{X,q}M_WP_{X,q}.
\]

Its exact two-point kernel is

\[
\boxed{
\mathbb K_W^{X,q}(x,y)
=
\int_X
B_{X,q}(x,z)W(z)B_{X,q}(z,y)\,dA(z).
}
\tag{2.1}
\]

For `s in H^0(X,K_X^q)`,

\[
(T_W^{X,q}s)(x)
=
\int_X\mathbb K_W^{X,q}(x,y)s(y)\,dA(y).
\]

Thus no representation-factor identification is required: the kernel acts directly on

\[
H^0(X,K_X^q)\simeq\mathcal M_q\otimes\ell_q^{\rm low}.
\]

After choosing a unit vector in the lowest-K line, the matrix of (2.1) is exactly the finite-dimensional multiplicity operator

\[
T_W^{X,q}\in\operatorname{End}(\mathcal M_q).
\]

Therefore

\[
\boxed{\textbf{AM-B1: PASS.}}
\]

---

## 3. Trace simplification

Because `P_{X,q}` is an orthogonal projection and the holomorphic space is finite-dimensional,

\[
\operatorname{Tr}T_W^{X,q}
=
\operatorname{Tr}(M_WP_{X,q}).
\]

Hence

\[
\boxed{
\operatorname{Tr}T_W^{X,q}
=
\int_X W(x)B_{X,q}(x,x)\,dA(x).
}
\tag{3.1}
\]

This is the correct scalar shadow of the full multiplicity operator.

Insert the automorphic expansion (1.1):

\[
\operatorname{Tr}T_W^{X,q}
=
\sum_{\gamma\in\Gamma}
\int_{F}
W(x)\,B_{\mathbb H,q}(\tilde x,\gamma\tilde x)
J_q(\gamma,\tilde x)\,dA(\tilde x),
\tag{3.2}
\]

where `F` is a fundamental domain.

The identity term is the local Bergman/Fisher contribution. The nonidentity terms carry global topology.

---

## 4. Conjugacy-class reorganization

Write every nontrivial hyperbolic element as a conjugate of a power of a primitive element:

\[
\gamma=h\delta^mh^{-1},
\qquad m\ge1.
\]

Grouping (3.2) by conjugacy classes and unfolding the sum over

\[
\Gamma_\delta\backslash\Gamma
\]

gives an integral over the primitive cyclic quotient

\[
Y_\delta=\langle\delta\rangle\backslash\mathbb H.
\]

Using the exact transported disk-kernel identity from `disk-transported-bergman.md`,

\[
B_{\mathbb H,q}(x,\delta^mx)J_q(\delta^m,x)
=
C_q\kappa_{q,m\ell}(u),
\]

with

\[
C_q=\frac{2q-1}{4\pi},
\qquad
\kappa_{q,L}(u)
=
\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}.
\]

Therefore the oriented class contribution is exactly

\[
\boxed{
C_q\ell\,\mathcal J_{q,m\ell}[W_\delta]
=
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W_\delta].
}
\tag{4.1}
\]

Thus the weighted compact Bergman trace decomposes as

\[
\boxed{
\operatorname{Tr}T_W^{X,q}
=
\text{identity/local term}
+
\sum_{[\delta]\in\mathcal P_{\rm or}}
\sum_{m\ge1}
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W_\delta],
}
\tag{4.2}
\]

subject to the orientation and convergence conventions already fixed in the cyclic/Sun notes.

Hence

\[
\boxed{\textbf{AM-B2: PASS.}}
\]

---

## 5. The corrected compact FCIG diagram

The compact theory is not

\[
\text{one scalar }f\in\mathcal S(G)
\to
\{\text{Toeplitz matrix},\text{orbital profile}\}.
\]

It is instead

\[
\boxed{
\begin{array}{ccc}
&\mathbb K_W^{X,q}(x,y)&\\[1mm]
\swarrow &&\searrow\\[1mm]
T_W^{X,q}\in\operatorname{End}(\mathcal M_q)
&&
\operatorname{Tr}_{\rm diag/conj}\mathbb K_W^{X,q}
\\[1mm]
&&\downarrow\\[-1mm]
&&\{C_q\ell\mathcal J_{q,m\ell}[W]\}_{[\delta],m}.
\end{array}}
\tag{5.1}
\]

The left leg retains the full multiplicity matrix. The right leg deliberately compresses to scalar conjugacy-class trace data.

Both are exact outputs of the same automorphic two-point kernel.

---

## 6. Relation to the universal representation-side theorem

The universal disk theory remains useful and exact:

- its coherent-state kernel supplies the local building block in (1.1);
- its discrete-series matrix coefficients supply the SAC/Schwartz semiclassical atlas;
- its group Fourier transform lives on \(\mathcal H_{\pi_q}\).

But compact descent changes the operator category. The correct relation is

\[
\boxed{
\text{universal discrete-series kernel}
\xrightarrow{\Gamma\text{-periodization}}
\text{automorphic two-point kernel}
\xrightarrow{\text{lowest-K multiplicity compression}}
T_W^{X,q}.
}
\tag{6.1}
\]

It is not

\[
\widehat f(\pi_q)=T_W^{X,q}.
\]

This is the central correction supplied by AM-A/AM-B.

---

## 7. What scalar orbital data forget

The family

\[
\{\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]\}
\]

consists of scalar traces. It cannot, in general, reconstruct the entire matrix

\[
T_W^{X,q}\in\operatorname{End}(\mathcal M_q).
\]

No contradiction is present: a trace formula is designed to compare traces/spectral sums with conjugacy classes, not to identify every matrix entry of an arbitrary non-equivariant Toeplitz operator.

If one wants matrix-entry-level orbital reconstruction, one must insert automorphic vectors or matrix coefficients and pass to a relative/pre-trace formula with external states. That is a stronger problem.

Define

\[
\boxed{\textbf{AM-C — Matrix-Element Relative Trace Closure.}}
\]

Its target is a two-state kernel pairing whose spectral side contains

\[
\langle s_i,T_W^{X,q}s_j\rangle
\]

and whose geometric side is a corresponding state-decorated conjugacy sum.

---

## 8. Gate ledger

\[
\boxed{\textbf{AM-A1: PASS — automorphic multiplicity identification.}}
\]
\[
\boxed{\textbf{AM-A2: PASS — scalar convolution/multiplicity no-go.}}
\]
\[
\boxed{\textbf{AM-B1: PASS — compact Toeplitz two-point kernel.}}
\]
\[
\boxed{\textbf{AM-B2: PASS — scalar trace descends to cyclic closed-geodesic orbitals.}}
\]
\[
\boxed{\textbf{AM-C: OPEN — state-decorated matrix-element trace formula.}}
\]

## Claim firewall

- AM-B does not identify `End(M_q)` with `End(H_{pi_q})`.
- The Poincare-series statement is asserted in the absolutely convergent high-weight regime (`q>=2`); low weight requires separate convergence treatment.
- The scalar conjugacy-class trace does not determine the full Toeplitz operator.
- Universal matrix-coefficient asymptotics remain local building blocks after periodization; they are not by themselves the compact spectral decomposition.
- The equality in (4.2) is a weighted Bergman/pre-trace decomposition with the previously fixed orientation and centralizer normalization.
- No novelty claim is made for standard automorphic Bergman-kernel periodization or pre-trace unfolding.

## References

1. Standard automorphic kernel / pre-trace formula for cocompact lattices.
2. Standard Bergman-kernel periodization for automorphic forms and holomorphic differentials.
3. A. Borel and N. Wallach, automorphic representations and discrete series.
4. Riemann--Roch for the dimension of `H^0(X,K_X^q)`.
5. FCIG notes `disk-transported-bergman.md`, `cyclic-relative-trace.md`, `automorphic-multiplicity-firewall.md`, and `semiclassical-atlas-closure.md`.