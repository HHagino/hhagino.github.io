# FCIG Model XVI — Explicit operator / heat-kernel effective-action bridge

**Status:** Established heat-kernel formulas + derived FCIG pullback bridge and no-go boundaries.  
**Milestone:** v0.16.  
**Scope:** a four-dimensional Euclidean Laplace-type operator, Seeley--DeWitt coefficients, one-loop determinant, renormalization split, and an explicit pullback of FCIG line curvature into the operator.  
**Not claimed:** that the spacetime realization map is derived by FCIG, that UV counterterm coefficients are predictions, or that a Lorentzian Einstein equation follows.

---

## 1. Why this model is the next required step

Model XV isolated the missing arrow

\[
\boxed{
\text{FCIG geometric/determinant data}
\xrightarrow{\ ?\ }
W_{\rm FCIG}^{\rm ren}[A,g].
}
\]

The present model supplies the first explicit **operator-level template** for that arrow.

The central discipline is to keep three layers distinct:

1. **Established spectral geometry:** heat kernels of Laplace-type operators and their local coefficients.
2. **Additional realization data:** a map from physical spacetime backgrounds into an FCIG parameter/base space.
3. **Derived FCIG consequence:** after pullback, FCIG line curvature appears as an ordinary bundle-curvature invariant in the one-loop effective action.

---

## 2. Physical Euclidean background and realization map

Let \((M,g)\) be a compact four-dimensional Euclidean Riemannian manifold without boundary.

Let \(\mathcal B_{\rm FCIG}\) be a base carrying a Hermitian line with unitary connection

\[
(\mathscr L_{\rm FCIG},\nabla^{\rm FCIG})
\longrightarrow
\mathcal B_{\rm FCIG}.
\]

This may represent, depending on the earlier model, a determinant/anomaly line or another explicitly chosen FCIG line object.

### Additional data — not derived here

Supply a smooth spacetime realization map

\[
\boxed{
\Phi:M\longrightarrow\mathcal B_{\rm FCIG}.
}
\]

Pull back the line and connection:

\[
L_M:=\Phi^*\mathscr L_{\rm FCIG},
\qquad
\nabla^M:=\Phi^*\nabla^{\rm FCIG}.
\]

Its curvature is

\[
\boxed{
\Omega:=F_{\nabla^M}=\Phi^*F_{\nabla^{\rm FCIG}}.
}
\]

This is the first place in the program where the FCIG line curvature is placed on a physical four-dimensional background without identifying it with frame curvature.

The map \(\Phi\) is extra structure. A future theory would have to derive or constrain it.

---

## 3. Laplace-type operator and convention

Consider a Laplace-type operator acting on sections of \(L_M\),

\[
\boxed{
P=-\left(g^{\mu\nu}\nabla^M_\mu\nabla^M_\nu+E\right),
}
\]

where \(E\) is a smooth endomorphism. For a line bundle it is simply a scalar function.

This is the standard Laplace-type convention used in heat-kernel references such as Vassilevich and Gilkey [Vas03, Gil95].

Define the heat trace

\[
K(t;P):=\operatorname{Tr}(e^{-tP}).
\]

On a closed four-manifold,

\[
\boxed{
K(t;P)
\sim
(4\pi t)^{-2}
\int_M\sqrt g\,\operatorname{tr}
\left[
 b_0+t b_2+t^2 b_4+\cdots
\right]
\qquad(t\downarrow0).
}
\]

The coefficients below are **Established** [Vas03, Gil95].

---

## 4. The local coefficients \(b_0,b_2,b_4\)

### 4.1 Zeroth coefficient

\[
\boxed{b_0=I.}
\]

It produces a local volume term.

### 4.2 Second coefficient

\[
\boxed{
b_2=E+\frac16 R I.
}
\]

Thus the first curvature correction already contains the scalar curvature.

### 4.3 Fourth coefficient

With

\[
\Omega_{\mu\nu}:=[\nabla^M_\mu,\nabla^M_\nu],
\]

the standard local coefficient is

\[
\boxed{
\begin{aligned}
 b_4=\frac1{360}\Big(&
60\nabla^2E
+60RE
+180E^2
+12\nabla^2R\\
&+5R^2
-2R_{\mu\nu}R^{\mu\nu}
+2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
+30\Omega_{\mu\nu}\Omega^{\mu\nu}
\Big).
\end{aligned}
}
\]

For a closed manifold the integrated total-derivative terms \(\nabla^2E\) and \(\nabla^2R\) vanish.

