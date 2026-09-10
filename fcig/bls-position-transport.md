# FCIG: BLS Position Transport and Intrinsic Bergman-DPP Fisher Closure

**Status:** exact ambient transport theorem + exact compression-defect theorem + local KE/BLS Hermitian Fisher closure + high-power WP corollary  
**Date:** 2026-09-10  
**Scope:** BLS Hilbert fields, Kähler--Einstein horizontal lift, position observables, Bergman compression, Slater determinants, determinantal point processes, Fisher information, and Weil--Petersson asymptotics.  
**Depends on:** [`hermitian-born-fisher.md`](hermitian-born-fisher.md), [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md), [`kodaira-spencer-information.md`](kodaira-spencer-information.md).

> **Claim policy.** **Established** means a cited theorem/construction. **Derived here** means a deduction from those constructions written explicitly below; it is not a literature-novelty claim. **No-go** records a genuine obstruction. **Interpretation** is project language. **Open** marks what remains after the transport problem is resolved.
>
> Dedicated bibliography: [`bls-position-transport.bib`](bls-position-transport.bib). Citation audit: [`bls-position-transport-citation-audit.md`](bls-position-transport-citation-audit.md).

---

## 0. Result in one page

The moving-fiber difficulty in the previous notes was real: a classical Fisher metric is not defined until probability spaces on neighboring fibers are identified. The key correction is that two different objects had been conflated:

1. the **ambient position measurement** on the full fiberwise \(L^2\) space;
2. its **Bergman compression** to the finite-dimensional holomorphic subspace.

They have different transport behavior.

Let

\[
p:\mathcal X\to B
\]

be a proper holomorphic submersion, let \((E,h)\to\mathcal X\) be Hermitian holomorphic, and choose a horizontal distribution \(\theta\). Write

\[
\mathscr L_t
=
L^2(X_t,K_{X_t}\otimes E_t)
\]

for the ambient fiberwise Hilbert field and

\[
\mathscr H_t
=
H^0(X_t,K_{X_t}\otimes E_t)
\subset\mathscr L_t
\]

for the holomorphic subfield. Varolin's BLS construction equips \(\mathscr L\) with a Chern-type connection induced by twisted Lie derivatives along horizontal lifts, and when \(\mathscr H\) is locally trivial its Chern connection is the orthogonal projection of the ambient one [Var24].

For a smooth function \(\varphi\) on \(\mathcal X\), let

\[
M_t(\varphi)u=\varphi|_{X_t}\,u
\]

be the ambient multiplication operator. If \(V_X^\theta\) denotes the real horizontal lift of a real base vector \(X\), then the twisted-Lie Leibniz rule gives the exact operator identity

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr L}M(\varphi)
=
M(V_X^\theta\varphi).
}
\tag{0.1}
\]

Hence a position observable advected by the horizontal flow,

\[
V_X^\theta\varphi=0,
\]

is exactly parallel:

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr L}M(\varphi)=0.
}
\tag{0.2}
\]

Thus the **ambient position PVM is covariantly constant under the BLS transport induced by the same horizontal flow**.

Now let \(P_t:\mathscr L_t\to\mathscr H_t\) be the Bergman projection, \(Q=1-P\), and define the second fundamental form

\[
\mathbb B_X
:=
Q\nabla_X^{\mathscr L}|_{\mathscr H}.
\tag{0.3}
\]

The compressed Toeplitz observable is

\[
T_\varphi=P M_\varphi P|_{\mathscr H}.
\]

Even when \(M_\varphi\) is ambient-parallel,

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr H}T_\varphi
=
\mathbb B_X^*Q M_\varphi P
+
P M_\varphi Q\mathbb B_X.
}
\tag{0.4}
\]

Therefore the Bergman-compressed position observable is **not generally parallel**. Its failure is controlled by exactly the same second fundamental form whose Hilbert--Schmidt norm is the Grassmannian/Slater information metric.

