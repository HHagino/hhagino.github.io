# FCIG: Casimir Transmutation for Weighted Bergman Orbitals

**Status:** exact derived identities + corrected theorem target  
**Date:** 2026-09-10  
**Scope:** compact hyperbolic Riemann surfaces, cyclic cylinders, canonical Bergman loop kernels, the FRZ/Schumacher resolvent field, conjugacy-length differentiation, and the precise obstruction to reducing the weighted Bergman orbital to the ordinary geodesic-length Hessian alone.  
**Depends on:** [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md), [`todd-selberg-origin.md`](todd-selberg-origin.md), [`bls-position-transport.md`](bls-position-transport.md).

> **Claim policy.** **Established** means a cited theorem/convention. **Derived here** means an explicit calculation in the conventions stated below; this is not a novelty certification. **No-go / insufficiency** means that the proposed reduction is not available from the stated scalar data alone. **Open problem** marks the remaining geometric restriction problem.
>
> Dedicated bibliography: [`casimir-orbital-transmutation.bib`](casimir-orbital-transmutation.bib). Citation audit: [`casimir-orbital-transmutation-citation-audit.md`](casimir-orbital-transmutation-citation-audit.md).

---

## 0. Result in one page

Let \(c\) be a primitive closed geodesic on a compact hyperbolic surface, and let \(L>0\) denote the length of a chosen hyperbolic conjugacy-class element (for the \(m\)-th power one has \(L=m\ell(c)\)). On the associated cyclic cylinder use Fermi coordinates

\[
(t,r),\qquad u=\sinh r,
\]

so

\[
ds^2=\frac{du^2}{1+u^2}+(1+u^2)dt^2,
\qquad dA=dt\,du.
\]

Sun's exact canonical Bergman loop geometry gives the oriented complex orbital kernel

\[
\boxed{
\kappa_{q,L}(u)
:=
\left(
\cosh\frac L2-i u\sinh\frac L2
\right)^{-2q}
}
\tag{0.1}
\]

whose real part is the length-plus-Chern-holonomy term occurring in the diagonal Bergman density [Sun26].

FRZ use

\[
\boxed{
\square_0=2\bar\partial^*\bar\partial=\frac12\Delta_0
}
\tag{0.2}
\]

on functions, where \(\Delta_0\) is the positive hyperbolic Laplacian [FRZ20]. After longitudinal averaging in \(t\),

\[
\boxed{
\square_0
=-\frac12\partial_u\!\left((1+u^2)\partial_u\right).
}
\tag{0.3}
\]

The first new identity is exact.

### Theorem A — normal-Laplacian / conjugacy-length transmutation

Define

\[
\mathscr C_L
:=
(\cosh L-1)\partial_L^2
+\sinh L\,\partial_L.
\tag{0.4}
\]

Then

\[
\boxed{
\square_0\kappa_{q,L}
=
\left[
q(q-1)(\cosh L-1)-\mathscr C_L
\right]\kappa_{q,L}.
}
\tag{0.5}
\]

Equivalently,

\[
\boxed{
\partial_u\!\left((1+u^2)\partial_u\kappa_{q,L}\right)
=
4\sinh^2\!\frac L2\,\partial_L^2\kappa_{q,L}
+4\sinh\frac L2\cosh\frac L2\,\partial_L\kappa_{q,L}
-4q(q-1)\sinh^2\!\frac L2\,\kappa_{q,L}.
}
\tag{0.6}
\]

**Derived here, exact.** This is obtained by direct differentiation of (0.1). The appearance of \(q(q-1)\) is compatible with the Casimir eigenvalue of the holomorphic discrete series, but the representation-theoretic identification of \(\mathscr C_L\) with a standard orbital radial part is left as an interpretation until conventions are matched [BW; DS].

Now let

\[
a_\mu=|\mu|^2,
\qquad
f_\mu=(1+\square_0)^{-1}a_\mu,
\tag{0.7}
\]

as in Schumacher/FRZ [Sch; FRZ20], and recall the FCIG weight

\[
\boxed{
W_q
=a_\mu+2(q-1)f_\mu
=(\square_0+2q-1)f_\mu.
}
\tag{0.8}
\]

For a periodic function \(b(t,u)\) on the cyclic cylinder, write

