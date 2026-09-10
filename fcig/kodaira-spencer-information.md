# FCIG: Kodaira--Spencer Information Tensor and the Weil--Petersson Limit

**Status:** worked theorem/no-go note  
**Date:** 2026-09-10  
**Scope:** compact genus-\(g\ge2\) curve families, direct-image curvature, Bergman high-power asymptotics, statistical transport.  
**Depends on:** [`hyperbolic-model.md`](hyperbolic-model.md), [`quillen-refinement.md`](quillen-refinement.md), [`fisher-bergman-quillen.md`](fisher-bergman-quillen.md).

> **Claim policy.** **Established** means a cited theorem/formula. **Derived here** means a deduction obtained below from the cited formulae in the stated normalization; it is not a novelty claim. **No-go** means a proved obstruction to an over-strong FCIG identification. **Open** means the remaining research problem.
>
> Milestone bibliography: [`kodaira-spencer-information.bib`](kodaira-spencer-information.bib).

---

## 0. Result in one page

Let

\[
\pi:\mathcal X\to B
\]

be a holomorphic family of compact Riemann surfaces of genus \(g\ge2\), equipped fiberwise with the hyperbolic Kähler--Einstein metric, and let

\[
E_q=\pi_*K_{\mathcal X/B}^{q},\qquad q\ge2.
\]

Write

\[
m=q-1,
\]

so that Berndtsson's natural adjoint bundle is

\[
E_q=\pi_*(K_{\mathcal X/B}\otimes K_{\mathcal X/B}^{m}).
\]

For a tangent vector \(\xi\in T_bB\), let \(\mu_\xi\) denote its harmonic Kodaira--Spencer representative on \(X_b\). If \(u_1,\dots,u_{N_q}\) is any \(L^2\)-orthonormal basis of \(H^0(X_b,K_{X_b}^{q})\), define

