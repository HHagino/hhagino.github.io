# FCIG Research Roadmap

**Current target:** v0.16 — local heat-kernel / effective-action bridge  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.10 — geometric, determinant, and differential-cohomology sector — COMPLETE

The flat/curved laboratories establish theta/state-count models, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos, and the global metrized Deligne--RR identity

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

for the canonical smooth curve-family model.

---

## v0.11 — target-structure / nonabelian bridge audit — COMPLETE

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

The determinant sector fixes trace/Ricci data but not a generic nonabelian frame connection for \(n>1\).

---

## v0.12–v0.13 — mixed anomaly polynomial and descent/inflow — COMPLETE

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z),
\]

and

\[
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1.
\]

Locally,

\[
I_5^{(0)}=a\wedge\left(\frac16c^2-\frac1{24}p_1\right),
\qquad dI_5^{(0)}=I_6,
\]

with standard four-dimensional boundary descent. Global quantization is controlled by the Dirac index / Dai--Freed anomaly theory.

---

## v0.14 — background-field functional response audit — COMPLETE WITH NO-GO

For invariant \(S_{\rm inv}\),

\[
W'=W+S_{\rm inv}
\]

has the same gauge/diffeomorphism anomaly while

\[
J'^\mu-J^\mu
=\frac1{\sqrt{|g|}}\frac{\delta S_{\rm inv}}{\delta A_\mu},
\qquad
T'_{\mu\nu}-T_{\mu\nu}
=-\frac2{\sqrt{|g|}}\frac{\delta S_{\rm inv}}{\delta g^{\mu\nu}}.
\]

Hence

\[
\boxed{
\text{same anomaly class}
\not\Rightarrow
\text{same }W,J,T_{\mu\nu}.
}
\]

The direct anomaly-to-Einstein route is closed.

---

## v0.15 — constitutive / semiclassical closure audit — COMPLETE WITH CONDITIONAL BRIDGE

Sources:

- `semiclassical-closure.md`
- `semiclassical-closure.py`
- `semiclassical-closure.bib`

### Gate AX — explicit dynamical input — PASS WITH CONDITIONAL BRIDGE

Supply independently

\[
S_{\rm grav}^{\rm ren}[g],
\qquad
W_{\rm ren}[A,g],
\]

and impose

\[
\delta_g\bigl(S_{\rm grav}^{\rm ren}+W_{\rm ren}\bigr)=0.
\]

With

\[
\mathcal E^{\rm grav}_{\mu\nu}
:=\frac{2}{\sqrt{|g|}}\frac{\delta S_{\rm grav}^{\rm ren}}{\delta g^{\mu\nu}},
\qquad
T_{\mu\nu}^{\rm ren}
:=-\frac{2}{\sqrt{|g|}}\frac{\delta W_{\rm ren}}{\delta g^{\mu\nu}},
\]

stationarity gives

\[
\boxed{\mathcal E^{\rm grav}_{\mu\nu}=T_{\mu\nu}^{\rm ren}}.
\]

The gravitational variational principle is additional input; it is not reconstructed from the anomaly class.

### Gate AY — FCIG insertion point — PASS WITH RESTRICTION

The legitimate semiclassical insertion point is a derived physical spacetime functional

\[
\boxed{W_{\rm FCIG}^{\rm ren}[A,g]}
\]

or, in a local derivative expansion, a local diffeomorphism-invariant term \(\Delta L_{\rm FCIG}\).

Then

\[
T_{\mu\nu}^{\rm FCIG}
=-\frac{2}{\sqrt{|g|}}
\frac{\delta W_{\rm FCIG}^{\rm ren}}{\delta g^{\mu\nu}}
\]

is an ordinary controlled contribution. Existing FCIG anomaly/state-count data do not yet determine this functional uniquely.

### Gate AZ — ambiguity propagation — PASS

Finite local curvature counterterms shift the renormalized stress tensor and the gravitational couplings. Scheme-independent predictions require fixed renormalization conditions/couplings or a separately justified scheme-fixing principle.

A transfer

\[
W\to W+S_{\rm ct},
\qquad
S_{\rm grav}\to S_{\rm grav}-S_{\rm ct}
\]

leaves the total action and stationarity condition invariant.

### Gate BA — Lorentzian / horizon data — PASS WITH CURRENT-FCIG NO-GO

Jacobson's 1995 route independently assumes local Rindler causal horizons, Unruh temperature, matter heat flux, an area-proportional entropy variation and the Clausius relation.

Current FCIG quantities

\[
S_k^{\rm cap}=\log h^0(X,L^k),
\qquad
s_k=\log B_k-d\log k
\]

do not yet define a canonical local Lorentz-covariant codimension-two horizon entropy density. A new horizon map/local limit is required.

### Gate BB — known limit / falsification — PASS

A semiclassical FCIG model must reduce to ordinary semiclassical gravity when its FCIG contribution is switched off.

A proposed FCIG horizon entropy map fails if arbitrary polarization/quantization-level dependence survives the physical horizon limit or if no local Lorentz-covariant entropy density emerges.

### Positive horizon bridge retained

If FCIG derives a local diffeomorphism-invariant spacetime term \(\Delta L_{\rm FCIG}\), then the same term contributes both to metric equations by variation and to stationary-horizon entropy through the Wald/Iyer--Wald Noether-charge construction.

This is a controlled bridge from a **derived local Lagrangian**, not from anomaly data alone.

References: Jacobson (1995); Wald (1993); Iyer--Wald (1994); Wald (1978); Hollands--Wald (2001, 2005); Birrell--Davies (1982).

### v0.15 conclusion

\[
\boxed{
\text{FCIG data}
\xrightarrow{\text{explicit spacetime realization}}
W_{\rm FCIG}\text{ or }\Delta L_{\rm FCIG}
\xrightarrow{\text{independent closure principle}}
\text{dynamical/horizon response}.
}
\]

The first arrow is now the principal technical bottleneck.

---

## v0.16 — local heat-kernel / effective-action bridge — ACTIVE

Start from an explicit elliptic/Dirac-type operator \(D\) on a physical spacetime/background and use its heat kernel to construct the determinant effective action.

### Gate BC — explicit operator/background map

Specify the physical background, field content, operator \(D\), bundle, connection, signature/Euclidean continuation, and the map from FCIG data to that operator family.

### Gate BD — heat-kernel coefficient audit

For a Laplace-type operator, audit

\[
\operatorname{Tr}(e^{-tD})
\sim
(4\pi t)^{-n/2}
\sum_{r\ge0} t^r A_{2r}(D),
\]

and identify which coefficients generate cosmological, Einstein--Hilbert and higher-curvature local terms in the one-loop determinant.

### Gate BE — renormalization split

Separate divergent/scheme-dependent local counterterms from finite or nonlocal terms. Match the former to renormalized gravitational couplings rather than treating them as predictions.

### Gate BF — FCIG-specific finite contribution

Determine whether the previously derived determinant/Bergman structures supply a controlled finite contribution after the physical operator map is fixed.

### Gate BG — metric variation / entropy consequence

Compute the metric variation of the resulting \(W_{\rm FCIG}^{\rm ren}\). If a local diffeomorphism-invariant term is obtained, compute its Wald entropy contribution as a consistency check.

**Pass condition:** an explicit operator-level bridge from FCIG data to a spacetime effective-action term with a controlled renormalization statement. A formal resemblance between heat-kernel coefficients and earlier FCIG curvature coefficients is not sufficient.

---

## Gravity Closure gate — NOT ACTIVE

The horizon/thermodynamic closure remains inactive until v0.16 or a later model provides an explicit physical spacetime effective-action/entropy realization.
