# FCIG Research Roadmap

**Current target:** v0.15 — constitutive / semiclassical closure audit  
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
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)=n\widehat{\mathcal A}
}
\]

and therefore cannot generate a new independent degree-two response direction.

---

## v0.9–v0.10 — \(\widehat\kappa_1\), Quillen, and global Deligne--RR — COMPLETE

For a smooth curve family,

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(K_{X/B})^2\bigr),
\qquad
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the fixed metrized Deligne-pairing convention.

---

## v0.11 — target-structure / nonabelian bridge audit — COMPLETE

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

Fixing the determinant connection leaves an affine space over \(\Omega^1(M;\mathfrak{su}(E))\). Therefore determinant data cannot reconstruct generic nonabelian frame geometry for \(n>1\). Kähler/Ricci, K3, and Spin\(^c\) tests make the information loss explicit.

---

## v0.12 — mixed characteristic-class / anomaly-polynomial audit — COMPLETE

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z)
\]

is a standard mixed invariant, and

\[
\boxed{
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1.
}
\]

Its degree-six nature blocks a direct interpretation as a local 4D action density.

---

## v0.13 — explicit descent / anomaly inflow — COMPLETE

On a local trivialization with \(da=c\),

\[
I_5^{(0)}
=a\wedge\left(\frac16c^2-\frac1{24}p_1\right),
\qquad
dI_5^{(0)}=I_6,
\]

and under \(a\mapsto a+d\alpha\),

\[
\delta I_5^{(0)}
=d\left[\alpha\left(\frac16c^2-\frac1{24}p_1\right)\right].
\]

The global fermionic anomaly phase is quantized by the spin Dirac index / Dai--Freed theory; local Chern--Simons forms are secondary representatives.

---

## v0.14 — background-field functional response audit — COMPLETE

Sources:

- `functional-response.md`
- `functional-response.py`
- `functional-response.bib`

Let \(\mathcal B\) be a background-field space carrying gauge and metric/frame data, and

\[
(\mathscr L_{\rm an},\nabla^{\rm an})\to\mathcal B
\]

the anomaly line. A partition function is a section \(Z\), and only after a local trivialization may one write \(Z=e^{-W}\).

### Gate AR — background-field hierarchy — PASS

\[
\boxed{
(\mathscr L_{\rm an},\nabla)
\to Z
\to W\text{ locally}
\to (J,T)
}
\]

is the controlled hierarchy. The line/connection alone does not specify the section or local effective action.

### Gate AS — invariant-functional no-go — PASS WITH NO-GO

For any globally defined gauge/diffeomorphism-invariant functional \(S_{\rm inv}\),

\[
W'=W+S_{\rm inv}
\]

has the same gauge/diffeomorphism anomaly while

\[
\boxed{
J'^\mu-J^\mu
=\frac1{\sqrt{|g|}}\frac{\delta S_{\rm inv}}{\delta A_\mu},
\qquad
T'_{\mu\nu}-T_{\mu\nu}
=-\frac2{\sqrt{|g|}}\frac{\delta S_{\rm inv}}{\delta g^{\mu\nu}}.
}
\]

Thus effective actions realizing a fixed anomaly class form an affine family under invariant functionals.

### Gate AT — explicit Maxwell witness — PASS

In four dimensions take

\[
S_\beta=-\frac\beta4\int\sqrt{|g|}\,F_{\mu\nu}F^{\mu\nu}.
\]

It is gauge and diffeomorphism invariant and classically Weyl invariant. Yet

\[
\Delta J^\nu=\beta\nabla_\mu F^{\mu\nu},
\]

and

\[
\boxed{
\Delta T_{\mu\nu}
=\beta\left(F_{\mu\rho}F_\nu{}^\rho-\frac14g_{\mu\nu}F^2\right)
}
\]

are generically nonzero. In \(d=4\), \(\Delta T^\mu{}_{\mu}=0\).

Therefore even equal gauge, diffeomorphism and Weyl anomaly data do not fix the full current or stress tensor.

### Gate AU — consistent/covariant current audit — PASS

The consistent current is obtained from one effective action,

\[
J_{\rm cons}\sim\frac{\delta W}{\delta A},
\]

while Bardeen--Zumino improvement gives

\[
J_{\rm cov}=J_{\rm cons}+J_{\rm BZ}.
\]

The two notions have different integrability/covariance properties. Local counterterms can change representatives without changing the underlying anomaly class.

### Gate AV — anomaly-line curvature versus first response — PASS WITH NO-GO

For fixed \((\mathscr L_{\rm an},\nabla)\),

\[
Z' = e^{-S_{\rm inv}}Z
\]

is a different section of the same line. The line curvature and holonomy are unchanged, but the first functional derivatives of \(-\log Z\) change.

Hence

\[
\boxed{
\text{same anomaly-line topology, curvature and holonomy}
\not\Rightarrow
\text{same }J\text{ or }T.
}
\]

### Gate AW — response-type separation — PASS

The following remain distinct:

1. gauge anomaly;
2. diffeomorphism anomaly;
3. Weyl/trace anomaly;
4. current response;
5. stress-energy response;
6. horizon/thermodynamic response.

### v0.14 conclusion

\[
\boxed{
\text{anomaly geometry constrains symmetry/integrability data,}
\quad
\text{but dynamics requires additional functional information.}
}
\]

The direct anomaly-to-Einstein route is therefore closed.

References: Wess--Zumino (1971); Bardeen--Zumino (1984); Osborn (1991); Freed (2014); Dai--Freed (1994); Birrell--Davies (1982).

---

## v0.15 — constitutive / semiclassical closure audit — ACTIVE

The next milestone must **add** a dynamical principle instead of trying to reconstruct it from anomaly data.

### Gate AX — explicit dynamical input

Choose and state one independent closure mechanism. Candidate mathematical forms include

\[
\delta_g\bigl(S_{\rm grav}[g]+W[A,g]\bigr)=0
\]

for a supplied gravitational action, or a separately justified local horizon/thermodynamic constitutive law.

No such input may be inferred from the anomaly class by analogy.

### Gate AY — FCIG insertion point

Identify exactly which FCIG quantity enters the chosen closure: state-count density, determinant/anomaly response, a renormalized effective-action term, or another derived observable. Do not identify these quantities with one another.

### Gate AZ — ambiguity propagation

Track the invariant-counterterm freedom of v0.14 through the proposed closure. A candidate gravitational prediction must either be invariant under the allowed scheme freedom or state how that freedom is fixed physically.

### Gate BA — Lorentzian/horizon data

If using a Jacobson-type route, independently specify local causal horizons, temperature/acceleration input, heat flux, and entropy functional before testing any Clausius relation.

### Gate BB — falsification / known limit

A closure proposal must produce a calculable limit or model that can fail. Recovering an Einstein-like equation by symbol matching is not a pass condition.

---

## Gravity Closure gate — NOT ACTIVE

A future gravitational closure still requires:

1. an actual Lorentzian spacetime/base object;
2. an independently specified frame/tangent connection;
3. a controlled effective or constitutive dynamical principle;
4. causal horizons and temperature if a thermodynamic route is chosen;
5. a justified entropy functional;
6. a known gravitational limit;
7. a falsification route.
