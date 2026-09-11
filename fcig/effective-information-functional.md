# Typed Effective Information Functional

## OIG-B1 — state, determinant, Quillen, and orbital channels without type collapse

**Status (2026-09-11).**

This note formulates the strongest variational object currently justified by FCIG without identifying inequivalent notions of entropy or double-counting the Selberg/Quillen sector.

The result has two levels:

1. an **exact typed potential vector** with exact first-variation formulas;
2. a **coefficient-weighted effective functional ansatz**, explicitly marked as an additional constitutive choice rather than a theorem forced by determinant/anomaly geometry.

We record

\[
\boxed{\textbf{OIG-B1a: PASS — exact typed potential vector and first variations.}}
\]

\[
\boxed{\textbf{OIG-B1b: PASS AS ANSATZ — well-typed effective functional family.}}
\]

No Lorentzian gravitational equation is claimed.

---

## 1. State sector

Let
\[
\mathcal M_q\simeq H^0(X,K_X^q),
\qquad
\varrho_q(x)=|\mathrm{ev}_x\rangle\langle\mathrm{ev}_x|,
\]
and for a nonnegative symbol \(W\) define
\[
T_W:=\int_XW(x)\varrho_q(x)dA(x).
\tag{1.1}
\]
Set
\[
Z_W:=\operatorname{Tr}T_W
=\int_XW(x)B_q(x,x)dA(x).
\tag{1.2}
\]
Whenever \(Z_W>0\), define
\[
\rho_W:=\frac{T_W}{Z_W}.
\tag{1.3}
\]

The exact state-sector potentials are
\[
\boxed{\Phi_{\rm mass}(W):=\log Z_W,}
\tag{1.4}
\]
\[
\boxed{S_{\rm mix}(W):=-\operatorname{Tr}(\rho_W\log\rho_W),}
\tag{1.5}
\]
and, for \(\varepsilon>0\),
\[
\boxed{\Phi_{\rm det,\varepsilon}(W):=\log\det(T_W+\varepsilon I).}
\tag{1.6}
\]
These have different meanings and are not identified.

---

## 2. Exact symbol variations

Because the Toeplitz map is linear,
\[
\boxed{\delta T_W=T_{\delta W}=\int_X\delta W(x)\varrho_q(x)dA(x).}
\tag{2.1}
\]
Hence
\[
\boxed{\delta Z_W=\operatorname{Tr}T_{\delta W}.}
\tag{2.2}
\]
Therefore
\[
\boxed{\delta\Phi_{\rm mass}
=\frac{\operatorname{Tr}T_{\delta W}}{Z_W}.}
\tag{2.3}
\]

For the normalized state,
\[
\delta\rho_W
=\frac{T_{\delta W}}{Z_W}
-\rho_W\frac{\operatorname{Tr}T_{\delta W}}{Z_W}.
\tag{2.4}
\]
Using \(\operatorname{Tr}\delta\rho_W=0\),
\[
\delta S_{\rm mix}
=-\operatorname{Tr}(\delta\rho_W\log\rho_W),
\]
so
\[
\boxed{
\delta S_{\rm mix}
=-\frac1{Z_W}
\operatorname{Tr}\left[
T_{\delta W}\left(\log\rho_W+S_{\rm mix}I\right)
\right].
}
\tag{2.5}
\]

For the regularized determinant,
\[
\boxed{
\delta\Phi_{\rm det,\varepsilon}
=\operatorname{Tr}\left[(T_W+\varepsilon I)^{-1}T_{\delta W}\right].
}
\tag{2.6}
\]

These are exact finite-dimensional matrix identities.

---

## 3. Pointwise functional gradients

Using \(T_{\delta W}=\int\delta W(x)\varrho_q(x)dA(x)\), the three gradients are
\[
\boxed{
\frac{\delta\Phi_{\rm mass}}{\delta W(x)}
=\frac{B_q(x,x)}{Z_W}.
}
\tag{3.1}
\]

\[
\boxed{
\frac{\delta S_{\rm mix}}{\delta W(x)}
=-\frac1{Z_W}
\operatorname{Tr}\left[
\varrho_q(x)(\log\rho_W+S_{\rm mix}I)
\right].
}
\tag{3.2}
\]

