# FCIG Model XV — Constitutive / semiclassical closure audit

**Status:** Derived conditional bridge + explicit no-go, with established semiclassical-gravity and horizon-thermodynamics background.  
**Milestone:** v0.15.  
**Scope:** semiclassical variational closure, renormalization ambiguity, Jacobson/Wald horizon routes, and the exact insertion point of FCIG data.  
**Not claimed:** an FCIG derivation of Einstein dynamics from anomaly data alone.

---

## 1. Question after Model XIV

Model XIV established

\[
\boxed{
\text{same anomaly class}
\not\Rightarrow
\text{same }W
\not\Rightarrow
\text{same }J,T_{\mu\nu}.
}
\]

Therefore any route from FCIG to gravitational dynamics must add a dynamical or constitutive principle which is logically independent of the anomaly class.

This note audits two such routes:

1. **Semiclassical variational track** — supply a renormalized gravitational action and a renormalized matter/effective action, then vary the total action.
2. **Local-horizon track** — supply Lorentzian causal horizons, Unruh temperature, heat flux, an entropy law, and the Clausius relation in the sense of Jacobson.

The purpose is not to choose between them, but to determine what FCIG can legitimately supply to each.

---

## 2. Track A — semiclassical variational closure

### 2.1 Established background

Let

\[
S_{\rm grav}^{\rm ren}[g]
\]

be an independently specified renormalized gravitational action and

\[
W_{\rm ren}[A,g]
\]

a renormalized effective action of quantum fields on the same background.

Fix

\[
T_{\mu\nu}^{\rm ren}
:=-\frac{2}{\sqrt{|g|}}
\frac{\delta W_{\rm ren}}{\delta g^{\mu\nu}},
\]

and

\[
\mathcal E^{\rm grav}_{\mu\nu}
:=\frac{2}{\sqrt{|g|}}
\frac{\delta S_{\rm grav}^{\rm ren}}{\delta g^{\mu\nu}}.
\]

Then stationarity of the supplied total action,

\[
\delta_g\bigl(S_{\rm grav}^{\rm ren}+W_{\rm ren}\bigr)=0,
\]

is equivalent in these conventions to

\[
\boxed{
\mathcal E^{\rm grav}_{\mu\nu}
=T_{\mu\nu}^{\rm ren}.
}
\]

For an Einstein--Hilbert gravitational term this reproduces the usual semiclassical Einstein equation after the conventional normalization of Newton's constant and the cosmological constant. This is standard semiclassical-gravity structure; see Birrell--Davies and the curved-spacetime renormalization literature [BD82, Wald78, HW01, HW04].

### 2.2 Important logical direction

This is a **positive bridge**, but its direction is

\[
\boxed{
S_{\rm grav}^{\rm ren}
+W_{\rm ren}
+\text{variational principle}
\Longrightarrow
\text{semiclassical field equation}.
}
\]

It is not

\[
\text{anomaly class}
\Longrightarrow
S_{\rm grav}^{\rm ren}
\text{ or }W_{\rm ren}.
\]

The gravitational variational principle is additional input.

---

## 3. Renormalization ambiguity propagates into the field equation

### Established background

Local/covariant renormalization in curved spacetime admits finite local curvature counterterms. Schematically one may shift

\[
W_{\rm ren}
\mapsto
W_{\rm ren}+S_{\rm ct}[g],
\]

with

\[
S_{\rm ct}[g]
=\int_M\!\sqrt{|g|}\,
\bigl(
\delta\Lambda
+\delta Z_R R
+\alpha R^2
+\beta R_{\mu\nu}R^{\mu\nu}
+\cdots
\bigr).
\]

Wald's stress-tensor analysis and Hollands--Wald local covariance show that renormalized local observables are fixed only up to a finite family of local curvature terms/couplings [Wald78, HW01, HW04].

Therefore

\[
T_{\mu\nu}^{\rm ren}
\mapsto
T_{\mu\nu}^{\rm ren}
-\frac{2}{\sqrt{|g|}}
\frac{\delta S_{\rm ct}}{\delta g^{\mu\nu}}.
\]

### Derived consequence for FCIG

A candidate FCIG correction to semiclassical dynamics is not predictive until either

1. the corresponding local gravitational couplings are fixed by renormalization conditions / experiment, or
2. the FCIG construction itself supplies a scheme-fixing principle which is independently justified.

Thus

\[
\boxed{
\text{scheme-dependent }W_{\rm FCIG}
\not\Rightarrow
\text{scheme-independent gravitational prediction}.
}
\]

This is the v0.14 ambiguity propagated through the candidate field equation.

---

## 4. Exact FCIG insertion point in Track A

The determinant/anomaly line by itself is not enough. The legitimate insertion point is a **specified effective-action contribution**

\[
W_{\rm FCIG}[A,g]
\]

