# FCIG: Chern-Holonomy Orbital Cancellation and a Selberg-Style Riemann–Roch Formula

**Status:** exact derived identities + corrected nonperturbative research target  
**Date:** 2026-09-10  
**Scope:** compact hyperbolic Riemann surfaces, canonical Bergman kernels, Chern holonomy, hyperbolic orbital integrals, Riemann–Roch, Selberg trace geometry, and the weighted remainder in the Fisher–Kodaira–Spencer closure.  
**Depends on:** [`todd-selberg-origin.md`](todd-selberg-origin.md), [`finite-q-information-offset.md`](finite-q-information-offset.md), [`bls-position-transport.md`](bls-position-transport.md).

> **Claim policy.** **Established** means a cited theorem or construction. **Derived here** means an explicit calculation from those inputs in the conventions below; it is not a novelty certification. **Interpretation** marks FCIG language. **Open problem** marks a step not proved here.
>
> **Correction notice.** A naive positive Laplace saddle obtained by dropping the Chern-holonomy phase is wrong. The phase oscillates on the same semiclassical scale and causes exact orbital moment cancellation. The earlier exponential *bound* remains valid, but the first coefficient cannot be obtained from the absolute-value length factor alone.
>
> Dedicated bibliography: [`systolic-bergman-orbital.bib`](systolic-bergman-orbital.bib). Citation audit: [`systolic-bergman-orbital-citation-audit.md`](systolic-bergman-orbital-citation-audit.md).

---

## 0. Result in one page

Let

\[
X=\Gamma\backslash\mathbb H
\]

be a compact hyperbolic Riemann surface of genus \(g\ge2\), with hyperbolic area form \(dA\). For \(q\ge2\), let

\[
\mathcal H_q=H^0(X,K_X^q)
\]

and let \(B_q(p)\) denote the diagonal Bergman density with respect to \(dA\).

Jingzhou Sun proves an exact geodesic-loop formula for the Bergman density of a polarized complex hyperbolic manifold. In complex dimension one and canonical polarization it takes the form

\[
\boxed{
B_q(p)
=
\frac{2q-1}{4\pi}
\left[
1+
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2q}\!\left(\frac{\ell(\gamma)}2\right)
\cos\bigl(2\pi q\alpha_\gamma\bigr)
\right].
}
\tag{0.1}
\]

Here \(\mathfrak G_p\) is the set of oriented geodesic loops based at \(p\), \(\ell(\gamma)\) is loop length, and \(e^{2\pi i\alpha_\gamma}\) is the Chern holonomy of \(K_X\) around the loop [Sun26]. Sun explicitly emphasizes the analogy with the Selberg trace formula.

Now fix a primitive closed geodesic of length \(L>0\), use its hyperbolic cylinder, and put

\[
C=\cosh\frac L2,
\qquad
S=\sinh\frac L2,
\qquad
\tau=\tanh\frac L2.
\]

Let \(r\) be signed distance from its axis and set

\[
u=\sinh r.\]

Sun's cylinder length and holonomy formulae imply, for one orientation and canonical central holonomy,

\[
\boxed{
\cosh^{-2q}\!\left(\frac{\ell_u}{2}\right)
 e^{iq\vartheta(u)}
=
C^{-2q}(1-i\tau u)^{-2q},
}
\tag{0.2}
\]

up to complex conjugation according to orientation. The area form in Fermi coordinates is

\[
dA=\cosh r\,dt\,dr=dt\,du.\]

This simple meromorphic kernel has a strong cancellation property.

### Theorem A — exact transverse moment annihilation

For every integer \(q\ge2\), \(\tau>0\), and integer

\[
0\le m\le2q-2,
\]

one has

\[
\boxed{
\int_{-\infty}^{\infty}
 u^m(1-i\tau u)^{-2q}\,du=0.
}
\tag{0.3}
\]

**Derived here.** The only pole is at \(u=-i/\tau\), in the lower half-plane, while the integrand is \(O(|u|^{-2})\) or better. Closing the contour in the upper half-plane gives zero.

In particular,

\[
\boxed{
\int_{-\infty}^{\infty}
(1+\tau^2u^2)^{-q}
\cos\bigl(2q\arctan(\tau u)\bigr)\,du=0.
}
\tag{0.4}
\]

Thus a nontrivial hyperbolic orbital with **constant transverse weight** contributes zero after the Chern phase is included.