\[
\boxed{
\frac{\delta\Phi_{\rm det,\varepsilon}}{\delta W(x)}
=
\operatorname{Tr}\left[(T_W+\varepsilon I)^{-1}\varrho_q(x)\right].
}
\tag{3.3}
\]

Equation (3.2) is the precise operator-valued version of an entropy gradient in the compact FCIG state sector.

---

## 4. Quillen/moduli sector

Let \(b\in B\) parametrize a family of compact complex/hyperbolic structures and let \(\lambda_q=\det R\pi_*K^q\) carry its Quillen metric \(h_Q\). For a local nonzero determinant frame \(\Sigma\), define
\[
\boxed{\Phi_Q(b;\Sigma):=-\log h_Q(\Sigma,\Sigma).}
\tag{4.1}
\]
With the FCIG curvature convention
\[
F_Q=-\partial\bar\partial\log h_Q,
\]
we have
\[
\boxed{\partial\bar\partial\Phi_Q=F_Q.}
\tag{4.2}
\]
For the hyperbolic curve family,
\[
\frac{i}{2\pi}F_Q
=\frac{c_q}{12\pi^2}\omega_{\rm WP},
\qquad
c_q=6q^2-6q+1,
\tag{4.3}
\]
in the convention fixed in `quillen-refinement.md`.

The Quillen potential decomposes as
\[
\Phi_Q
=-\log h_{L^2}-\mathcal T_q,
\tag{4.4}
\]
where \(\mathcal T_q\) is analytic torsion in that convention. Thus the spectral/closed-geodesic correction is already contained in the Quillen sector.

---

## 5. Orbital sector is a resolution, not an extra energy by default

The compact trace response has the classwise decomposition
\[
\operatorname{Tr}T_W
=\text{identity contribution}
+\sum_{[\delta]\ne[1]}\sum_{m\ge1}
C_q\ell_\delta\,\mathcal J_{q,m\ell_\delta}[W],
\tag{5.1}
\]
with the precise normalization inherited from the compact automorphic closure.

Meanwhile the torsion term in \(\Phi_Q\) is encoded by Selberg/spectral data. Therefore adding an arbitrary independent 'Selberg energy' to \(\Phi_Q\) risks double counting.

The safe object is the **orbital resolution map**
\[
\boxed{
\mathcal O_q(W)
:=\left\{C_q\ell_\delta\mathcal J_{q,m\ell_\delta}[W]\right\}_{[\delta],m}.
}
\tag{5.2}
\]
It resolves global topology by conjugacy sector but is not automatically an additional scalar potential.

If one wants a generating functional, introduce external sources \(\eta_{[\delta],m}\):
\[
\boxed{
\mathcal W_{\rm orb}[W;\eta]
:=\sum_{[\delta]\ne[1]}\sum_{m\ge1}
\eta_{[\delta],m}
C_q\ell_\delta\mathcal J_{q,m\ell_\delta}[W].
}
\tag{5.3}
\]
At \(\eta=0\), no new physical energy has been inserted; functional derivatives in \(\eta\) recover the orbit-resolved observables.

---

## 6. The typed potential vector

The mathematically controlled FCIG information datum is therefore
\[
\boxed{
\mathbf\Phi_{q,\varepsilon}[W,b]
=
\left(
\Phi_{\rm mass},
S_{\rm mix},
\Phi_{\rm det,\varepsilon},
\Phi_Q,
\mathcal O_q
\right).
}
\tag{6.1}
\]
Each component has a distinct domain/codomain and a distinct variation theory.

We record
\[
\boxed{\textbf{OIG-B1a: PASS.}}
\]
The pass concerns the typed vector and the exact identities above; it does not assert that nature selects any particular scalar combination.

---

## 7. Effective functional ansatz

A scalar variational model requires additional constitutive coefficients. The minimal well-typed family is
\[
\boxed{
\Gamma_{q,\varepsilon}[W,b;\Sigma]
=
\alpha\,\Phi_{\rm mass}(W)
+\beta\,S_{\rm mix}(W)
+\gamma\,\Phi_{\rm det,\varepsilon}(W)
+\delta\,\Phi_Q(b;\Sigma)
+\mathcal R[W,b],
}
\tag{7.1}
\]
where \(\mathcal R\) denotes any separately specified invariant regularization/interaction functional.

