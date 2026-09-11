# Matrix-Element / Trace Firewall

## AM-C — what the scalar Selberg shadow can and cannot recover

**Status (2026-09-11).**

The compact two-point-kernel closure raises a natural question: can the closed-geodesic scalar data reconstruct the full Toeplitz matrix

\[
T_W^{X,q}\in\operatorname{End}(H^0(X,K_X^q))?
\]

The answer is **not in general**. This is not a missing estimate; it is a distinction between operator matrix elements and conjugacy-invariant traces.

We record

\[
\boxed{\textbf{AM-C1: PASS — exact matrix-element formula and trace-information firewall.}}
\]

A stronger state-decorated relative trace formula is a different problem:

\[
\boxed{\textbf{AM-C2: OPEN — state-decorated/double-quotient geometric expansion.}}
\]

---

## 1. Exact compact matrix element

Let

\[
s_i,s_j\in H^0(X,K_X^q)
\]

and

\[
T_W^{X,q}=P_{X,q}M_WP_{X,q}.
\]

Since the Bergman projection is the identity on holomorphic states,

\[
\boxed{
\langle s_i,T_W^{X,q}s_j\rangle
=
\int_X
W(x)\,\langle s_i(x),s_j(x)\rangle_{K_X^q}\,dA(x).
}
\tag{1.1}
\]

Thus every matrix entry is already an exact automorphic integral.

Under

\[
H^0(X,K_X^q)\simeq\mathcal M_q\otimes\ell_q^{\rm low},
\]

these are precisely the matrix entries of the multiplicity operator.

---

## 2. Rank-one trace formulation

Let

\[
E_{ji}=|s_j\rangle\langle s_i|.
\]

Then

\[
\boxed{
\langle s_i,T_W^{X,q}s_j\rangle
=\operatorname{Tr}(E_{ji}T_W^{X,q}).
}
\tag{2.1}
\]

This looks formally like a trace, but the rank-one insertion \(E_{ji}\) is not invariant under the regular group action in general. Therefore the ordinary Selberg trace mechanism does not turn (2.1) into the same scalar conjugacy-class distribution that appears for \(\operatorname{Tr}T_W^{X,q}\).

The external states carry noncentral automorphic information.

---

## 3. Why conjugacy classes appear for the ordinary trace

For the scalar trace,

\[
\operatorname{Tr}T_W^{X,q}
=
\int_XW(x)B_{X,q}(x,x)dA(x).
\]

The diagonal \(x=y\) permits the automorphic kernel sum

\[
B_{X,q}(x,x)
=
\sum_{\gamma\in\Gamma}
B_{\mathbb H,q}(\tilde x,\gamma\tilde x)J_q(\gamma,\tilde x)
\]

to be grouped by conjugacy classes. This is what produces primitive closed geodesics and centralizer quotients.

For a fixed matrix entry, the two external states distinguish source and target data. The corresponding geometric object is no longer a scalar class function of \(\gamma\).

Hence

\[
\boxed{
\text{conjugacy-class compression is trace-level information loss.}
}
\tag{3.1}
\]

---

## 4. Dimension count makes the loss unavoidable

Let

\[
d_q^X:=\dim H^0(X,K_X^q).
\]

The full Toeplitz operator has

\[
(d_q^X)^2
\]

complex matrix coordinates before self-adjoint/symbol restrictions are imposed. The ordinary trace provides one scalar for each chosen symbol \(W\), and the classwise decomposition provides scalar orbital contributions indexed by conjugacy data.

There is no general injectivity theorem from these scalar trace shadows to the full matrix algebra

\[
\operatorname{End}(H^0(X,K_X^q)).
\]

Therefore FCIG should not demand one unless additional families of probes are inserted.

---

## 5. Correct state-decorated target

If matrix-level geometric reconstruction is desired, introduce external automorphic states or rank-one probes before tracing. A model quantity is

\[
\boxed{
\mathscr T_{ij,q}[W;K]
:=
\operatorname{Tr}
\left(E_{ji}\,\mathcal K_W^{X,q}\right)
=
\langle s_i,T_W^{X,q}s_j\rangle.
}
\tag{5.1}
\]

A geometric expansion of such quantities will generally involve state-decorated kernels, matrix coefficients, periods, or double-quotient orbital integrals rather than the undeformed scalar Selberg conjugacy distribution.

This motivates

\[
\boxed{\textbf{AM-C2 — State-Decorated Relative Trace Closure.}}
\]

The target is to identify a natural family of external-state periods whose spectral side resolves \(\operatorname{End}(\mathcal M_q)\) and whose geometric side retains interpretable closed-orbit data.

---

## 6. FCIG architecture after the firewall

The compact branch is now

\[
\boxed{
\mathbb K_W^{X,q}
\longrightarrow
\begin{cases}
T_W^{X,q}&\text{full multiplicity operator},\\
\operatorname{Tr}T_W^{X,q}&\text{scalar trace},\\
\{C_q\ell\mathcal J_{q,m\ell}[W]\}&\text{closed-geodesic decomposition of the trace}.
\end{cases}}
\]

These outputs are compatible but contain different amounts of information.

The slogan is:

\[
\boxed{
\textbf{two-point kernel remembers the matrix; diagonal conjugacy trace remembers its Selberg shadow.}
}
\]

---

## 7. Gate ledger

\[
\boxed{\textbf{AM-C1: PASS — exact matrix-element formula and noninjectivity firewall.}}
\]

\[
\boxed{\textbf{AM-C2: OPEN — state-decorated relative/pre-trace theory.}}
\]

## Claim firewall

- The statement is not that matrix entries have no geometric expansion; it is that they are not encoded by the same scalar conjugacy trace without additional probes.
- Rank-one insertion turns an ordinary trace into a matrix element but destroys the central invariance needed for the scalar Selberg class expansion.
- A future relative trace formula may recover matrix-level data using external states or subgroup periods.
- No novelty claim is made for the elementary Toeplitz matrix-element identity or the general distinction between pre-trace and trace formulas.