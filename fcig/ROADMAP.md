# FCIG Research Roadmap

**Current target:** v0.13 — explicit descent / anomaly-inflow realization  
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

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=n\widehat{\mathcal A}
}
\]

on each connected component. Factorized degree restoration cannot generate an independent degree-two response direction.

---

## v0.9–v0.10 — \(\widehat\kappa_1\), Quillen, and global Deligne--RR — COMPLETE

For a smooth curve family,

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(K_{X/B})^2\bigr),
\]

and the metrized Deligne-pairing realization closes the comparison globally:

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q.
}
\]

Thus topology, curvature and loop holonomy satisfy the same connection-level identity.

---

## v0.11 — target-structure / nonabelian bridge audit — COMPLETE

The determinant sequence

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1
\]

induces

\[
F_{\det E}=\operatorname{Tr}F_E.
\]

But fixing the determinant connection leaves an affine space over

\[
\Omega^1(M;\mathfrak{su}(E)),
\]

so determinant data cannot reconstruct a generic nonabelian connection for \(n>1\). Kähler tangent geometry identifies the determinant curvature with Ricci/trace curvature; Ricci-flat K3 geometry gives an explicit loss-of-information witness. Spin\(^c\) gives a positive extension bridge only when the frame connection is supplied independently.

Source: `structure-group-bridge.md`.

---

## v0.12 — mixed characteristic-class / anomaly-polynomial degree audit — COMPLETE

Source and checker:

- `mixed-characteristic.md`
- `mixed-characteristic.py`
- `mixed-characteristic.bib`

### Gate AI — independent-field setup — PASS

On a common base \(M\), keep

\[
\widehat a:=\widehat c_1(L,\nabla^L)
\in\widehat H^2(M;\mathbf Z)
\]

and an independent frame connection with

\[
\widehat p_1(TM,\nabla^{\mathrm{fr}})
\in\widehat H^4(M;\mathbf Z).
\]

No structure-group identification is used.

### Gate AJ — mixed characteristic class — PASS

Differential-cohomology multiplication gives

\[
\boxed{
\widehat a\cup\widehat p_1(TM)
\in\widehat H^6(M;\mathbf Z).
}
\]

This is a genuine mixed invariant of the independent line and frame sectors.

### Gate AK — index/anomaly polynomial — PASS

Standard index theory gives

\[
\widehat A(TM)=1-\frac{p_1}{24}+\cdots,
\qquad
\operatorname{ch}(L)=e^{c_1},
\]

hence

\[
\boxed{
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac16c_1^3
-
\frac1{24}c_1p_1.
}
\]

Classic gauge/gravitational anomaly theory identifies the corresponding degree-six gauge and mixed gauge--gravitational structures as anomaly-polynomial data, with physical signs and \(2\pi\) conventions handled separately.

References: Alvarez-Gaumé--Witten; Zumino--Wu--Zee; Bardeen--Zumino; Alvarez-Gaumé--Ginsparg; Freed; Lawson--Michelsohn.

### Gate AL — four-dimensional dimensional audit — PASS WITH NO-GO

\[
\boxed{
\deg(c_1p_1)=6>4.
}
\]

A degree-six anomaly polynomial is not itself a local four-form action density on a four-manifold. Its four-dimensional role requires descent/transgression, anomaly inflow, a boundary/extension geometry, or another explicitly specified construction.

### Gate AM — gravitational degree-two audit — PASS WITH QUALIFIED NO-GO

For generic semisimple higher-rank orthogonal frame algebras there is no nonzero invariant linear Chern--Weil polynomial analogous to \(c_1\). The first Pontryagin class occurs in degree four. The abelian exception

\[
SO(2)\cong U(1)
\]

has a degree-two Euler/first-Chern class and is recorded explicitly.

### v0.12 conclusion

\[
\boxed{
\text{independent }U(1)\text{ connection}
+
\text{independent frame connection}
\longrightarrow
\text{mixed degree-six characteristic/anomaly class}
}
\]

is mathematically legitimate. It couples the two sectors at the invariant level without reconstructing one from the other.

But

\[
\boxed{
\text{anomaly polynomial}\neq\text{gravitational field equation}.
}
\]

---

## v0.13 — explicit descent / anomaly-inflow realization — ACTIVE

The next task is to make the degree-six class act on four-dimensional boundary data through a specified higher-dimensional geometry.

### Gate AN — five-dimensional secondary form

For an abelian normalized curvature \(c=dA\) and closed \(p_1\), construct a local secondary form for

\[
I_6=\frac16c^3-\frac1{24}cp_1.
\]

Locally one expects

\[
I_5^{(0)}
=A\wedge\left(\frac16c^2-\frac1{24}p_1\right),
\qquad
dI_5^{(0)}=I_6,
\]

with the normalization and global differential-cohomology meaning audited from anomaly-descent literature.

### Gate AO — boundary variation

Under the abelian transformation \(A\mapsto A+d\alpha\), audit

\[
\delta I_5^{(0)}
=d\left[\alpha\left(\frac16c^2-\frac1{24}p_1\right)\right].
\]

This supplies a four-dimensional boundary anomaly form, not an Einstein equation.

### Gate AP — global refinement

Replace the local potential-dependent Chern--Simons expression by the appropriate global differential character / anomaly-inflow datum when the line bundle is topologically nontrivial.

### Gate AQ — response-type audit

Separate:

1. gauge variation/anomaly response;
2. stress-energy response to metric variation;
3. horizon/thermodynamic response.

No equality among them is assumed.

---

## Gravity Closure gate — NOT ACTIVE

A future gravitational closure still requires:

1. an actual physical spacetime/base object;
2. a map/correspondence from FCIG parameter geometry;
3. an independently specified frame/tangent connection;
4. Lorentzian causal structure;
5. a horizon/thermodynamic entropy functional;
6. a controlled dynamical principle or variational law;
7. a known gravitational limit and falsification route.
