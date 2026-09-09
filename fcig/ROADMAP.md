# FCIG Research Roadmap

**Current target:** v0.14 — background-field functional response audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.6 — geometry, determinants and differential characters — COMPLETE

The flat and curved laboratories established exact theta/state-count models, local/global Bergman sectors, determinant lines, Quillen versus \(L^2\) metrics, analytic torsion, and degree-two differential characters carrying topology, curvature, and holonomy.

---

## v0.7–v0.8 — transgression and factorized pushforward — COMPLETE

Loop transgression is a genuine response operation,

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z),
\]

while factorized degree-restoring pushforwards satisfy

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=n\widehat{\mathcal A}
}
\]

and therefore cannot generate a new independent degree-two response direction.

---

## v0.9–v0.10 — \(\widehat\kappa_1\), Quillen, and global Deligne--RR — COMPLETE

For a smooth curve family,

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(K_{X/B})^2\bigr),
\]

and the metrized Deligne-pairing realization gives the global connection-level identity

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q.
}
\]

---

## v0.11 — target-structure / nonabelian bridge audit — COMPLETE

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

Fixing the determinant connection leaves an affine space over \(\Omega^1(M;\mathfrak{su}(E))\), so determinant data cannot reconstruct generic nonabelian frame geometry for \(n>1\). Kähler/Ricci, K3, and Spin\(^c\) tests make the loss explicit.

Source: `structure-group-bridge.md`.

---

## v0.12 — mixed characteristic-class / anomaly-polynomial audit — COMPLETE

With independent line and frame connections,

\[
\boxed{
\widehat c_1(L)\cup\widehat p_1(TM)
\in\widehat H^6(M;\mathbf Z)
}
\]

is a standard mixed invariant. The line-twisted Dirac index gives

\[
\boxed{
I_6
=
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac16c_1^3-rac1{24}c_1p_1.
}
\]

The class has degree six, so it is not itself a local four-form action density in four dimensions. The generic semisimple orthogonal frame sector also has no first-Chern-type real degree-two Chern--Weil polynomial; \(SO(2)\cong U(1)\) is the explicit abelian exception.

Source: `mixed-characteristic.md`.

---

## v0.13 — explicit descent / anomaly inflow — COMPLETE

Sources:

- `descent-inflow.md`
- `descent-inflow.py`
- `descent-inflow.bib`

### Gate AN — local five-dimensional secondary form — PASS

On a local trivialization with normalized \(da=c\),

\[
\boxed{
I_5^{(0)}
=
a\wedge\left(\frac16c^2-\frac1{24}p_1\right),
\qquad
dI_5^{(0)}=I_6.
}
\]

### Gate AO — boundary gauge descent — PASS

Under \(a\mapsto a+d\alpha\),

\[
\boxed{
\delta_\alpha I_5^{(0)}
=
d\left[
\alpha\left(\frac16c^2-\frac1{24}p_1\right)
\right].
}
\]

Thus the five-dimensional bulk variation reduces to a four-dimensional boundary anomaly form.

### Gate AP — global refinement / quantization — PASS WITH QUALIFICATION

The integral product

\[
\widehat c_1\cup\widehat p_1
\]

is an ordinary degree-six differential character. By contrast,

\[
\frac16c_1^3-rac1{24}c_1p_1
\]

has rational coefficients and must not be declared an arbitrary integral differential character term-by-term.

For a closed spin six-manifold with line twist,

\[
\boxed{
\int_Z[\widehat A(TZ)\operatorname{ch}(L)]_{(6)}
=
\operatorname{Index}(D_L)
\in\mathbf Z.
}
\]

Therefore the global fermionic anomaly/inflow phase is correctly quantized by the Dirac index / Dai--Freed anomaly theory. Local Chern--Simons potentials are only secondary representatives.

### Gate AQ — response-type audit — PASS WITH NO-GO

\[
\boxed{
\text{anomaly descent}
\neq
\text{stress-energy response}
\neq
\text{horizon thermodynamics}.
}
\]

The anomaly polynomial controls symmetry/anomaly response. It does not reconstruct the full metric dependence of an effective action or supply a Clausius/horizon law.

References: Zumino--Wu--Zee; Bardeen--Zumino; Alvarez-Gaumé--Ginsparg; Cheeger--Simons; Bär--Becker; Dai--Freed; Freed.

### v0.13 conclusion

\[
\boxed{
\text{index polynomial}
\to
\text{5D secondary/inflow data}
\to
\text{4D symmetry anomaly}
}
\]

is now explicit and globally audited. No Einstein equation follows from it.

---

## v0.14 — background-field functional response audit — ACTIVE

The next bottleneck is dynamical rather than topological.

Let \(\mathcal B\) denote a space of background gauge and metric/frame fields. The anomaly/determinant line over \(\mathcal B\) carries connection curvature and holonomy, but a physical effective action \(W[A,g]\) contains additional functional information.

### Gate AR — background-space geometry

Specify the background space \(\mathcal B\), the determinant/anomaly line over it, and the meaning of tangent directions corresponding to \(\delta A\) and \(\delta g\).

### Gate AS — current response

Audit the distinction between anomaly-line connection data and the functional derivative

\[
J^\mu
\sim
\frac{\delta W}{\delta A_\mu}.
\]

An anomaly determines a failure of symmetry/conservation, not the full current functional.

### Gate AT — stress-energy response

Audit

\[
T_{\mu\nu}
\sim
\frac{\delta W}{\delta g^{\mu\nu}}
\]

and determine which parts of the determinant/Quillen data constrain metric variation. Do not infer \(T_{\mu\nu}\) from the anomaly polynomial alone.

### Gate AU — trace / diffeomorphism anomaly distinction

Separate gauge anomalies, diffeomorphism anomalies, and trace/Weyl anomalies. Their Ward identities and dimensions differ.

### Gate AV — pre-thermodynamic no-go

Record explicitly what extra constitutive/effective-action information is still missing before any Jacobson-style local horizon argument can be tested.

---

## Gravity Closure gate — NOT ACTIVE

A future gravitational closure still requires:

1. an actual Lorentzian spacetime/base object;
2. an independently specified frame/tangent connection;
3. a controlled effective or constitutive dynamical principle;
4. causal horizons and temperature;
5. a justified entropy functional;
6. a known gravitational limit;
7. a falsification route.
