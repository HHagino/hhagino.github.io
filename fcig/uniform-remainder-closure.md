# Uniform Remainder Closure

## UR-A — generic proportional-\(K\) uniformity and the boundary double-scaling law

**Status (2026-09-10).**

\[
\boxed{\textbf{UR-A1: PASS — generic proportional sector admits uniform saddle/Airy asymptotics.}}
\]

\[
\boxed{\textbf{UR-A2: PASS — both boundary degenerations become critical at a }q^{-1}\textbf{ parameter scale.}}
\]

\[
\boxed{\textbf{BC-A: OPEN — one must replace the ordinary Airy model inside the critical boundary layers.}}
\]

This note completes the generic remainder architecture behind `jacobi-asymptotic-closure.md`, `proportional-k-type-rate-function.md`, `steepest-descent-rate-closure.md`, `explicit-rate-function-closure.md`, `off-diagonal-rate-surface.md`, `two-sheet-airy-normalization.md`, and `global-off-diagonal-rate-closure.md`.

The main point is deliberately conservative.  The ordinary Chester--Friedman--Ursell two-saddle Airy construction is uniform on compact proportional-parameter sets on which the relevant cubic coefficient stays nonzero and the saddles remain separated from the logarithmic singularities of the coefficient-extraction phase.  It is **not** uniform when the inner caustic collapses into \(t=0\), nor when the two caustic sheets merge at \(\beta=0\).  Those two failures occur at the same semiclassical scale.

No literature-novelty claim is made.

---

## 1. Exact proportional coefficient integral

For

\[
m=\alpha q,\qquad n=\beta q,
\]

with \(\alpha\ge \beta>0\), set

\[
r=\tanh\frac t2.
\]

The radial holomorphic-discrete-series matrix coefficient can be written as

\[
M_{m,n}^{(q)}(t)
=
\frac{c_{n,q}}{c_{m,q}}
\left(\cosh\frac t2\right)^{-2q}
\frac{1}{2\pi i}
\oint
\exp\!\bigl(q\Psi_{\alpha,\beta,r}(z)\bigr)
\frac{dz}{z},
\]

where

\[
\boxed{
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z.
}
\]

The saddle equation is

\[
\boxed{
\frac{\beta}{z+r}
-
\frac{r(\beta+2)}{1+rz}
-
\frac{\alpha}{z}=0.
}
\]

After clearing denominators,

\[
r(\alpha+2)z^2+Bz+\alpha r=0,
\]

with

\[
B=(\alpha-\beta)+(\alpha+\beta+2)r^2.
\]

The discriminant is

\[
\Delta_{\rm sad}
=B^2-4\alpha(\alpha+2)r^2.
\]

---

## 2. Exact two-sheet caustic geometry

Put

\[
\alpha+1=\cosh u_\alpha,\qquad
\beta+1=\cosh u_\beta.
\]

Then the two caustic sheets are

\[
\boxed{
t_-=u_\alpha-u_\beta,
\qquad
t_+=u_\alpha+u_\beta
}
\]

for \(\alpha\ge\beta\).  The three chambers are

\[
0<t<t_- \quad\text{(inner forbidden)},
\]

\[
t_-<t<t_+ \quad\text{(oscillatory)},
\]

\[
t>t_+ \quad\text{(outer forbidden)}.
\]

At either caustic, the two saddles coalesce at

\[
\boxed{
z_*=-\sqrt{\frac{\alpha}{\alpha+2}}.}
\]

Set

\[
x=\sqrt{\frac{\alpha}{\alpha+2}},
\qquad
y=\sqrt{\frac{\beta}{\beta+2}}.
\]

The cubic coefficients are

\[
\boxed{
\Psi'''_+
=
\frac{4(x+y)(1+xy)}{xy(1-x^2)^3}>0,
}
\]

\[
\boxed{
\Psi'''_-
=
-\frac{4(x-y)(1-xy)}{xy(1-x^2)^3}<0,
}
\]

and the radial unfolding coefficient is the same on both sheets:

\[
\boxed{
\partial_t\Psi'(z_*,t_\pm)=-(\alpha+2).
}
\]