on a physical spacetime background.

If such a functional is derived, then FCIG contributes

\[
\boxed{
T_{\mu\nu}^{\rm FCIG}
:=-\frac{2}{\sqrt{|g|}}
\frac{\delta W_{\rm FCIG}}{\delta g^{\mu\nu}}
}
\]

and similarly a current

\[
J_{\rm FCIG}^{\mu}
:=\frac{1}{\sqrt{|g|}}
\frac{\delta W_{\rm FCIG}}{\delta A_\mu}.
\]

This is a conditional but mathematically ordinary bridge.

### Current FCIG status

Models I--XIV provide, among other things,

- state counts and Bergman densities;
- determinant/Quillen line geometry;
- differential characters and holonomy;
- anomaly polynomials and descent;
- exact no-go results for reconstructing full frame geometry or first functional response.

They do **not** yet provide a unique spacetime functional \(W_{\rm FCIG}[A,g]\).

Hence the next technical problem is naturally to derive local/nonlocal effective-action terms from an explicit operator family, rather than to identify anomaly curvature with a stress tensor.

---

## 5. Track B — Jacobson local-horizon closure

### 5.1 Established prerequisites

Jacobson's 1995 argument assumes a Lorentzian spacetime and demands the Clausius relation

\[
\boxed{\delta Q=T\,\delta S}
\]

for all local Rindler causal horizons through each spacetime point [Jac95]. The required ingredients include:

1. local causal/Rindler horizons;
2. an approximate boost Killing flow near the chosen horizon generator;
3. Unruh temperature associated with the accelerated observer;
4. matter heat flux through the local horizon;
5. an entropy variation proportional to horizon-area variation,
   \[
   \delta S=\eta\,\delta A;
   \]
6. the Raychaudhuri equation and local conservation input.

With these assumptions Jacobson obtains the Einstein equation, with the cosmological constant entering as an integration freedom. The key point for FCIG is that the horizon/temperature/entropy structure is **input to the thermodynamic closure**, not output of an anomaly line [Jac95].

### 5.2 Current FCIG entropy candidates do not yet meet this input

The present FCIG state-count hierarchy contains

\[
S_k^{\rm cap}=\log h^0(X,L^k)
\]

and a local normalized Bergman quantity

\[
s_k(x)=\log B_k(x)-d\log k.
\]

For positive compact complex geometry,

\[
S_k^{\rm cap}
=d\log k+O(1),
\]

while locally

\[
s_k(x)\sim \frac{c}{k}\,\mathrm{Scal}(x)+\cdots
\]

in the Bergman asymptotic regime.

### Derived no-go XV.1

As presently defined, neither quantity is automatically a Lorentzian codimension-two horizon entropy density proportional to area variation.

In particular, FCIG has not yet supplied a canonical map

\[
(X,L,k,B_k)
\longrightarrow
(\mathcal H_{\rm local},\delta A,\delta S)
\]

which is local, Lorentz covariant, independent of arbitrary polarization/quantization choices, and compatible with the Rindler scaling used by Jacobson.

Therefore

\[
\boxed{
S_k^{\rm cap}\text{ or }s_k
\not\equiv
\eta A
\quad\text{without an additional horizon map/limit.}
}
\]

This blocks a direct substitution of the existing FCIG entropy quantities into Jacobson's derivation.

---

## 6. A legitimate positive horizon bridge: effective Lagrangian \(\to\) Wald entropy

Wald's Noether-charge construction gives a separate positive route. For a supplied diffeomorphism-invariant local gravitational Lagrangian, stationary black-hole entropy is determined by the corresponding Noether charge [Wald93, IW94].

Therefore, if a future FCIG calculation derives a **local diffeomorphism-invariant spacetime effective Lagrangian contribution**

\[
\Delta L_{\rm FCIG}(g,R,\nabla R,\ldots),
\]

then the same term has two controlled consequences:

\[
\boxed{
\Delta L_{\rm FCIG}
\longrightarrow
\begin{cases}
\Delta \mathcal E_{\mu\nu} & \text{by metric variation},\\
\Delta S_{\rm Wald} & \text{by Noether charge on a stationary horizon}.
\end{cases}
}
\]

This is a real dynamics/entropy bridge because both responses come from the **same supplied local Lagrangian**.

It does not follow from the anomaly class alone.

A nonlocal determinant functional such as a full \(\log\det\) generally requires additional care; the standard local Wald formula applies directly to local diffeomorphism-invariant Lagrangians, not to an unspecified nonlocal functional.

---

## 7. Theorem XV.2 — minimal additional data required for closure

### Derived statement

Given the results of Models XI--XIV, an FCIG gravitational closure requires at least one of the following independent structures.

### Variational route

A tuple