\[
\boxed{
\mathfrak K_q(\xi,\bar\eta)
:=
m\sum_{a=1}^{N_q}
\left\langle
(m+\Delta')^{-1}i_{\mu_\xi}u_a,
 i_{\mu_\eta}u_a
\right\rangle .
}
\tag{0.1}
\]

This is the trace of the Kodaira--Spencer resolvent summand in Berndtsson's direct-image curvature formula [Bern09; WZ21]. It is basis-independent and positive semidefinite.

Define the Weil--Petersson Hermitian pairing in the normalization used in this note by

\[
\boxed{
G_{\mathrm{WP}}(\xi,\bar\eta)
:=
\int_{X_b}
\langle\mu_\xi,\mu_\eta\rangle\,\omega_b.
}
\tag{0.2}
\]

Then the main deduction is

\[
\boxed{
\mathfrak K_q(\xi,\bar\eta)
=
\frac{q-1}{4\pi}
G_{\mathrm{WP}}(\xi,\bar\eta)
+O(1),
\qquad q\to\infty.
}
\tag{0.3}
\]

Equivalently,

\[
\boxed{
\frac{4\pi}{q-1}\,\mathfrak K_q
\longrightarrow
G_{\mathrm{WP}}.
}
\tag{0.4}
\]

The convergence is to be understood locally on a smooth family (or uniformly on compact subsets where the geometric bounds entering the Bergman/resolvent asymptotics are uniform). No uniform statement through Deligne--Mumford degeneration is claimed.

**Derived here from established formulas.** The constant \(1/(4\pi)\) is not fitted. It is the product of two independently fixed high-power factors:

\[
\boxed{
\underbrace{\frac12}_{\text{KS resolvent symbol}}
\times
\underbrace{\frac{m}{2\pi}}_{\text{Bergman state density}}
=
\frac{m}{4\pi}.
}
\tag{0.5}
\]

The note also proves a separate obstruction:

\[
\boxed{
\text{a classical Fisher metric of a moving-fiber point process is not transport-gauge invariant.}
}
\tag{0.6}
\]

Thus (0.4) is a theorem for the **canonical Kodaira--Spencer curvature response** \(\mathfrak K_q\), not yet a theorem identifying an arbitrarily trivialized classical DPP Fisher metric with Weil--Petersson geometry.

This splits the old FCIG question into one solved geometric statement and one sharply formulated statistical transport problem.

---

# Part I. The curvature-side object

## 1. Hyperbolic family and notation

Let \(X_b=\pi^{-1}(b)\) be a compact genus-\(g\ge2\) Riemann surface. Equip \(K_{X_b}\) with the Hermitian metric induced by the hyperbolic Kähler--Einstein form \(\omega_b\).

We use the adjoint high-power convention of Wan--Zhang:

\[
L=K_{\mathcal X/B},
\qquad
m=q-1,
\qquad
E^m=\pi_*(L^m\otimes K_{\mathcal X/B})=E_q.
\]

This index shift is essential. The state space in the earlier hyperbolic note was \(H^0(K^q)\), while Berndtsson/Wan--Zhang naturally write \(H^0(K\otimes L^m)\).

For \(\xi\in T_bB\), the horizontal lift determined by the Hermitian weight has a vertical \(\bar\partial\)-derivative

\[
\mu_\xi\in A^{0,1}(X_b,T^{1,0}X_b)
\]

representing the Kodaira--Spencer class. In the Teichmüller/hyperbolic gauge we take its harmonic representative. The Weil--Petersson metric is the \(L^2\) pairing of these harmonic representatives [Wol86; Sch12].

---

## 2. Berndtsson's exact split

**Established.** For a relatively positive Hermitian line bundle \(L\), Berndtsson proves positivity of the \(L^2\) direct image

\[
\pi_*(K_{\mathcal X/B}\otimes L),
\]

and the curvature formula used by Wan--Zhang separates a weight/geodesic-curvature term from a Kodaira--Spencer resolvent term [Bern09; WZ21]. For \(E^m\),

\[
\boxed{
\begin{aligned}
\langle i\Theta^{E^m}u,u\rangle(\xi,\bar\eta)
&=
\int_{X_b}
m\,c(\phi)(\xi,\bar\eta)
|u|^2e^{-m\phi}
\\
&\quad+
m\left\langle
(m+\Delta')^{-1}i_{\mu_\xi}u,
 i_{\mu_\eta}u
\right\rangle .
\end{aligned}
}
\tag{2.1}
\]

Here \(\Delta'\) is the relevant \((1,0)\)-Laplacian on the contracted form and \(c(\phi)\) is the geodesic curvature of the Hermitian weight.

The decomposition has a useful conceptual meaning:

\[
\boxed{
\text{direct-image curvature}
=
\text{horizontal metric response}
+
\text{complex-structure excitation response}.
}
\tag{2.2}
\]

The second term is positive because \(m+\Delta'\) is positive.

---

## 3. Definition and intrinsicness of the KS information tensor

### Definition 3.1

For \(q=m+1\), define \(\mathfrak K_q\) by (0.1).

### Proposition 3.2

\(\mathfrak K_q\) is independent of the choice of orthonormal basis of \(H^0(X_b,K_{X_b}^q)\), Hermitian in \((\xi,\eta)\), and positive semidefinite.

### Proof

Let \(T_{\xi\bar\eta}\) be the quadratic-form operator on \(E_q|_b\) whose matrix element is

\[
\langle T_{\xi\bar\eta}u,v\rangle
=
m\left\langle
(m+\Delta')^{-1}i_{\mu_\xi}u,
 i_{\mu_\eta}v
\right\rangle.
\]

Then

\[
\mathfrak K_q(\xi,\bar\eta)=\operatorname{Tr}_{E_q}T_{\xi\bar\eta},
\]

so basis independence is immediate. Hermitian symmetry follows from self-adjointness of \((m+\Delta')^{-1}\). For \(\eta=\xi\),

\[
\mathfrak K_q(\xi,\bar\xi)
=
m\sum_a
\left\|(m+\Delta')^{-1/2}i_{\mu_\xi}u_a\right\|^2
\ge0.
\]

\(\square\)

**Derived here.** This is elementary operator bookkeeping applied to the established Berndtsson summand.

---

# Part II. The coefficient \(1/(4\pi)\)

## 4. Why the resolvent contributes one half

A central step in Wan--Zhang's high-power analysis is the expansion

\[
\boxed{
(m+\Delta')^{-1}
=
\frac{1}{2m}
+
O(m^{-2})
}
\tag{4.1}
\]

on the Kodaira--Spencer contraction sector, with the lower-order terms written explicitly in their Lemma 3.1 [WZ21]. More precisely, their expansion begins with \(1/(2m)\) and contains operators involving \(m-\Delta'\) and the curvature action \(R^*\).

Substituting the leading symbol in (2.1),

\[
\begin{aligned}
m\left\langle
(m+\Delta')^{-1}i_\mu u,i_\mu u
\right\rangle
&=
\frac12\|i_\mu u\|^2+O(m^{-1})
\\
&=
\frac12\int_{X_b}|\mu|^2|u|^2e^{-m\phi}+O(m^{-1}).
\end{aligned}
\tag{4.2}
\]

The important point is the factor \(1/2\), not \(1\).

**FCIG slogan.**

\[
\boxed{
\text{KS excitation sits at spectral energy }\Delta'\sim m;
\quad
(m+\Delta')^{-1}\sim(2m)^{-1}.
}
\tag{4.3}
\]

This is the spectral origin of the normalization in the final Weil--Petersson limit.

---

## 5. Trace and Bergman density

Let \(u_1,\dots,u_{N_q}\) be an \(L^2\)-orthonormal basis of \(H^0(K^q)\), and let

\[
B_q(x)=\sum_a|u_a(x)|^2
\]

be the corresponding diagonal Bergman density in the hyperbolic normalization.

For \(q=m+1\), the one-dimensional Bergman expansion used by Wan--Zhang reads

\[
\boxed{
B_q(x)
=
\frac{1}{2\pi}
\left(m-\frac{\rho}{2}\right)
+O(m^{-1}),
}
\tag{5.1}
\]

where \(\rho\) is the scalar curvature in their convention. For the hyperbolic metric, \(\rho=-1\), so

\[
\boxed{
B_q(x)
=
\frac{m}{2\pi}
+
\frac{1}{4\pi}
+O(m^{-1}).
}
\tag{5.2}
\]

This agrees with the exact local factor already obtained in [`hyperbolic-model.md`](hyperbolic-model.md):

\[
\frac{2q-1}{4\pi}
=
\frac{m}{2\pi}+\frac{1}{4\pi}.
\tag{5.3}
\]

On a fixed thick compact family the exact geodesic-loop correction is exponentially small in \(q\); it does not alter the coefficient of \(m\).

---

## 6. Theorem: normalized KS response converges to Weil--Petersson

### Theorem 6.1 — KS--WP leading law

For a smooth family of compact hyperbolic Riemann surfaces and \(q=m+1\to\infty\),

\[
\boxed{
\mathfrak K_q(\xi,\bar\eta)
=
\frac{m}{4\pi}
G_{\mathrm{WP}}(\xi,\bar\eta)
+O(1).
}
\tag{6.1}
\]

Equivalently,

\[
\boxed{
\lim_{q\to\infty}
\frac{4\pi}{q-1}\,
\mathfrak K_q(\xi,\bar\eta)
=
G_{\mathrm{WP}}(\xi,\bar\eta).
}
\tag{6.2}
\]

### Proof

Wan--Zhang's expansion of the second Berndtsson summand gives, after tracing over an orthonormal basis,

\[
\mathfrak K_q(\xi,\bar\eta)
=
\frac12
\int_{X_b}
\langle\mu_\xi,\mu_\eta\rangle
B_q\,\omega_b
+O(1).
\tag{6.3}
\]

The next resolvent coefficient is order \(m^{-1}\); after tracing against a Bergman density of order \(m\) in complex dimension one, it contributes only \(O(1)\). Insert (5.2):

\[
\begin{aligned}
\mathfrak K_q(\xi,\bar\eta)
&=
\frac12
\int_{X_b}
\langle\mu_\xi,\mu_\eta\rangle
\left(
\frac{m}{2\pi}+O(1)
\right)\omega_b
+O(1)
\\
&=
\frac{m}{4\pi}
\int_{X_b}
\langle\mu_\xi,\mu_\eta\rangle\omega_b
+O(1)
\\
&=
\frac{m}{4\pi}G_{\mathrm{WP}}(\xi,\bar\eta)+O(1).
\end{aligned}
\]

The off-diagonal Hermitian statement follows by polarization from the diagonal expansion if desired. \(\square\)

**Status.** **Derived here from [WZ21] plus the standard Weil--Petersson \(L^2\) identification.** The derivation fixes the coefficient; it is not a claim that Theorem 6.1 is absent from the literature in an equivalent formulation.

---

## 7. Chern-normalized version

Wan--Zhang use

\[
-i\,c_1(E^m,\|\cdot\|_m)
=
\frac{1}{2\pi}\operatorname{Tr}\Theta^{E^m}.
\]

Therefore the Chern-normalized KS contribution is

\[
\boxed{
\widehat{\mathfrak K}_q
:=
\frac{1}{2\pi}\mathfrak K_q
=
\frac{q-1}{8\pi^2}G_{\mathrm{WP}}+O(1).
}
\tag{7.1}
\]

This formula is intentionally kept in the Wan--Zhang Hermitian-pairing convention. The older FCIG hyperbolic note quotes the Zograf--Takhtajan first-Chern-form formula using its own \(\omega_{\mathrm{WP}}\) convention. Factors of \(i\), \(2\), and \(2\pi\) vary across the literature.

### Normalization firewall

Until an explicit convention crosswalk is written, do **not** compare the numerical coefficient in (7.1) directly with

\[
c_1(\lambda_q,h_Q)
=
\frac{6q^2-6q+1}{12\pi^2}\omega_{\mathrm{WP}}
\]

from the older note merely by matching the symbol \(\omega_{\mathrm{WP}}\).

The invariant content of Theorem 6.1 is the ratio with the explicitly defined Hermitian pairing (0.2).

---

# Part III. Quillen placement

## 8. Analytic torsion does not alter the \(m\)-order KS coefficient

Wan--Zhang compare the \(L^2\) direct-image curvature with the Quillen curvature and prove

\[
\boxed{
\partial\bar\partial\log\tau_m(\bar\partial)^2
=o(m^{n-1}).
}
\tag{8.1}
\]

For curves \(n=1\),

\[
\boxed{
\partial\bar\partial\log\tau_m(\bar\partial)^2=o(1).
}
\tag{8.2}
\]

They further note that for Teichmüller space of compact genus-\(g\ge2\) surfaces with \(L=K_{\mathcal X/B}\), the analytic torsion decay is exponentially small in \(m\) [WZ21, Remark 1.5].

Thus the \(O(m)\) coefficient in the KS direct-image response survives the \(L^2\)-to-Quillen comparison. This does **not** mean that the isolated KS summand is itself a separate Quillen curvature; Quillen curvature packages the total determinant response.

The safe statement is

\[
\boxed{
\text{KS resolvent coefficient at order }m
\text{ is not generated by an }O(m)\text{ torsion correction.}
}
\tag{8.3}
\]

---

# Part IV. Why this is not yet classical Fisher geometry

## 9. Moving sample spaces require a transport

For a fixed probability space, Fisher information is intrinsic under parameter-independent changes of sample coordinates. A family of fibers is different: the sample space itself moves.

For the \(q\)-particle Bergman process, locally consider the regular configuration space

\[
Y_b^\circ
=
\left(X_b^{N_q}\setminus\text{collision/zero locus}\right)/S_{N_q}.
\]

To differentiate a density \(P_b\) with respect to \(b\), one must identify nearby \(Y_b^\circ\) with a fixed \(Y_{b_0}^\circ\). Choose a smooth local transport

\[
\tau_b:Y_{b_0}^\circ\to Y_b^\circ,
\qquad
\tau_{b_0}=\mathrm{id},
\]

and pull the probability measures back to \(Y_{b_0}^\circ\).

The corresponding classical score is denoted

\[
S_\xi^\tau
=
D_\xi\log p_b^\tau\big|_{b=b_0}.
\]

---

## 10. Theorem: transport-gauge transformation of the score

### Theorem 10.1 — transport-gauge no-go

Let \(P_b\) be a smooth family of probability densities on moving sample spaces, and let \(\tau\) and \(\tau'\) be two local transports. Suppose

\[
\tau'_b=\tau_b\circ F_b,
\qquad
F_{b_0}=\mathrm{id},
\]

where the infinitesimal generator in direction \(\xi\) is \(V_\xi\). With the pullback convention above,

\[
\boxed{
S_\xi^{\tau'}
=
S_\xi^{\tau}
+
\operatorname{div}_{P_0}V_\xi,
}
\tag{10.1}
\]

where \(\operatorname{div}_{P_0}V\) is defined by

\[
\mathcal L_VP_0
=
(\operatorname{div}_{P_0}V)P_0.
\]

Consequently,

\[
\boxed{
\begin{aligned}
I^{\tau'}(\xi,\bar\eta)-I^\tau(\xi,\bar\eta)
&=
\mathbb E[S_\xi^\tau\,\overline{\delta_\eta}]
+
\mathbb E[\delta_\xi\,\overline{S_\eta^\tau}]
+
\mathbb E[\delta_\xi\,\overline{\delta_\eta}],
\\
\delta_\xi&:=\operatorname{div}_{P_0}V_\xi.
\end{aligned}
}
\tag{10.2}
\]

Thus the Fisher tensor is not invariant under arbitrary parameter-dependent changes of transport.

### Proof

By definition,

\[
P_b^{\tau'}
=(\tau'_b)^*P_b
=F_b^*(\tau_b^*P_b).
\]

Differentiate at \(b_0\):

\[
D_\xi P_b^{\tau'}
=
D_\xi P_b^\tau+\mathcal L_{V_\xi}P_0.
\]

Divide by \(P_0\) to obtain (10.1). Since both scores and probability divergences have zero mean under the usual compact/support assumptions, the Fisher pairing is their \(L^2(P_0)\) pairing. Expanding

\[
(S_\xi^\tau+\delta_\xi)
(\overline{S_\eta^\tau+\delta_\eta})
\]

gives (10.2). \(\square\)

**No-go.** A marking of a Teichmüller family fixes the topological identification up to isotopy, but it does not by itself make every parameter-dependent representative of that identification statistically equivalent. A literal moving-fiber classical Fisher metric is therefore not a canonical moduli tensor until a transport rule is fixed.

This is the obstruction that the earlier Fisher--Bergman--Quillen note left implicit.

**FCIG slogan.**

\[
\boxed{
\text{changing the fiber identification}
\Longrightarrow
\text{score }+\text{ probability divergence}.
}
\tag{10.3}
\]

---

## 11. What the theorem does and does not close

Theorem 6.1 closes a canonical geometric channel:

\[
\boxed{
\text{Kodaira--Spencer deformation}
\to
\text{Berndtsson resolvent response}
\to
\text{Weil--Petersson metric}
}
\]

with an explicit high-power coefficient.

Theorem 10.1 simultaneously blocks the over-strong statement

\[
\text{arbitrary classical moving-fiber Fisher}
=
C\,\omega_{\mathrm{WP}}.
\]

The remaining question is narrower and better posed:

> **Open statistical-transport problem.** Is there a geometrically preferred transport -- for example the real flow induced by the Kähler--Einstein/Chern horizontal lift -- for which the Bergman-DPP classical Fisher tensor has a controlled asymptotic relation to \(\mathfrak K_q\), and hence to \(G_{\mathrm{WP}}\)?

Hino--Yano show independently that finite DPPs are curved exponential families and that Hessian/Fisher identities hold only in special partially flat directions [HY24]. That result is not used as a proof here, but it supports the decision not to assume global exponential-family flatness for the moving Bergman DPP.

---

# Part V. Refined Information Closure

## 12. Replacement for the old conjectural triangle

The previous schematic decomposition

\[
\mathcal I_q
\stackrel{?}{=}
\mathcal R_q^Q
+\mathfrak D_q^{\mathrm{met}}
+\mathfrak D_q^{KS}
+\mathfrak D_q^{\mathrm{tors}}
\]

mixed a transport-dependent classical statistical tensor with intrinsic bundle curvature data.

The corrected architecture is

\[
\boxed{
\begin{array}{ccc}
\text{classical DPP Fisher}^{\tau}
&\xrightarrow{\text{transport choice}}&
\text{statistical response}
\\[2mm]
&&\downarrow\text{comparison open}
\\[2mm]
\text{Kodaira--Spencer class}
&\xrightarrow{\text{Berndtsson}}&
\mathfrak K_q
\\[2mm]
&&\downarrow\frac{4\pi}{q-1}
\\[2mm]
&&G_{\mathrm{WP}}.
\end{array}
}
\tag{12.1}
\]

The right-hand lower chain is now controlled. The top-to-bottom statistical comparison remains open.

### Information Closure v2

A publication-level closure should therefore prove one of the following stronger statements:

1. **Canonical transport closure:** exhibit a natural transport \(\tau^{\mathrm{can}}\) and prove
   \[
   \frac{4\pi}{q-1}I_q^{\tau^{\mathrm{can}}}
   \to
   G_{\mathrm{WP}}
   \]
   or compute its explicit defect from \(G_{\mathrm{WP}}\); or
2. **Gauge-quotient closure:** construct a transport-invariant statistical tensor by quotienting/minimizing over the probability-divergence gauge and prove that its high-power limit is \(G_{\mathrm{WP}}\); or
3. **Hilbert/quantum closure:** replace position-measurement Fisher data by an intrinsic Grassmannian/Hilbert-space information metric and compare that object with \(\mathfrak K_q\).

None of these three is claimed here.

---

## 13. Quantitative status table

| Channel | Object | Status | Leading genus-\(g\ge2\) result |
| --- | --- | --- | --- |
| local state density | \(B_q\) | established | \(B_q=(q-1)/(2\pi)+1/(4\pi)+\cdots\) |
| KS direct-image response | \(\mathfrak K_q\) | **derived here from established expansion** | \(\mathfrak K_q=(q-1)G_{WP}/(4\pi)+O(1)\) |
| Chern-normalized KS response | \(\widehat{\mathfrak K}_q\) | derived here | \((q-1)G_{WP}/(8\pi^2)+O(1)\) |
| total \(L^2\) direct-image curvature | \(c_1(E^m,h_{L^2})\) | established | Wan--Zhang expansion |
| total Quillen curvature | \(c_1(\lambda,h_Q)\) | established | same high-power orders up to torsion remainder |
| torsion curvature, curves | \(\partial\bar\partial\log\tau_m^2\) | established | \(o(1)\); exponential in the compact Teichmüller canonical case cited by WZ |
| moving-fiber classical Fisher | \(I_q^\tau\) | transport-dependent | no canonical coefficient without \(\tau\) |
| transport change | \(S^{\tau'}-S^\tau\) | **derived here / no-go** | \(\operatorname{div}_{P}V\) |

---

# 14. Next proof target

The next calculation is no longer “find the Kodaira--Spencer coefficient.” That coefficient is fixed by Theorem 6.1.

The next target is:

\[
\boxed{
\text{Choose the KE/Chern horizontal transport and compute }
I_q^{\tau^{\mathrm{KE}}}-\mathfrak K_q
\text{ to leading order.}
}
\tag{14.1}
\]

A pass would determine whether the transport divergence precisely supplies the difference between classical DPP Fisher response and the intrinsic Berndtsson/Weil--Petersson response.

A failure would still be a precise theorem: it would identify the obstruction tensor rather than hiding it in the word “information.”

---

# 15. Reference map

- **Direct-image positivity and curvature:** [Bern09].
- **High-power curvature, resolvent expansion, Bergman expansion, torsion comparison:** [WZ21].
- **Weil--Petersson/Kodaira--Spencer geometry:** [Wol86; Sch12].
- **Quillen/Weil--Petersson benchmark:** [ZT87].
- **DPP information geometry / curved exponential-family caution:** [HY24].

No cited source is claimed to prove Theorem 10.1 in the exact FCIG transport notation; it is the elementary Lie-derivative calculation written above. Theorem 6.1 is explicitly labeled a deduction from [WZ21], not a literature-novelty claim.
