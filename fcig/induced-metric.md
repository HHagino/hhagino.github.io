# FCIG Model XVIII — Induced realization-map metric from one-loop determinants

**Status:** Derived-here determinant-response calculation + standard differential geometry/modular facts. No spacetime-gravity identification is made.

## 1. Question

Model XVII promoted the realization map

\[
\Phi:M\to\mathbb H,
\qquad
\tau=u+iY,
\]

to a harmonic-map field with target metric

\[
G_{\rm hyp}=\frac{du^2+dY^2}{Y^2}.
\]

Its overall two-derivative normalization was still external. Model XVIII asks whether a one-loop determinant can induce that target metric rather than merely postulating it.

The operational definition used here is deliberately narrow: **the induced metric is the coefficient of the external-momentum \(p^2\) term in the one-loop 1PI two-point function around a constant background**. This avoids identifying that response automatically with a unique global off-shell derivative-expanded functional; derivative-expansion prescriptions require care [Chan1986; HenningLuMurayama2018; CanevaroloProkopec2024].

---

## 2. One heavy scalar: bubble-defined two-derivative response

Take a real Euclidean heavy scalar with

\[
P(\Phi)=-\partial^2+V(\Phi),
\qquad V(\Phi)>0,
\]

and

\[
W[\Phi]=\frac12\operatorname{Tr}\log P(\Phi).
\]

Around a constant background \(\Phi_0\), write

\[
V(\Phi)=V_0+\delta V.
\]

The quadratic term is

\[
W^{(2)}
=-\frac14\operatorname{Tr}(G\,\delta V\,G\,\delta V),
\qquad
G=(-\partial^2+V_0)^{-1}.
\]

In momentum space the bubble integral is

\[
I(p)=\int\frac{d^4q}{(2\pi)^4}
\frac1{(q^2+V_0)((q+p)^2+V_0)}.
\]

Feynman parametrization gives

\[
I(p)=\int_0^1dx\int\frac{d^4q}{(2\pi)^4}
\frac1{\left[q^2+V_0+x(1-x)p^2\right]^2}.
\]

Using

\[
\int\frac{d^4q}{(2\pi)^4}\frac1{(q^2+V_0)^3}
=\frac1{32\pi^2V_0}
\]

and \(\int_0^1x(1-x)dx=1/6\),

\[
\boxed{
I(p)=I(0)-\frac{p^2}{96\pi^2V_0}+O(p^4).
}
\]

Therefore the bubble-defined two-derivative part is

\[
\boxed{
W_{(2,\partial)}
=\frac1{384\pi^2V_0}
\int d^4x\,(\partial_\mu\delta V)(\partial^\mu\delta V)
+O(\partial^4).
}
\]

For background coordinates \(\Phi^A\), with \(\delta V=V_{,A}\delta\Phi^A+\cdots\), define

\[
W_{(2,\partial)}
=\frac12\int d^4x\,
G^{\rm ind}_{AB}(\Phi_0)
\partial_\mu\delta\Phi^A\partial^\mu\delta\Phi^B.
\]

Then

\[
\boxed{
G^{\rm ind}_{AB}
=\frac1{192\pi^2}
\frac{V_{,A}V_{,B}}{V}.
}
\]

This metric has rank at most one.

> **Result XVIII.1 (single-species rank no-go).** A single diagonal field-dependent mass determinant cannot induce the rank-two Poincare metric on the elliptic FCIG target.

The coefficient above is the result in the fixed bubble/1PI convention. Chan and modern covariant derivative-expansion methods provide the broader functional-determinant context [Chan1986; HenningLuMurayama2018]. Canevarolo--Prokopec obtain a different conclusion for a single-field one-loop gradient term in a midpoint/Wigner-space expansion, so Model XVIII does **not** promote this bubble coefficient to a unique prescription-independent global off-shell functional [CanevaroloProkopec2024].

---

## 3. Several diagonal heavy species

For independent real scalars

\[
P_i(\Phi)=-\partial^2+V_i(\Phi),
\qquad V_i>0,
\]

the one-loop responses add:

\[
\boxed{
G^{\rm ind}_{AB}
=\frac1{192\pi^2}
\sum_{i=1}^N
\frac{\partial_AV_i\,\partial_BV_i}{V_i}.
}
\]

Define

\[
s_i(\Phi):=\sqrt{V_i(\Phi)}.
\]

Then

\[
\frac{dV_i\otimes dV_i}{V_i}=4\,ds_i\otimes ds_i,
\]

hence

