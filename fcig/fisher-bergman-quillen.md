# FCIG: Fisher–Bergman–Quillen Information Closure

**Status:** source-audited mathematical research note  
**Date:** 2026-09-10  
**Scope:** probability/information geometry, Bergman quantization, determinant/Quillen geometry. Lorentzian gravity is **not** derived here.

> **Claim policy.** **Established** means a cited theorem or standard construction. **Derived here** means a calculation carried out below in the stated conventions; this label is not a novelty claim. **FCIG interpretation** means terminology or a proposed reading. **Conjecture/Open problem** marks the genuinely unproved bridge.
>
> Milestone bibliography: [`fisher-bergman-quillen.bib`](fisher-bergman-quillen.bib). General FCIG bibliography: [`references.bib`](references.bib).

---

## 0. Why this note exists

The general FCIG note separates the quantization line on the total space, the direct image, the determinant line on parameter space, the Bergman density, and the eventual gravity-closure problem. The Quillen refinement then separates the ordinary \(L^2\) determinant metric from the Quillen metric and analytic torsion.

The missing mathematical layer was information geometry itself. This note inserts it without identifying unrelated objects by analogy.

The target is the controlled chain

\[
\boxed{
\text{event logic / probability law}
\to
\text{Bergman determinantal process}
\to
\text{Fisher response}
\to
\text{direct-image / determinant response}
\to
\text{Quillen / index curvature}.
}
\]

The central question is not whether all arrows are literally identities. It is:

\[
\boxed{
\text{which correction terms measure the failure of the triangle to commute?}
}
\]

---

# Part I. Probability, schemes, and the correct home of information geometry

## 1. Event logic as a Boolean spectrum

Let \((\Omega,\mathcal F,p)\) be a probability space. Give the event algebra the Boolean-ring operations

\[
E+F:=E\triangle F,
\qquad
EF:=E\cap F.
\]

Then

\[
A_{\mathcal F}:=(\mathcal F,\triangle,\cap)
\]

is a Boolean ring. Every element is idempotent,

\[
a^2=a,
\]

so \(A_{\mathcal F}\) is reduced. Stone duality identifies Boolean algebras with compact totally disconnected Stone spaces; ring-theoretically one may use

\[
X_{\mathcal F}:=\operatorname{Spec}A_{\mathcal F}.
\]

**Established.** This is the Stone representation picture [Sto36].

A point of \(X_{\mathcal F}\) is generally an ultrafilter of events, not literally a sample point \(\omega\in\Omega\). Thus

\[
\boxed{
\operatorname{Spec}A_{\mathcal F}
=\text{the spectrum of event logic},
\quad\text{not a canonical replacement for }\Omega.
}
\]

### Null events

Set

\[
\mathcal N_p:=\{E\in\mathcal F:p(E)=0\}.
\]

It is an ideal, and the quotient

\[
A_p:=A_{\mathcal F}/\mathcal N_p
\]

implements

\[
E\sim F
\iff
p(E\triangle F)=0.
\]

**Derived here / correction of an earlier FCIG heuristic.** Null events must not be called nilpotents. Since every Boolean ring is reduced,

\[
\operatorname{Nil}(A_{\mathcal F})=0.
\]

Therefore

\[
\boxed{
\text{a.e. identification}
=\text{quotient by the null ideal},
\qquad
\text{not scheme-theoretic reduction}.
}
\]

We will use the descriptive term

\[
\mathfrak S_p=(\operatorname{Spec}A_p,\bar p)
\]

for the Stone spectrum together with the descended probability valuation.

**FCIG interpretation.** “Measured Stone scheme” is terminology used in this project, not a claim that ordinary scheme structure alone encodes sigma-additivity. The measure/valuation remains additional data. Simpson's probability-sheaf framework provides a genuinely categorical/sheaf-theoretic treatment of probability spaces and random variables [Sim17].

---

## 2. Information geometry lives on deformations of probability laws

A smooth statistical model is a family

\[
B\ni b\longmapsto p_b.
\]

Its Fisher metric is

\[
g^{\mathrm F}_{\alpha\beta}(b)
=
\mathbb E_b
\left[
\partial_\alpha\log p_b\,
\partial_\beta\log p_b
\right],
\]

with the Amari--Chentsov cubic tensor obtained from the third score moment. These are standard information-geometric objects [Cen82; AN00].