Thus, whenever \(|\Psi'''_\pm|\) stays bounded away from zero and infinity, the phase has the standard nondegenerate fold normal form.

---

## 3. Generic uniform domain

Fix constants

\[
0<\varepsilon<M<\infty.
\]

For the **two-sheet** statement use a compact parameter set

\[
\boxed{
\mathcal K_{\varepsilon,M}
=
\{(\alpha,\beta):
\varepsilon\le\beta\le\alpha\le M,
\ \alpha-\beta\ge\varepsilon\}.
}
\]

On this set:

1. \(x,y\) stay in a compact subinterval of \((0,1)\);
2. \(x-y\) stays bounded away from zero;
3. \(|\Psi'''_\pm|\) are bounded above and below by positive constants;
4. the two logarithmic singularities \(z=-r\), \(z=-1/r\) remain controlled relative to the local fold neighborhoods after restricting \(t\) to a compact radial interval;
5. the saddle equation has only the two roots already identified.

These are exactly the local hypotheses needed for the standard Chester--Friedman--Ursell cubic reduction of a pair of coalescing saddles.  The DLMF formulation states that when two simple saddle points coalesce, an analytic change of variable reduces the phase to a cubic polynomial and the resulting approximation is reducible to Airy/Scorer canonical integrals.  In the present FCIG contour, the relevant branch is the Airy branch.

Hence near either caustic there are smooth coefficient functions \(A_j^\pm,B_j^\pm\) and an Airy coordinate \(\zeta_\pm\) such that the coefficient has a full expansion of the structural form

\[
\boxed{
M_{\alpha q,\beta q}^{(q)}(t)
\sim
\mathcal E_{\alpha,\beta,q}(t)
\left[
q^{-1/3}\operatorname{Ai}(q^{2/3}\zeta_\pm)
\sum_{j\ge0}\frac{A_j^\pm}{q^j}
+
q^{-2/3}\operatorname{Ai}'(q^{2/3}\zeta_\pm)
\sum_{j\ge0}\frac{B_j^\pm}{q^j}
\right],
}
\]

uniformly for \((\alpha,\beta)\in\mathcal K_{\varepsilon,M}\) and \(t\) in a fixed fold neighborhood.  The common exponential/normalization factor is denoted by \(\mathcal E_{\alpha,\beta,q}\); away from the fold it reproduces the global forbidden rates \(\Phi_\pm\) or the oscillatory phase.

The statement here is a **reduction theorem**, not a claim that all coefficient functions have already been printed in closed form.  Once the cubic map is chosen, the standard CFU recursion generates them and gives a remainder after truncation which is uniformly of the next asymptotic order on each such compact generic set.

Away from fixed neighborhoods of \(t_\pm\), ordinary steepest descent applies uniformly and gives the usual half-integer expansion in \(q^{-1}\) around the nondegenerate saddle(s).

Therefore the generic proportional sector is covered by overlapping ordinary-saddle and Airy charts.

\[
\boxed{\textbf{UR-A1: PASS.}}
\]

---

## 4. Outer sheet remains regular through the diagonal

The restriction \(\alpha-\beta\ge\varepsilon\) is needed for the **inner** fold, not for the outer one.

Indeed, as \(\beta\to\alpha\),

\[
\Psi'''_+
\to
\frac{8}{(1-x^2)^3}>0
\]

up to the equivalent algebraic simplification following from \(x=y\).  The outer caustic converges smoothly to

\[
t_+=2u_\alpha,
\]

which is exactly the diagonal turning point already analyzed in `explicit-rate-function-closure.md`.

Thus the outer Airy chart extends continuously to the diagonal stratum \(\alpha=\beta>0\).

What degenerates is only the inner sheet.

---

## 5. Diagonal collapse: exact critical scale

Let

\[
\delta=\alpha-\beta\downarrow0
\]

with \(\alpha\) fixed in a compact subset of \((0,\infty)\).

Since

\[
u'(\gamma)=\frac{1}{\sqrt{\gamma(\gamma+2)}},
\]

we have

\[
\boxed{
t_-
=
\frac{\delta}{\sqrt{\alpha(\alpha+2)}}
+O(\delta^2).}
\]

Also

\[
x'(\gamma)
=
\frac{1}{\sqrt\gamma\,(\gamma+2)^{3/2}},
\]

and direct expansion of the exact cubic coefficient gives

\[
\boxed{
\Psi'''_-
=
-\left(\frac{\alpha+2}{\alpha}\right)^{3/2}\delta
+O(\delta^2).
}
\]

Therefore