\[
\overline b(u)
=\frac1{\ell(c)}\int_0^{\ell(c)}b(t,u)dt
\tag{0.9}
\]

and define the oriented real orbital functional

\[
\boxed{
\mathcal J_{q,L}[b]
:=
\Re\int_{\mathbb R}\overline b(u)\kappa_{q,L}(u)du.
}
\tag{0.10}
\]

### Theorem B — exact weighted-orbital reduction

Assume \(\overline f_\mu\) and its first derivative are bounded (or satisfy any condition making the boundary terms below vanish). Then

\[
\boxed{
\mathcal J_{q,L}[W_q]
=
\mathscr D_{q,L}\,\mathcal J_{q,L}[f_\mu],
}
\tag{0.11}
\]

where

\[
\boxed{
\mathscr D_{q,L}
:=
2q-1
+q(q-1)(\cosh L-1)
-\mathscr C_L.
}
\tag{0.12}
\]

**Derived here, exact under the stated integration-by-parts hypothesis.** Indeed,

\[
W_q=(\square_0+2q-1)f_\mu,
\]

and after longitudinal averaging the \(t\)-derivative part of the Laplacian integrates to zero. Self-adjointness on the normal variable gives

\[
\begin{aligned}
\mathcal J_{q,L}[W_q]
&=\Re\int
(\square_0+2q-1)\overline f_\mu\,\kappa_{q,L}\,du\\
&=\Re\int
\overline f_\mu(\square_0+2q-1)\kappa_{q,L}\,du,
\end{aligned}
\]

and Theorem A gives (0.11).

The parameter derivative \(\partial_L\) in (0.11) is a derivative of the **kernel with respect to its conjugacy-length parameter while the lifted geometric weight is held fixed**. It is not, by itself, a Teichmüller derivative of the surface.

This is the exact bridge that was missing in the preceding note:

\[
\boxed{
\text{elliptic resolvent on the surface}
\longleftrightarrow
\text{differential operator in hyperbolic conjugacy length}.
}
\tag{0.13}
\]

---

# Part I. Derivation of the transmutation identity

## 1. Algebraic normal form

Put

\[
C=\cosh\frac L2,
\qquad
S=\sinh\frac L2,
\qquad
h=C-iSu.
\]

Then

\[
\kappa=h^{-2q}.
\]

Introduce also

\[
k=S-iCu.
\]

The elementary identities

\[
\partial_Lh=\frac12k,
\qquad
h^2-k^2=1+u^2
\tag{1.1}
\]

are the entire calculation.

Direct differentiation gives

\[
\partial_u\kappa
=2qiS\,h^{-2q-1},
\]

\[
\partial_u^2\kappa
=-2q(2q+1)S^2h^{-2q-2},
\]

and

\[
\frac{\partial_L\kappa}{\kappa}
=-q\frac{k}{h}.
\tag{1.2}
\]

A second \(L\)-derivative yields

\[
\frac{\partial_L^2\kappa}{\kappa}
=
q^2
-
\frac{q(2q+1)}{2}\frac{1+u^2}{h^2}.
\tag{1.3}
\]

Substituting (1.2)--(1.3) into the normal divergence operator gives precisely (0.6).

No asymptotic expansion is used.

---

## 2. FRZ Laplacian normalization

FRZ explicitly define

\[
\square_0=2\bar\partial^*\bar\partial
\]

on functions [FRZ20, Eq. (2.5) discussion]. They also record that their scalar Laplacian \(\Delta_0\) satisfies \(\square_0=\Delta_0/2\). In Fermi coordinates the positive scalar Laplacian is

\[
\Delta_0
=-\left[
\partial_u((1+u^2)\partial_u)
+\frac1{1+u^2}\partial_t^2
\right].
\tag{2.1}
\]

After averaging over the periodic longitudinal variable, the \(\partial_t^2\) term drops, giving (0.3). This fixes all signs in Theorem A.

---

# Part II. The common resolvent field

## 3. Schumacher/FRZ field

For a harmonic Beltrami differential \(\mu\), Schumacher's horizontal-geodesic-curvature equation gives

\[
\boxed{
f_\mu=(1+\square_0)^{-1}|\mu|^2.}
\tag{3.1}
\]