The important typing rule is

\[
\boxed{
\operatorname{Spec}A_p
=\text{event geometry},
\qquad
B
=\text{deformation geometry of probability laws}.
}
\]

Thus FCIG does not put a Fisher metric on the Stone spectrum by fiat. It puts Fisher geometry on the parameter/moduli base carrying a family of probability valuations.

Global dual flatness is not an axiom of this construction. Exponential families provide an important flat special case; a general statistical manifold need not be globally Hessian or dually flat.

---

# Part II. From Bergman kernels to statistical models

## 3. One-particle Fisher--Bergman correspondence

For a reproducing-kernel Hilbert space with kernel \(K(x,y)\), write

\[
B(x)=K(x,x).
\]

The normalized kernel density

\[
\boxed{
p_x(y)=\frac{|K(x,y)|^2}{B(x)}}
\]

is a probability density whenever the reproducing identity gives

\[
\int |K(x,y)|^2d\nu(y)=B(x).
\]

For bounded complex domains, Cho--Yum construct precisely such a statistical embedding and prove that the pullback Fisher metric is the Bergman metric [CY23]. Earlier Fisher/Bergman connections occur in work of Burbea and Rao.

**Established in the cited setting.**

The slogan is therefore literal in that setting:

\[
\boxed{
\text{Bergman metric}
=\text{Fisher metric of a canonical kernel probability model}.
}
\]

This does not yet see the determinant line. For that, one needs the many-body state.

---

## 4. Bergman determinantal process as the common many-body object

Let \(X\) be compact complex, \(L\to X\) positive, and

\[
\mathcal H_k=H^0(X,L^k),
\qquad
N_k=\dim\mathcal H_k.
\]

Choose a basis \(s_1,\dots,s_{N_k}\). On \(X^{N_k}\), define the Slater determinant

\[
\Psi_k(x_1,\dots,x_{N_k})
=
\det(s_i(x_j)).
\]

For a Hermitian metric \(h_\phi=h_0e^{-\phi}\) and Kähler volume

\[
dV_\phi=\frac{\omega_\phi^n}{n!},
\qquad
\omega_\phi=\omega_0+i\partial\bar\partial\phi,
\]

set

\[
q_{k,\phi}(\mathbf x)
=
\frac1{N_k!}
|\Psi_k(\mathbf x)|^2_{h_\phi^{k\boxtimes N_k}}
\prod_{a=1}^{N_k}dV_\phi(x_a).
\]

The partition function is

\[
Z_k[\phi]=\int_{X^{N_k}}q_{k,\phi}.
\]

By the Gram/Andreief identity,

\[
\boxed{Z_k[\phi]=\det G_k(\phi)},
\]

where \(G_k\) is the \(L^2\) Gram matrix. The normalized law

\[
d\mathbf P_{k,\phi}=Z_k[\phi]^{-1}q_{k,\phi}
\]

is the Bergman projection DPP; its correlation kernel is the Bergman kernel and its one-point intensity is

\[
\rho_{k,\phi}(x)=K_{k,\phi}(x,x).
\]

**Established background.** Bergman DPPs on polarized complex manifolds and their large-\(k\) asymptotics are developed by Berman [Ber08]. General projection-DPP identities are standard [HKPV09]. Eum studies the corresponding polarized-Kähler partition functions and derives their full asymptotic expansion both from Bergman asymptotics and from Quillen anomaly plus analytic torsion [Eum26].

---

# Part III. Exact fixed-complex-structure identities

Throughout this part the complex manifold \((X,J)\) and holomorphic line \(L\) are fixed. Only the Kähler/Hermitian potential \(\phi\) varies.

We use the Laplacian convention

\[
\Delta_\phi f=g_\phi^{i\bar j}\partial_i\partial_{\bar j}f.
\]

## 5. Proposition A: exact score operator

Let \(\psi\in C^\infty(X,\mathbb R)\) be a tangent direction. Then

\[
D_\psi\log
|\Psi_k|^2_{h_\phi^{k\boxtimes N_k}}
=
-k\sum_a\psi(x_a),
\]

while

\[
D_\psi\log dV_\phi
=
\Delta_\phi\psi.
\]

Hence, defining

\[
\boxed{A_{k,\phi}:=\Delta_\phi-k},
\]

we obtain