This resolves the apparent contradiction in the earlier FCIG formulation. A Bergman DPP is obtained by putting a Slater state in the ambient many-body \(L^2\) space and applying the ordinary position measurement. It does **not** require treating the compressed one-particle Toeplitz POVM as the fundamental measurement.

For a hyperbolic curve family of genus \(g\ge2\), choose the Kähler--Einstein horizontal lift \(\theta_{KE}\), and set

\[
E=K_{\mathcal X/B}^{q-1},
\qquad
\mathscr H_{q,t}=H^0(X_t,K_{X_t}^q),
\qquad q\ge2.
\]

The KE lift gives the harmonic Kodaira--Spencer representative [Sch12], while the BLS connection gives the ambient covariant realization [Var24]. Locally on the base, the determinant/Slater line of \(\mathscr H_q\) is projectively holomorphic, and the ambient \(N_q\)-particle position measurement is parallel under the induced product transport. Therefore the exact Hermitian Born--Fisher theorem applies in this local covariant realization:

\[
\boxed{
I_{q}^{KE}(X,Y)
+
I_{q}^{KE}(JX,JY)
=
4g_{\mathrm{Pl},q}^{KE}(X,Y).
}
\tag{0.5}
\]

Here \(I_q^{KE}\) is the classical Fisher tensor of the Bergman DPP after identifying configuration spaces by the KE horizontal flow, and \(g_{\mathrm{Pl},q}^{KE}\) is the projective/Plücker metric of the moving Slater ray.

Using the already-audited minimal-solution/Grassmannian asymptotic

\[
\boxed{
 g_{\mathrm{Pl},q}^{KE}
 =
\frac{q-1}{4\pi}G_{\mathrm{WP}}+O(1),
}
\tag{0.6}
\]

we obtain

\[
\boxed{
I_q^{KE}(X,Y)
+
I_q^{KE}(JX,JY)
=
\frac{q-1}{\pi}G_{\mathrm{WP}}(X,Y)+O(1),
}
\tag{0.7}
\]

and hence

\[
\boxed{
\frac{\pi}{q-1}
\left(I_q^{KE}+J^*I_q^{KE}\right)
\longrightarrow
G_{\mathrm{WP}}.
}
\tag{0.8}
\]

This removes the previous conditional assumption that a **compressed Bergman POVM** itself had to be parallel. The correct parallel object is the ambient position measurement.

Finally, if \(\mathfrak K_q\) denotes the positive Kodaira--Spencer resolvent tensor from the companion note,

\[
\mathfrak K_q
=
\frac{q-1}{4\pi}G_{\mathrm{WP}}+O(1),
\]

then

\[
\boxed{
\frac14\left(I_q^{KE}+J^*I_q^{KE}\right)
-
\mathfrak K_q
=O(1),
}
\tag{0.9}
\]

so after the natural \(4\pi/(q-1)\) normalization the Hermitianized classical Fisher channel and the intrinsic KS resolvent channel have the same Weil--Petersson limit.

---

# Part I. BLS ambient Hilbert field

## 1. Why an ordinary holomorphic ambient Hilbert bundle should not be assumed

For a proper holomorphic family \(p:\mathcal X\to B\), the fibers

\[
\mathscr L_t=L^2(X_t,K_{X_t}\otimes E_t)
\]

form a smooth Hilbert bundle after choosing local differentiable trivializations, but a natural ordinary holomorphic Hilbert-bundle structure need not exist. Berndtsson already emphasized this obstruction in the original direct-image curvature setting [Bern09].

Varolin's BLS formalism is designed precisely for this situation [Var24]. It gives a complex-analytic/Chern-curvature framework for Hilbert fields even when they do not fit together as a conventional holomorphic vector bundle. The finite-dimensional direct-image field

\[
\mathscr H_t=H^0(X_t,K_{X_t}\otimes E_t)
\]

