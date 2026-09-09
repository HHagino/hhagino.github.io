# FCIG Explicit Model XIII: Five-Dimensional Descent, Global Inflow, and the Index-Quantization Audit

**Status:** citation-audited research note  
**Milestone:** v0.13 — explicit descent / anomaly-inflow realization  
**Updated:** 2026-09-09

## Citation policy

- **Established** — standard anomaly descent, index, differential-character, and Dai--Freed results with references.
- **Derived here** — explicit abelian transgression algebra in the fixed topological normalization.
- **FCIG consequence** — architectural interpretation only.
- **No-go / correction** — an identification that fails unless additional quantization or global data are supplied.

This note sharply distinguishes three objects:

1. an **integral differential characteristic class**, such as \(\widehat c_1\cup\widehat p_1\);
2. the **rational index polynomial** \([\widehat A\operatorname{ch}]_6\);
3. the **global fermionic anomaly theory**, whose quantization is controlled by the Dirac index / eta invariant rather than by pretending every rational polynomial is an arbitrary integral Cheeger--Simons character.

---

## 1. Starting point from Model XII

Let \(M\) carry an independently specified unitary line connection and frame connection. Write the normalized abelian curvature

\[
c:=\frac{F_L}{2\pi i},
\]

and use the standard normalized first Pontryagin form \(p_1\) for the frame connection.

For a charge-one line twist, the degree-six index polynomial is

\[
\boxed{
I_6
:=
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac16c^3-rac1{24}c\,p_1.
}
\]

For charge \(q\),

\[
\boxed{
I_6(q)
=
\frac{q^3}{6}c^3-rac{q}{24}c\,p_1.
}
\]

The local anomaly/descent interpretation of such characteristic polynomials is standard. [ZWZ84; BZ84; AGG85]

Model XII established that \(I_6\) is not itself a local four-form action density in four dimensions. Model XIII now makes the descent explicit.

---

## 2. Local normalized potential

On a patch where the line bundle is trivialized, choose a normalized local gauge potential \(a\) satisfying

\[
\boxed{
da=c.
}
\]

This \(a\) is \(A/(2\pi i)\) in the corresponding local convention.

The Pontryagin form is closed by Chern--Weil theory:

\[
\boxed{
dp_1=0.
}
\]

Since \(dc=0\), define the local five-form

\[
\boxed{
I_5^{(0)}
:=
a\wedge
\left(
\frac16c^2-rac1{24}p_1
\right).
}
\]

Then, **Derived here**,

\[
\begin{aligned}
dI_5^{(0)}
&=
da\wedge\left(\frac16c^2-\frac1{24}p_1\right)
-a\wedge d\left(\frac16c^2-\frac1{24}p_1\right)\\
&=
c\wedge\left(\frac16c^2-\frac1{24}p_1\right)\\
&=
\boxed{
\frac16c^3-rac1{24}c\,p_1
}\\
&=I_6.
\end{aligned}
\]

So the degree-six polynomial has the expected local Chern--Simons/transgression representative.

For charge \(q\), one may equivalently use \(a_q=q a\), \(c_q=q c\), giving

\[
\boxed{
I_5^{(0)}(q)
=
\frac{q^3}{6}a\,c^2
-
\frac{q}{24}a\,p_1.
}
\]

---

## 3. Abelian gauge descent

Under a local infinitesimal \(U(1)\) gauge transformation,

\[
\boxed{
a\longmapsto a+d\alpha,
\qquad
c\longmapsto c,
}
\]

while the frame connection is held fixed for this particular descent channel.

Then

\[
\begin{aligned}
\delta_\alpha I_5^{(0)}
&=
d\alpha\wedge
\left(
\frac16c^2-rac1{24}p_1
\right)\\
&=
d\left[
\alpha
\left(
\frac16c^2-rac1{24}p_1
\right)
\right]
\end{aligned}
\]

because \(c\) and \(p_1\) are closed.

Thus the local descent four-form is