The bundle-curvature contribution is therefore

\[
\boxed{
 b_4\supset\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}.
}
\]

This coefficient is standard heat-kernel geometry; the new FCIG content comes only after inserting \(\Omega=\Phi^*F_{\rm FCIG}\).

---

## 5. Explicit FCIG curvature insertion

Substituting the pullback curvature gives

\[
\boxed{
 b_4^{\rm FCIG}
\supset
\frac1{12}
\left(\Phi^*F_{\rm FCIG}\right)_{\mu\nu}
\left(\Phi^*F_{\rm FCIG}\right)^{\mu\nu}.
}
\]

This is the first explicit local spacetime effective-action invariant in the program built from FCIG line curvature through a standard physical operator.

### Crucial type statement

This does **not** say

\[
F_{\rm FCIG}=R_{\mu\nu\rho\sigma}.
\]

Instead,

\[
\boxed{
F_{\rm FCIG}
\xrightarrow{\Phi^*}
\Omega\text{ of a matter/bundle connection}
\xrightarrow{\text{heat kernel}}
\Omega^2\text{ in }W_{1\text{-loop}}.
}
\]

The frame curvature remains an independent ingredient and appears separately through the Riemann invariants in \(b_4\).

---

## 6. One-loop determinant and proper time

For a bosonic Gaussian operator, write with a statistics/multiplicity factor \(\sigma\)

\[
W_{1\text{-loop}}=\sigma\,\log\det P.
\]

For one real scalar \(\sigma=1/2\); for one complex scalar the two real components give \(\sigma=1\). The precise overall factor does not affect the degree audit below.

The proper-time representation is

\[
\boxed{
W_{1\text{-loop}}
=-\sigma\int_0^\infty\frac{dt}{t}\,K(t;P),
}
\]

under the usual spectral assumptions/regularization [Vas03, BD82].

Introduce a UV cutoff \(t\ge\Lambda^{-2}\). Using the four-dimensional expansion,

\[
\boxed{
W_{\Lambda}^{\rm UV}
\sim
-\frac{\sigma}{(4\pi)^2}
\left[
\frac12\Lambda^4 B_0
+\Lambda^2 B_2
+\log(\Lambda^2)B_4
\right],
}
\]

up to the convention-dependent choice of logarithmic reference scale and finite/IR terms, where

\[
B_{2r}:=\int_M\sqrt g\,\operatorname{tr}(b_{2r}).
\]

The key established fact is regulator-independent at the structural level:

\[
\boxed{
\text{in 4D the UV local divergences are controlled by }b_0,b_2,b_4.
}
\]

Vassilevich explicitly relates the short-time coefficients with one-loop divergences/counterterms [Vas03].

---

## 7. Gravitational degree hierarchy

The local heat-kernel hierarchy now has a direct effective-action meaning.

### \(b_0\) — volume / cosmological sector

\[
B_0\propto\int_M\sqrt g.
\]

This renormalizes a cosmological/volume coupling.

### \(b_2\) — Einstein--Hilbert sector

If \(E\) contains no cancellation of the scalar-curvature term,

\[
B_2\supset\int_M\sqrt g\,R.
\]

Thus it renormalizes the Einstein--Hilbert/Newton coupling.

### \(b_4\) — curvature-squared and bundle-curvature sector

\[
B_4\supset
\int_M\sqrt g\,
\left(
R^2,
R_{\mu\nu}R^{\mu\nu},
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma},
\Omega_{\mu\nu}\Omega^{\mu\nu},
RE,E^2
\right).
\]

These are higher-derivative gravitational/matter-background counterterms.

### Derived conclusion

The heat-kernel hierarchy provides exactly the missing local map

\[
\boxed{
\text{operator spectrum}
\to
\text{local gravitational/matter effective-action terms}.
}
\]

But the divergent coefficients are renormalization data, not parameter-free predictions.

---

## 8. Scalar-curvature specialization

Take a rank-one operator with

\[
E=-\xi R.
\]

Equivalently, the differential operator is

\[
P=-\nabla^2+\xi R
\]

in the convention of this note.

Then

\[
\boxed{
b_2=\left(\frac16-\xi\right)R.
}
\]

On a closed four-manifold, dropping integrated total derivatives and retaining the FCIG pullback curvature,

\[
\boxed{
\begin{aligned}
 b_4
=&\frac12\left(\xi-\frac16\right)^2R^2
+\frac1{180}
\left(
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
-R_{\mu\nu}R^{\mu\nu}
\right)\\
&+\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}.
\end{aligned}
}
\]