is a BLS holomorphic subfield of \(\mathscr L\), and whenever it is locally trivial its Chern connection is the orthogonal projection of the ambient BLS--Chern connection.

This distinction is a type requirement throughout this note:

\[
\boxed{
\text{ambient BLS Hilbert field}
\neq
\text{assumed ordinary holomorphic Hilbert bundle}.
}
\tag{1.1}
\]

For the hyperbolic \(q\)-differential application with \(q\ge2\), \(H^1(X,K_X^q)=0\), so Riemann--Roch gives constant rank

\[
N_q=h^0(X,K_X^q)=(2q-1)(g-1),
\tag{1.2}
\]

and the finite-dimensional direct image \(\mathscr H_q\) is an ordinary holomorphic vector bundle locally on the smooth base.

---

## 2. Twisted Lie derivative and BLS--Chern connection

Let \(\xi\) be a vector field on \(\mathcal X\), and let \(D\) be the Chern connection of \((E,h)\). The twisted Lie derivative is

\[
\boxed{
\mathcal L^D_\xi u
=
D(\xi\lrcorner u)
+
\xi\lrcorner Du.
}
\tag{2.1}
\]

[Var24]. After choosing a horizontal distribution \(\theta\), a base vector is lifted to \(\xi_X^\theta\), and the BLS connection on the fiberwise \(L^2\) field is induced by the appropriate type components of these twisted Lie derivatives.

If \(D\) is metric, the resulting connection preserves the fiberwise \(L^2\) metric [Var24].

The corresponding pointwise top-form identity is the geometric reason the construction works: the ordinary Lie derivative of the fiberwise Hermitian density is the sum of the two twisted-Lie derivatives acting on the two entries. Integrating gives metric compatibility of the \(L^2\) pairing.

---

# Part II. Ambient position measurement

## 3. Multiplication algebra

For \(\varphi\in C^\infty(\mathcal X)\), define

\[
M_t(\varphi):\mathscr L_t\to\mathscr L_t,
\qquad
M_t(\varphi)u
=\varphi|_{X_t}u.
\tag{3.1}
\]

This is the smooth functional calculus of the fiberwise position observable.

The covariant derivative of an operator field is

\[
(\nabla_X^{\operatorname{End}\mathscr L}A)u
:=
\nabla_X^{\mathscr L}(Au)-A\nabla_X^{\mathscr L}u.
\tag{3.2}
\]

### Theorem 3.1 — exact covariance of multiplication observables

For every real base vector \(X\),

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr L}M(\varphi)
=
M(V_X^\theta\varphi),
}
\tag{3.3}
\]

where \(V_X^\theta\) is the corresponding real horizontal lift.

### Proof

The BLS connection is induced by twisted Lie derivative along the horizontal lift. Since the coefficient connection acts trivially on the scalar \(\varphi\), the twisted Lie derivative obeys the ordinary Leibniz rule

\[
\mathcal L^D_{V_X}(\varphi u)
=(V_X\varphi)u
+\varphi\mathcal L^D_{V_X}u.
\tag{3.4}
\]

Restrict to the fiber and substitute the BLS connection formula. Subtract \(M(\varphi)\nabla_Xu\). The second term cancels, leaving multiplication by \(V_X\varphi\). \(\square\)

**Status:** **Derived here from the established BLS connection formula.** Equation (3.3) is not attributed as a separately named theorem of Varolin.

### Corollary 3.2 — horizontal observables are parallel

If \(\varphi\) is transported by the horizontal flow,

\[
V_X^\theta\varphi=0,
\tag{3.5}
\]

then

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr L}M(\varphi)=0.
}
\tag{3.6}
\]

This gives the correct meaning of a **parallel position measurement** in a moving family.

---

## 4. From smooth observables to the position PVM

Let \(F_{t\leftarrow0}^\theta:X_0\to X_t\) be a local horizontal flow. A Borel set \(A_0\subset X_0\) is transported to

\[
A_t=F_{t\leftarrow0}^\theta(A_0).
\tag{4.1}
\]