\[
\boxed{
I_4^{(1)}(\alpha)
=
\alpha
\left(
\frac16c^2-rac1{24}p_1
\right).
}
\]

For charge \(q\),

\[
\boxed{
I_4^{(1)}(q;\alpha)
=
\alpha
\left(
\frac{q^3}{6}c^2-rac{q}{24}p_1
\right),
}
\]

when \(\alpha\) is the gauge parameter for the underlying normalized connection \(a\).

This is the elementary abelian instance of the standard descent mechanism developed in the anomaly literature. [ZWZ84; BZ84; AGG85]

---

## 4. Boundary inflow

Let \(Y^5\) be an oriented five-manifold with boundary

\[
\partial Y=M^4.
\]

If all relevant data are globally trivializable so that the local representative is globally available, consider schematically

\[
S_{\mathrm{inflow}}[Y]
=2\pi i\int_Y I_5^{(0)}.
\]

Under the abelian gauge transformation above,

\[
\begin{aligned}
\delta_\alpha S_{\mathrm{inflow}}
&=2\pi i\int_Y d I_4^{(1)}(\alpha)\\
&=2\pi i\int_M I_4^{(1)}(\alpha).
\end{aligned}
\]

Hence the bulk variation is a boundary functional. This is the basic inflow pattern.

The sign with which it cancels a boundary fermion anomaly depends on the orientation/chirality convention and is not fixed by the bare algebra above.

---

## 5. Local Chern--Simons forms are not global connections

The expression

\[
a\wedge\left(\frac16c^2-\frac1{24}p_1\right)
\]

uses a local potential \(a\). For a topologically nontrivial line bundle there need not be a globally defined one-form \(a\) on \(Y\).

Therefore

\[
\boxed{
I_5^{(0)}\text{ is a local secondary representative, not the global primary object.}
}
\]

This is precisely the sort of situation differential cohomology is designed to organize: connections are represented by local potentials plus transition/gluing data, while global holonomy is retained. [CS85; BB14]

However, one must make an additional distinction for the full fermionic polynomial.

---

## 6. Integral mixed class versus rational index polynomial

The product

\[
\boxed{
\widehat c_1(L)\cup\widehat p_1(TM)
\in\widehat H^6(-;\mathbf Z)
}
\]

is an ordinary integral differential-cohomology class when the characteristic classes have their standard integral normalizations.

By contrast,

\[
\boxed{
I_6
=
\frac16c_1^3-rac1{24}c_1p_1
}
\]

contains rational coefficients.

It is therefore **not correct in complete generality** to declare

\[
\frac16\widehat c_1^3-rac1{24}\widehat c_1\widehat p_1
\]

to be an arbitrary class of ordinary integral \(\widehat H^6(-;\mathbf Z)\) without checking divisibility/quantization.

### Correction 6.1 — global anomaly quantization is index-theoretic

For a closed spin six-manifold \(Z\) with a line bundle \(L\), the Atiyah--Singer theorem gives

\[
\boxed{
\int_Z
\left[
\widehat A(TZ)\operatorname{ch}(L)
\right]_{(6)}
=
\operatorname{Index}(D_L)
\in\mathbf Z.
}
\]

Thus the *combined* rational polynomial has the required integrality on the appropriate spin/index cycles, even though its individual rational coefficients are not ordinary integral cohomology coefficients term by term.

The correct global fermionic anomaly object is therefore more naturally described through the determinant/eta-invariant or invertible anomaly theory associated to the Dirac operator. [DF94; Freed14]

This is stronger and safer than pretending the local polynomial by itself is always an unrestricted integral differential character.

---

## 7. Extension independence from the index theorem

Suppose a four-dimensional boundary background extends over two five-dimensional fillings \(Y_1\) and \(Y_2\). Gluing them with opposite orientations gives a closed five-manifold, and comparing further extensions in the standard inflow construction reduces the ambiguity of the exponentiated fermionic phase to an index on a closed six-dimensional spin manifold.

