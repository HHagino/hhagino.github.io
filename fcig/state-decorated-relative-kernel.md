# State-Decorated Relative Kernel Closure

## AM-C2 — resolving compact Toeplitz matrix elements without scalarizing too early

**Status (2026-09-11).**

The matrix-element firewall showed that the ordinary scalar Selberg trace cannot recover a generic compact Toeplitz matrix. The correct next object is not another scalar group test function. It is a **state-decorated automorphic two-point distribution**.

We formulate the exact algebraic closure first and isolate the genuinely open geometric step.

\[
\boxed{\textbf{AM-C2a: PASS — complete rank-one probe resolution of the multiplicity operator.}}
\]

\[
\boxed{\textbf{AM-C2b: OPEN — closed-orbit/double-quotient expansion of the decorated probes.}}
\]

---

## 1. Multiplicity-space resolution

Let
\[
\mathcal M_q\simeq H^0(X,K_X^q)
\]
with orthonormal basis \(s_1,\dots,s_d\), where \(d=\dim H^0(X,K_X^q)\). Define matrix units
\[
E_{ji}=|s_j\rangle\langle s_i|.
\]
For any compact Toeplitz operator
\[
T_W=P_qM_WP_q
\]
we have
\[
\boxed{\mathscr T_{ij,q}(W):=\operatorname{Tr}(E_{ji}T_W)=\langle s_i,T_Ws_j\rangle.}
\tag{1.1}
\]
The family \(\{\mathscr T_{ij,q}(W)\}_{i,j}\) is complete:
\[
\boxed{T_W=\sum_{i,j}\mathscr T_{ij,q}(W)E_{ij}.}
\tag{1.2}
\]
Thus no information is lost once the full rank-one probe family is retained.

---

## 2. Exact geometric density

Because \(P_qs_i=s_i\),
\[
\boxed{\mathscr T_{ij,q}(W)=\int_XW(x)\,s_j(x)\overline{s_i(x)}\,dA(x).}
\tag{2.1}
\]
Define the transition density
\[
\rho_{ij,q}(x):=s_j(x)\overline{s_i(x)}.
\]
Then
\[
\boxed{\mathscr T_{ij,q}(W)=\langle W,\rho_{ij,q}\rangle_X.}
\tag{2.2}
\]
For \(i=j\), \(\rho_{ii,q}\) is a state density. For \(i\neq j\), it is a coherent transition density and carries phase information invisible to the ordinary trace.

The scalar Bergman density is recovered by summing diagonal probes:
\[
\boxed{B_{X,q}(x,x)=\sum_i\rho_{ii,q}(x).}
\tag{2.3}
\]
Hence the ordinary trace is the coarse-graining
\[
\boxed{\operatorname{Tr}T_W=\sum_i\mathscr T_{ii,q}(W).}
\tag{2.4}
\]

---

## 3. Operator-valued information density

The basis-dependent matrix of transition densities can be packaged invariantly as
\[
\boxed{\varrho_q(x):=|\mathrm{ev}_x\rangle\langle\mathrm{ev}_x|\in\operatorname{End}(\mathcal M_q),}
\tag{3.1}
\]
where \(\mathrm{ev}_x\) is the evaluation/coherent-state vector under the Bergman identification. Then
\[
\boxed{T_W=\int_XW(x)\,\varrho_q(x)\,dA(x).}
\tag{3.2}
\]
This is the compact operator-valued analogue of the scalar Bergman density. Taking the multiplicity trace gives
\[
\operatorname{Tr}_{\mathcal M_q}\varrho_q(x)=B_{X,q}(x,x).
\tag{3.3}
\]

**Slogan:** scalar Bergman density is the trace of an operator-valued information density.

---

## 4. Why this is the natural FCIG upgrade

The compact FCIG hierarchy is therefore
\[
\boxed{
\varrho_q(x)
\xrightarrow{\int W(\cdot)dA}
T_W
\xrightarrow{\operatorname{Tr}_{\mathcal M_q}}
\operatorname{Tr}T_W
\xrightarrow{\Gamma\text{-unfolding}}
\text{identity}+\text{closed-geodesic sectors}.
}
\tag{4.1}
\]
The first arrow retains the full quantum/information matrix; the second deliberately forgets phase and off-diagonal multiplicity information; the third reorganizes the remaining scalar invariant by conjugacy classes.