The associated multiplication projection is

\[
E_t(A_t)=M_t(\mathbf 1_{A_t}).
\tag{4.2}
\]

The unitary transport generated by the metric BLS connection intertwines these projections:

\[
\boxed{
U_{t\leftarrow0}^\theta
E_0(A_0)
(U_{t\leftarrow0}^\theta)^{-1}
=
E_t(A_t).
}
\tag{4.3}
\]

Locally this follows directly from horizontal pullback plus the coefficient-bundle unitary transport; multiplication by a characteristic function commutes with the latter. Thus the entire ambient position PVM is carried along by the horizontal flow.

**Regularity note.** The differential identity (3.3) is stated for smooth multiplication observables. Equation (4.3) is the corresponding finite-flow statement for Borel projectors. No derivative of a discontinuous characteristic function is required.

---

# Part III. Bergman compression is not parallel

## 5. Direct-image subfield and second fundamental form

Let

\[
P_t:\mathscr L_t\to\mathscr H_t
\]

be the orthogonal Bergman projection and set \(Q_t=1-P_t\). The induced Chern connection on the finite-dimensional direct image is

\[
\boxed{
\nabla_X^{\mathscr H}
=P\nabla_X^{\mathscr L}|_{\mathscr H}.
}
\tag{5.1}
\]

This is the BLS Gauss formula [Var24]. Define

\[
\boxed{
\mathbb B_X
:=Q\nabla_X^{\mathscr L}|_{\mathscr H}.
}
\tag{5.2}
\]

For a metric connection and real \(X\), the off-diagonal derivative of \(P\) has blocks

\[
Q(\nabla_XP)P=\mathbb B_X,
\qquad
P(\nabla_XP)Q=\mathbb B_X^*.
\tag{5.3}
\]

The Hilbert--Schmidt pairing

\[
\operatorname{Tr}(\mathbb B_Y^*\mathbb B_X)
\tag{5.4}
\]

is the Grassmannian/Plücker metric of the moving holomorphic subspace.

---

## 6. Theorem 6.1 — exact compression defect

Define the compressed Toeplitz observable

\[
T_\varphi
=P M_\varphi P|_{\mathscr H}.
\tag{6.1}
\]

Then

\[
\boxed{
\begin{aligned}
\nabla_X^{\operatorname{End}\mathscr H}T_\varphi
={}&
P M(V_X^\theta\varphi)P
\\
&+
\mathbb B_X^*Q M_\varphi P
+
P M_\varphi Q\mathbb B_X.
\end{aligned}
}
\tag{6.2}
\]

In particular, if \(\varphi\) is horizontally advected,

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr H}T_\varphi
=
\mathbb B_X^*Q M_\varphi P
+
P M_\varphi Q\mathbb B_X.
}
\tag{6.3}
\]

### Proof

Differentiate \(P M_\varphi P\) using the ambient connection:

\[
\nabla_X(PMP)
=(\nabla_XP)MP
+P(\nabla_XM)P
+PM(\nabla_XP).
\tag{6.4}
\]

Sandwich by \(P\) to obtain the induced endomorphism derivative on \(\mathscr H\). Since

\[
P(\nabla_XP)P=0,
\tag{6.5}
\]

only the off-diagonal blocks survive. Insert (3.3) and (5.3). \(\square\)

**Status:** **Derived here.** This is the elementary differentiated-compression identity in the BLS setting.

### Corollary 6.2 — compressed position is generically nonparallel

Even if the ambient observable is parallel,

\[
\nabla_X^{\operatorname{End}\mathscr L}M_\varphi=0,
\]

the compressed observable need not be:

\[
\nabla_X^{\operatorname{End}\mathscr H}T_\varphi\ne0
\]

unless the two off-diagonal terms in (6.3) cancel.

Thus

\[
\boxed{
\text{ambient position PVM: parallel},
\qquad
\text{Bergman-compressed POVM: generally not parallel}.
}
\tag{6.6}
\]