### Proposition B — orbital Riemann–Roch identity

Under the standard conjugacy-class unfolding of the absolutely convergent compact loop sum, every nonidentity hyperbolic conjugacy-class orbital in the integral of (0.1) has constant transverse weight and vanishes by (0.4). Hence only the identity orbital remains:

\[
\boxed{
\begin{aligned}
\dim H^0(X,K_X^q)
&=\int_XB_q\,dA\\
&=\frac{2q-1}{4\pi}\operatorname{Area}(X)\\
&=(2q-1)(g-1).
\end{aligned}
}
\tag{0.5}
\]

This reproduces the Riemann–Roch dimension formula from the exact Bergman loop expansion.

**Status:** **Derived here from Sun's exact formula plus standard Selberg-style conjugacy-class unfolding.** The numerical dimension formula itself is classical Riemann–Roch. This is an alternate orbital derivation, not a novelty claim.

### Theorem C — weighted orbital transform

For a Schwartz transverse weight \(a\), define

\[
\mathcal O_{q,\tau}[a]
:=
\Re\int_{\mathbb R}
a(u)(1-i\tau u)^{-2q}\,du.
\tag{0.6}
\]

Using the Gamma representation

\[
(1-i\tau u)^{-2q}
=
\frac1{\Gamma(2q)}
\int_0^\infty
s^{2q-1}e^{-s}e^{i\tau us}\,ds,
\tag{0.7}
\]

one obtains

\[
\boxed{
\mathcal O_{q,\tau}[a]
=
\frac1{\Gamma(2q)}
\int_0^\infty
s^{2q-1}e^{-s}
\Re\widehat a(\tau s)\,ds,
}
\tag{0.8}
\]

with

\[
\widehat a(\xi)=\int_{\mathbb R}a(u)e^{i\xi u}\,du.
\]

**Derived here.** Thus the weighted Bergman orbital does not probe only \(a(0)\) or a finite Taylor jet. The Gamma distribution is concentrated at \(s\sim2q\), so the transform samples transverse Fourier frequency

\[
\boxed{
\xi\sim2q\tanh(L/2).
}
\tag{0.9}
\]

This is why the naive positive local saddle fails.

The correct structural summary is therefore

\[
\boxed{
\text{Todd gives the local constant; Chern holonomy annihilates local hyperbolic moments; weighted orbital data carries the global remainder.}
}
\tag{0.10}
\]

---

# Part I. Exact Bergman loop geometry

## 1. Sun's loop formula

Sun's 2026 revision proves an exact formula for Bergman kernels on polarized complex hyperbolic manifolds. In the compact one-dimensional case, the admissible threshold is \(q\ge2\). The formula depends on two pieces of data attached to each based geodesic loop:

\[
\ell(\gamma)
\quad\text{and}\quad
\operatorname{Hol}_{K_X}(\gamma)=e^{2\pi i\alpha_\gamma}.
\]

The exact density is (0.1). [Sun26]

**Established.** The geodesic-loop formula, including the Chern-holonomy phase, is Sun's theorem. Sun also notes explicitly that the structure is strikingly analogous to the Selberg trace formula, while leaving a deeper connection as an interesting problem.

This phase is not optional. Since the bundle is raised to the \(q\)-th power, the loop phase is multiplied by \(q\). A length-only estimate can therefore give the right absolute exponential bound while giving the wrong leading signed orbital coefficient.

---

## 2. Canonical holonomy on the central geodesic

For the canonical bundle on a hyperbolic surface, Sun proves that the holonomy around a simple closed geodesic itself is trivial. In particular this applies to a systole [Sun26].

This does **not** imply that a based loop through a nearby point has trivial holonomy. Moving away from the axis sweeps hyperbolic area, and the Chern connection records precisely that curvature flux. That nearby phase is the mechanism responsible for the cancellation below.

---

# Part II. Hyperbolic cylinder normal form

## 3. Fermi coordinates

Fix a primitive closed geodesic \(c\) of length \(L\). On its cyclic cover use Fermi coordinates

\[
(t,r)\in(\mathbb R/L\mathbb Z)\times\mathbb R,
\]

with metric

\[
ds^2=dr^2+\cosh^2r\,dt^2.\]

Set

\[
u=\sinh r.\]

Then

\[
\boxed{dA=dt\,du.}
\tag{3.1}
\]