The local unintegrated formula also contains

\[
\frac{1-5\xi}{30}\nabla^2R.
\]

### Conformal check

For \(\xi=1/6\),

\[
\boxed{b_2=0}
\]

and the algebraic \(R^2\) term in \(b_4\) cancels, leaving the standard curvature-combination plus the independent bundle-curvature term (and a total derivative locally).

This is a useful convention check, not a new FCIG result.

---

## 9. Local versus global FCIG data survives the physical operator test

Earlier FCIG models separated local curvature from flat/global holonomy. The present operator realizes that distinction concretely.

### Flat FCIG line

If

\[
F_{\rm FCIG}=0
\]

but the line has nontrivial flat holonomy, then

\[
\Omega=\Phi^*F_{\rm FCIG}=0.
\]

Therefore every **local** heat-kernel term depending polynomially on \(\Omega\) vanishes.

Yet the global spectrum/determinant can still depend on flat holonomy or twisted boundary/global data.

Thus

\[
\boxed{
F=0,\ \operatorname{Hol}\neq1
\Longrightarrow
\text{local heat coefficients may miss data retained by the global determinant.}
}
\]

This is the physical-operator version of the local/global separation already isolated in Models II, IIIc and VI.

### Curved FCIG line

If \(F_{\rm FCIG}\neq0\), its pullback enters the local coefficient through \(\Omega^2\) at order \(b_4\).

Hence the two cases remain sharply distinct after spacetime realization.

---

## 10. Heat-kernel versus Bergman asymptotics

There is a real analogy but not an identity.

### Heat kernel

\[
t\downarrow0,
\qquad
\operatorname{Tr}e^{-tP}
\sim
(4\pi t)^{-2}
\sum_r t^rB_{2r}.
\]

### Bergman kernel

For a positive line bundle at large tensor power,

\[
k\to\infty,
\qquad
B_k(x)
\sim
k^d+a_1(x)k^{d-1}+a_2(x)k^{d-2}+\cdots.
\]

Both are local spectral/geometric asymptotic expansions whose coefficients are curvature invariants. But they arise from different operators, scaling parameters, Hilbert spaces and normalization conventions.

Therefore

\[
\boxed{
\text{Bergman coefficient hierarchy}
\neq
\text{Seeley--DeWitt hierarchy}
\quad\text{without an explicit operator/functorial identification.}
}
\]

The present model does not make that identification.

### Genuine determinant-level connection

Quillen/determinant constructions are spectral determinants of elliptic families, so determinant geometry and heat-kernel regularization are genuinely related at the spectral level [Vas03 and the Quillen/Bismut references used in earlier FCIG models].

However, the four-dimensional operator \(P\) used here is not automatically the same family as the Cauchy--Riemann operators of the curve models.

---

## 11. Finite versus local data

The short-time coefficients determine UV divergences and local large-mass/derivative expansions. They do not determine the entire finite nonlocal effective action.

Schematically,

\[
\boxed{
W_{\rm ren}
=W_{\rm local}^{\rm scheme\ fixed}
+W_{\rm finite/nonlocal}.
}
\]

The first few \(b_{2r}\) constrain the first term. The second term depends on more of the spectrum/global heat kernel.

This prevents a second overclaim:

\[
\boxed{
(b_0,b_2,b_4)
\not\Rightarrow
\text{full determinant/effective action}.
}
\]

This is consistent with Vassilevich's distinction between local short-time data and more global/nonlocal information [Vas03].

---

## 12. Metric variation and Wald consequences

Once a local term is present in a renormalized effective action, Model XV applies.

### Metric variation

For a local contribution

\[
W_{\rm local}=\int_M\sqrt g\,\mathcal L_{\rm local},
\]

define

\[
T_{\mu\nu}^{\rm local}
=-\frac2{\sqrt g}
\frac{\delta W_{\rm local}}{\delta g^{\mu\nu}}.
\]

Thus the heat-kernel bridge produces actual terms whose metric variation is well-defined after a renormalization prescription is fixed.

### Stationary-horizon entropy

For a local diffeomorphism-invariant gravitational term, Wald/Iyer--Wald give the corresponding stationary-horizon Noether-charge entropy [Wald93, IW94].

Consequently:

- a local \(R\) term shifts the area-law coefficient;
- curvature-squared terms give higher-curvature Wald corrections;
- a pure volume/cosmological term has no explicit \(\partial\mathcal L/\partial R_{\mu\nu\rho\sigma}\) contribution;
- a pure \(\Omega^2\) matter/bundle term, when \(\Omega\) is treated as independent of Riemann curvature, does not directly contribute through the Wald curvature derivative, though it contributes to stress-energy and can backreact through the field equation.