For \(\varphi=1\), the defect vanishes automatically because \(QM_1P=0\), as required by \(T_1=I_{\mathscr H}\).

### Interpretation

The same tensor \(\mathbb B_X\) has two roles:

\[
\boxed{
\begin{array}{c}
\operatorname{Tr}(\mathbb B_Y^*\mathbb B_X)
=\text{Grassmannian quantum information},
\\[1mm]
\mathbb B_X^*QMP+PMQ\mathbb B_X
=\text{compressed-measurement transport defect}.
\end{array}
}
\tag{6.7}
\]

So the failure of a projected measurement to remain fixed is not an unrelated nuisance; it is controlled by the geometry of the moving quantum subspace itself.

---

# Part IV. Why the Bergman DPP uses the ambient measurement

## 7. Slater state in the ambient many-body space

Let \(\{u_a\}_{a=1}^{N}\) be an orthonormal basis of \(\mathscr H_t\). The normalized fermionic Slater state is

\[
\Psi_t
=u_1\wedge\cdots\wedge u_N
\in
\bigwedge^N\mathscr H_t
\subset
\bigwedge^N\mathscr L_t.
\tag{7.1}
\]

In the position representation,

\[
\Psi_t(x_1,\dots,x_N)
=\frac1{\sqrt{N!}}
\det[u_a(x_b)].
\tag{7.2}
\]

Its Born density is

\[
\boxed{
|\Psi_t(x_1,\dots,x_N)|^2
=\frac1{N!}
\det[K_t(x_i,x_j)]_{i,j=1}^{N},
}
\tag{7.3}
\]

which is the projection determinantal point process associated with the Bergman kernel. This is the exact Slater-to-DPP identity reviewed in [`born-slater-information.md`](born-slater-information.md).

Crucially, the measurement in (7.3) is the ordinary position measurement on the **ambient antisymmetric many-body \(L^2\) space**. It is not the one-particle compressed Toeplitz operator \(PMP\).

The observable algebra relevant for unordered fermionic configurations consists of symmetric multiplication functions on \(X_t^N\); these preserve the antisymmetric subspace. Under the product horizontal flow

\[
(F_{t\leftarrow0}^\theta)^{\times N},
\]

the corresponding many-body position PVM is parallel by the tensor/exterior-power version of Theorem 3.1.

This is the missing typing correction.

---

## 8. Exact many-body transport identity

For a smooth symmetric configuration observable

\[
\Phi\in C^\infty(\mathcal X^{[N]}_B),
\]

where locally one may work on the ordered fiber product and impose permutation symmetry, let \(M^{(N)}_t(\Phi)\) denote multiplication on \(\bigwedge^N\mathscr L_t\). Then

\[
\boxed{
\nabla_X^{\operatorname{End}\wedge^N\mathscr L}
M^{(N)}(\Phi)
=
M^{(N)}(V_X^{(N)}\Phi),
}
\tag{8.1}
\]

where

\[
V_X^{(N)}
=\sum_{a=1}^N V_{X,a}^\theta.
\tag{8.2}
\]

Thus for an advected configuration observable,

\[
V_X^{(N)}\Phi=0,
\]

we have exact parallelism.

No determinantal identity is needed for (8.1); it follows from the Leibniz rule on the ambient many-body Hilbert field. The determinant enters only through the state \(\Psi_t\).

---

# Part V. Hyperbolic Kähler--Einstein specialization

## 9. Canonical horizontal lift

Let

\[
p:\mathcal X\to B
\]

be a smooth family of compact hyperbolic Riemann surfaces of genus \(g\ge2\). The fiberwise Kähler--Einstein metrics determine a distinguished horizontal lift. Schumacher shows that this lift produces the harmonic representative of the Kodaira--Spencer deformation [Sch12].

We denote it by

\[
\theta_{KE}.
\tag{9.1}
\]