FRZ use the same field in Berndtsson's direct-image curvature formula [FRZ20]. In their notation the direct-image curvature contains

\[
(m-1)\int_X f_\mu B_m\,dA
\]

as its geodesic-curvature sector.

The same \(f_\mu\) appears in Axelsson--Schumacher's second variation of a closed-geodesic length:

\[
\boxed{
\bar\partial_\mu\partial_\mu\ell(\gamma)
=
\frac12\int_\gamma
\left[
 f_\mu
+
\left(-D_t^2+2\right)^{-1}(\mu)\bar\mu
\right]dt
+
\frac1{\ell(\gamma)}|\partial_\mu\ell(\gamma)|^2.
}
\tag{3.2}
\]

[AS12; FRZ20].

So the earlier observation was correct but incomplete:

\[
\boxed{
\text{weighted Bergman curvature and length Hessian share the same field }f_\mu.
}
\tag{3.3}
\]

They do **not**, however, apply the same functional to that field.

---

# Part III. What the Bergman orbital actually measures

## 4. Gamma/Fourier representation revisited

Since

\[
\kappa_{q,L}(u)
=C^{-2q}(1-i\tau u)^{-2q},
\qquad
\tau=\tanh\frac L2,
\]

for a Schwartz longitudinal average \(a(u)\),

\[
\boxed{
\mathcal J_{q,L}[a]
=
\frac{C^{-2q}}{\Gamma(2q)}
\int_0^\infty
s^{2q-1}e^{-s}
\Re\widehat a(\tau s)ds.
}
\tag{4.1}
\]

Thus the Bergman orbital samples the transverse Fourier transform near

\[
\boxed{
\xi\simeq2q\tanh(L/2)
}
\tag{4.2}
\]

with a frequency width of order \(\sqrt q\).

In contrast, the \(f_\mu\)-part of the ordinary geodesic-length Hessian reads only

\[
\int_\gamma f_\mu dt
=\ell(\gamma)\overline f_\mu(0),
\tag{4.3}
\]

that is, the **axis trace** of the longitudinal zero mode. The second term in (3.2) is a longitudinal resolvent of \(\mu\) restricted to the axis.

Hence the two observables are geometrically different:

\[
\boxed{
\begin{array}{rcl}
\text{length Hessian} &:& \text{axis trace + longitudinal resolvent},\\
\text{Bergman orbital} &:& \text{high-frequency transverse transform}.
\end{array}
}
\tag{4.4}
\]

---

## 5. General-profile insufficiency theorem

Let \(\mathcal S(\mathbb R)\) be the Schwartz class. The linear functionals

\[
E_0[a]=a(0),
\qquad
J_{q,L}[a]=\mathcal J_{q,L}[a]
\]

are not proportional.

Indeed, \(E_0\) is the delta distribution at the origin, while \(J_{q,L}\) is represented by the smooth integrable kernel \(\Re\kappa_{q,L}(u)\). Therefore there exists \(a\in\mathcal S(\mathbb R)\) such that

\[
a(0)=0,
\qquad
\mathcal J_{q,L}[a]\ne0.
\tag{5.1}
\]

More generally no finite jet