\[
\boxed{
D_\psi\log q_{k,\phi}
=
\sum_{a=1}^{N_k}A_{k,\phi}\psi(x_a).
}
\tag{5.1}
\]

The normalized score is therefore

\[
\boxed{
\mathcal S_{k,\phi}[\psi]
=
L_{A_k\psi}-\mathbb E_\phi L_{A_k\psi},
\qquad
L_f:=\sum_af(x_a).
}
\tag{5.2}
\]

**Derived here.** Equation (5.1) is a direct variation of the Hermitian weight and Kähler volume. It is not attributed as a named theorem to the references above.

**FCIG slogan.**

\[
\boxed{
\text{score}
=
\text{volume/Laplacian response}
-
\text{quantization response}.
}
\]

---

## 6. Proposition B: exact Fisher--Bergman kernel energy

Define the Fisher bilinear form

\[
\mathcal I_{k,\phi}(\psi,\eta)
=
\mathbb E_\phi
[\mathcal S[\psi]\mathcal S[\eta]].
\]

From (5.2),

\[
\boxed{
\mathcal I_{k,\phi}(\psi,\eta)
=
\operatorname{Cov}_\phi
(L_{A_k\psi},L_{A_k\eta}).
}
\tag{6.1}
\]

For a projection DPP,

\[
\operatorname{Cov}(L_f,L_g)
=
\int_Xfg\,\rho_kdV
-
\iint_{X\times X}
f(x)g(y)|K_k(x,y)|^2dV_xdV_y.
\]

Using the projection identity

\[
\int_X|K_k(x,y)|^2dV_y=K_k(x,x),
\]

this symmetrizes to

\[
\boxed{
\begin{aligned}
\mathcal I_{k,\phi}(\psi,\eta)
&=\frac12
\iint_{X\times X}
\bigl(A_k\psi(x)-A_k\psi(y)\bigr)
\\
&\qquad\times
\bigl(A_k\eta(x)-A_k\eta(y)\bigr)
|K_k(x,y)|^2dV_xdV_y.
\end{aligned}
}
\tag{6.2}
\]

**Derived here from established projection-DPP covariance identities** [HKPV09].

This gives the first exact side of the triangle:

\[
\boxed{
\textbf{Fisher information is an off-diagonal Bergman-kernel energy.}
}
\]

Hino--Yano independently place DPPs inside the framework of curved exponential families and information geometry [HY24]. Their setting is finite/discrete; equation (6.2) is the FCIG continuous Bergman-DPP specialization derived here.

---

## 7. Proposition C: exact free-energy Hessian defect

The first variation of the partition function is

\[
D_\psi\log Z_k
=
\mathbb E_\phi L_{A_k\psi}
=
\int_X(\Delta_\phi\psi-k\psi)\rho_{k,\phi}\,dV_\phi.
\tag{7.1}
\]

After integration by parts,

\[
D_\psi\log Z_k
=
\int_X\psi(\Delta_\phi\rho_{k,\phi}-k\rho_{k,\phi})dV_\phi.
\tag{7.2}
\]

The important point is that this is **not** a fixed sufficient-statistic exponential family: \(A_{k,\phi}=\Delta_\phi-k\) itself moves with \(\phi\).

For fixed tangent functions \(\psi,\eta\),

\[
D_\eta(\Delta_\phi\psi)
=
-
\langle i\partial\bar\partial\psi,
i\partial\bar\partial\eta\rangle_\phi.
\tag{7.3}
\]

Differentiating the expectation in (7.1) gives

\[
\boxed{
\operatorname{Hess}_\phi\log Z_k(\psi,\eta)
=
\mathcal I_{k,\phi}(\psi,\eta)
-
\mathfrak D^{\mathrm{met}}_{k,\phi}(\psi,\eta),
}
\tag{7.4}
\]

where

\[
\boxed{
\mathfrak D^{\mathrm{met}}_{k,\phi}(\psi,\eta)
=
\int_X
\rho_{k,\phi}
\langle i\partial\bar\partial\psi,
i\partial\bar\partial\eta\rangle_\phi
dV_\phi.
}
\tag{7.5}
\]

Equivalently,

\[
\boxed{
\mathcal I_k
=
\operatorname{Hess}\log Z_k
+
\mathfrak D^{\mathrm{met}}_k.
}
\tag{7.6}
\]

**Derived here.** This is the correction to the too-strong statement “Fisher = Hessian of \(\log Z\)” for the moving Kähler-volume model.

