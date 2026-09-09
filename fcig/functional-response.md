# FCIG Model XIV — Background-field functional response and the anomaly-to-dynamics no-go

**Status:** Derived theorem/no-go with established QFT background.  
**Milestone:** v0.14.  
**Scope:** anomaly-line geometry, effective-action response, current/stress-tensor ambiguity.  
**Not claimed:** a Lorentzian gravitational field equation, horizon thermodynamics, or a derivation of Einstein dynamics.

---

## 1. Why this model is necessary

Models VI–XIII established a controlled chain

\[
\text{determinant/anomaly line}
\to
\text{differential character}
\to
\text{mixed characteristic class}
\to
\text{descent / inflow}.
\]

This determines genuine topological, curvature, holonomy and symmetry-anomaly data. It does **not** yet determine the first functional response of the quantum effective action to a background gauge field or metric.

The present model isolates that missing logical step.

The main conclusion is

\[
\boxed{
\text{same anomaly class}
\not\Rightarrow
\text{same effective action}
\not\Rightarrow
\text{same current or stress tensor}.
}
\]

This is not merely a statement about unknown coefficients. It follows from an explicit infinite-dimensional affine freedom.

---

## 2. Background-field hierarchy

Let \(\mathcal B\) be a space of backgrounds. For the present discussion a point is schematically

\[
b=(A,g,\ldots)\in\mathcal B,
\]

where \(A\) is a background gauge connection and \(g\) a background metric or frame geometry.

### Established structure

An anomalous quantum theory need not have a globally defined complex-valued partition function on \(\mathcal B\). Instead one may have a determinant/anomaly line

\[
\mathscr L_{\rm an}\longrightarrow\mathcal B
\]

with connection \(\nabla^{\rm an}\), and the partition function is a section

\[
Z\in\Gamma(\mathcal B,\mathscr L_{\rm an}).
\]

This is the geometric viewpoint used by determinant-line and Dai–Freed anomaly theory; see Freed (2014), Dai–Freed (1994), and the determinant-line references in earlier FCIG models.

On a patch \(U\subset\mathcal B\) where the line is trivialized and \(Z\neq0\), write

\[
Z=e^{-W}.
\]

The local effective action \(W\) therefore requires more information than the abstract line and its curvature: it requires a section and a local trivialization.

This gives the hierarchy

\[
\boxed{
(\mathscr L_{\rm an},\nabla^{\rm an})
\quad\supsetneq\quad
Z
\quad\supsetneq\quad
W\text{ locally}
\quad\to\quad
\delta W.
}
\]

The first-response observables live at the last step.

---

## 3. Current and stress tensor conventions

Fix the local conventions

\[
\boxed{
J^\mu_{\rm cons}
:=
\frac{1}{\sqrt{|g|}}\frac{\delta W}{\delta A_\mu},
}
\]

and

\[
\boxed{
T_{\mu\nu}
:=
-\frac{2}{\sqrt{|g|}}\frac{\delta W}{\delta g^{\mu\nu}}.
}
\]

The overall signs are conventional; none of the no-go statements below depend on them.

The first formula gives the **consistent** current because it is by construction the functional derivative of a single effective action. The distinction between consistent and covariant currents is reviewed in Section 8 below.

---

## 4. Main theorem: invariant-functional freedom

### Theorem XIV.1 — anomaly-preserving affine freedom

Let \(W[A,g]\) be a local representative of an effective action with a fixed gauge/diffeomorphism anomaly. Let

\[
S_{\rm inv}[A,g]
\]

be any globally defined functional invariant under the same gauge and diffeomorphism transformations. Define

\[
W':=W+S_{\rm inv}.
\]

Then

\[
\boxed{
\delta_{\rm gauge}W'
=
\delta_{\rm gauge}W,
\qquad
\delta_{\rm diff}W'
=
\delta_{\rm diff}W.
}
\]

But

\[
\boxed{
J'^\mu-J^\mu
=
\frac{1}{\sqrt{|g|}}
\frac{\delta S_{\rm inv}}{\delta A_\mu},
}
\]

and

\[
\boxed{
T'_{\mu\nu}-T_{\mu\nu}
=
-\frac{2}{\sqrt{|g|}}
\frac{\delta S_{\rm inv}}{\delta g^{\mu\nu}}.
}
\]

Hence the anomaly does not determine either first response.