\[
\boxed{
(M,g;\ S_{\rm grav}^{\rm ren};\ W_{\rm FCIG}^{\rm ren};\ \text{renormalization conditions})
}
\]

with a specified variational principle.

### Horizon route

A tuple

\[
\boxed{
(M,g_{\rm Lor};\ \mathcal H_{\rm local};\ T_{\rm Unruh};\ \delta Q;\ S_{\rm horizon};\ \delta Q=T\delta S)
}
\]

plus a derivation of the FCIG contribution to \(S_{\rm horizon}\).

Without one of these tuples, topology/anomaly/state-count data alone do not close the dynamical problem.

---

## 8. Gate audit

### Gate AX — explicit dynamical input: PASS WITH CONDITIONAL BRIDGE

The semiclassical action principle and the Jacobson Clausius principle are both explicit additional inputs. Neither is supplied by the anomaly class.

### Gate AY — FCIG insertion point: PASS WITH RESTRICTION

The clean semiclassical insertion point is a derived \(W_{\rm FCIG}^{\rm ren}[A,g]\). A clean stationary-horizon insertion point is a derived local \(\Delta L_{\rm FCIG}\), which then contributes through Wald entropy.

The existing state-count/Bergman quantities are not yet a Jacobson horizon entropy.

### Gate AZ — ambiguity propagation: PASS

Finite invariant/covariant counterterms shift \(T_{\mu\nu}\) and gravitational couplings. Predictions require scheme fixing or coupling renormalization.

### Gate BA — Lorentzian / horizon data: PASS WITH NO-GO FOR CURRENT FCIG

Jacobson's causal horizon, Unruh temperature, heat flux and area entropy are independent inputs. Current FCIG complex/Kähler state-count data do not provide them canonically.

### Gate BB — known limit / falsification: PASS

A valid semiclassical FCIG model must reduce to ordinary semiclassical gravity when the FCIG contribution is switched off.

A proposed horizon map is falsified if its entropy density retains arbitrary dependence on quantization level/polarization or fails to become a local Lorentz-covariant codimension-two density in the proposed physical limit.

---

## 9. What is now closed

The direct chain

\[
\boxed{
\text{FCIG anomaly/state count}
\Longrightarrow
\text{Einstein dynamics}
}
\]

is closed as an unsupported inference.

The controlled replacement is

\[
\boxed{
\text{FCIG observable}
\xrightarrow{\text{explicit spacetime realization}}
W_{\rm FCIG}\text{ or }\Delta L_{\rm FCIG}
\xrightarrow{\text{independent closure principle}}
\text{dynamical / horizon response}.
}
\]

The missing first arrow is now the principal technical target.

---

## 10. Next target

**v0.16 — local heat-kernel / effective-action bridge.**

The next model should start from an explicit elliptic/Dirac-type operator on a physical background and audit the proper-time/heat-kernel expansion of its determinant. The objective is to identify:

1. which local Seeley--DeWitt coefficients generate cosmological, Einstein--Hilbert and higher-curvature counterterms;
2. which pieces are scheme dependent and absorbed into renormalized gravitational couplings;
3. whether any FCIG-specific determinant/Bergman structure produces a controlled finite contribution to \(W_{\rm ren}\);
4. the corresponding metric variation and, where local, Wald entropy correction.

Only after this bridge is explicit should the horizon/thermodynamic track be re-opened.

---

## References used in this model

- [Jac95] T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State*, Phys. Rev. Lett. **75** (1995) 1260--1263.
- [Wald93] R. M. Wald, *Black Hole Entropy is the Noether Charge*, Phys. Rev. D **48** (1993) R3427--R3431.
- [IW94] V. Iyer and R. M. Wald, *Some Properties of Noether Charge and a Proposal for Dynamical Black Hole Entropy*, Phys. Rev. D **50** (1994) 846--864.
- [Wald78] R. M. Wald, *Trace Anomaly of a Conformally Invariant Quantum Field in Curved Spacetime*, Phys. Rev. D **17** (1978) 1477--1484.
- [HW01] S. Hollands and R. M. Wald, *Local Wick Polynomials and Time Ordered Products of Quantum Fields in Curved Spacetime*, Commun. Math. Phys. **223** (2001) 289--326.
- [HW04] S. Hollands and R. M. Wald, *Conservation of the Stress Tensor in Perturbative Interacting Quantum Field Theory in Curved Spacetimes*, Rev. Math. Phys. **17** (2005) 227--312.
- [BD82] N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space*, Cambridge University Press (1982).

### Citation boundary

The semiclassical variational framework, curved-spacetime renormalization ambiguity, Jacobson local-horizon assumptions, and Wald/Iyer--Wald Noether-charge entropy are established literature. The FCIG insertion/no-go statements and the comparison of the existing FCIG state-count hierarchy with the required Jacobson horizon entropy are **Derived here**.