The defect is positive semidefinite on real tangent directions:

\[
\mathfrak D^{\mathrm{met}}_k(\psi,\psi)\ge0.
\]

So the failure of the exponential-family Hessian identity is itself geometric and computable.

---

## 8. Semiclassical structure of the metric defect

The Tian--Yau--Zelditch expansion gives, with convention-dependent constants,

\[
\rho_{k,\phi}
\sim
c_0k^n+c_1\operatorname{Scal}(\omega_\phi)k^{n-1}+\cdots
\]

[Zel98; Lu00; MM07]. Hence

\[
\boxed{
\mathfrak D^{\mathrm{met}}_k(\psi,\eta)
\sim
c_0k^n
\int_X
\langle i\partial\bar\partial\psi,
i\partial\bar\partial\eta\rangle dV
+O(k^{n-1}).
}
\tag{8.1}
\]

All literal coefficients remain tied to the normalization of \(\omega\), \(L\), and the Laplacian.

Berman proves Gaussian fluctuation results for Bergman DPP linear statistics in the bulk [Ber08]. Those results motivate a detailed scaling analysis of (6.2), but this note does **not** promote a universal leading coefficient for \(\mathcal I_k\) without carrying out that normalization audit.

---

# Part IV. Quillen bookkeeping without hiding the torsion term

## 9. \(L^2\) determinant versus Quillen determinant

Assume \(k\gg1\) so higher cohomology vanishes, and put

\[
\lambda_k=\det H^0(X,L^k).
\]

For the determinant frame

\[
\Sigma=s_1\wedge\cdots\wedge s_{N_k},
\]

our \(L^2\) convention is

\[
\boxed{
h_{L^2}(\Sigma,\Sigma)=\det G_k=Z_k.}
\tag{9.1}
\]

Following the convention already fixed in [`quillen-refinement.md`](quillen-refinement.md), define holomorphic analytic torsion \(\mathcal T_k\) by

\[
\boxed{h_Q=e^{\mathcal T_k}h_{L^2}.}
\tag{9.2}
\]

Quillen introduced the determinant metric in the Cauchy--Riemann setting [Qui85]; Bismut--Gillet--Soulé proved the holomorphic-family curvature/anomaly formula [BGS88]; high-power analytic-torsion asymptotics were studied by Bismut--Vasserot [BV89].

From (9.1)--(9.2), on the real space of Kähler potentials,

\[
\operatorname{Hess}\log Z_k
=
\operatorname{Hess}\log h_Q(\Sigma,\Sigma)
-
\operatorname{Hess}\mathcal T_k.
\]

Combining with (7.6),

\[
\boxed{
\mathcal I_k
=
\operatorname{Hess}\log h_Q
-
\operatorname{Hess}\mathcal T_k
+
\mathfrak D^{\mathrm{met}}_k.
}
\tag{9.3}
\]

**Derived here in the convention (9.2).** Equation (9.3) is a real functional-Hessian identity; it should not be confused with a Chern-curvature \((1,1)\)-form until a complex parameter family is specified.

For a complex base coordinate, using

\[
F_h=-\partial\bar\partial\log h,
\]

one instead has the convention-sensitive relation

\[
\partial\bar\partial\log Z_k
=
-F_Q-\partial\bar\partial\mathcal T_k.
\tag{9.4}
\]

Thus any slogan “Fisher curvature = Quillen curvature” is false without specifying dualization/sign conventions and the two correction channels.

The robust statement is

\[
\boxed{
\text{Fisher response}
=
\text{Quillen response}
+\text{torsion correction}
+\text{metric/volume defect},
}
\]

with signs fixed only after choosing whether one works on \(\lambda_k\) or \(\lambda_k^\vee\) and whether the response is a real Hessian or a Chern form.

---

## 10. What is already closed in the literature

Eum proves a full asymptotic expansion for polarized-Kähler DPP partition functions and derives it in two ways: via Bergman-kernel asymptotics and via the Quillen anomaly formula plus Ray--Singer analytic torsion [Eum26]. This gives a powerful established Bergman--Quillen bridge.

Eum's subsequent preprint constructs determinant lines over the space of compatible integrable complex structures, studies the asymptotic expansion of their Quillen curvature, and identifies moment maps generalizing the Donaldson--Fujiki scalar-curvature picture [Eum25].

