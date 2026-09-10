# FCIG: Orbital–Character Closure for the Nonperturbative Information Remainder

**Status:** exact synthesis + sharply typed conjectural closure target  
**Date:** 2026-09-10  
**Scope:** compact hyperbolic Riemann surfaces, canonical Bergman kernels, cyclic Fourier modes, the Schumacher resolvent field, Harish--Chandra discrete-series characters, Selberg class factors, and the remaining weighted Fisher/Bergman orbital.  
**Depends on:** [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md), [`casimir-orbital-transmutation.md`](casimir-orbital-transmutation.md), [`cyclic-fourier-profile.md`](cyclic-fourier-profile.md), [`cyclic-mode-asymptotics.md`](cyclic-mode-asymptotics.md), [`sun-selberg-unfolding.md`](sun-selberg-unfolding.md), [`discrete-series-selberg-crosswalk.md`](discrete-series-selberg-crosswalk.md).

> **Claim firewall.** Nothing below identifies the weighted FCIG orbital with the ordinary Harish--Chandra character. The character, an orbital integral, and a matrix coefficient are different typed objects. The purpose of this note is to state exactly what would have to be proved for a representation-theoretic closure.

---

## 0. Result in one page

For a primitive closed geodesic \(c\) of length \(\ell_c\), let

\[
\nu_n=\frac{2\pi n}{\ell_c},
\qquad
\phi_c(t+i\theta)
=\sum_{n\in\mathbb Z}b_{n,c}e^{i\nu_nt}e^{-\nu_n(\theta-\pi/2)}
\]

be the cyclic Fourier expansion of the holomorphic quadratic differential representing a Teichmüller tangent direction. The already-established FCIG cylinder calculation gives

\[
\overline f_{c,\mu}(u)
=\sum_{n\in\mathbb Z}|b_{n,c}|^2F_{n,c}(u),
\qquad
f_\mu=(1+\square_0)^{-1}|\mu|^2.
\tag{0.1}
\]

For the \(m\)-fold winding, set \(L=m\ell_c\) and

\[
\kappa_{q,L}(u)
=\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}.
\tag{0.2}
\]

Define

\[
\Lambda_{n,c}^{(q,m)}
:=
\Re\int_{\mathbb R}F_{n,c}(u)\kappa_{q,m\ell_c}(u)\,du.
\tag{0.3}
\]

The Casimir-transmutation operator is

\[
\mathscr D_{q,L}
=
2q-1+q(q-1)(\cosh L-1)
-(\cosh L-1)\partial_L^2-\sinh L\,\partial_L.
\tag{0.4}
\]

Hence the weighted Bergman/Fisher orbital is exactly diagonal in the cyclic modes:

\[
\boxed{
\mathcal J_{q,m\ell_c}[W_q]
=
\sum_{n\in\mathbb Z}|b_{n,c}|^2
\,\mathscr D_{q,L}\Lambda_{n,c}^{(q,m)}
\big|_{L=m\ell_c}.
}
\tag{0.5}
\]

This is the **geometric side** of the remaining problem.

On the representation-theory side, with the convention of the companion crosswalk, holomorphic \(q\)-differentials match the discrete series \(D_{2q-1}^{+}\), and for a hyperbolic element of translation length \(L\),

\[
\boxed{
\Theta_{2q-1}^{+}(a_{L/2})
=
\frac{e^{-qL}}{1-e^{-L}}.
}
\tag{0.6}
\]

This is exactly the Selberg descendant denominator appearing in the large-\(q\) class factor. But (0.5) contains the deformation field, whereas (0.6) is a distributional trace. Therefore the correct target is not

\[
\mathcal J[W_q]=\Theta_{2q-1}^{+},
\]

which is ill-typed.

The target is instead a **weighted character transform**

\[
\boxed{
\mathfrak T_{q,c}[\mu]
=
\operatorname{Tr}_{D_{2q-1}^{+}}
\bigl(\mathcal A_{c,\mu}\,\pi_q(a_{\ell_c/2})\bigr)
}
\tag{0.7}
\]

or an equivalent relative/orbital distribution, for a geometrically defined operator \(\mathcal A_{c,\mu}\) whose cyclic \(K/A\)-mode expansion reproduces (0.5).