For \(q\ge2\), put

\[
E=K_{\mathcal X/B}^{q-1}.
\tag{9.2}
\]

Then the adjoint direct image in the BLS setup is exactly

\[
\mathscr H_q
=p_*(K_{\mathcal X/B}\otimes E)
=p_*K_{\mathcal X/B}^q.
\tag{9.3}
\]

This removes the earlier mismatch between the canonical-twist direct-image formalism and the \(q\)-differential state space.

---

## 10. Minimal solution as second fundamental motion

For \(u\in H^0(X_t,K_{X_t}^q)\) and harmonic Beltrami/Kodaira--Spencer tensor \(\mu_X\), define

\[
\eta_X=-\mu_X\cdot u.
\tag{10.1}
\]

The direct-image curvature formulas of Berndtsson and the hyperbolic calculation of Fedosova--Rowlett--Zhang identify the negative Gauss term with the norm of an \(L^2\)-minimal \(\bar\partial\)-solution [Bern09; FRZ20]. In BLS language this is precisely the second-fundamental direction

\[
\mathbb B_Xu
=Q\nabla_X^{\mathscr L}u
\tag{10.2}
\]

up to the sign convention used to write the minimal-solution equation. The sign drops out of the metric

\[
\operatorname{Tr}(\mathbb B_Y^*\mathbb B_X).
\]

Accordingly the Plücker/Grassmannian metric is

\[
\boxed{
 g_{\mathrm{Pl},q}^{KE}(X,Y)
=
\operatorname{Tr}(\mathbb B_Y^*\mathbb B_X)
=\mathfrak B_q(X,Y).
}
\tag{10.3}
\]

The companion 50--50 calculation gives

\[
\boxed{
\mathfrak B_q
=
\frac{q-1}{4\pi}G_{\mathrm{WP}}+O(1).
}
\tag{10.4}
\]

**Normalization firewall.** Equation (10.4) uses the WP normalization fixed in the companion notes. It should not be mixed with a \(2\pi\)-normalized Chern form without an explicit conversion.

---

# Part VI. Intrinsic DPP Fisher closure

## 11. Definition of the KE-transported DPP Fisher tensor

Let

\[
P_{q,t}
\]

be the Bergman DPP on the configuration space of \(N_q\) points of \(X_t\). Use the KE horizontal flow to pull all nearby configuration measures back to the reference fiber:

\[
\widetilde P_{q,t}^{KE}
:=
\left((F_{t\leftarrow0}^{KE})^{\times N_q}\right)^*P_{q,t}.
\tag{11.1}
\]

The classical score in a real tangent direction \(X\) is

\[
S_{q,X}^{KE}
=
D_X\log\widetilde p_q^{KE},
\tag{11.2}
\]

and the Fisher tensor is

\[
\boxed{
I_q^{KE}(X,Y)
=
\mathbb E_{P_q}
[S_{q,X}^{KE}S_{q,Y}^{KE}].
}
\tag{11.3}
\]

This removes the arbitrary moving-sample-space choice: the transport is now the geometrically distinguished KE lift.

---

## 12. Theorem 12.1 — exact KE/BLS Hermitian Born--Fisher identity

For the holomorphic determinant/Slater line

\[
\det\mathscr H_q
=\bigwedge^{N_q}\mathscr H_q
\subset
\bigwedge^{N_q}\mathscr L_q,
\]

the BLS Chern connection induces the Chern connection of the determinant line. Locally, a holomorphic determinant frame therefore defines a projectively holomorphic ray in the ambient covariant realization.

By the many-body covariance identity (8.1), the position measurement transported by \(\theta_{KE}\) is parallel. Hence, locally on the base and with the same BLS/Chern realization used on both the state and measurement sides, the hypotheses of the exact Hermitian Born--Fisher theorem are satisfied, and

\[
\boxed{
I_q^{KE}(X,Y)
+
I_q^{KE}(JX,JY)
=
4g_{\mathrm{Pl},q}^{KE}(X,Y).
}
\tag{12.1}
\]

