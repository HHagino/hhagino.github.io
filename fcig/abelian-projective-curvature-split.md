# Abelian / Projective Curvature Split

## OIG-C3 — determinant U(1) versus projective information transport

**Status (2026-09-11).**

The direct-image bundle carries both determinant-line and projective-state geometry. They are complementary components of one unitary connection and must not be identified.

We record
\[
\boxed{\textbf{OIG-C3a: PASS — exact U(1)/projective curvature decomposition.}}
\]
The explicit high-\(q\) asymptotics of the full traceless curvature remain open:
\[
\boxed{\textbf{OIG-C3b: OPEN.}}
\]

---

## 1. Curvature decomposition

Let
\[
E_q=\pi_*K_{\mathcal X/B}^q
\]
have rank \(d_q\), Hermitian metric, and Chern curvature
\[
F_q\in\Omega^{1,1}(B,\operatorname{End}E_q).
\]
Decompose
\[
\boxed{
F_q
=\frac1{d_q}(\operatorname{Tr}F_q)I+F_q^{\circ},
\qquad
\operatorname{Tr}F_q^{\circ}=0.
}
\tag{1.1}
\]
This is the orthogonal Lie-algebra splitting
\[
\mathfrak u(d_q)=\mathfrak u(1)\oplus\mathfrak{su}(d_q)
\]
(up to the usual central quotient at group level).

---

## 2. Determinant channel

For the \(L^2\) determinant line,
\[
\boxed{
F_{\det E_q}=\operatorname{Tr}F_q.
}
\tag{2.1}
\]
The Quillen metric changes this scalar determinant-line connection by the analytic-torsion correction described in `quillen-refinement.md`:
\[
F_Q
=\operatorname{Tr}F_q-\partial\bar\partial\mathcal T_q
\tag{2.2}
\]
in the project convention.

Thus Quillen/WP geometry belongs to the abelian determinant channel.

---

## 3. Projective channel

The connection induced on the projective bundle \(\mathbb P(E_q)\) forgets scalar multiples of the identity. Its curvature is therefore represented by the class of \(F_q\) in
\[
\operatorname{End}(E_q)/\mathbb C I,
\]
or, after choosing the Hermitian trace splitting, by
\[
\boxed{F_q^{\circ}.}
\tag{3.1}
\]
Hence the projective coherent-state geometry and Chern--Fisher/Grassmannian information geometry depend on the noncentral curvature channel rather than on determinant curvature alone.

---

## 4. Density-operator curvature sees only the projective part

For any endomorphism-valued state \(\rho\),
\[
(\nabla^{\rm End})^2\rho=[F_q,\rho].
\]
Because the scalar part commutes with every endomorphism,
\[
\boxed{
(\nabla^{\rm End})^2\rho
=[F_q^{\circ},\rho].
}
\tag{4.1}
\]
Thus the determinant/U(1) curvature is invisible to the commutator transport of the normalized information state.

This gives an exact no-identification theorem:
\[
\boxed{
\text{determinant/Quillen curvature}
\neq
\text{projective density-state curvature}.
}
\tag{4.2}
\]
They are complementary outputs of the same direct-image connection architecture.

---

## 5. Relation to Chern--Fisher and Grassmannian geometry

The Chern--Fisher construction differentiates a state/subspace covariantly and projects out the ray/tangential component. This is inherently projective. The Grassmannian second-fundamental-form metric similarly measures motion of the subspace rather than its determinant phase.

Therefore the chain is
\[
\boxed{
F_q^{\circ}
\longrightarrow
\text{projective/Grassmannian holonomy}
\longrightarrow
\text{Chern--Fisher / quantum-information response},
}
\tag{5.1}
\]
whereas
\[
\boxed{
\operatorname{Tr}F_q
\longrightarrow
\det E_q
\longrightarrow
\text{Quillen/torsion/WP determinant response}.
}
\tag{5.2}
\]
The two channels may share the same Kodaira--Spencer source geometry without being equal tensors.

---

## 6. FCIG curvature pair

The natural curvature datum before any scalarization is therefore the pair
\[
\boxed{
\mathfrak F_q^{\rm FCIG}
:=\left(F_Q,\;F_q^{\circ}\right).
}
\tag{6.1}
\]
The first component is determinant-line/abelian and includes analytic torsion; the second is projective/nonabelian and controls operator-state holonomy.

This is a mathematically cleaner replacement for trying to force all information into one scalar curvature.

---

## 7. High-power information already known

Existing FCIG notes control several traces/quadratic contractions of the direct-image geometry at large \(q\):

- the traced Kodaira--Spencer resolvent channel tends to a multiple of the Weil--Petersson metric;
- the Grassmannian/Chern--Fisher metric has the same leading WP scaling in the chosen connection model;
- Quillen determinant curvature is exactly proportional to WP with the Mumford polynomial coefficient.

These results constrain contractions of the two channels but do **not** yet determine the full matrix-valued tensor \(F_q^{\circ}\).

---

## 8. Remaining sharp target

The next matrix-valued problem is to obtain an asymptotic expansion
\[
\boxed{
F_q^{\circ}
\sim q^{a_0}\mathcal F_0^{\circ}
+q^{a_1}\mathcal F_1^{\circ}+\cdots
}
\tag{8.1}
\]
in a natural trivialization/connection model, with explicit control of its action on coherent states and Toeplitz density operators.

A useful weaker target is to estimate gauge-invariant contractions such as
\[
\operatorname{Tr}(F_q^{\circ}F_q^{\circ *}),
\qquad
\operatorname{Tr}(\rho_WF_q^{\circ}),
\qquad
\operatorname{Tr}([F_q^{\circ},\rho_W]^*[F_q^{\circ},\rho_W]).
\tag{8.2}
\]
These retain projective information while remaining scalar observables on the base.

---

## 9. Gate ledger

\[
\boxed{\textbf{OIG-C3a: PASS — exact determinant/projective split.}}
\]
\[
\boxed{\textbf{OIG-C3b: OPEN — explicit full traceless-curvature asymptotics.}}
\]
\[
\boxed{\textbf{OIG-C3c: OPEN — relation of projective curvature invariants to state-decorated closed-orbit data.}}
\]

## Claim firewall

- The determinant trace and projective curvature are complementary pieces, not two normalizations of one scalar.
- Quillen torsion modifies the determinant-line metric/connection; it does not define a lift back to a unique connection on \(E_q\).
- The Chern--Fisher and Grassmannian metrics are projective response tensors, not identical to \(F_q^{\circ}\) itself.
- Known WP limits of traces/contractions do not determine the full matrix-valued curvature.
- No novelty claim is made without a separate literature audit.