Equation (0.7) is a **conjectural typing template**, not a theorem. The operator \(\mathcal A_{c,\mu}\) has not yet been constructed.

The slogan is

\[
\boxed{
\text{Selberg denominator = representation trace;}
\qquad
\text{FCIG remainder = representation trace with a deformation insertion.}
}
\tag{0.8}
\]

---

# Part I. Three transforms that must not be conflated

## 1. Character

For a unitary representation \(\pi_q\), the Harish--Chandra character is the distribution

\[
\Theta_q(g)=\operatorname{Tr}\pi_q(g)
\]

in the distributional sense. On the regular hyperbolic set it is represented by a real-analytic class function. It depends only on the conjugacy class of \(g\).

It contains no Teichmüller tangent vector \(\mu\) by itself.

## 2. Orbital integral

For a test function \(h\) on \(G=PSL(2,\mathbb R)\), the hyperbolic orbital integral is schematically

\[
\mathcal O_g(h)
=
\int_{G_g\backslash G}h(x^{-1}gx)\,dx.
\tag{1.1}
\]

This is the object naturally produced by Selberg-style unfolding. Its normalization contains Haar measure and the centralizer measure.

The Sun/FCIG transverse cylinder integral belongs to this family of operations after the geometric kernel is translated into group language.

## 3. Matrix coefficient / inserted trace

For vectors \(v,w\) or an operator \(A\), one may instead form

\[
\langle v,\pi_q(g)w\rangle,
\qquad
\operatorname{Tr}(A\pi_q(g)).
\tag{1.2}
\]

These objects retain state/deformation information absent from the ordinary character.

This makes them the natural candidate type for the weighted FCIG response.

Thus the first closure principle is a type statement:

\[
\boxed{
\text{ordinary character}
\neq
\text{orbital integral}
\neq
\text{inserted trace/matrix coefficient}.
}
\tag{1.3}
\]

Any future equality must specify the map between these types and all measure normalizations.

---

# Part II. What already matches exactly

## 4. Casimir scale

The cylinder kernel obeys the exact transmutation identity

\[
\square_0\kappa_{q,L}
=
\left[q(q-1)(\cosh L-1)-\mathscr C_L\right]\kappa_{q,L},
\tag{2.1}
\]

where

\[
\mathscr C_L=(\cosh L-1)\partial_L^2+\sinh L\,\partial_L.
\]

The scalar \(q(q-1)\) is the expected holomorphic-discrete-series Casimir scale, subject to the convention crosswalk already isolated in the COT note.

## 5. Hyperbolic length variable

The same \(L=m\ell_c\) simultaneously labels

1. the deck transformation on the cyclic cover;
2. the Sun based-loop kernel;
3. the split-Cartan element \(a_{L/2}\);
4. the Selberg primitive/power factor.

No asymptotic identification is needed at this level.

## 6. Selberg denominator

The character crosswalk gives

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}}
=\sum_{k\ge0}e^{-(q+k)L}.
\tag{2.2}
\]

The denominator is therefore not a mysterious numerical correction: it is the descendant tower of the holomorphic discrete series in the chosen convention.

## 7. The zero-mode limitation

The FCIG zero cyclic mode already gives the correct exponential scale \(e^{-qL}\), but by itself it cannot generate the full denominator \((1-e^{-L})^{-1}\).

Hence the nonzero cyclic modes are not optional bookkeeping. They are the remaining degrees of freedom through which the representation tower can enter the deformation-weighted orbital.

---

# Part III. The operator-insertion conjecture

## 8. Geometric insertion

The deformation enters the Bergman curvature through

\[
W_q
=|\mu|^2+2(q-1)(1+\square_0)^{-1}|\mu|^2.
\tag{3.1}
\]

On the cyclic cover, longitudinal averaging makes this a positive quadratic expression in the Fourier data \(|b_{n,c}|^2\).

The sought-for representation operator \(\mathcal A_{c,\mu}\) must therefore satisfy at least:

- **quadraticity:** \(\mathcal A_{c,\lambda\mu}=|\lambda|^2\mathcal A_{c,\mu}\);
- **phase blindness after averaging:** dependence on the cyclic coefficients is through \(|b_{n,c}|^2\) at the diagonal level;
- **resolvent covariance:** the factor \((1+\square_0)^{-1}\) must become a resolvent/function of the representation Casimir or of the appropriate transverse generator;
- **centralizer covariance:** translating the base point along the closed geodesic must not change the final class coefficient;
- **orientation reality:** the two orientations combine by complex conjugation and produce a real Hessian contribution.

These are necessary conditions, not a construction.

## 9. Candidate spectral form

Let \(\{e_n\}\) denote the cyclic Fourier basis after passing to the cylinder model. A minimal candidate is an operator diagonal in this basis,

\[
\mathcal A_{c,\mu}^{(q)}e_n
=a_{n,c}^{(q)}(\mu)e_n,
\qquad
a_{n,c}^{(q)}(\mu)\propto |b_{n,c}|^2,
\tag{3.2}
\]

with coefficients chosen so that

\[
\boxed{
\operatorname{Tr}\left(
\mathcal A_{c,\mu}^{(q)}\pi_q(a_{m\ell_c/2})
\right)
=
\sum_n|b_{n,c}|^2
\mathscr D_{q,L}\Lambda_{n,c}^{(q,m)}
\big|_{L=m\ell_c}.
}
\tag{3.3}
\]

Equation (3.3) is the **Orbital–Character Closure Conjecture (OCC)** in its strongest useful classwise form.

It should first be proved on one cyclic cylinder. Only then should it be summed over primitive classes.

---

# Part IV. Local, classwise and global closure are different theorems

## 10. Level 1 — kernel closure

Construct an intertwiner between

\[
\kappa_{q,L}(u)
\]

and a standard matrix coefficient or coherent-state kernel of \(D_{2q-1}^{+}\), with the Chern-holonomy phase retained.

This is a local/cylinder statement.

## 11. Level 2 — classwise closure

Prove (3.3), including

- centralizer length;
- the \(m\)-fold winding convention;
- orientation factor;
- the \(L\)-derivatives in \(\mathscr D_{q,L}\);
- convergence of the cyclic-mode trace.

This is the first level at which comparison with the FRZ class coefficient is mathematically meaningful.

## 12. Level 3 — global trace closure

Only after Level 2 may one sum over primitive classes and powers:

\[
\sum_{[c]_{\rm prim}}\sum_{m\ge1}
\mathfrak T_{q,c,m}[\mu].
\tag{4.1}
\]

To identify this with a global Selberg/Quillen/Fisher remainder requires an independent absolute-convergence or regularized-trace argument.

Therefore

\[
\boxed{
\text{kernel match}
\not\Rightarrow
\text{classwise coefficient match}
\not\Rightarrow
\text{global determinant identity}.
}
\tag{4.2}
\]

This is the main normalization firewall for the next stage of FCIG.

---

# Part V. A falsifiable mode test

## 13. Numerical/analytic checker target

Before trying to prove OCC abstractly, the existing explicit cylinder model gives a direct falsification test.

For fixed \((q,\ell,m)\):

1. solve
   \[
   \left[1-\frac12\partial_u((1+u^2)\partial_u)\right]F_{n,\ell}=A_{n,\ell};
   \]
2. compute
   \[
   \Lambda_n^{(q,m)}(\ell)
   =\Re\int F_{n,\ell}(u)\kappa_{q,m\ell}(u)du;
   \]
3. apply \(\mathscr D_{q,L}\);
4. study the multiplier sequence
   \[
   B_n^{(q,m)}(\ell)
   :=\mathscr D_{q,L}\Lambda_n^{(q,m)}(\ell)|_{L=m\ell};
   \]
5. compare its generating function
   \[
   \mathcal B_{q,m}(z;\ell)
   :=\sum_{n\in\mathbb Z}B_n^{(q,m)}(\ell)z^n
   \tag{5.1}
   \]
   with the generating functions of the appropriate discrete-series matrix coefficients.

A representation-theoretic closure should force nontrivial recurrences in \(n\) coming from the \(\mathfrak{sl}_2\) raising/lowering operators. Failure of those recurrences would falsify the simplest diagonal-insertion ansatz (3.2) without threatening the already-proved geometric identities.