### Proof

Gauge/diffeomorphism invariance of \(S_{\rm inv}\) gives

\[
\delta S_{\rm inv}=0
\]

for those transformations, so the anomalous variation is unchanged. Functional differentiation is linear, giving the displayed shifts in \(J\) and \(T\). \(\square\)

### Geometric interpretation

The set of effective actions realizing a fixed anomaly is an affine space under invariant functionals:

\[
\boxed{
\mathfrak W_{[\mathcal A]}
\text{ is affine over }
\mathcal F_{\rm inv}.
}
\]

The anomaly class fixes an obstruction/equivalence class, not a unique point of this affine space.

---

## 5. Same anomaly line, different section

There is an even sharper line-bundle version.

Fix the same anomaly line with connection

\[
(\mathscr L_{\rm an},\nabla^{\rm an}).
\]

For a globally defined invariant functional \(S_{\rm inv}\), define a new section

\[
Z':=e^{-S_{\rm inv}}Z.
\]

Then \(Z\) and \(Z'\) are sections of the **same** line with the **same** connection. Therefore the underlying

\[
\boxed{
F_{\nabla^{\rm an}}
\quad\text{and}\quad
\operatorname{Hol}_{\nabla^{\rm an}}
}
\]

are unchanged.

In a common local trivialization,

\[
W'=W+S_{\rm inv}.
\]

Thus

\[
\boxed{
\text{same anomaly-line topology, curvature and holonomy}
\not\Rightarrow
\text{same first functional response}.
}
\]

This is the differential-geometric form of Theorem XIV.1.

It also explains a common type error: the curvature of the anomaly line is a two-form on **background-field space**; the stress tensor is a first functional derivative with respect to the spacetime metric. These are different differential degrees on different spaces.

---

## 6. Explicit four-dimensional counterexample

The abstract freedom can be made concrete.

Work on a closed four-dimensional background, or take compactly supported variations so boundary terms vanish. Let

\[
\boxed{
S_\beta[A,g]
=
-\frac{\beta}{4}
\int_M d^4x\,\sqrt{|g|}\,
F_{\mu\nu}F^{\mu\nu}.
}
\]

For constant \(\beta\), this is gauge invariant and diffeomorphism invariant.

In four dimensions it is also classically Weyl invariant:

\[
\sqrt{|g|}\mapsto e^{4\sigma}\sqrt{|g|},
\qquad
F_{\mu\nu}F^{\mu\nu}\mapsto e^{-4\sigma}F_{\mu\nu}F^{\mu\nu}.
\]

Therefore adding \(S_\beta\) does not change the gauge, diffeomorphism, or classical Weyl variation of \(W\).

### 6.1 Current shift

Varying \(A\) gives, after integration by parts,

\[
\boxed{
\Delta J^\nu
=
\beta\nabla_\mu F^{\mu\nu}
}
\]

in the current convention of Section 3.

This is generically nonzero.

### 6.2 Stress-tensor shift

Metric variation gives

\[
\boxed{
\Delta T_{\mu\nu}
=
\beta\left(
F_{\mu\rho}F_\nu{}^\rho
-
\frac14g_{\mu\nu}F_{\rho\sigma}F^{\rho\sigma}
\right).
}
\]

Again this is generically nonzero.

### 6.3 Four-dimensional trace check

Contracting indices,

\[
\Delta T^\mu{}_{\mu}
=
\beta\left(1-\frac d4\right)F^2.
\]

Hence at \(d=4\),

\[
\boxed{
\Delta T^\mu{}_{\mu}=0.
}
\]

Therefore even fixing the gauge anomaly, diffeomorphism anomaly, **and** Weyl/trace anomaly does not determine the full current or stress tensor.

This is the explicit witness promised in Gate AT.

---

## 7. Ward identities do not determine the full response

An anomaly gives a Ward-identity obstruction, schematically

\[
\nabla_\mu J^\mu=\mathcal A_{\rm gauge},
\]

or

\[
\nabla_\mu T^{\mu}{}_{\nu}
=
\mathcal A^{\rm diff}_{\nu}
+\text{background-force terms},
\]

while a Weyl anomaly fixes a trace equation

\[
T^\mu{}_{\mu}=\mathcal A_{\rm Weyl}.
\]

These are constraints on divergences and/or traces. They are not a reconstruction formula for the full tensor fields.

The Maxwell deformation in Section 6 supplies a nonzero conserved/traceless response deformation compatible with the same anomaly data in four dimensions.

Thus

\[
\boxed{
(\nabla\!\cdot J,\ \nabla\!\cdot T,\ \operatorname{tr}T)
\text{ do not determine }(J,T).
}
\]

This is a second, purely response-theoretic obstruction independent of the determinant-line argument.

---

## 8. Consistent versus covariant current

### Established result

For an anomalous gauge theory, the current obtained by differentiating one effective action is the consistent current:

\[
J_{\rm cons}\sim\frac{\delta W}{\delta A}.
\]

It satisfies the Wess–Zumino consistency condition because the anomaly is the variation of the effective action. Wess and Zumino (1971) established the integrability/consistency condition for anomalous Ward identities.

Bardeen and Zumino (1984) showed that one can add a local Bardeen–Zumino current/polynomial to obtain a covariant current,

\[
\boxed{
J_{\rm cov}
=
J_{\rm cons}+J_{\rm BZ}.
}
\]

The covariant current transforms covariantly, but it is not in general the functional derivative of a single effective action.

This yields two logically distinct ambiguities:

1. **Invariant-functional freedom:** \(W\mapsto W+S_{\rm inv}\) leaves even the anomaly representative unchanged but shifts first responses.
2. **Counterterm/Bardeen–Zumino freedom:** local non-invariant counterterms and BZ polynomials can move between anomaly representatives/current conventions while preserving the underlying anomaly cohomology class.

Therefore neither the anomaly class nor one chosen local anomaly representative uniquely fixes a physical current without additional renormalization and operator conventions.

References: Wess–Zumino (1971), Bardeen–Zumino (1984), Osborn (1991).

---

## 9. Weyl anomaly is a different response channel

A Weyl variation acts schematically by

\[
\delta_\sigma g_{\mu\nu}=2\sigma g_{\mu\nu}.
\]

The associated anomaly constrains the trace of the stress tensor,

\[
\delta_\sigma W
\sim
\int\sqrt{|g|}\,\sigma\,T^\mu{}_{\mu}.
\]

This is distinct from

- a gauge anomaly,
- a diffeomorphism anomaly,
- the complete stress tensor,
- and the anomaly-line curvature over the full background space.

Osborn's local renormalization-group framework is a standard setting in which local Weyl variations, background couplings and counterterm/scheme dependence are treated systematically.

The Maxwell witness makes the separation explicit: in \(d=4\), \(S_\beta\) shifts \(T_{\mu\nu}\) while its trace remains zero.

Hence

\[
\boxed{
\text{trace anomaly}
\not\Rightarrow
\text{full stress tensor}.
}
\]

---

## 10. Curvature on background space is not a constitutive law

Let

\[
\mathcal F_{\rm an}=F_{\nabla^{\rm an}}
\in\Omega^2(\mathcal B)
\]

be the curvature of the anomaly line over background space.

It measures the infinitesimal failure of parallel transport/integrability around two-parameter background variations. It is therefore naturally a **second antisymmetrized response on \(\mathcal B\)**.

By contrast,

\[
J\sim\frac{\delta W}{\delta A},
\qquad
T\sim\frac{\delta W}{\delta g}
\]

are first derivatives of a chosen local functional representative.

Knowing a two-form curvature does not select a unique section of a line bundle. In the same way, anomaly curvature does not select a unique effective action or constitutive response.

The mathematical analogy is exact:

\[
\boxed{
\text{curvature fixes the curl/obstruction data, not the potential/section uniquely}.
}
\]

A globally defined invariant functional changes the section while leaving the anomaly line and its curvature untouched.

---

## 11. The direct anomaly-to-Einstein route is closed

Combining Models XI–XIV gives

\[
\boxed{
\begin{aligned}
\text{determinant }U(1)
&\not\Rightarrow
\text{full frame connection},\\
\text{anomaly class}
&\not\Rightarrow
\text{unique effective action},\\
\text{anomaly class}
&\not\Rightarrow
\text{unique }J^\mu,\\
\text{anomaly class}
&\not\Rightarrow
\text{unique }T_{\mu\nu}.
\end{aligned}
}
\]

Therefore a gravitational field equation cannot be extracted from the determinant/anomaly data alone.

To obtain dynamics one must add an independent dynamical/constitutive principle. Examples of the **type** of missing input are

- a gravitational action and a variational principle,
- a constitutive relation selecting one effective response,
- or a separate thermodynamic/horizon closure law.

FCIG does not yet choose among these.

---

## 12. What a legitimate semiclassical variational closure would look like

If one independently supplies a gravitational functional

\[
S_{\rm grav}[g]
\]

and a renormalized matter effective action

\[
W[A,g],
\]

then a semiclassical variational principle would have the form

\[
\boxed{
\delta_g\left(S_{\rm grav}[g]+W[A,g]\right)=0.
}
\]

This can produce a metric field equation because the gravitational action has been supplied as **additional data**.

But the anomaly line does not determine \(S_{\rm grav}\), and Theorem XIV.1 shows that it does not uniquely determine \(W\) either.

Thus a statement of the form

\[
\text{anomaly}\Rightarrow\text{Einstein equation}
\]

is not justified by Models I–XIV.

---

## 13. Relation to Jacobson-type closure

Jacobson's thermodynamic route requires additional physical inputs: local causal horizons, an entropy assignment, temperature/acceleration input, a heat flux and a Clausius-type relation. Those ingredients are not contained in the anomaly class by themselves.

Accordingly the correct future FCIG question is no longer

> Can the anomaly determine gravity?

but rather

> Can the FCIG state-count/anomaly data provide one controlled ingredient in an independently specified constitutive or horizon-thermodynamic closure?

That is a different and testable question.

---

## 14. Gate results

### Gate AR — background-field hierarchy

**PASS.**

\[
(\mathscr L_{\rm an},\nabla)
\to Z
\to W\text{ locally}
\to(J,T)
\]

is the correct hierarchy; each arrow requires additional data.

### Gate AS — invariant-functional no-go

**PASS WITH NO-GO.**

\[
W\sim W+S_{\rm inv}
\]

preserves gauge/diffeomorphism anomaly but changes first response.

### Gate AT — explicit Maxwell counterexample

**PASS.**

In four dimensions \(S_\beta\) changes both \(J\) and \(T\) while preserving gauge/diffeomorphism invariance and classical Weyl invariance.

### Gate AU — consistent/covariant current audit

**PASS.**

Bardeen–Zumino improvement distinguishes the current obtained from the effective action from the covariant current.

### Gate AV — anomaly curvature versus first response

**PASS WITH NO-GO.**

The same anomaly line/connection admits inequivalent sections related by invariant functionals; curvature/holonomy therefore do not determine first functional derivatives.

### Gate AW — response-type separation

**PASS.**

Gauge, diffeomorphism and Weyl anomalies, current response, stress-energy response, and horizon thermodynamics remain distinct structures.

---

## 15. Model XIV conclusion

The controlled statement is

\[
\boxed{
\text{anomaly geometry constrains symmetry/integrability data,}
\quad
\text{but dynamics requires additional functional information.}
}
\]

More sharply,

\[
\boxed{
\text{same anomaly line + same curvature + same holonomy}
\not\Rightarrow
\text{same }J\text{ or }T_{\mu\nu}.
}
\]

This closes the direct anomaly-to-dynamics route.

The next legitimate FCIG milestone should therefore test a **separately specified constitutive or gravitational closure**, rather than attempting another reconstruction from anomaly data alone.

---

## References used in this model

- J. Wess and B. Zumino, *Consequences of anomalous Ward identities*, Physics Letters B **37** (1971), 95–97, DOI 10.1016/0370-2693(71)90582-X.
- W. A. Bardeen and B. Zumino, *Consistent and covariant anomalies in gauge and gravitational theories*, Nuclear Physics B **244** (1984), 421–453, DOI 10.1016/0550-3213(84)90322-5.
- H. Osborn, *Weyl consistency conditions and a local renormalisation group equation for general renormalisable field theories*, Nuclear Physics B **363** (1991), 486–526, DOI 10.1016/0550-3213(91)80030-P.
- D. S. Freed, *Anomalies and Invertible Field Theories*, arXiv:1404.7224 (2014).
- X. Dai and D. S. Freed, *Eta-Invariants and Determinant Lines*, Journal of Mathematical Physics **35** (1994), 5155–5194, DOI 10.1063/1.530747.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space*, Cambridge University Press (1982), DOI 10.1017/CBO9780511622632.
