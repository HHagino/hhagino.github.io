# FCIG Model XXI — Field-content / supertrace completion audit

**Status:** COMPLETE WITH A SPIN-CONNECTION OBSTRUCTION. The local six-dimensional trace sector and the scalar-type finite threshold are fixed. For genuine spinor/vector bundles, the scalar finite-threshold rule is proven insufficient; their representation-dependent finite coefficient is separated into the next milestone. No gravitational field equation is claimed.

## 1. Question

Model XX used one real minimally coupled six-dimensional scalar and found

\[
G^{\rm ren}=Z_R g_{\rm hyp}
-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2]+\cdots.
\]

The Poincare trace term is local/renormalization-sensitive, whereas the displayed weight-four term is the finite Epstein/zeta threshold in the fixed scalar model.

Model XXI asks which parts of that answer can be extended to **independently specified field content** by a supertrace, and where spin, gauge fixing and ghosts introduce genuinely new data.

The background remains the restricted Model-XX family

\[
 ds_6^2=g_{\mu\nu}dx^\mu dx^\nu
 +L^2G_{ab}(\tau(x))dy^ady^b,
\qquad \det G=1.
\]

---

## 2. Determinant conventions

We work with the parity-even / absolute-value sector of free determinants. Phases and chiral/global anomalies remain separate determinant-line data.

For a real scalar,

\[
W_0=\frac12\log\det\Delta_0.
\]

For a complex Dirac fermion,

\[
W_{1/2}=-\log\det \slashed D
\]

and its parity-even part is represented by

\[
\boxed{
W_{1/2}^{\rm even}
=-\frac12\log\det \slashed D^2.
}
\]

For an Abelian Maxwell field in background/Feynman gauge,

\[
\boxed{
W_1=\frac12\log\det\Delta_1-\log\det\Delta_0,
}
\]

where the second determinant is the complex Faddeev--Popov ghost. Gauge and ghost terms are never separated when a gauge-invariant conclusion is stated.

These are standard one-loop determinant structures; see Vassilevich [Vassilevich2003].

---

## 3. Six-dimensional local heat-kernel coefficient

Use the Laplace-type convention

\[
P=-\left(\nabla^2+E\right),
\qquad
b_2=E+\frac16R\,I.
\]

### 3.1 Real scalar

For a minimal real scalar,

\[
E_0=0,
\qquad
\operatorname{tr}b_2^{(0)}=\frac16R.
\]

Its one-loop proper-time weight is \(-\tfrac12\operatorname{Tr}e^{-t\Delta_0}\).

### 3.2 Complex Dirac fermion

The Lichnerowicz formula gives

\[
\boxed{
\slashed D^2=-\nabla^2+\frac14R.
}
\]

Thus in the convention above

\[
E_{1/2}=-\frac14R.
\]

A complex Dirac spinor in six Euclidean dimensions has complex spinor rank

\[
N_{\rm D}=2^{6/2}=8,
\]

so

\[
\operatorname{tr}b_2^{(1/2)}
=8\left(-\frac14+\frac16\right)R
=-\frac23R.
\]

The fermionic determinant reverses the proper-time sign relative to a bosonic determinant. Comparing the final \(R\)-term with one real scalar gives

\[
\boxed{c_{\rm loc}^{\rm Dirac}=4.}
\]

A complex Weyl determinant contributes half of this parity-even coefficient:

\[
\boxed{c_{\rm loc}^{\rm Weyl}=2.}
\]

### 3.3 Maxwell field plus ghost

The Hodge/Weitzenbock formula on one-forms is

\[
(\Delta_1A)_M
=-\nabla^2A_M+R_M{}^N A_N.
\]

Hence

\[
(E_1)_M{}^N=-R_M{}^N,
\]

and in dimension \(d\)

\[
\operatorname{tr}b_2^{(1)}
=\left(\frac d6-1\right)R.
\]

For \(d=6\),

\[
\boxed{\operatorname{tr}b_2^{(1)}=0.}
\]

The complex scalar ghost has \(b_2^{\rm gh}=R/6\). Combining

\[
W_1=\frac12\log\det\Delta_1-\log\det\Delta_0
\]

and comparing with one real scalar yields

\[
\boxed{c_{\rm loc}^{\rm Maxwell+gh}=-2.}
\]

---

## 4. Exact local supertrace table

Normalize one real minimal scalar to one unit. Then

\[
\boxed{
\begin{array}{c|c}
\text{field} & c_{\rm loc}\ \text{in }d=6\\ \hline
\text{real scalar} & 1\\
\text{complex scalar} & 2\\
\text{complex Dirac} & 4\\
\text{complex Weyl (parity-even)} & 2\\
\text{Maxwell + FP ghost} & -2
\end{array}}
\]

Therefore, for free untwisted fields of these types,

\[
\boxed{
C_{\rm loc}
=N_{\rm real\ scalar}
+4N_{\rm Dirac}
-2N_{\rm Maxwell}
}
\]

with obvious half/double replacements for Weyl/complex scalars.

Model XX gave, for one real scalar,

\[
W_{\rm div}^{(\tau,0)}
=\frac{\Lambda^4L^2}{48(4\pi)^3}
\int\sqrt{g_4}\,
\frac{\partial_\mu\tau\partial^\mu\bar\tau}{Y^2}.
\]

Hence the field-content local result is

\[
\boxed{
W_{\rm div}^{(\tau)}
=C_{\rm loc}\,
W_{\rm div}^{(\tau,0)}
}
\]

within the same proper-time convention.

> **Result XXI.1 (Derived here).** The local modulus-kinetic supertrace is not the naive signed count of physical polarizations. Curvature endomorphisms and gauge ghosts change it.