\[
\kappa_-
:=
\left(\frac{|\Psi'''_-|}{2}\right)^{1/3}
=
2^{-1/3}
\sqrt{\frac{\alpha+2}{\alpha}}
\,\delta^{1/3}
\bigl(1+O(\delta)\bigr).
\]

The inner Airy coordinate is

\[
\zeta_-
=-q^{2/3}\frac{\alpha+2}{\kappa_-}(t-t_-).
\]

Hence its physical radial width is

\[
\boxed{
\Delta t_-^{\rm Airy}
\asymp
\frac{\kappa_-}{q^{2/3}(\alpha+2)}
=
\frac{2^{-1/3}\delta^{1/3}}
{q^{2/3}\sqrt{\alpha(\alpha+2)}}
(1+o(1)).
}
\]

Dividing by the distance from the inner fold to the endpoint \(t=0\),

\[
\boxed{
\frac{\Delta t_-^{\rm Airy}}{t_-}
\sim
2^{-1/3}(q\delta)^{-2/3}.
}
\]

Therefore:

- if \(q\delta\to\infty\), the inner Airy layer is parametrically separated from \(t=0\);
- if \(q\delta=O(1)\), the Airy layer reaches the endpoint and ordinary two-saddle CFU uniformity is no longer the correct canonical description.

The diagonal boundary critical scale is

\[
\boxed{\alpha-\beta=O(q^{-1}).}
\]

---

## 6. Lowest-\(K\) edge: exact critical scale

Now fix \(\alpha>0\) and let \(\beta\downarrow0\).

Since

\[
u_\beta=\operatorname{arcosh}(1+\beta)
=\sqrt{2\beta}+O(\beta^{3/2}),
\]

the two caustics satisfy

\[
\boxed{
t_+-t_-=2u_\beta
=2\sqrt{2\beta}+O(\beta^{3/2}).}
\]

Moreover

\[
y=\sqrt{\frac{\beta}{\beta+2}}
=\sqrt{\frac\beta2}\,(1+O(\beta)),
\]

and the exact two-sheet cubic coefficients obey

\[
\boxed{
|\Psi'''_\pm|
\sim
\frac{(\alpha+2)^3}{\sqrt{2\beta}}.
}
\]

Consequently

\[
\boxed{
\kappa_\pm
=
\left(\frac{|\Psi'''_\pm|}{2}\right)^{1/3}
\sim
\frac{\alpha+2}{\sqrt2\,\beta^{1/6}}.
}
\]

The radial Airy width near either sheet is therefore

\[
\boxed{
\Delta t_\pm^{\rm Airy}
\asymp
\frac{1}{\sqrt2\,q^{2/3}\beta^{1/6}}.
}
\]

Relative to the sheet separation,

\[
\boxed{
\frac{\Delta t_\pm^{\rm Airy}}{t_+-t_-}
\sim
\frac14(q\beta)^{-2/3}.
}
\]

Thus:

- if \(q\beta\to\infty\), the two Airy folds remain asymptotically separated;
- if \(q\beta=O(1)\), the two Airy neighborhoods overlap and the separated-fold description fails.

The lowest-\(K\) boundary critical scale is

\[
\boxed{\beta=O(q^{-1}).}
\]

---

## 7. One boundary law

The two superficially different degenerations therefore obey the same semiclassical rule:

\[
\boxed{
q\,d_{\rm bdry}\gg1
\quad\Longrightarrow\quad
\text{ordinary separated Airy folds are uniform},
}
\]

where

\[
d_{\rm bdry}
\in\{\,|\alpha-\beta|,\ \beta\,\}.
\]

The critical crossover is

\[
\boxed{
q\,d_{\rm bdry}=O(1).
}
\]

This is the natural boundary between the proportional-\(K\) theory developed in the previous notes and a mixed proportional/fixed-\(K\) boundary theory.

\[
\boxed{\textbf{UR-A2: PASS.}}
\]

---

## 8. Why the remaining boundary problem is not another Airy calculation

At \(\alpha\to\beta\), the inner cubic coefficient itself vanishes:

\[
\Psi'''_-\to0.
\]

Therefore the fold normal form loses its uniform nondegeneracy at the same time that the caustic reaches the radial endpoint \(t=0\).  DLMF explicitly separates ordinary two-saddle coalescence from problems in which saddles, endpoints, poles, or algebraic singularities coalesce; such problems generally require different canonical approximants.

At \(\beta\to0\), the factor

\[
(z+r)^{\beta q}
\]

changes character when \(\beta q=O(1)\).  At exactly \(\beta=0\), the logarithmic term \(\beta\log(z+r)\) disappears and the quadratic saddle equation obtained after clearing denominators contains a root associated with the vanished factor.  Thus the two-sheet saddle geometry is singular as a parametrization of the \(\beta=0\) boundary.

This is why the final boundary completion must be performed directly in the double-scaled integral, not by taking a formal limit of the separated Airy formulas.

Possible canonical models must be selected from the transformed integral itself.  General asymptotic theory includes parabolic-cylinder, complementary-error-function, and other canonical functions when saddles coalesce with endpoints or algebraic singularities.  We do **not** choose one by analogy alone.

\[
\boxed{\textbf{BC-A remains OPEN until the double-scaled integral is reduced explicitly.}}
\]

---

## 9. Consequence for HC-Schwartz control

The previous unrestricted-\(K\) problem was

\[
\boxed{\textbf{UQ-A2: full parameter-uniform Harish--Chandra Schwartz control.}}
\]

The present analysis isolates its proportional-parameter obstruction much more sharply.

For compact subsets satisfying

\[
q\beta\to\infty,
\qquad
q|\alpha-\beta|\to\infty
\]

whenever the inner sheet is relevant, the generic matrix coefficients admit a uniform cover by ordinary saddle and Airy charts.  In the forbidden regions the already-derived rate functions give exponential \(q\)-decay; in the oscillatory region the coefficient is of standard semiclassical size away from the folds; at the folds the canonical scale is \(q^{-1/3}\).

Thus the genuinely new uncontrolled pieces are concentrated in the two boundary double scalings

\[
\boxed{
q|\alpha-\beta|=O(1)
\quad\text{and}\quad
q\beta=O(1).
}
\]

This is substantially smaller than the original undifferentiated problem “all \(m,n=O(q)\).”

---

## 10. Gate ledger

The proportional-\(K\) track now reads:

- **JA-A1:** PASS — fixed \(K\)-window, uniform in \(q\).
- **JA-B1:** PASS — proportional saddle equation and turning discriminant.
- **JA-B2:** PASS — diagonal steepest-descent / Airy regime closure.
- **RF-A:** PASS — explicit diagonal forbidden rate and Airy normalization.
- **RF-B1:** PASS — exact off-diagonal caustic surface.
- **RF-B2:** PASS — two-sheet Airy normalization.
- **RF-C:** PASS — global inner/outer forbidden rate functions.
- **UR-A1:** PASS — generic compact proportional sector has uniform saddle/Airy remainder architecture.
- **UR-A2:** PASS — both edge failures occur at a \(q^{-1}\) parameter distance.
- **BC-A:** OPEN — explicit boundary double-scaling canonical integral.

The next and intended final local-asymptotic gate is therefore

\[
\boxed{
\textbf{BC-A — Boundary Canonical Model Closure.}
}
\]

A successful BC-A should start from the exact coefficient integral and introduce

\[
\rho=q(\alpha-\beta)
\]

for the diagonal-endpoint crossover and

\[
\nu=q\beta
\]

for the lowest-\(K\) crossover, holding \(\rho\) or \(\nu\) fixed as \(q\to\infty\).  The goal is to identify the actual canonical integral in each boundary chart and match it to the generic Airy theory as \(\rho,\nu\to\infty\).

---

## References

1. C. Chester, B. Friedman, F. Ursell, *An extension of the method of steepest descents*, Proc. Cambridge Philos. Soc. **53** (1957), 599–611.
2. NIST Digital Library of Mathematical Functions, §2.4(v), *Coalescing Saddle Points: Chester, Friedman, and Ursell’s Method*, and §2.4(vi), *Other Coalescing Critical Points*, release 2026-06-15.
3. F. W. J. Olver, *Asymptotics and Special Functions*, A K Peters/CRC Press, 1997, especially the chapters on uniform asymptotics and coalescing turning points.
4. A. Gil, J. Segura, N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss-Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. **494** (2021), 124642.
5. R. Wong, *Asymptotic Approximations of Integrals*, Academic Press, 1989.
6. N. Bleistein and R. A. Handelsman, *Asymptotic Expansions of Integrals*, Holt, Rinehart and Winston, 1975 / Dover reprint.

## Claim firewall

- The standard CFU theorem is established literature; its application to the FCIG coefficient integral is derived here.
- The formulas for the FCIG caustic sheets, cubic coefficients, and the two \(q^{-1}\) boundary scales are derived here from the exact coefficient integral.
- A generic CFU reduction does **not** prove a uniform theorem through \(q|\alpha-\beta|=O(1)\) or \(q\beta=O(1)\).
- No parabolic-cylinder, Bessel, Pearcey, or error-function model is assigned to BC-A before an explicit reduction of the double-scaled FCIG integral.
- The transverse orbital variable \(\xi\), the radial Cartan variable \(t\), the longitudinal deformation mode, and the Harish--Chandra spectral variable remain distinct typed variables.