These works do **not** by themselves prove the FCIG identity (7.6) or the full fibered Fisher decomposition below. They substantially narrow the open part of the problem.

---

# Part V. The moving-family problem

## 11. Direct-image curvature already contains the missing geometric channels

Let

\[
\pi:\mathcal X\to B
\]

be a proper holomorphic submersion with compact fibers and let \(L\to\mathcal X\) be relatively positive. The natural bundle for Berndtsson's theorem is

\[
E_k
=
\pi_*(K_{\mathcal X/B}\otimes L^k).
\]

With its fiberwise \(L^2\) metric, \(E_k\) has Nakano-positive curvature under the standard positivity hypotheses [Bern09]. More refined curvature formulae separate two geometric mechanisms:

1. variation of the Hermitian/Kähler weight (geodesic-curvature sector);
2. variation of complex structure, represented by the Kodaira--Spencer class.

Wan--Zhang compute the high-\(k\) asymptotics of both the \(L^2\) direct-image curvature and Quillen curvature for \(\pi_*(L^k\otimes K_{\mathcal X/B})\), and show in particular that

\[
\partial\bar\partial\log\tau_k^2=o(k^{n-1})
\]

in their normalization [WZ21]. Their coefficients contain the fiber curvature and Kodaira--Spencer geometry.

**Established.**

This makes the FCIG target much sharper: the direct-image/Quillen side already knows the Kodaira--Spencer deformation. What remains is to identify precisely how the score of the **fibered Bergman DPP** records the same deformation.

---

## 12. Information Closure Conjecture

To compare probability measures on distinct fibers, one must first choose a geometrically natural identification, e.g. an Ehresmann/horizontal connection, and prove that the resulting Fisher form is independent of irrelevant choices or record its dependence explicitly.

Let

\[
\mathcal I_{k,b}(\xi,\bar\xi)
\]

be the Fisher form of the resulting family of Bergman DPPs in a base direction \(\xi\in T_bB\).

### Conjectural decomposition

**Conjecture.** After fixing a precise horizontal transport and determinant-line convention, there is a decomposition of the schematic form

\[
\boxed{
\mathcal I_k
=
\mathcal R_k^{Q}
+
\mathfrak D_k^{\mathrm{met}}
+
\mathfrak D_k^{KS}
+
\mathfrak D_k^{\mathrm{tors}},
}
\tag{12.1}
\]

where

- \(\mathcal R_k^{Q}\) is the appropriately signed/dualized Quillen response;
- \(\mathfrak D_k^{\mathrm{met}}\) reduces to (7.5) when the complex structure is fixed;
- \(\mathfrak D_k^{KS}\) is determined by Kodaira--Spencer deformation data;
- \(\mathfrak D_k^{\mathrm{tors}}\) is the analytic-torsion correction already isolated by the Quillen metric.

The conjecture deliberately does **not** assert that the Kodaira--Spencer term equals a particular resolvent expression until the statistical transport is defined and the bundle \(H^0(L^k)\) versus \(H^0(K\otimes L^k)\) convention is reconciled.

The desired asymptotic statement is

\[
\boxed{
\mathfrak D_k^{KS}
\sim
k^n C_n\|\mu_\xi\|_{L^2}^2
+k^{n-1}(\text{curvature/derivative terms})+\cdots,
}
\tag{12.2}
\]

with a coefficient \(C_n\) determined, not guessed, by the normalization.

This is the **Information Closure Problem** of FCIG.

---

## 13. First serious laboratory: genus \(g\ge2\)

For a family of compact hyperbolic Riemann surfaces, the Kodaira--Spencer tangent vector is represented by a harmonic Beltrami differential \(\mu\), and the Weil--Petersson metric is its \(L^2\) pairing.

The first falsifiable target is therefore:

\[
\boxed{
\text{Does the leading complex-structure Fisher form of the Bergman DPP converge, after normalization, to }C\,\omega_{WP}?
}
\tag{13.1}
\]

A pass requires all of the following:

1. define the fiber-to-fiber statistical transport;
2. compute the score including motion of the complex structure, metric, and volume;
3. identify the Kodaira--Spencer contribution without fitting a coefficient;
4. compare it with the known \(L^2\)/Quillen direct-image asymptotics [Bern09; WZ21];
5. determine \(C\) from the calculation;
6. check compatibility with the exact hyperbolic Quillen/Weil--Petersson formulas already recorded in this repository.