**Status:** **Derived here from established BLS/Chern machinery plus the exact Hermitian Born--Fisher identity of the companion note.** Equation (12.1) is exact in this local KE/BLS covariant realization. It does not assert that the ambient BLS field is a globally trivial holomorphic Hilbert bundle, nor does it require parallelism of the compressed Toeplitz POVM.

### Proof sketch with the transport issue exposed

Choose a local BLS/Chern covariant realization of the ambient many-body field. Because the position multiplication algebra is transported by the same horizontal flow, no extra parameter-dependent measurement derivative appears in the Born score. The determinant line is holomorphic, so the projective Cauchy--Riemann identity

\[
D_{JX}^\perp\widehat\Psi
=iD_X^\perp\widehat\Psi
\]

holds. Apply Theorem 4.1 of `hermitian-born-fisher.md`. \(\square\)

---

## 13. Corollary 13.1 — Weil--Petersson limit

Insert (10.4) into (12.1):

\[
\boxed{
I_q^{KE}(X,Y)
+
I_q^{KE}(JX,JY)
=
\frac{q-1}{\pi}G_{\mathrm{WP}}(X,Y)+O(1).
}
\tag{13.1}
\]

Therefore

\[
\boxed{
\frac{\pi}{q-1}
\left[
I_q^{KE}+J^*I_q^{KE}
\right]
\longrightarrow
G_{\mathrm{WP}}.
}
\tag{13.2}
\]

Equivalently, with the Hermitianized Born--Fisher tensor

\[
I_{\mathrm{HBF},q}^{KE}
:=
\frac14(I_q^{KE}+J^*I_q^{KE}),
\tag{13.3}
\]

we have

\[
\boxed{
I_{\mathrm{HBF},q}^{KE}
=
\frac{q-1}{4\pi}G_{\mathrm{WP}}+O(1),
}
\tag{13.4}
\]

and

\[
\boxed{
\frac{4\pi}{q-1}I_{\mathrm{HBF},q}^{KE}
\longrightarrow G_{\mathrm{WP}}.
}
\tag{13.5}
\]

This is the intrinsic moving-fiber classical statistical closure in the local KE/BLS realization; it is invariantly defined from the distinguished KE transport, although the proof is carried out in local covariant charts.

---

# Part VII. Comparison with the intrinsic KS resolvent channel

## 14. Leading Fisher--Kodaira--Spencer matching

The companion note defines the positive KS resolvent tensor

\[
\mathfrak K_q
\]

and derives

\[
\boxed{
\mathfrak K_q
=
\frac{q-1}{4\pi}G_{\mathrm{WP}}+O(1).
}
\tag{14.1}
\]

Comparing with (13.4),

\[
\boxed{
I_{\mathrm{HBF},q}^{KE}-\mathfrak K_q=O(1).
}
\tag{14.2}
\]

Thus

\[
\boxed{
\frac{4\pi}{q-1}
\left(
I_{\mathrm{HBF},q}^{KE}-\mathfrak K_q
\right)
\longrightarrow0.
}
\tag{14.3}
\]

This is the precise asymptotic answer to the earlier FI-H question. The raw single-direction Fisher tensor was the wrong object to compare to the Hermitian KS tensor; the \(J\)-completed Fisher tensor is the correctly typed object.

### 50--50 interpretation

Recall the exact source decomposition

\[
\mathfrak A_q
=
\mathfrak B_q+
\mathfrak K_q.
\tag{14.4}
\]

The previous calculation gives

\[
\mathfrak B_q
\sim
\mathfrak K_q
\sim
\frac12\mathfrak A_q.
\tag{14.5}
\]

Since

\[
I_{\mathrm{HBF},q}^{KE}
=
\mathfrak B_q,
\tag{14.6}
\]

we can write the leading-order triangle

