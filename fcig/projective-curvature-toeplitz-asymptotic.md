# Projective Curvature Toeplitz Asymptotic

## OIG-C3b — leading matrix-valued curvature symbol

**Status (2026-09-11).**

Wan--Zhang's high-power direct-image curvature formula is strong enough to identify not only the trace asymptotics but the leading operator-valued Toeplitz symbol of the direct-image curvature. This closes the first matrix-valued step of OIG-C3.

We record
\[
\boxed{\textbf{OIG-C3b1: PASS — leading Toeplitz-symbol expansion of direct-image curvature.}}
\]
A complete all-orders projective-curvature expansion remains open:
\[
\boxed{\textbf{OIG-C3b2: OPEN.}}
\]

---

## 1. Setup and convention

Let
\[
E_q=\pi_*K_{\mathcal X/B}^{q},
\qquad k:=q-1,
\]
so that
\[
E_q=\pi_*(K_{\mathcal X/B}\otimes K_{\mathcal X/B}^{k}).
\]
Fix a base direction \(\xi\), with harmonic Kodaira--Spencer tensor \(\mu_\xi\), and let \(c_\xi\) denote the corresponding geodesic-curvature function in the direct-image curvature formula.

Write \(T_f^{(q)}\) for the Toeplitz operator on \(H^0(X,K_X^q)\) with scalar symbol \(f\).

---

## 2. Exact Berndtsson/Wan--Zhang quadratic form