A failure is also informative: it would exhibit a precise noncommutativity defect between statistical and determinant geometry.

---

# Part VI. Relation to the FCIG program

## 14. What this changes

The earlier heuristic

\[
\text{gravity}\sim\nabla S
\]

is neither needed nor supported by the calculations here.

The controlled replacement is

\[
\boxed{
\begin{aligned}
\text{probability variation}
&\to\text{Fisher covariance},\\
\text{quantized state variation}
&\to\text{Bergman kernel},\\
\text{complex-structure variation}
&\to\text{Kodaira--Spencer geometry},\\
\text{global determinant response}
&\to\text{Quillen / families index geometry}.
\end{aligned}
}
\]

**FCIG interpretation.** Fisher and Quillen are two response geometries of one quantized statistical family: Fisher probes fluctuations of the normalized microscopic process, while Quillen packages the determinant/index response including its spectral correction.

The research question is whether they are related by explicit, computable defect tensors.

---

## 15. Scheme layer, information layer, determinant layer

The integrated architecture is now

\[
\boxed{
\begin{array}{rcl}
\text{event layer} &:& A_{\mathcal F}/\mathcal N_p,\ \operatorname{Spec}A_p,\\
\text{probability layer} &:& p_b\text{ or }\mathbf P_{k,b},\\
\text{information layer} &:& g_F,\ C_{ijk},\\
\text{quantization layer} &:& H^0(X_b,L_b^k),\ K_k,\rho_k,\\
\text{determinant layer} &:& \det R\pi_*L^k,\ h_{L^2},\ h_Q,\\
\text{index layer} &:& \pi_*(\operatorname{Td}(T_\pi)\operatorname{ch}(L^k)).
\end{array}
}
\]

No layer is identified with another solely because their curvature forms look similar.

---

## 16. Gravity Closure remains inactive

Nothing in this note supplies causal structure, Lorentz signature, local horizon thermodynamics, or a map from a \(U(1)\) determinant curvature to an \(\mathfrak{so}(1,3)\)-valued Riemann curvature.

Therefore the repository policy remains:

\[
\boxed{
\text{Information Closure first; Lorentzian Gravity Closure later.}
}
\]

---

# 17. Proof obligations before promotion beyond research-note status

The fixed-complex-structure identities (5.1), (6.2), and (7.6) are short enough to audit directly. The next publication-level obligations are harder:

- [ ] write the DPP measure relative to one fixed reference density and verify all Jacobian conventions;
- [ ] prove the regularity/interchange-of-derivative hypotheses used in the score calculation;
- [ ] audit constants in the \(\Delta\), \(dd^c\), curvature, and \(2\pi\) conventions;
- [ ] formulate the complex-base Fisher tensor separately from the real Kähler-potential Hessian;
- [ ] reconcile \(H^0(L^k)\) with Berndtsson's natural \(H^0(K_{X/B}\otimes L^k)\) bundle;
- [ ] define horizontal statistical transport for moving fibers;
- [ ] derive, rather than postulate, the Kodaira--Spencer score term;
- [ ] compute the genus-\(g\ge2\) leading coefficient and compare with Weil--Petersson geometry;
- [ ] search the literature specifically for an existing theorem equivalent to (7.6) or (12.1) before any novelty claim.

Until those gates pass, (12.1) is a conjectural research target, not a theorem.

---

# 18. Source map

- **Stone/event spectrum:** [Sto36].
- **Probability sheaves:** [Sim17].
- **Fisher/information geometry:** [Cen82; AN00].
- **Kernel statistical embedding:** [CY23].
- **General DPP covariance identities:** [HKPV09].
- **Information geometry of DPPs:** [HY24].
- **Bergman DPP / fluctuations:** [Ber08].
- **Bergman/TYZ asymptotics:** [Zel98; Lu00; MM07].
- **Direct-image curvature:** [Bern09].
- **High-power \(L^2\)/Quillen curvature comparison:** [WZ21].
- **Quillen metric / anomaly:** [Qui85; BGS88].
- **High-power analytic torsion:** [BV89].
- **DPP partition functions, Bergman vs Quillen derivations:** [Eum26].
- **Quillen variation / moment-map expansion:** [Eum25].

The formulas explicitly tagged **Derived here** above should be checked from the derivation itself, not attributed to these sources.