\[
\boxed{
G^{\rm ind}
=\frac1{48\pi^2}
\sum_{i=1}^N ds_i^2
=\frac1{48\pi^2}\,s^*\delta_{\mathbb R^N},
\qquad
s=(s_1,\ldots,s_N).
}
\]

This is the key structural theorem: the diagonal-mass determinant metric is the pullback of a flat Euclidean metric by the **mass map** \(s\).

---

## 4. Two species: rank restoration but exact curvature no-go

Let \(N=2\). If \(ds\) has rank smaller than two, \(G^{\rm ind}\) is degenerate. If \(ds\) has rank two, the inverse-function theorem makes \((s_1,s_2)\) local coordinates. In those coordinates,

\[
G^{\rm ind}=\frac1{48\pi^2}(ds_1^2+ds_2^2),
\]

so its Gaussian curvature is exactly zero.

Therefore:

\[
\boxed{
N=2:\quad
G^{\rm ind}\text{ is either degenerate or locally flat.}
}
\]

Since

\[
K(G_{\rm hyp})=-1,
\]

we obtain:

> **Result XVIII.2 (two-species curvature no-go).** No choice of two positive diagonal scalar mass functions \(V_1(u,Y),V_2(u,Y)\) can reproduce the Poincare metric on any open set where the induced metric is nondegenerate.

This is stronger than a rank count: adding a second species restores rank but still cannot reproduce the FCIG target curvature.

### Explicit rank-two witness

For example,

\[
V_1=e^{2au},
\qquad
V_2=e^{2aY},
\]

gives

\[
s_1=e^{au},\qquad s_2=e^{aY},
\]

and therefore

\[
G^{\rm ind}
=\frac{a^2}{48\pi^2}
\left(e^{2au}du^2+e^{2aY}dY^2\right).
\]

It has rank two but becomes a constant Euclidean metric after the coordinate changes \(U=e^{au}\), \(W=e^{aY}\). It is not hyperbolic.

---

## 5. Modular-invariant two-species witness

The failure is not repaired by modular invariance.

Klein's complete invariant satisfies

\[
J(\gamma\tau)=J(\tau),
\qquad \gamma\in SL(2,\mathbb Z),
\]

as recorded in DLMF \S23.18 [DLMF23].

Choose positive modular-invariant masses

\[
\boxed{
V_1=M^2e^{2a\,\Re J(\tau)},
\qquad
V_2=M^2e^{2a\,\Im J(\tau)}.
}
\]