This makes the information-loss mechanism explicit rather than treating it as a defect of the trace formula.

---

## 5. Decorated automorphic kernel target

Let \(\widetilde s_i\) denote the automorphic lift of \(s_i\) to the universal cover. The natural noncentral summand attached to \(\gamma\in\Gamma\) is schematically
\[
\boxed{
\mathcal O^{ij}_{\gamma,q}[W]
:=\int_F W(x)\,\widetilde s_j(x)\overline{\widetilde s_i(\gamma x)}\,J_q(\gamma,x)\,dA(x),
}
\tag{5.1}
\]
with the precise automorphy convention fixed by the chosen model of \(K_X^q\).

Unlike the scalar trace summand, this object need not depend only on the conjugacy class of \(\gamma\): the external states transform as well. A conjugacy-invariant geometric object can only be obtained after simultaneously transporting the state labels, or by passing to an appropriate relative/double-quotient distribution.

Thus the correct geometric target is not
\[
[\gamma]\mapsto O_\gamma(f),
\]
but a decorated object of the form
\[
\boxed{(s_i,s_j;\gamma)\mapsto\mathcal O^{ij}_{\gamma,q}[W]}
\tag{5.2}
\]
modulo the natural diagonal \(\Gamma\)-action.

---

## 6. Relative-orbit covariance

Under a change \(\gamma\mapsto\eta\gamma\eta^{-1}\), the corresponding lifted states are transported by the automorphic representation. Therefore the invariant datum is expected to live on an orbit of triples
\[
(s_i,s_j,\gamma)
\]
rather than on a conjugacy class of \(\gamma\) alone.

This suggests the quotient principle
\[
\boxed{
(s_i,s_j,\gamma)
\sim
(R(\eta)s_i,R(\eta)s_j,\eta\gamma\eta^{-1}).
}
\tag{6.1}
\]
The scalar Selberg trace is recovered after contracting the state indices with the identity operator, i.e. summing a complete diagonal family.

---

## 7. Gate split

The algebraic/information-theoretic part is exact:
\[
\boxed{\textbf{AM-C2a: PASS.}}
\]
Rank-one probes resolve the complete multiplicity operator, and the operator-valued density \(\varrho_q(x)\) integrates exactly to \(T_W\).

The remaining geometric problem is:
\[
\boxed{\textbf{AM-C2b: OPEN.}}
\]
Construct a rigorous relative/pre-trace unfolding of the decorated kernel, identify the correct stabilizer/double quotient, and determine whether its hyperbolic pieces admit useful period or closed-geodesic interpretations.

A successful AM-C2b theorem should satisfy three tests:

1. summing diagonal state labels recovers the ordinary scalar Selberg/cyclic trace;
2. retaining all state labels reconstructs \(T_W\);
3. the geometric side is covariant under simultaneous transport of states and conjugacy data.

---

## 8. FCIG interpretation

The operator-valued density provides a sharper information-geometric reading:
\[
\boxed{
\text{local point }x
\longmapsto
\varrho_q(x)
\longmapsto
\text{global Toeplitz response }T_W.
}
\]
The scalar Fisher/Bergman density is obtained only after taking a trace. Thus, before scalarization, FCIG naturally carries a matrix-valued information field on the automorphic multiplicity bundle.

This suggests that the genuinely noncommutative extension of FCIG is not obtained by forcing a scalar entropy functional to encode all state data, but by retaining \(\operatorname{End}(\mathcal M_q)\)-valued local information until the final observable is chosen.

## Claim firewall

- Equation (5.1) is a target schematic form; exact cocycle placement depends on the automorphic convention and is not claimed here as a completed relative trace formula.
- AM-C2a is finite-dimensional linear algebra plus the exact Toeplitz/Bergman coherent-state identity.
- AM-C2b remains open and requires a genuine relative/pre-trace derivation.
- Closed geodesics encode the scalar trace shadow automatically; recovering individual matrix entries requires decorated probes.
- No novelty claim is made without a literature audit.