\[
\boxed{
I_{\mathrm{HBF},q}^{KE}
\sim
\mathfrak K_q
\sim
\frac12\mathfrak A_q
\sim
\frac{q-1}{4\pi}G_{\mathrm{WP}}.
}
\tag{14.7}
\]

This is a **filtered** Fisher--Bergman--Quillen correspondence, not an equality with the full direct-image/Quillen curvature, whose leading order is different.

---

# Part VIII. What was actually resolved

## 15. Resolution of the transport question

The earlier question was phrased too strongly:

\[
\text{“Does the KE/Chern connection make the Bergman position POVM parallel?”}
\]

The exact answer is:

\[
\boxed{
\begin{array}{ll}
\textbf{Yes} & \text{for the ambient position PVM under BLS/KE transport},\\
\textbf{No in general} & \text{for its Bergman-compressed Toeplitz observable}.
\end{array}
}
\tag{15.1}
\]

The DPP uses the first object, so the statistical closure survives. The second object's nonparallelism is measured by \(\mathbb B\), and is therefore geometrically informative rather than fatal.

This is stronger than merely choosing a convenient trivialization: the transport is built from the same KE horizontal geometry that supplies the harmonic Kodaira--Spencer representative and from the same BLS/Chern structure that controls the direct-image connection.

---

# Part IX. Remaining open problems

## 16. What is still not proved

The main transport obstruction is removed, but several publication-level tasks remain.

### Open A — finite-\(q\) coefficient beyond the WP leading term

Compute the full expansion of

\[
I_{\mathrm{HBF},q}^{KE}-\mathfrak K_q
=
\mathfrak B_q-\mathfrak K_q.
\tag{16.1}
\]

The current result gives \(O(1)\). The constant and lower terms should contain local curvature/Beltrami invariants and may be accessible from the next coefficients of the Bergman and resolvent expansions.

### Open B — single-real-direction anisotropy

The Hermitian completion is canonical, but an individual real Fisher component

\[
I_q^{KE}(X,X)
\]

can distribute information unevenly between \(X\) and \(JX\). Quantify that anisotropy and determine whether distinguished real slices have single-direction saturation.

### Open C — higher-dimensional canonically polarized fibers

Replace the curve WP metric by the generalized Weil--Petersson metric and determine which powers of \(k\) occur in the ambient DPP/Hermitian Fisher channel.

### Open D — relation to Quillen curvature at subleading order

The full Quillen/direct-image curvature contains larger-order horizontal/geodesic-curvature pieces. Isolate the KS-filtered coefficient functorially at the determinant-line level and compare it with (14.2).

### Open E — novelty audit

A targeted search found nearby work on BLS Hilbert fields, Bergman direct-image curvature, Fisher/phase decompositions, DPP information geometry and WP/Grassmannian geometry, but no source stating the exact chain (3.3), (6.3), (12.1), and (13.2) as one theorem package. This is **not** a certification of novelty; a broader MathSciNet/zbMATH/reference-chain audit is still required before submission.

---

# 17. Reference map

- **BLS Hilbert fields, twisted-Lie Chern connection, projected direct-image connection, second fundamental form:** [Var24].
- **Original direct-image curvature / minimal-solution viewpoint and warning about ambient holomorphic Hilbert bundles:** [Bern09].
- **Kähler--Einstein horizontal lift and harmonic Kodaira--Spencer representatives:** [Sch12].
- **Hyperbolic \(q\)-differentials, minimal solutions and resolvent curvature asymptotics:** [FRZ20].
- **Fisher + phase covariance decomposition of projective quantum geometry:** [FKMMSV10].
- **Quantum Fisher as optimized measurement distinguishability:** [BC94].
- **Bergman DPP/free-fermion context:** [Ber08].
- **General DPP information geometry context:** [HY24].

No source is cited as proving the full FCIG KE/BLS DPP Fisher/WP closure. The displayed closure is a synthesis/deduction from the stated ingredients and remains subject to external peer verification.
