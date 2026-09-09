# FCIG Research Roadmap

**Current target:** v0.17 — realization-map / sigma-model dynamics audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.15 — geometry through conditional semiclassical closure — COMPLETE

Earlier milestones establish the geometric/determinant foundation, differential-cohomology local/global anomaly structure, transgression and pushforward no-gos, Deligne--RR closure, nonabelian reconstruction no-go, mixed anomaly polynomial and descent, the anomaly-to-first-response no-go, and the requirement that any gravitational dynamics enter through an explicit additional variational/constitutive principle.

The clean semiclassical insertion point is a derived physical functional \(W_{\rm FCIG}^{\rm ren}[g,\ldots]\), not the anomaly class by itself.

---

## v0.16 — explicit operator / heat-kernel effective-action bridge — COMPLETE WITH CONDITIONAL REALIZATION

Sources:

- `heat-kernel-bridge.md`
- `heat-kernel-bridge.py`
- `heat-kernel-bridge.bib`

### Gate BC — explicit operator/background map — PASS WITH ADDITIONAL DATA

Let \(M\) be a compact four-dimensional Euclidean background and supply

\[
\boxed{\Phi:M\to\mathcal B_{\rm FCIG}}.
\]

For an FCIG line with connection,

\[
L_M=\Phi^*\mathscr L_{\rm FCIG},
\qquad
\Omega=F_{L_M}=\Phi^*F_{\rm FCIG}.
\]

The realization map \(\Phi\) is additional data and is not derived by the current FCIG construction.

Use the Laplace-type operator

\[
P=-\left(g^{\mu\nu}\nabla_\mu\nabla_\nu+E\right)
\]

on the pulled-back bundle.

### Gate BD — heat-kernel coefficient audit — PASS

In the fixed convention,

\[
\operatorname{Tr}(e^{-tP})
\sim(4\pi t)^{-2}\int_M\sqrt g\,\operatorname{tr}(b_0+t b_2+t^2b_4+\cdots),
\]

with

\[
b_0=I,
\qquad
b_2=E+\frac16R,
\]

and

\[
\begin{aligned}
b_4=\frac1{360}\Big(&60\nabla^2E+60RE+180E^2+12\nabla^2R\\
&+5R^2-2R_{\mu\nu}R^{\mu\nu}+2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
+30\Omega_{\mu\nu}\Omega^{\mu\nu}\Big).
\end{aligned}
\]

These are standard Vassilevich/Gilkey heat-kernel coefficients.

### Gate BE — determinant / proper-time bridge — PASS

For a Gaussian one-loop determinant,

\[
W_{1\text{-loop}}=-\sigma\int_0^\infty\frac{dt}{t}\,\operatorname{Tr}(e^{-tP}).
\]

In four dimensions the UV local divergences are controlled by \(b_0,b_2,b_4\): quartic/volume, quadratic/Einstein--Hilbert-type, and logarithmic/curvature-squared sectors respectively.

### Gate BF — gravitational interpretation — PASS WITH RENORMALIZATION QUALIFICATION

The local UV hierarchy is

\[
\boxed{
b_0\to\text{volume/cosmological},\quad
b_2\to\text{Einstein--Hilbert},\quad
b_4\to\text{curvature-squared / bundle-curvature}.}
\]

Their divergent coefficients renormalize gravitational/matter couplings and are not parameter-free predictions.

### Gate BG — FCIG-specific comparison — PASS WITH NON-IDENTIFICATION

Since

\[
\Omega=\Phi^*F_{\rm FCIG},
\]

the local coefficient contains

\[
\boxed{
b_4^{\rm FCIG}\supset\frac1{12}(\Phi^*F_{\rm FCIG})_{\mu\nu}(\Phi^*F_{\rm FCIG})^{\mu\nu}.}
\]

This is a genuine operator/effective-action insertion of FCIG line curvature, but it does not identify FCIG curvature with frame/Riemann curvature.

Bergman and heat-kernel coefficient hierarchies remain distinct unless a further operator/functorial identification is supplied.

### Gate BH — metric variation / Wald test — PASS

After renormalization, local effective-action terms have ordinary metric variations and contribute to stress energy. Local curvature-dependent gravitational terms also possess the corresponding Wald/Iyer--Wald stationary-horizon entropy corrections.

A pure pulled-back \(\Omega^2\) term, when \(\Omega\) is independent of Riemann curvature, contributes to stress/backreaction but not directly to the Wald curvature derivative.

### Local/global check — PASS

If \(F_{\rm FCIG}=0\) but the line has nontrivial flat holonomy, then all local \(\Omega\)-polynomial heat coefficients vanish while the global determinant/spectrum may still retain holonomy dependence. The earlier FCIG local/global decomposition therefore survives the explicit physical-operator realization.

### v0.16 conclusion

\[
\boxed{
(\mathscr L_{\rm FCIG},\nabla^{\rm FCIG})+\Phi
\to P_\Phi
\to \operatorname{Tr}e^{-tP_\Phi}
\to W_{1\text{-loop}}^{\rm ren}[g,\Phi]
}
\]

is now an explicit conditional operator bridge.

References: Vassilevich (2003); Gilkey (1995); Birrell--Davies (1982); Wald (1993); Iyer--Wald (1994).

---

## v0.17 — realization-map / sigma-model dynamics audit — ACTIVE

The remaining new object is

\[
\Phi:M\to\mathcal B_{\rm FCIG}.
\]

The next milestone tests whether \(\Phi\) can be promoted from an arbitrary realization map to a controlled dynamical field using geometry genuinely present on the FCIG target.

### Gate BI — target metric provenance

Identify an actual positive/nondegenerate target metric \(G_{AB}\) on the relevant \(\mathcal B_{\rm FCIG}\) — e.g. a Fisher/Hessian/Kähler or moduli metric already established in a specific model. Do not invent a metric solely to write a sigma model.

### Gate BJ — sigma-model action and harmonic-map equation

Audit the candidate

\[
S_\Phi=\frac{Z_\Phi}{2}\int_M\sqrt g\,G_{AB}(\Phi)\,\partial_\mu\Phi^A\partial^\mu\Phi^B
\]

and derive its Euler--Lagrange/tension-field equation using the Levi--Civita connection of \(G\).

### Gate BK — stress tensor

Compute the ordinary spacetime stress tensor of \(\Phi\) and distinguish it from the FCIG anomaly-line curvature.

### Gate BL — coupling to the pulled-back line

Determine how \(\Phi\) simultaneously controls

\[
\Omega=\Phi^*F_{\rm FCIG}
\]

inside the v0.16 heat-kernel operator and whether the sigma-model equation couples consistently to that determinant sector.

### Gate BM — constitutive-input audit

Determine whether \(Z_\Phi\) and the sigma-model term are derived from prior FCIG spectral/index data or are independent EFT couplings. If independent, record that explicitly.

### Gate BN — explicit model / falsification

Use at least one concrete target, preferably the elliptic upper-half-plane/Hodge model or another target with explicit metric and line curvature. A proposal fails if its target metric, normalization or physical map is arbitrary in a way that defeats prediction.

**Pass condition:** a complete, typed sigma-model realization with a concrete target, equations of motion, stress tensor and coupling to the pulled-back FCIG line, together with a clear statement of which constants/data remain external.

---

## Gravity Closure gate — NOT ACTIVE

A sigma-model realization, even if successful, supplies an additional matter/response sector. It is not by itself a derivation of spacetime gravity. Lorentzian/horizon closure remains separate.