At regular points where \(J'(\tau)\neq0\), the map

\[
\tau\longmapsto
\left(e^{a\Re J(\tau)},e^{a\Im J(\tau)}\right)
\]

has rank two, so the induced metric is nondegenerate. Nevertheless Result XVIII.2 applies: it is locally flat, not Poincare.

The orbifold fixed points make the mismatch even sharper. If \(\tau_*\) is fixed by a nontrivial modular transformation with derivative not equal to one, differentiating \(J(\gamma\tau)=J(\tau)\) at \(\tau_*\) forces \(J'(\tau_*)=0\). Thus this explicit two-species metric loses rank at the elliptic branch points, whereas the hyperbolic orbifold metric remains the underlying target geometry.

> **Result XVIII.3.** Modular invariance plus two diagonal determinant species is still insufficient to induce the elliptic FCIG Poincare metric.

---

## 6. Three species: local fitting is possible, global complete fitting is not

For \(N=3\), exact matching

\[
G^{\rm ind}=G_{\rm hyp}
\]

would mean that the rescaled mass map

\[
\widetilde s
:=\frac1{\sqrt{48}\,\pi}(s_1,s_2,s_3)
\]

is an isometric immersion of the hyperbolic target into Euclidean \(\mathbb R^3\).

Locally, negatively curved pseudospherical patches exist, so a sufficiently unconstrained choice of three mass functions can be reverse-engineered to fit a hyperbolic patch. Shifting the immersion coordinates by constants on a sufficiently small patch can make all \(s_i\) positive without changing \(ds_i\), and then \(V_i=s_i^2\) reproduces the same local metric. This is standard local surface geometry; see do Carmo [doCarmo1976].

Globally, however, Hilbert's theorem forbids a complete regular isometric immersion of the full constant-negative-curvature hyperbolic plane into \(\mathbb R^3\) [Hilbert1901; doCarmo1976]. Therefore:

> **Result XVIII.4 (three-species global obstruction).** Three diagonal scalar mass functions cannot reproduce the complete Poincare metric on all of \(\mathbb H\) through a regular mass map.

If the masses are modular invariant and the equality is required upstairs on \(\mathbb H\), the same obstruction applies before quotienting.

---

## 7. Predictivity boundary

The previous results separate two very different claims.

### 7.1 Genuine prediction would require

A microscopic FCIG construction that independently fixes:

1. the number and statistics of heavy species;
2. their operators and mixings;
3. the functions \(V_i(\Phi)\);
4. the renormalization/matching prescription;
5. modular/orbifold transformation laws;
6. the physical normalization relating the determinant response to the sigma kinetic term.

Only then could one compare the resulting \(G^{\rm ind}\) with \(G_{\rm hyp}\) without fitting.

### 7.2 What fails if masses are arbitrary

Because

\[
G^{\rm ind}\propto s^*\delta,
\]

choosing the mass map is mathematically the same as choosing Euclidean embedding coordinates for the desired target metric. Local hyperbolic fitting can already be engineered with three unconstrained functions. Thus an exact local match obtained by solving backwards for \(V_i\) is not a prediction of FCIG; it merely hides the target metric inside the mass spectrum.

This is the central constitutive-input no-go of Model XVIII.

\[
\boxed{
\text{determinant induces a metric only after the operator spectrum is supplied;}
\quad
\text{an arbitrary spectrum can encode the metric by construction.}
}
\]

---

## 8. Relation to Models XVI--XVII

The controlled chain is now

\[
(\mathscr L_{\rm FCIG},\nabla)
\xrightarrow{\Phi^*}
P(\Phi)
\xrightarrow{\frac12\log\det}
W_{\rm 1PI}[\Phi]
\xrightarrow{p^2\text{ response}}
G^{\rm ind}_{AB}.
\]

Model XVI showed that pulled-back line curvature enters the four-derivative \(\Omega^2\) heat-kernel sector. Model XVII showed that a two-derivative Poincare sigma metric can be written using pre-existing target geometry but its normalization was external. Model XVIII now shows:

\[
\boxed{
\begin{aligned}
&\text{one diagonal mass species} &&\Rightarrow \operatorname{rank}\le1,\\
&\text{two species} &&\Rightarrow K=0\text{ where nondegenerate},\\
&\text{three species} &&\Rightarrow \text{local fitting possible, global complete }\mathbb H\text{ impossible in }\mathbb R^3.
\end{aligned}
}
\]

The remaining question is no longer whether a determinant can *mathematically* generate a two-derivative metric. It can. The question is whether FCIG itself fixes a non-arbitrary microscopic operator family whose determinant produces the pre-existing Hodge/Poincare geometry.

---

## 9. Method caveat

Chan developed a systematic derivative expansion for functional determinants with spacetime-dependent backgrounds [Chan1986], and modern covariant derivative-expansion methods provide a broad EFT framework [HenningLuMurayama2018]. However, Canevarolo--Prokopec report that a midpoint/Wigner-space one-loop gradient expansion gives a vanishing single-scalar correction and emphasize nontrivial constraints on gradient expansions [CanevaroloProkopec2024].

Accordingly, all rank and curvature statements in this note refer to the **explicitly defined constant-background 1PI two-point \(p^2\) response** above. They should not be read as a proof that every off-shell global derivative-expansion prescription produces the same local functional.

---

## 10. References used in this milestone

- L.-H. Chan, *Derivative Expansion for the One-Loop Effective Actions with Internal Symmetry*, Phys. Rev. Lett. **57** (1986) 1199--1202. [Chan1986]
- B. Henning, X. Lu, H. Murayama, *One-loop matching and running with covariant derivative expansion*, JHEP **2018** (2018) 123. [HenningLuMurayama2018]
- S. Canevarolo, T. Prokopec, *Gradient corrections to the quantum effective action*, JHEP **2024** (2024) 037. [CanevaroloProkopec2024]
- NIST DLMF, Chapter 23, especially \S23.18, modular invariance of Klein's complete invariant. [DLMF23]
- M. P. do Carmo, *Differential Geometry of Curves and Surfaces*, Prentice-Hall (1976). [doCarmo1976]
- D. Hilbert, *Ueber Flächen von constanter Gaussscher Krümmung*, Trans. Amer. Math. Soc. **2** (1901), 87--99. [Hilbert1901]

## Bottom line

\[
\boxed{
\text{The determinant route reaches the target metric only if the microscopic mass map carries enough geometry.}
}
\]

For one or two diagonal species there are exact obstructions; for three species local fitting becomes possible but complete global hyperbolic fitting is obstructed. Once enough freely chosen spectral data are allowed, matching becomes an inverse-design problem rather than an FCIG prediction.
