# FCIG Research Roadmap

**Current target:** v0.12 — mixed characteristic-class / anomaly-polynomial degree audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.6 — geometry, determinants and differential characters — COMPLETE

The flat and curved laboratories established exact theta/state-count models, local/global Bergman sectors, determinant lines, Quillen versus \(L^2\) metrics, analytic torsion, and degree-two differential characters carrying topology, curvature, and holonomy.

---

## v0.7 — response / transgression — COMPLETE

Loop transgression gives a genuine standard response

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z),
\]

while positive-dimensional fiber integration lowers degree.

---

## v0.8 — factorized pushforward — COMPLETE WITH NO-GO

For a smooth proper oriented real \(d\)-dimensional family \(p:Z\to M\),

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=n\widehat{\mathcal A}
}
\]

on each connected component. Factorized degree restoration cannot generate an independent degree-two response direction.

---

## v0.9 — non-factorized \(\widehat\kappa_1\) / Quillen comparison — COMPLETE

For a smooth family of curves, \(\omega=K_{X/B}\),

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(\omega)^2\bigr),
\]

and GRR plus the Quillen local-index theorem give

\[
I(\widehat\kappa_1)=12I(\widehat\lambda_Q),
\qquad
R(\widehat\kappa_1)=12R(\widehat\lambda_Q).
\]

---

## v0.10 — global metrized Deligne--Riemann--Roch closure — COMPLETE

The metrized Deligne-pairing realization closes the remaining flat ambiguity:

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q
}
\]

globally in the fixed convention, hence

\[
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
=
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}.
\]

Source: `global-deligne-rr.md`.

---

## v0.11 — target-structure / nonabelian bridge audit — COMPLETE

Source and checker:

- `structure-group-bridge.md`
- `structure-group-bridge.py`

### Gate AD — determinant trace bridge — PASS

The standard exact sequence

\[
\boxed{
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1
}
\]

induces

\[
\boxed{
F_{\det E}=\operatorname{Tr}F_E.
}
\]

Thus a nonabelian unitary connection canonically determines a determinant/trace \(U(1)\) connection.

### Gate AE — lift nonuniqueness — PASS WITH NO-GO

For two unitary connections on the same Hermitian bundle,

\[
\boxed{
\det\nabla'=\det\nabla
\iff
\nabla'-\nabla\in\Omega^1(M;\mathfrak{su}(E)).
}
\]

Hence fixing the determinant connection leaves an affine space of traceless nonabelian connection data. For \(n>1\), determinant data cannot reconstruct a generic \(U(n)\) connection.

The exceptional case \(n=1\) has \(SU(1)=\{1\}\). This explains why complex one-dimensional curve models can close much more completely in the determinant sector.

### Gate AF — Kähler canonical test — PASS WITH NO-GO

For Kähler tangent geometry,

\[
\det T^{1,0}M=K_M^{-1},
\qquad
c_1(T^{1,0}M,\nabla)=\frac{\rho_\omega}{2\pi}
\]

in the fixed convention. Thus determinant curvature is Ricci/trace curvature, not full Riemann curvature.

Ricci-flat K3 geometry gives an explicit witness: the determinant/canonical curvature can vanish while the full tangent curvature and \(SU(2)\) holonomy remain nontrivial.

### Gate AG — Spin\(^c\) extension bridge — PASS WITH NON-IDENTIFICATION

The standard group

\[
\operatorname{Spin}^c(n)
=\bigl(\operatorname{Spin}(n)\times U(1)\bigr)/\{\pm1\}
\]

combines frame and determinant-line data. A frame connection together with a determinant \(U(1)\) connection gives a \(Spin^c\) connection. The determinant line alone does not determine the frame connection.

### Gate AH — fixed-homomorphism audit — PASS WITH NO-GO

For any fixed homomorphism

\[
\varphi:U(1)\to G,
\]

the image of

\[
d\varphi:i\mathbf R\to\mathfrak g
\]

is at most one-dimensional and abelian. A connection induced from one \(U(1)\) field therefore cannot reproduce generic noncommuting curvature in a nonabelian frame group.

### v0.11 conclusion

\[
\boxed{
\begin{aligned}
\text{nonabelian connection}&\to\text{determinant/trace }U(1)&&\text{canonical},\\
\text{determinant }U(1)&\not\to\text{full nonabelian connection}&&\text{without extra data}.
\end{aligned}
}
\]

The FCIG determinant sector may constrain a trace/Ricci sector of target geometry, but the traceless frame sector must be supplied or dynamically determined independently.

References: Hall; Huybrechts; Lawson--Michelsohn; Yamashita; Yau; Huybrechts on K3 surfaces.

---

## v0.12 — mixed characteristic-class / anomaly-polynomial degree audit — ACTIVE

The next test **assumes the frame connection is an independent geometric field**. The objective is no longer to reconstruct it from \(U(1)\), but to determine which standard gauge-invariant characteristic classes can couple the two sectors without identifying their structure groups.

Let \(M\) carry

\[
\widehat a:=\widehat c_1(L,\nabla^L)\in\widehat H^2(M;\mathbf Z)
\]

and an independent oriented/spin/frame connection with differential Pontryagin class

\[
\widehat p_1(TM,\nabla^{\mathrm{fr}})\in\widehat H^4(M;\mathbf Z).
\]

### Gate AI — independent-field setup

Require an explicit common base \(M\), a line connection, and a frame connection. No structure-group identification is permitted.

### Gate AJ — Chern--Weil degree audit

Audit the first mixed product

\[
\boxed{
\widehat a\cup\widehat p_1(TM)
\in
\widehat H^6(M;\mathbf Z).
}
\]

Its curvature is a degree-six form proportional, in the chosen normalization, to

\[
F_L\wedge p_1(\Omega_{\mathrm{fr}}).
\]

No coefficient will be fixed until the anomaly-polynomial convention is audited from primary literature.

### Gate AK — four-dimensional no-go / descent alternatives

On a four-dimensional spacetime, a degree-six mixed characteristic class is not itself a local top-degree action density. A legitimate use must specify a descent/transgression, anomaly inflow from a higher-dimensional bulk, a boundary term, or an explicitly metric-dependent non-topological construction.

### Gate AL — gravitational degree-two no-go

Audit that an \(SO(n)\) frame connection has no canonical first Chern-type degree-two Chern--Weil class analogous to \(c_1(L)\); its first standard Pontryagin class appears in degree four. This blocks a naive degree-two equality between a determinant Chern form and a generic orthogonal gravitational characteristic class.

### Gate AM — anomaly-polynomial provenance

Compare the allowed mixed classes with established gauge/gravitational anomaly-polynomial formulas. Cite primary sources and keep exact numerical coefficients convention-dependent until checked.

**Pass condition:** identify at least one mathematically standard mixed invariant together with its correct degree and one explicit dimensional obstruction. No field equation is inferred from the existence of the invariant.

---

## Gravity Closure gate — NOT ACTIVE

The determinant sector and the inverse structure-group problem are no longer the bottleneck. A future gravitational closure would still require:

1. an actual physical spacetime/base object;
2. a map/correspondence from FCIG parameter geometry;
3. an independently specified frame/tangent connection;
4. Lorentzian causal structure;
5. a horizon/thermodynamic entropy functional;
6. a controlled dynamical principle or variational law;
7. a known gravitational limit and falsification route.