Schematically, if two choices differ by a closed six-dimensional index cycle \(Z\), then

\[
\exp\left(
2\pi i\int_Z I_6
\right)
=
\boxed{1}
\]

because the integral is an integer index.

This is the global quantization mechanism behind the local polynomial.

The full mathematically precise construction is captured by Dai--Freed type anomaly theories/eta invariants rather than by a globally chosen Chern--Simons potential. [DF94; Freed14]

---

## 8. Differential-character viewpoint for genuinely integral pieces

For an integral degree-six differential character

\[
\widehat x\in\widehat H^6(Y;\mathbf Z),
\]

its defining property includes evaluation on smooth five-cycles

\[
\widehat x:Z_5(Y)\to\mathbf R/\mathbf Z
\]

with

\[
\boxed{
\widehat x(\partial C)
=
\int_C R(\widehat x)
\pmod{\mathbf Z}
}
\]

for a six-chain \(C\). [CS85; BB14]

This is the global version of “Chern--Simons form whose derivative is the characteristic form.”

For the integral mixed product \(\widehat c_1\cup\widehat p_1\), this statement applies directly.

For the fractional fermionic combination \(I_6\), one uses the index/anomaly refinement explained in Sections 6--7.

---

## 9. Descent representative is not unique

The invariant polynomial \(I_6\) is the robust object. A local five-form \(I_5^{(0)}\) is defined only up to

\[
I_5^{(0)}
\longmapsto
I_5^{(0)}+dB_4
\]

and related local counterterm choices.

When both gauge and gravitational transformations are considered, one may redistribute the consistent anomaly between different current/conservation equations by local counterterms. The classic Bardeen--Zumino analysis distinguishes consistent and covariant forms. [BZ84]

Therefore FCIG should not attach physical significance to one particular local descent representative before the current convention and counterterm scheme are specified.

The hierarchy is

\[
\boxed{
\text{anomaly polynomial}
\;\text{more invariant than}\;
\text{chosen Chern--Simons representative}
\;\text{more invariant than}\;
\text{a particular current formula}.
}
\]

---

## 10. Three different response notions

The descent computation produces a **symmetry/anomaly response**.

It does not automatically produce either of the following.

### 10.1 Stress-energy response

A stress tensor is obtained from variation of an effective action with respect to the metric/frame data, schematically

\[
T_{\mu\nu}
\sim
\frac{\delta W}{\delta g^{\mu\nu}}.
\]

The anomaly polynomial constrains symmetry variation of the quantum effective theory, but it does not by itself reconstruct the full metric dependence of \(W\).

### 10.2 Horizon/thermodynamic response

A Clausius or horizon-entropy argument additionally requires local causal horizons, temperature, entropy variation, and a physical flux law. None of those is contained in the descent algebra alone.

Hence

\[
\boxed{
\text{anomaly descent}
\neq
\text{stress-energy constitutive law}
\neq
\text{horizon thermodynamics}.
}
\]

This distinction is necessary before FCIG returns to the gravity-closure question.

---

## 11. What v0.13 genuinely adds

Before this note, FCIG had a mixed degree-six invariant but no explicit four-dimensional response mechanism.

Model XIII supplies:

1. a local five-dimensional secondary form;
2. its explicit abelian boundary descent;
3. a global distinction between local potentials and differential characters;
4. an index-theoretic quantization audit for the rational fermionic polynomial;
5. a separation of anomaly response from stress-energy and horizon response.

The positive bridge is now

\[
\boxed{
I_6
\xrightarrow{\text{descent/inflow}}
I_5^{(0)}
\xrightarrow{\delta}
I_4^{(1)}.
}
\]

But the result is still a statement about anomaly/symmetry response, not gravitational dynamics.

---

## 12. Symbolic checker

The companion file

`descent-inflow.py`

checks the formal coefficient algebra

\[
d\left[
 a\left(\frac16c^2-\frac1{24}p_1\right)
\right]
=
\frac16c^3-\frac1{24}cp_1
\]