\[
(a(0),a'(0),\dots,a^{(N)}(0))
\]

determines \(\mathcal J_{q,L}[a]\) on \(\mathcal S(\mathbb R)\).

**Derived here, exact functional-analytic no-go for unrestricted profiles.**

This does **not** prove a no-go on the finite-dimensional subspace of profiles arising from harmonic Beltrami differentials on a fixed compact surface. It does show that any reduction to ordinary length variation must use substantial extra geometry (harmonicity, automorphy, analyticity, or a representation-theoretic identity), rather than the scalar length Hessian formula alone.

---

# Part IV. Corrected closure target

## 6. Why the previous target was too small

The previous SBO note proposed expressing the weighted Bergman orbital solely through

\[
\partial_\mu\ell(\gamma),
\qquad
\bar\partial_\mu\partial_\mu\ell(\gamma).
\]

Theorem B and (4.4) show that this is not the natural first target. The length Hessian compresses the full transverse profile too aggressively.

The more appropriate object is the **resolvent geodesic profile**

\[
\boxed{
\mathfrak F_{\gamma,\mu}(\xi)
:=
\widehat{\overline f_{\gamma,\mu}}(\xi),
\qquad
f_\mu=(1+\square_0)^{-1}|\mu|^2,
}
\tag{6.1}
\]

or an equivalent representation-theoretic orbital transform.

Then

\[
\boxed{
\mathcal J_{q,L}[f_\mu]
=
\frac{\cosh^{-2q}(L/2)}{\Gamma(2q)}
\int_0^\infty
s^{2q-1}e^{-s}
\Re\mathfrak F_{\gamma,\mu}\!\left(s\tanh\frac L2\right)ds.
}
\tag{6.2}
\]

Combining (6.2) with Theorem B gives the weighted Bergman orbital exactly.

The revised problem is therefore:

\[
\boxed{
\text{identify }\mathfrak F_{\gamma,\mu}(\xi)
\text{ from automorphic / holomorphic-discrete-series data, not merely from }\ell(\gamma).
}
\tag{6.3}
\]

---

# Part V. Relation to Selberg variation

## 7. Selberg side remains ordinary length-spectrum data

FRZ prove

\[
\bar\partial_\mu\partial_\mu\log Z(s)
=
\sum_{\gamma\in\mathrm{Prim}(\Gamma)}
\bar\partial_\mu\partial_\mu\log\ell(\gamma)\,A_\gamma(s)
+
\sum_{\gamma\in\mathrm{Prim}(\Gamma)}
|\partial_\mu\log\ell(\gamma)|^2
(A_\gamma(s)+B_\gamma(s)),
\tag{7.1}
\]

with explicit scalar functions \(A_\gamma,B_\gamma\) [FRZ20]. Their large-\(s\) theorem shows that the shortest closed geodesics dominate this scalar length-spectrum expansion.

Thus the exact finite-information remainder now has a more precise two-channel structure:

\[
\boxed{
D_q
=
\underbrace{\text{Selberg scalar length-spectrum Hessian}}_{\partial\ell,\,\bar\partial\partial\ell}
+
\underbrace{\text{Bergman resolvent-profile orbital}}_{\mathfrak F_{\gamma,\mu}(\xi)}.
}
\tag{7.2}
\]

The two channels share the same hyperbolic conjugacy classes and the same deformation \(\mu\), but the Bergman term contains finer transverse information.

---

## 8. A concrete common-basis conjecture

A publishable closure theorem would identify a representation-theoretic transform \(\mathscr T_\gamma\) such that

\[
\boxed{
\mathfrak F_{\gamma,\mu}(\xi)
=
\mathscr T_\gamma
\left[
\mu,\bar\mu
\right](\xi),
}
\tag{8.1}
\]

with \(\mathscr T_\gamma\) written in automorphic Fourier data along the cyclic cover. The ordinary geodesic-length variations should then occur as special low-complexity functionals of the same data, while the Bergman term evaluates it at the discrete-series frequency window (4.2).

**Conjecture / theorem target.** The correct common basis is therefore expected to be an **enriched conjugacy-class transform**, not the scalar marked length spectrum alone.

This is compatible with the general trace-formula principle: the geometric side is organized by conjugacy classes, while the spectral/test-function choice controls which orbital transform is evaluated [Hejhal; McK72].

---

# Part VI. Representation-theoretic meaning

## 9. Why \(q(q-1)\) matters

The coefficient

\[
q(q-1)
\]

in Theorem A is the characteristic Casimir scale of a holomorphic discrete-series representation, up to the conventional normalization of the Casimir [BW; DS]. Weighted Bergman spaces on the hyperbolic disc realize holomorphic discrete series, so the appearance of this number in a direct differentiation of Sun's orbital kernel is not accidental.

**FCIG interpretation.** Equation (0.5) is a local coordinate shadow of the fact that the same Casimir can be represented either as a differential operator on the symmetric space (normal variable) or as an invariant differential operator on conjugacy/orbital data (length variable).

This statement should be promoted to a representation-theoretic theorem only after matching the exact PSL(2,R) Casimir and Haar/orbital normalizations.

---

## 10. Relation to Euler--Poincare / pseudo-coefficient vanishing

Pseudo-coefficients of discrete series have vanishing orbital integrals on non-elliptic regular semisimple elements in the standard representation-theoretic setting [Lab; Huang]. This is structurally consistent with the exact Chern-holonomy cancellation in the preceding SBO note.

But the current repository deliberately does **not** identify Sun's diagonal Bergman kernel itself with a standard compactly supported Euler--Poincare test function. The relation is a representation-theoretic target, not an established equality.

---

# Part VII. Consequences for the FCIG information closure

## 11. The mediator is a field, not a scalar

The decisive correction is conceptual:

\[
\boxed{
\text{the common object is }f_\mu=(1+\square_0)^{-1}|\mu|^2,
\text{ not merely }\bar\partial\partial\ell(\gamma).
}
\tag{11.1}
\]

The same \(f_\mu\) enters

1. Schumacher's horizontal geometry;
2. Berndtsson/FRZ direct-image curvature;
3. Axelsson--Schumacher geodesic-length Hessians;
4. the FCIG weighted Bergman orbital.

Different observables apply different transforms to it.

This gives a sharper closure diagram:

\[
\boxed{
\begin{array}{ccc}
&& f_\mu=(1+\square_0)^{-1}|\mu|^2\\[1mm]
&\swarrow&&\searrow\\[-1mm]
\text{axis/longitudinal transform}
&&
\text{Chern-holonomy transverse transform}\\
\downarrow&&\downarrow\\
\text{length Hessian / Selberg zeta}
&&
\text{weighted Bergman orbital / Fisher defect}.
\end{array}
}
\tag{11.2}
\]

---

## 12. What has actually been solved

The following pieces are now exact in the stated cylinder conventions:

\[
\boxed{
\square_0\kappa_{q,L}
=
\left[q(q-1)(\cosh L-1)-\mathscr C_L\right]\kappa_{q,L},
}
\]

\[
\boxed{
\mathcal J_{q,L}[W_q]
=
\mathscr D_{q,L}\mathcal J_{q,L}[f_\mu],
}
\]

and

\[
\boxed{
\mathcal J_{q,L}[f_\mu]
=
\text{Gamma average of the transverse Fourier profile of }f_\mu.
}
\]

So the weighted term has been reduced from an unexplained two-dimensional surface integral to a **one-dimensional conjugacy-length differential operator applied to a one-dimensional microlocal profile**.

That is a genuine reduction in complexity.

---

## 13. What remains open

The next serious steps are now sharply separated.

### Gate COT-1 — exact Sun-unfolding lemma

Complete the conditional SBO orbital Riemann--Roch proof by proving the absolute-convergence and centralizer-unfolding step in Sun's exact conventions.

### Gate COT-2 — geometric profile theorem

For harmonic Beltrami \(\mu\), express

\[
\mathfrak F_{\gamma,\mu}(\xi)
\]

in terms of the Fourier coefficients of the corresponding holomorphic quadratic differential on the cyclic cover.

### Gate COT-3 — compare with length Hessian

Write Axelsson--Schumacher's

\[
\partial\ell(\gamma),
\qquad
\bar\partial\partial\ell(\gamma)
\]

in the **same cyclic-cover Fourier coefficients**. Determine precisely which modes are shared and which information is lost by passing to the scalar length Hessian.

### Gate COT-4 — first total nonperturbative coefficient

Only after COT-2/3 should one combine the Bergman and Selberg class contributions and determine the leading coefficient of

\[
D_q
=
I_{{\rm HBF},q}^{KE}
-\mathfrak K_q
-\frac1{12\pi}G_{\rm WP}.
\]

The previous positive length-only saddle is not to be reused.

---

# 14. Reference map

- **Sun exact Bergman loop kernel and Chern holonomy:** [Sun26].
- **FRZ Laplacian convention, resolvent field, direct-image curvature, Selberg Hessian:** [FRZ20].
- **Geodesic length first/second variation:** [AS12].
- **Classical Selberg conjugacy-class machinery:** [McK72; Hejhal].
- **Holomorphic discrete-series / Casimir background:** [BW; DS].
- **Pseudo-coefficient orbital vanishing background:** [Lab; Huang].

No cited source is claimed to state Theorem A or Theorem B in the form above. Those are explicit FCIG calculations whose publication novelty still requires a broader literature audit.