In the positive Hermitian curvature convention, the direct-image curvature satisfies
\[
\langle i\Theta_q u,u\rangle(\xi,\bar\xi)
=
\int_X k c_\xi |u|^2
+
k\left\langle (k+\Delta')^{-1}i_{\mu_\xi}u,
i_{\mu_\xi}u\right\rangle.
\tag{2.1}
\]
Wan--Zhang expand the resolvent contribution and obtain, uniformly in unit vectors \(u\),
\[
\begin{aligned}
\left\langle (k+\Delta')^{-1}i_{\mu_\xi}u,i_{\mu_\xi}u\right\rangle
=
\int_X\Bigg[
&\frac{1}{2k}|\mu_\xi|^2\\
&+\frac1{k^2}\left(
-\frac16|\bar\nabla\mu_\xi|^2
+\frac14|\mu_\xi|^2_{R^*}
\right)
+o(k^{-2})
\Bigg]|u|^2.
\end{aligned}
\tag{2.2}
\]
Multiplying by \(k\) gives
\[
\boxed{
\begin{aligned}
\langle i\Theta_q u,u\rangle(\xi,\bar\xi)
=
\int_X\Bigg[
&k c_\xi
+\frac12|\mu_\xi|^2\\
&+\frac1k\left(
-\frac16|\bar\nabla\mu_\xi|^2
+\frac14|\mu_\xi|^2_{R^*}
\right)
+o(k^{-1})
\Bigg]|u|^2.
\end{aligned}
}
\tag{2.3}
\]

---

## 3. Operator-valued Toeplitz expansion

Since the right-hand side is a Toeplitz quadratic form and the remainder is uniform on the unit sphere, polarization yields the operator expansion
\[
\boxed{
\begin{aligned}
i\Theta_q(\xi,\bar\xi)
={}&
 kT_{c_\xi}^{(q)}
+\frac12T_{|\mu_\xi|^2}^{(q)}\\
&+\frac1kT_{\,-\frac16|\bar\nabla\mu_\xi|^2+\frac14|\mu_\xi|^2_{R^*}}^{(q)}
+o(k^{-1})
\end{aligned}
}
\tag{3.1}
\]
in operator norm, in the conventions/regularity regime of the high-power expansion.

Off-diagonal Hermitian base directions \((\xi,\bar\eta)\) follow by polarization.

Thus the direct-image curvature itself is asymptotically a Toeplitz operator-valued (1,1)-form on the base.

---

## 4. Traceless/projective channel

For any endomorphism \(A\) on \(E_q\), define
\[
A^\circ:=A-\frac{\operatorname{Tr}A}{d_q}I.
\]
Applying this to (3.1),
\[
\boxed{
\begin{aligned}
(i\Theta_q)^\circ(\xi,\bar\xi)
={}&
 k\left(T_{c_\xi}^{(q)}\right)^\circ
+\frac12\left(T_{|\mu_\xi|^2}^{(q)}\right)^\circ\\
&+\frac1k\left(
T_{\,-\frac16|\bar\nabla\mu_\xi|^2+\frac14|\mu_\xi|^2_{R^*}}^{(q)}
\right)^\circ
+o(k^{-1}).
\end{aligned}}
\tag{4.1}
\]
This is the leading projective/nonabelian curvature expansion sought in OIG-C3.

In particular, unless \(c_\xi\) is fiberwise constant, the projective curvature generically remains of order \(k\): determinant abelianization does not remove a negligible correction but a leading matrix-valued sector.

---

## 5. Trace channel versus projective channel

Taking the trace of (3.1) gives the determinant/L2 curvature asymptotics studied by Wan--Zhang and used in the FCIG Weil--Petersson notes. Taking the traceless part gives (4.1).

Therefore one and the same Toeplitz-symbol expansion splits as
\[
\boxed{
\text{direct-image curvature}
=
\text{scalar trace/WP channel}
+
\text{projective Toeplitz channel}.
}
\tag{5.1}
\]
The Quillen torsion correction modifies the determinant-line channel; it does not cancel the projective operator (4.1).

---

## 6. Consequence for density-state transport

For an FCIG density operator \(\rho_W\),
\[
(\nabla^{\rm End})^2\rho_W=[F_q^\circ,\rho_W].
\]
Using the leading projective symbol,
\[
\boxed{
(\nabla^{\rm End})^2\rho_W
\sim
k\,[T_{c_\xi}^{(q)},\rho_W]
+\frac12[T_{|\mu_\xi|^2}^{(q)},\rho_W]
+\cdots.
}
\tag{6.1}
\]
This is a curvature/holonomy identity, not a dynamical equation.

It shows explicitly how Kodaira--Spencer/geodesic-curvature data drive noncommutative transport in the automorphic information state.

---

## 7. Semiclassical symbol interpretation

Berezin--Toeplitz quantization implies, schematically for smooth symbols,
\[
[T_f,T_g]
=\frac{i}{q}T_{\{f,g\}}+O(q^{-2})
\]
under standard normalization conventions. Therefore if \(\rho_W\) itself admits a semiclassical Toeplitz symbol, the leading commutator in (6.1) is controlled by a Poisson bracket with the geodesic-curvature symbol.

This suggests the semiclassical projective transport slogan
\[
\boxed{
\text{nonabelian curvature transport}
\leadsto
\text{Hamiltonian transport generated by the curvature symbol}.
}
\tag{7.1}
\]
This last interpretation is conditional on the standard Toeplitz symbol calculus and the symbol class chosen for \(\rho_W\); it is not promoted here to an independent FCIG dynamics theorem.

---

## 8. Gate ledger

\[
\boxed{\textbf{OIG-C3b1: PASS — leading operator-valued curvature symbol.}}
\]
\[
\boxed{\textbf{OIG-C3b2: OPEN — full all-orders matrix-valued curvature expansion.}}
\]
\[
\boxed{\textbf{OIG-C3c: OPEN — identify state-decorated closed-orbit invariants of the projective curvature channel.}}
\]

## Claim firewall

- The expansion uses the Wan--Zhang high-power direct-image curvature/resolvent regime and its normalization.
- The `o(k^{-1})` statement is inherited from that regime; no uniform claim through moduli degeneration is made.
- Tracing the curvature and taking its traceless part are different operations with different information content.
- Equation (6.1) is curvature-induced holonomy of a density state, not a gravitational equation.
- The final Poisson-bracket statement is a standard semiclassical Toeplitz interpretation, not an exact identity at finite \(q\).
- No novelty claim is made without a dedicated prior-art audit.