This gives FCIG a useful computational principle:

\[
\boxed{
\text{do not fit the Selberg denominator; test the }\mathfrak{sl}_2\text{ recurrence that would force it.}
}
\tag{5.2}
\]

---

# Part VI. Relation to the information-geometry program

## 14. Why the insertion is the information tensor

The Hermitian Born--Fisher / Kodaira--Spencer track already isolates a canonical high-\(q\) Weil--Petersson term plus a finite/global remainder. The present orbital calculation asks what microscopic object carries that remainder.

The deformation insertion \(\mathcal A_{c,\mu}\) would provide a precise representation-theoretic answer:

\[
\boxed{
\text{information response}
=
\text{character geometry with an infinitesimal deformation insertion}.
}
\tag{6.1}
\]

This would connect three descriptions of the same finite-\(q\) phenomenon:

\[
\text{Bergman/DPP Fisher curvature}
\longleftrightarrow
\text{Kodaira--Spencer resolvent}
\longleftrightarrow
\text{weighted automorphic orbital data}.
\tag{6.2}
\]

The arrows are currently partly proved asymptotically and partly conjectural nonperturbatively. No Lorentzian or gravitational dynamics is implied by (6.2).

---

# Part VII. Open gates

## OCC-A — explicit discrete-series kernel realization

**OPEN.** Write Sun's oriented cylinder kernel as a standard coherent-state/matrix-coefficient kernel of \(D_{2q-1}^{+}\), including the exact normalization.

## OCC-B — resolvent-to-Casimir insertion

**OPEN.** Translate

\[
(1+\square_0)^{-1}|\mu|^2
\]

into a canonical representation-theoretic operator insertion, rather than a coordinate-dependent multiplier.

## OCC-C — cyclic-mode recurrence

**OPEN / computationally testable.** Derive the \(\mathfrak{sl}_2\) recurrence satisfied by the candidate mode coefficients and test it against \(B_n^{(q,m)}\).

## OCC-D — classwise character coefficient

**OPEN.** Prove or refute that the first varying-length channel of the inserted trace reduces asymptotically to

\[
-q^2\Theta_{2q-1}^{+}(a_{\ell_c/2})
|\partial_\mu\ell_c|^2
\]

with the FRZ normalization.

## OCC-E — total primitive-class sum

**OPEN.** Establish convergence/regularization and compare the sum with the finite Selberg/Bergman correction in the Fisher--Kodaira--Spencer closure.

---

## 15. Research boundary

What is now established is unusually rigid:

\[
\boxed{
\begin{array}{c}
\text{same cyclic Fourier deformation data}\\
\downarrow\\
\text{two different spectral filters: length/Selberg and Bergman/Fisher},\\[1mm]
q(q-1)\text{ Casimir scale},\\
\Theta_{2q-1}^{+}(a_{L/2})=e^{-qL}/(1-e^{-L}),\\
\text{exact Chern-phase orbital cancellation for constant weight}.
\end{array}
}
\]

The remaining leap is no longer “perhaps Selberg and Bergman are related.” It is the sharply falsifiable question:

\[
\boxed{
\text{Is the weighted FCIG orbital an inserted discrete-series trace, and if so what is the insertion?}
}
\]

That is the nonperturbative representation-theory frontier.

## Sources

- Harish--Chandra, *Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters*, Acta Math. **116** (1966), 1--111.
- Jingzhou Sun, *On the Bergman Kernel of Hyperbolic Riemann Surfaces*, exact geodesic-loop Bergman formula; see the dedicated Sun bibliography/audit in the companion FCIG notes.
- K. Fedosova, J. Rowlett, G. Zhang, *Second Variation of Selberg Zeta Functions and Curvature Asymptotics*, Ann. Global Anal. Geom. **57** (2020), 23--60.
- Axelsson--Schumacher, closed-geodesic first/second variation formulae; see `casimir-orbital-transmutation.bib`.
- Labesse and standard Euler--Poincare/pseudo-coefficient literature for the distinction between discrete-series characters and nonelliptic orbital integrals; see the COT citation audit.