Let \(\gamma_u\) be the based geodesic loop through \((t,r)\) representing one winding around the cylinder.

Sun's cylinder geometry yields

\[
\cosh^2\frac{\ell_u}{2}
=
C^2+S^2u^2
=
C^2(1+\tau^2u^2).
\tag{3.2}
\]

For canonical central holonomy, his holonomy formula reduces to

\[
\cos\vartheta(u)
=
\frac{1-\tau^2u^2}{1+\tau^2u^2}.
\tag{3.3}
\]

Choosing one orientation continuously gives

\[
\vartheta(u)=2\arctan(\tau u)
\tag{3.4}
\]

up to overall sign. Reversing the orientation complex-conjugates the result.

---

## 4. Length and Chern phase combine holomorphically

Since

\[
e^{2i\arctan x}=\frac{1+ix}{1-ix},
\]

we get

\[
\begin{aligned}
&\cosh^{-2q}\frac{\ell_u}{2}\,e^{iq\vartheta(u)}\\
&\qquad=
C^{-2q}(1+\tau^2u^2)^{-q}
\left(\frac{1+i\tau u}{1-i\tau u}\right)^q\\
&\qquad=
\boxed{C^{-2q}(1-i\tau u)^{-2q}}.
\end{aligned}
\tag{4.1}
\]

This is the fundamental simplification.

If the phase is discarded, one sees a positive real bump of width \(q^{-1/2}\). With the phase restored, the same bump becomes the boundary value of a function whose pole lies entirely in one half-plane. That analytic placement forces the moment cancellation.

---

# Part III. Exact moment cancellation

## 5. Theorem A

Let

\[
I_{m,q}(\tau)
=
\int_{\mathbb R}u^m(1-i\tau u)^{-2q}\,du.
\]

For

\[
0\le m\le2q-2,
\]

the integrand behaves at infinity as

\[
O(|u|^{m-2q})=O(|u|^{-2})
\]

or faster. Its only finite pole is

\[
u=-\frac{i}{\tau},\]

which lies strictly in the lower half-plane. Closing the contour by an upper semicircle therefore gives

\[
\boxed{I_{m,q}(\tau)=0.}
\tag{5.1}
\]

No stationary-phase approximation is involved.

By taking real parts,

\[
\boxed{
\int_{\mathbb R}
u^m
(1+\tau^2u^2)^{-q}
\cos\bigl(2q\arctan(\tau u)\bigr)\,du=0
}
\tag{5.2}
\]

for the same range of \(m\).

**Interpretation.** The Chern phase behaves as a semiclassical analytic projector: low transverse polynomial moments of every hyperbolic cylinder orbital are annihilated exactly.

This interpretation suggests a relation to holomorphic discrete-series orbital integrals, but that representation-theoretic identification is not proved here.

---

## 6. Why ordinary Laplace's method gives the wrong answer

If one keeps only the length factor,

\[
C^{-2q}(1+\tau^2u^2)^{-q},
\]

then near \(u=0\)

\[
(1+\tau^2u^2)^{-q}
\approx e^{-q\tau^2u^2}
\]

and a positive \(q^{-1/2}C^{-2q}\) normal integral appears.

But the phase satisfies

\[
q\vartheta(u)
=2q\tau u+O(qu^3).
\]

On the amplitude width \(u\sim q^{-1/2}\), the phase therefore oscillates \(O(q^{1/2})\) times. It is not a subleading perturbation. The exact contour identity (5.1) shows that the would-be leading saddle, and in fact every polynomial transverse moment up to degree \(2q-2\), cancels.

Thus any claimed positive coefficient obtained from \(|\cosh^{-2q}(\ell/2)|\) alone must be rejected for the signed Bergman orbital.

---

# Part IV. Riemann–Roch from orbital cancellation

## 7. Conjugacy-class unfolding

The compact surface has only hyperbolic nonidentity elements. Standard Selberg-style unfolding rewrites a group/loop sum integrated over a fundamental domain as a sum of orbital integrals over cyclic covers associated to nontrivial conjugacy classes [McK72; Hejhal].

For \(\gamma=\delta^m\), where \(\delta\) is primitive of length \(L_\delta\), the centralizer is generated by \(\delta\). The unfolded cylinder has longitudinal length \(L_\delta\); the based-loop length/holonomy factor is the \(m\)-winding version of (4.1), with