For example, a six-dimensional Dirac field and Maxwell field have respectively four and minus two scalar units, rather than minus eight and plus four from a naive off-shell component count.

---

## 5. A physically specified local cancellation: the 6d \(\mathcal N=(1,0)\) vector multiplet

A six-dimensional \(\mathcal N=(1,0)\) vector multiplet contains a gauge field and a symplectic-Majorana-Weyl gaugino; this standard field content is reviewed in the 6d supersymmetry literature [6dN10Multiplets].

A symplectic-Majorana-Weyl doublet has the parity-even determinant content of one unconstrained complex Weyl spinor. Thus

\[
c_{\rm loc}^{\rm gaugino}=2,
\qquad
c_{\rm loc}^{\rm Maxwell+gh}=-2.
\]

Therefore

\[
\boxed{
C_{\rm loc}^{(1,0)\,\mathrm{vector}}=0.
}
\]

> **Result XXI.2 (Derived here).** In this free-field local heat-kernel audit, a 6d \(\mathcal N=(1,0)\) vector multiplet cancels the one-loop \(R_6\) / Poincare-trace renormalization at this order.

This statement concerns the parity-even local two-derivative sector. It does **not** imply cancellation of the chiral anomaly, determinant-line phase, or finite nonlocal threshold.

---

## 6. Scalar-type finite threshold theorem

There is one class for which Model XX extends by a pure multiplicity with no further calculation.

Let the quadratic operator be

\[
P=-\Delta_6\otimes I_r
\]

on a trivial flat rank-\(r\) spectator bundle, with no additional connection, endomorphism or modulus-dependent mixing. Then

\[
\log\det P=r\log\det\Delta_6
\]

and the complete one-loop response scales by the determinant power/statistics.

Define the **scalar-equivalent determinant multiplicity** \(\nu\):

\[
\nu(\text{real bosonic scalar})=1,
\qquad
\nu(\text{complex bosonic scalar})=2,
\qquad
\nu(\text{complex Grassmann scalar})=-2.
\]

Then the Model-XX finite threshold is exactly

\[
\boxed{
G^{\rm fin}_{\nu}
=-\frac{\nu}{16\pi^3L^2}
\operatorname{Re}\!\left[\mathcal G_4(\tau)(d\tau)^2\right].
}
\]

> **Result XXI.3 (Derived here).** Signed multiplicity is exact only for scalar-type operators whose connection/endomorphism data are truly identical.

---

## 7. Why true spin fields are not scalar multiplicities

For a genuine Dirac field,

\[
\slashed D^2=-(\nabla_{\rm spin})^2+\frac14R,
\]

and for a one-form,

\[
\Delta_1=-\nabla_{T^*}^2+\operatorname{Ric}.
\]

Thus spinors and vectors differ from scalar copies in **two independent ways**:

1. the endomorphism \(E\) is curvature dependent;
2. the bundle connection is nontrivial when \(\tau(x)\) varies.

In a toroidal winding/heat-kernel representation, the nonlocal coefficient transports the field around a winding cycle. For a general bundle this parallel transport contains the spin connection. Consequently its expansion at two derivatives depends on traces of Lorentz generators, schematically

\[
\operatorname{tr}_R(\Sigma_{AB}\Sigma_{CD}),
\]

an invariant which is absent for scalars. Covariant torus one-loop formalisms explicitly retain both the field-dependent \(E\) matrix and spin/gauge parallel transport [vonGersdorff2008].

Therefore

\[
\boxed{
G^{\rm fin}_{\rm spin>0}
\neq
(\text{signed number of components})\,G^{\rm fin}_{\rm scalar}
\quad\text{in general}.
}
\]

> **Result XXI.4 (No-go).** Local supersymmetric cancellation does not imply cancellation of the Model-XX finite weight-four threshold. The latter requires a representation-dependent spin-connection calculation.

This is precisely why the vector-multiplet example above cannot be promoted from \(C_{\rm loc}=0\) to \(G^{\rm fin}=0\) without a new calculation.

---

## 8. What v0.21 does and does not complete

### Complete

- determinant/statistics conventions;
- exact 6d local coefficients for scalar, Dirac and Maxwell+ghost;
- exact local supertrace formula;
- exact local cancellation for a specified \(\mathcal N=(1,0)\) vector multiplet;
- exact scalar-type finite multiplicity theorem;
- proof that true spin fields require more than scalar multiplicity.

### Deliberately moved to the next gate

The representation-dependent finite coefficient from spin parallel transport and curvature endomorphisms is not guessed. The next milestone must compute it explicitly for Dirac and Maxwell+ghost on the Model-XX elliptic family.

This split is forced by the operator geometry, not by lack of a desired answer.

---

## 9. References

- D. V. Vassilevich, *Heat Kernel Expansion: User's Manual*, Phys. Rept. **388** (2003), 279--360. [Vassilevich2003]
- G. von Gersdorff, *One-Loop Effective Action in Orbifold Compactifications*, JHEP **08** (2008) 097. [vonGersdorff2008]
- Standard Lichnerowicz formula and Hodge--Weitzenbock formula; see the spin-geometry / heat-kernel references listed in the milestone bibliography. [LawsonMichelsohn1989]
- Six-dimensional \(\mathcal N=(1,0)\) multiplet field content: vector = gauge field + symplectic-Majorana-Weyl gaugino. [6dN10Multiplets]

## Bottom line

\[
\boxed{
\text{local supertrace: }1:4:-2
\quad\text{for scalar:Dirac:Maxwell},
}
\]

but

\[
\boxed{
\text{finite automorphic threshold}
\text{ requires Lorentz-representation data for spin}>0.
}
\]

So the next nontrivial object is no longer a species count; it is a **spin-connection automorphic threshold**.