The coefficients \(\alpha,\beta,\gamma,\delta\) are **not** fixed by the preceding geometry. Choosing them is extra physical/model data, exactly as required by the anomaly-to-dynamics no-go in `functional-response.md`.

If orbit-resolved responses are desired, use the source-extended generator
\[
\boxed{
\Gamma^{\rm src}
=\Gamma+\mathcal W_{\rm orb}[W;\eta].
}
\tag{7.2}
\]
This avoids silently counting the same Selberg information twice.

We therefore record
\[
\boxed{\textbf{OIG-B1b: PASS AS ANSATZ.}}
\]

---

## 8. Exact W-gradient of the ansatz

At fixed background \(b\),
\[
\boxed{
\begin{aligned}
\frac{\delta\Gamma}{\delta W(x)}
={}&
\alpha\frac{B_q(x,x)}{Z_W}\\
&-\frac{\beta}{Z_W}
\operatorname{Tr}\left[
\varrho_q(x)(\log\rho_W+S_{\rm mix}I)
\right]\\
&+\gamma\operatorname{Tr}\left[
(T_W+\varepsilon I)^{-1}\varrho_q(x)
\right]\\
&+\frac{\delta\mathcal R}{\delta W(x)}.
\end{aligned}}
\tag{8.1}
\]

Thus a symbolic gradient flow
\[
\partial_\tau W
=-\mathcal G^{-1}\frac{\delta\Gamma}{\delta W}
\tag{8.2}
\]
can be defined once a metric/operator \(\mathcal G\) on symbol space is independently specified.

**Firewall:** equation (8.2) is a chosen gradient dynamics on symbol space, not a derivation of spacetime gravity.

---

## 9. Moduli response

At fixed \(W\), the moduli derivative receives separate contributions because \(T_W\), \(B_q\), and \(\varrho_q\) depend on complex/Kähler structure, while \(\Phi_Q\) carries determinant-line geometry.

The Quillen curvature gives the exact antisymmetrized second moduli response
\[
\boxed{
\partial\bar\partial\Phi_Q=F_Q
\propto\omega_{\rm WP}.
}
\tag{9.1}
\]
The state-sector moduli derivatives require the variation of the Bergman projector/coherent-state family and should not be replaced by (9.1). This is the same curvature-versus-first-response distinction enforced by `functional-response.md`.

---

## 10. Information-gradient slogan, corrected

The strongest mathematically justified FCIG slogan is not
\[
\text{gravity}=\nabla S.
\]
It is
\[
\boxed{
\text{chosen information dynamics}
=
-\operatorname{grad}_{\mathcal G}\Gamma,
}
\tag{10.1}
\]
where
\[
\Gamma
=\text{a separately chosen combination of typed state/determinant/Quillen potentials}.
\]

The geometry supplies the allowed potentials and their exact derivatives; a physical theory must still supply the coefficients, the metric on configuration space, and any Lorentzian/spacetime interpretation.

---

## 11. Gate ledger

\[
\boxed{\textbf{OIG-B1a: PASS — exact typed potentials and variations.}}
\]
\[
\boxed{\textbf{OIG-B1b: PASS AS ANSATZ — well-typed effective functional family.}}
\]
\[
\boxed{\textbf{OIG-B2: OPEN — choose/derive a canonical constitutive principle fixing coefficients and configuration-space metric.}}
\]
\[
\boxed{\textbf{OIG-B3: OPEN — derive state-decorated orbital response of the mixed operator }\rho_W\textbf{ beyond scalar trace data.}}
\]

## Claim firewall

- Mixed-state entropy, state counting, Bergman density, Toeplitz log determinant, and Quillen potential are distinct objects.
- Analytic torsion/Quillen data already contain spectral/closed-geodesic information; the orbital source functional is a resolution/generator, not an automatically independent energy term.
- The coefficients in (7.1) are constitutive parameters, not consequences of index theory.
- A gradient flow on symbol/moduli space is not a Lorentzian gravitational field equation.
- Determinant/anomaly curvature does not uniquely determine first functional response.
- No novelty claim is made without a dedicated literature audit.