\[
C_m=\cosh\frac{mL_\delta}{2},
\qquad
\tau_m=\tanh\frac{mL_\delta}{2}.
\]

Thus the constant-weight normal orbital is proportional to

\[
\Re\int_{\mathbb R}(1-i\tau_m u)^{-2q}du=0.
\tag{7.1}
\]

Every nonidentity conjugacy-class contribution to the trace of the Bergman projector therefore vanishes.

---

## 8. Proposition B — identity orbital equals the RR dimension

By definition of the Bergman projection,

\[
\int_XB_qdA=\operatorname{Tr}P_q=\dim H^0(X,K^q).
\tag{8.1}
\]

Using Sun's loop formula and the unfolding above, all nonidentity orbitals vanish, so

\[
\dim H^0(X,K^q)
=
\frac{2q-1}{4\pi}\operatorname{Area}(X).
\tag{8.2}
\]

Gauss–Bonnet gives

\[
\operatorname{Area}(X)=4\pi(g-1),
\]

hence

\[
\boxed{
\dim H^0(X,K^q)=(2q-1)(g-1),
\qquad q\ge2.
}
\tag{8.3}
\]

This is exactly the pluricanonical Riemann–Roch formula.

**Established endpoint:** (8.3) is classical Riemann–Roch.

**Derived bridge:** Sun's geodesic-loop Bergman formula + Chern-holonomy cancellation + standard conjugacy-class unfolding give an orbital proof in which only the identity orbital survives.

This gives a second, spectral/orbital realization of the previous Todd/GRR statement:

\[
\boxed{
\text{the local RR polynomial is the identity orbital; nontrivial hyperbolic orbitals cancel in the unweighted index trace.}
}
\tag{8.4}
\]

---

# Part V. Weighted orbitals are the genuinely global information

## 9. Gamma/Fourier representation

For a Schwartz function \(a\),

\[
(1-i\tau u)^{-2q}
=
\frac1{\Gamma(2q)}
\int_0^\infty s^{2q-1}e^{-s}e^{i\tau us}ds.
\]

Fubini gives

\[
\boxed{
\mathcal O_{q,\tau}[a]
=
\frac1{\Gamma(2q)}
\int_0^\infty
s^{2q-1}e^{-s}
\Re\widehat a(\tau s)ds.
}
\tag{9.1}
\]

If \(S\sim\mathrm{Gamma}(2q,1)\), this may be written

\[
\mathcal O_{q,\tau}[a]
=
\mathbb E\bigl[\Re\widehat a(\tau S)\bigr].
\tag{9.2}
\]

Since

\[
\mathbb E S=2q,
\qquad
\operatorname{Var}S=2q,
\]

one sees that the orbital transform samples the transverse Fourier transform around

\[
\xi=2q\tau
\]

with a frequency window of order \(\sqrt q\).

This is a high-frequency transform, not a local Taylor functional at the geodesic axis.

---

## 10. Exact polynomial annihilation versus nonlocal weights

For a polynomial \(a(u)=u^m\) with \(m\le2q-2\), Theorem A gives

\[
\mathcal O_{q,\tau}[a]=0.
\]

For a genuine geometric weight, the orbital depends on its global analytic/Fourier structure on the cylinder.

This is the corrected meaning of “nonperturbative Bergman correction” in the TSO note. The absolute size is exponentially controlled by loop length/injectivity radius, but the **signed coefficient** is determined only after the Chern phase and the weighted orbital transform are included.

---

# Part VI. Return to the Fisher–Kodaira–Spencer remainder

## 11. Exact remainder from TSO

The preceding note established

\[
\boxed{
\begin{aligned}
D_q(\mu)
:={}&I_{{\rm HBF},q}^{KE}(\mu,\mu)
-\mathfrak K_q(\mu,\mu)
-\frac1{12\pi}G_{\rm WP}(\mu,\mu)\\
={}&2\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
+\int_XW_q\,\beta_q\,dA,
\end{aligned}
}
\tag{11.1}
\]

where

\[
W_q
=|\mu|^2+2(q-1)f_\mu,
\qquad
f_\mu=(1+\square_0)^{-1}|\mu|^2,
\tag{11.2}
\]

and

\[
\beta_q=B_q-\frac{2q-1}{4\pi}.
\tag{11.3}
\]

The proven safe estimate remains

\[
D_q(\mu)=O(q^2e^{-c_Xq}).
\tag{11.4}
\]