This is the first controlled answer to the question "where could FCIG enter both dynamics and horizon entropy?": it must first become an appropriate local spacetime Lagrangian term.

---

## 13. Gate audit

### Gate BC — explicit operator/background map: PASS WITH ADDITIONAL DATA

A concrete map \(\Phi:M\to\mathcal B_{\rm FCIG}\), pulled-back line connection and Laplace-type operator are specified. The map is extra input, not derived by FCIG.

### Gate BD — heat-kernel coefficients: PASS

The \(b_0,b_2,b_4\) formulas are fixed in the \(P=-(\nabla^2+E)\) convention and sourced to standard heat-kernel literature.

### Gate BE — determinant / proper-time bridge: PASS

The one-loop determinant is represented by proper time; in four dimensions the UV local terms are controlled by \(b_0,b_2,b_4\).

### Gate BF — gravitational interpretation: PASS WITH RENORMALIZATION QUALIFICATION

The volume, Einstein--Hilbert and curvature-squared sectors are explicit, but their divergent local coefficients renormalize couplings and are not parameter-free FCIG predictions.

### Gate BG — FCIG-specific comparison: PASS WITH NON-IDENTIFICATION

Pulled-back FCIG line curvature enters explicitly through \(\Omega^2\). Bergman and heat-kernel asymptotic hierarchies remain distinct unless a further operator-level identification is supplied.

### Gate BH — metric variation / Wald test: PASS

Local terms can be varied to obtain stress-energy corrections; local curvature terms have corresponding Wald entropy corrections.

---

## 14. Main result of v0.16

The missing arrow of Model XV now has an explicit conditional realization:

\[
\boxed{
(\mathscr L_{\rm FCIG},\nabla^{\rm FCIG})
+\Phi:M\to\mathcal B_{\rm FCIG}
\to
P_{\Phi}
\to
\operatorname{Tr}e^{-tP_{\Phi}}
\to
W_{1\text{-loop}}^{\rm ren}[g,\Phi].
}
\]

At local order \(b_4\),

\[
\boxed{
W_{\rm local}^{\rm FCIG}
\supset
\text{renormalized coefficient}\times
\int_M\sqrt g\,
(\Phi^*F_{\rm FCIG})_{\mu\nu}
(\Phi^*F_{\rm FCIG})^{\mu\nu}.
}
\]

The coefficient requires a renormalization prescription and field-content normalization; it is not claimed as a new universal constant.

This is a real operator/effective-action bridge, but still conditional on the spacetime realization map \(\Phi\).

---

## 15. Next target

**v0.17 — realization-map dynamics / sigma-model audit.**

The remaining new object is \(\Phi\). The next controlled question is whether \(\Phi:M\to\mathcal B_{\rm FCIG}\) can itself be given a natural, covariant spacetime action using the geometry already present on \(\mathcal B_{\rm FCIG}\), for example a sigma-model kinetic term

\[
\int_M\sqrt g\,G_{AB}(\Phi)\,\partial_\mu\Phi^A\partial^\mu\Phi^B,
\]

and whether such a term is genuinely induced by FCIG data or merely another arbitrary constitutive input.

A successful v0.17 would have to specify the target metric/connection, its origin, renormalization, and a falsifiable model. No identification with spacetime gravity is assumed.

---

## References used in this model

- [Vas03] D. V. Vassilevich, *Heat Kernel Expansion: User's Manual*, Physics Reports **388** (2003) 279--360.
- [Gil95] P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah--Singer Index Theorem*, 2nd ed., CRC Press (1995).
- [BD82] N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space*, Cambridge University Press (1982).
- [Wald93] R. M. Wald, *Black Hole Entropy is the Noether Charge*, Phys. Rev. D **48** (1993) R3427--R3431.
- [IW94] V. Iyer and R. M. Wald, *Some Properties of Noether Charge and a Proposal for Dynamical Black Hole Entropy*, Phys. Rev. D **50** (1994) 846--864.

### Citation boundary

The Laplace-type coefficient formulas, proper-time determinant relation, UV-divergence hierarchy and Wald/Iyer--Wald entropy construction are established literature. The explicit pullback realization \(\Omega=\Phi^*F_{\rm FCIG}\), its insertion into the FCIG program, and the local/global comparison with earlier FCIG models are **Derived here / conditional construction**.