under \(da=c\), \(dc=dp_1=0\), and the gauge variation

\[
\delta_\alpha I_5^{(0)}
=dI_4^{(1)}(\alpha).
\]

It is not a substitute for the global index/anomaly theorem.

---

## 13. Gate results

### Gate AN — local secondary form: PASS

\[
\boxed{
I_5^{(0)}
=a\left(\frac16c^2-\frac1{24}p_1\right),
\qquad
dI_5^{(0)}=I_6.
}
\]

### Gate AO — boundary gauge descent: PASS

\[
\boxed{
\delta_\alpha I_5^{(0)}
=d\left[
\alpha\left(\frac16c^2-\frac1{24}p_1\right)
\right].
}
\]

### Gate AP — global refinement: PASS WITH QUANTIZATION QUALIFICATION

- integral pieces such as \(\widehat c_1\cup\widehat p_1\) are ordinary differential characters;
- the full rational fermionic polynomial is globally quantized by the Dirac index / Dai--Freed anomaly theory, not by an unqualified assertion that the fractional polynomial is an arbitrary integral \(\widehat H^6\) class.

### Gate AQ — response-type audit: PASS WITH NO-GO

Anomaly descent gives symmetry/nonconservation data. It does not provide a stress-energy constitutive law or horizon thermodynamics.

---

## 14. v0.13 conclusion

The mixed FCIG/frame invariant now has an explicit and globally audited route to four-dimensional anomaly data:

\[
\boxed{
\text{index polynomial}
\to
\text{5D secondary/inflow data}
\to
\text{4D symmetry anomaly}.
}
\]

The main correction is equally important:

\[
\boxed{
\text{rational index density}
\neq
\text{arbitrary integral differential character}.
}
\]

Global quantization belongs to the index/eta-invariant anomaly theory.

No Einstein equation follows from this construction.

---

## 15. Next controlled milestone

The next bottleneck is **not** characteristic classes or descent. It is the difference between anomaly variation and actual dynamical response.

A natural v0.14 target is a **background-field response audit**:

1. place the determinant/anomaly theory over a space of gauge and metric backgrounds;
2. distinguish connection curvature on background space from functional derivatives of an effective action;
3. compare gauge-current variation and metric stress-tensor variation;
4. identify what extra effective-action or constitutive data would be required to turn a trace/Ricci constraint into dynamics;
5. only then revisit Jacobson-type horizon thermodynamics.

No gravitational closure should be activated before that audit passes.

---

## References used in this note

- **[ZWZ84]** Bruno Zumino, Yong-Shi Wu, and A. Zee, “Chiral Anomalies, Higher Dimensions, and Differential Geometry,” *Nuclear Physics B* 239 (1984), 477–507.
- **[BZ84]** William A. Bardeen and Bruno Zumino, “Consistent and Covariant Anomalies in Gauge and Gravitational Theories,” *Nuclear Physics B* 244 (1984), 421–453.
- **[AGG85]** Luis Alvarez-Gaumé and Paul Ginsparg, “The Structure of Gauge and Gravitational Anomalies,” *Annals of Physics* 161 (1985), 423–490; erratum 171 (1986), 233.
- **[CS85]** Jeff Cheeger and James Simons, “Differential Characters and Geometric Invariants,” in *Geometry and Topology*, LNM 1167, Springer, 1985.
- **[BB14]** Christian Bär and Christian Becker, “Differential Characters and Geometric Chains,” in *Differential Characters*, LNM 2112, Springer, 2014.
- **[DF94]** Xianzhe Dai and Daniel S. Freed, “Eta-Invariants and Determinant Lines,” *Journal of Mathematical Physics* 35 (1994), 5155–5194.
- **[Freed14]** Daniel S. Freed, “Anomalies and Invertible Field Theories,” *Proceedings of Symposia in Pure Mathematics* 88 (2014), arXiv:1404.7224.

The local descent algebra in Sections 2--4 is derived explicitly in this note. The global quantization and anomaly interpretation are standard results supported by the references above.