Nothing in the present correction weakens (11.4).

---

## 12. Weighted Bergman term after conjugacy-class unfolding

Insert Sun's loop formula into the second term of (11.1) and unfold by hyperbolic conjugacy classes. For a class represented by \(\delta^m\), define the longitudinal average of the lifted weight on the cyclic cylinder by

\[
\overline W_{q,\delta,m}(u)
=
\frac1{L_\delta}
\int_0^{L_\delta}
W_q(t,u)dt.
\tag{12.1}
\]

Up to the explicit oriented-conjugacy multiplicity inherited from the chosen Selberg unfolding convention, its orbital is

\[
\boxed{
\mathcal B_{q,\delta^m}[W_q]
\propto
\frac{2q-1}{4\pi}
L_\delta
C_{m}^{-2q}
\mathcal O_{q,\tau_m}
[\overline W_{q,\delta,m}].
}
\tag{12.2}
\]

Thus the Bergman remainder is reduced to a family of one-dimensional Fourier/Gamma orbital transforms.

**Derived reduction.** Equation (12.2) is the precise object that must be evaluated to obtain the first nonzero Bergman coefficient. We deliberately do not guess its sign or leading exponent from the absolute length factor.

---

# Part VII. Comparison with Selberg length variation

## 13. FRZ systole asymptotic

Fedosova–Rowlett–Zhang prove that if the first variation of the systole length is nonzero, then

\[
\boxed{
\bar\partial_\mu\partial_\mu\log Z_{\rm Sel}(q)
\sim
-
\frac{q^2e^{-q\ell_0}}{1-e^{-\ell_0}}
\sum_{\gamma\in S(X)}
|\partial_\mu\ell(\gamma)|^2.
}
\tag{13.1}
\]

If all first systole variations vanish, the leading scale changes to \(qe^{-q\ell_0}\) and involves second length variation [FRZ20].

This is an established closed-geodesic expansion on the Selberg side.

---

## 14. The same resolvent weight occurs in the Hessian of length

Axelsson–Schumacher's second variation formula, as used explicitly by FRZ, contains

\[
(1+\square_0)^{-1}|\mu|^2=f_\mu.
\]

Schematically, for a closed geodesic \(\gamma\),

\[
\bar\partial_\mu\partial_\mu\ell(\gamma)
=
\frac12\int_\gamma
\left[
f_\mu+
(-D_t^2+2)^{-1}(\mu)\bar\mu
\right]
+
\frac1{\ell(\gamma)}
|\partial_\mu\ell(\gamma)|^2,
\tag{14.1}
\]

with the precise tensor conventions of [AS10; FRZ20].

But \(f_\mu\) is also the leading \(O(q)\) component of the Bergman weight \(W_q\) in (11.2).

This is the key structural overlap:

\[
\boxed{
\text{the weighted Bergman orbital and the Selberg length Hessian already contain the same elliptic resolvent }(1+\square_0)^{-1}|\mu|^2.
}
\tag{14.2}
\]

---

## 15. Open theorem target — common conjugacy-class basis

The remaining problem can now be formulated sharply.

**Open problem.** For every hyperbolic conjugacy class \([\gamma]\), express

\[
\mathcal O_{q,\tau_\gamma}
[\overline W_{q,\gamma}]
\]

in terms of the Teichmüller variations

\[
\partial_\mu\ell(\gamma),
\qquad
\bar\partial_\mu\partial_\mu\ell(\gamma),
\]

and possibly explicitly identified additional orbital data.

A positive solution would put both terms of (11.1) on the **same closed-geodesic/conjugacy-class basis**:

\[
\boxed{
D_q
=
\sum_{[\gamma]\ne1}
\left(
\text{Selberg length-variation orbital}
+
\text{Bergman Chern-holonomy orbital}
\right).
}
\tag{15.1}
\]

At that point the first nonperturbative coefficient could be determined rather than bounded.

---

# Part VIII. Representation-theoretic interpretation

## 16. Holomorphic discrete series viewpoint

The kernel

\[
(1-i\tau u)^{-2q}
\]

has exactly the analytic one-sided pole structure expected from holomorphic representation theory. Characters of holomorphic discrete series admit global formulas in the general Hermitian symmetric-space setting [Mar75], while Selberg's trace formula organizes spectral traces into conjugacy-class orbital integrals [McK72; Hejhal].

