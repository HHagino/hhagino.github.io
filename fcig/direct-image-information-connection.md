# Direct-Image Information Connection

## OIG-C — matrix-valued moduli transport before determinant abelianization

**Status (2026-09-11).**

The canonical information deficit lives in the automorphic multiplicity/direct-image space, while the Quillen metric lives on its determinant line. This note separates those levels and gives the exact covariant derivative of the FCIG mixed state.

We record
\[
\boxed{\textbf{OIG-C1: PASS — exact direct-image covariant transport of }\rho_W.}
\]
\[
\boxed{\textbf{OIG-C2: PASS WITH NO-GO — determinant/Quillen data alone do not determine the full operator-valued transport.}}
\]

---

## 1. Direct-image bundle

Let
\[
\pi:\mathcal X\to B
\]
be a smooth family of compact curves and, for \(q\ge2\), set
\[
\boxed{E_q:=\pi_*K_{\mathcal X/B}^q.}
\tag{1.1}
\]
Its fiber is
\[
(E_q)_b=H^0(X_b,K_{X_b}^q).
\]
On a fixed-genus family its rank is constant:
\[
\operatorname{rk}E_q=(2q-1)(g-1).
\]
The fiberwise \(L^2\) metric defines a Chern connection
\[
\nabla^{E_q}.
\]
It induces the endomorphism connection
\[
\boxed{
\nabla^{\rm End}A
=\nabla^{E_q}\circ A-A\circ\nabla^{E_q}
}
\tag{1.2}
\]
on \(\operatorname{End}(E_q)\).

---

## 2. Toeplitz and density-operator fields

Let \(W_b\) be a smooth family of nonnegative symbols. Define
\[
T_W(b)=P_{q,b}M_{W_b}P_{q,b}
\in\operatorname{End}(E_{q,b}),
\tag{2.1}
\]
\[
Z_W(b)=\operatorname{Tr}T_W(b),
\tag{2.2}
\]
and
\[
\rho_W(b)=\frac{T_W(b)}{Z_W(b)}.
\tag{2.3}
\]
Then \(\rho_W\) is a smooth section of \(\operatorname{End}(E_q)\) wherever \(Z_W>0\).

---

## 3. Exact covariant derivative

Using the induced connection and the scalar derivative of \(Z_W\),
\[
\boxed{
\nabla^{\rm End}\rho_W
=
\frac{\nabla^{\rm End}T_W}{Z_W}
-\rho_W\,d\log Z_W.
}
\tag{3.1}
\]
Because the trace is connection-compatible,
\[
dZ_W=\operatorname{Tr}(\nabla^{\rm End}T_W),
\tag{3.2}
\]
so
\[
\boxed{
\operatorname{Tr}(\nabla^{\rm End}\rho_W)=0.
}
\tag{3.3}
\]
Thus the normalized state moves in the affine hyperplane of trace-one endomorphisms.

This is the natural moduli-covariant replacement for an ordinary derivative of a density matrix whose Hilbert space itself varies with \(b\).

---

## 4. Curvature action on the state

The induced curvature acts by commutator:
\[
\boxed{
(\nabla^{\rm End})^2A
=[F_{E_q},A].
}
\tag{4.1}
\]
Hence
\[
\boxed{
(\nabla^{\rm End})^2\rho_W
=[F_{E_q},\rho_W].
}
\tag{4.2}
\]
The noncommuting part of the direct-image curvature therefore controls holonomy/transport of the operator-valued information state.

If \(F_{E_q}\) were purely scalar, \(F_{E_q}=\omega I\), then the commutator would vanish; in general there is no reason for this to hold.

---

## 5. Determinant line and abelianization

The determinant line is
\[
\lambda_q=\det E_q.
\]
For the determinant of the \(L^2\) Chern connection,
\[
\boxed{
F_{\det E_q}=\operatorname{Tr}F_{E_q}.
}
\tag{5.1}
\]
Thus passage from \(E_q\) to \(\det E_q\) keeps only the trace/U(1) part of the curvature.

The Quillen metric modifies the determinant-line metric by analytic torsion. In the convention of `quillen-refinement.md`,
\[
F_Q
=F_{L^2,\det}-\partial\bar\partial\mathcal T_q.
\tag{5.2}
\]
Therefore Quillen geometry is still determinant-line/abelian data: it refines the scalar determinant connection but does not reconstruct the traceless matrix part of \(F_{E_q}\).

---

## 6. Determinant no-go

Suppose two direct-image connections have curvatures
\[
F_{E_q},\qquad F'_{E_q}=F_{E_q}+\Omega,
\]
where
\[
\operatorname{Tr}\Omega=0.
\]
Then they induce the same determinant curvature, but in general
\[
[\Omega,\rho_W]\ne0.
\]
Hence the operator-state transport changes while determinant curvature does not.

Therefore
\[
\boxed{
\text{Quillen/determinant curvature}
\not\Rightarrow
\text{full }\operatorname{End}(E_q)\text{-valued information transport}.
}
\tag{6.1}
\]
This is the direct-image version of the earlier FCIG principle
\[
\text{determinant }U(1)\neq\text{full structure-group connection}.
\]

We record
\[
\boxed{\textbf{OIG-C2: PASS WITH NO-GO.}}
\]

---

## 7. Covariant state-sector information geometry

The normalized state family allows connection-covariant information tensors on moduli. For example, on the full-rank locus one may form the Bogoliubov/Kubo--Mori type quadratic form schematically from
\[
\nabla_i\rho_W
\]
and the operator logarithm. Likewise, for pure coherent-state rays the projective Fubini--Study/quantum-Fisher tensor is obtained before taking the determinant trace.

The important structural rule is
\[
\boxed{
\text{matrix-valued state geometry lives on }E_q;
\qquad
\text{Quillen geometry lives on }\det E_q.
}
\tag{7.1}
\]
They interact but are not interchangeable.

---

## 8. Corrected coupling target

A well-typed future coupling should involve both
\[
(E_q,h_{L^2},\nabla^{E_q},\rho_W)
\]
and
\[
(\lambda_q,h_Q,\nabla^Q).
\]
A schematic scalar functional may depend on invariants such as
\[
D(\rho_W\Vert I/d_q),
\qquad
\operatorname{Tr}(F_{E_q}\rho_W),
\qquad
\log h_Q,
\]
but coefficients and contraction rules are additional constitutive choices.

The determinant line cannot supply them uniquely.

---

## 9. Gate ledger

\[
\boxed{\textbf{OIG-C1: PASS — direct-image covariant density-operator transport.}}
\]
\[
\boxed{\textbf{OIG-C2: PASS WITH NO-GO — Quillen determinant does not determine full matrix transport.}}
\]
\[
\boxed{\textbf{OIG-C3: OPEN — compute/characterize the traceless direct-image curvature in the FCIG hyperbolic model and relate it to state-decorated orbital data.}}
\]

## Claim firewall

- `E_q` and `det E_q` are different geometric objects.
- The Quillen correction refines determinant-line geometry; it does not restore information discarded by the determinant functor.
- Equation (4.2) is a standard induced-connection identity, not a dynamical equation.
- Any physical coupling between matrix curvature, entropy, and orbital sectors requires extra constitutive input.
- No novelty claim is made without a literature audit.