Sun's formula itself was inspired by trace-formula/Poincaré-series methods and explicitly highlights the analogy [Sun26].

**FCIG interpretation / conjectural representation-theory bridge.** The canonical Bergman projector may be viewed as a holomorphic-discrete-series test object whose unweighted nonidentity hyperbolic orbital integrals vanish, leaving precisely the identity/Riemann–Roch index term.

This sentence is an interpretation, not a cited theorem. A publication-level treatment should identify the precise discrete-series representation, test function, normalization and orbital integral in the Harish-Chandra/Selberg formalism.

---

# Part IX. What this changes in the FCIG picture

## 17. Local arithmetic versus global orbital information

The preceding TSO note found

\[
\frac1{12}
=
\frac{B_2}{2!}
=
-\zeta_{\mathbb R}(-1)
\]

inside the Todd class, and showed that relative dimension one makes the local determinant response a finite quadratic polynomial in \(q\).

The present note explains why the global Bergman realization does not contradict that exact local polynomial even though its pointwise kernel contains exponentially small loop terms: after integration with constant weight, the Chern phases annihilate all nonidentity hyperbolic orbitals.

So there are now two complementary exact mechanisms:

\[
\boxed{
\begin{array}{rcl}
\text{HRR/GRR side} &:&
\text{degree truncation fixes the local index polynomial},\\[1mm]
\text{Bergman orbital side} &:&
\text{Chern holonomy kills the unweighted nonidentity orbitals}.
\end{array}
}
\tag{17.1}
\]

They meet at the same Riemann–Roch state count.

---

## 18. Revised nonperturbative picture

The safe structural statement is now

\[
\boxed{
I_{{\rm HBF},q}^{KE}-\mathfrak K_q
=
\frac1{12\pi}G_{\rm WP}
+
\text{weighted hyperbolic orbital remainder}.
}
\tag{18.1}
\]

The remainder is exponentially small on a fixed compact surface, but its leading coefficient cannot be read from shortest-loop **length alone**. It depends on Chern phase and on the high-frequency transverse transform of the geometric weight.

Thus the earlier transseries slogan should be sharpened to

\[
\boxed{
\text{local Todd/index term}
+
\text{global holonomy-weighted conjugacy-class spectrum}.
}
\tag{18.2}
\]

This is closer to an actual trace formula than a simple instanton analogy.

---

# Part X. Proof obligations before publication

## 19. Remaining audit gates

1. Write the conjugacy-class unfolding of Sun's loop sum in one fixed oriented/unoriented convention and audit the centralizer volume and powers \(\delta^m\).
2. Give a self-contained proof of absolute convergence sufficient for termwise integration in the compact \(q\ge2\) case, or quote the exact proposition in Sun/periodization literature.
3. Match Sun's cylinder Chern-holonomy angle to the chosen canonical-bundle connection with all orientation signs. The moment-zero conclusion is orientation invariant, but a weighted complex orbital formula needs the sign fixed.
4. Extend the Fourier/Gamma transform from Schwartz weights to the actual cyclic-cover weight \(W_q\), using cutoffs or a distributional argument with justified limits.
5. Derive an explicit formula relating \(\mathcal O_{q,\tau}[\overline W_q]\) to first/second geodesic-length variations.
6. Identify the exact holomorphic-discrete-series test function/character whose hyperbolic orbital integral reproduces the kernel above; do not claim the representation-theory interpretation as a theorem before this step.
7. Only after 1–6 compute the first total nonperturbative coefficient in \(D_q\) and compare it with the FRZ systole coefficient.
8. Run a broader MathSciNet/zbMATH/reference-chain novelty audit before any originality claim. The present note is a research derivation, not a priority claim.

---

# 20. Reference map

- **Exact geodesic-loop Bergman formula and cylinder holonomy:** [Sun26].
- **Poincaré-series realization of quotient Bergman/Szegő kernels:** [LZ16].
- **Exponential Bergman estimates:** [Ber12; MM15].
- **Selberg trace/unfolding background:** [McK72; Hejhal].
- **Selberg-zeta Teichmüller variation and systole asymptotics:** [FRZ20].
- **Geodesic-length first/second variation:** [AS10].
- **Holomorphic discrete-series character background:** [Mar75].

No cited source is claimed to state Theorem A, the orbital Riemann–Roch bridge in Proposition B, or the FCIG weighted-orbital reduction in the precise form written here.
