# FCIG: Toeplitz Orbital Insertion for the Weighted Discrete-Series Trace

**Status:** exact operator-typing observation + conjectural cyclic trace closure  
**Date:** 2026-09-10  
**Depends on:** [`bls-position-transport.md`](bls-position-transport.md), [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md), [`orbital-character-closure.md`](orbital-character-closure.md).

> **Claim firewall.** The compact Bergman trace identity below is elementary operator theory. Its promotion to a trace on the full noncompact discrete-series realization is **not** automatic: trace-class, centralizer-volume and regularization issues must be handled on the cyclic quotient/orbital side.

---

## 0. Main observation

Let \(P_q\) be the Bergman projection onto the holomorphic \(q\)-differential Hilbert space and let \(M_W\) be multiplication by a geometric weight \(W\). The canonical quantization of \(W\) already present in the BLS/Bergman formalism is the Toeplitz operator

\[
\boxed{
T_W^{(q)}:=P_qM_WP_q.
}
\tag{0.1}
\]

For the FCIG deformation weight

\[
\boxed{
W_q
=|\mu|^2+2(q-1)(1+\square_0)^{-1}|\mu|^2,
}
\tag{0.2}
\]

the first candidate for the unknown Orbital--Character Closure insertion is therefore

\[
\boxed{
\mathcal A_\mu^{(q)}=T_{W_q}^{(q)}.
}
\tag{0.3}
\]

More economically, after the Casimir-transmutation step one may use

\[
T_{f_\mu}^{(q)},
\qquad
f_\mu=(1+\square_0)^{-1}|\mu|^2,
\tag{0.4}
\]

and let the differential operator \(\mathscr D_{q,L}\) act on the conjugacy-length parameter.

The slogan is

\[
\boxed{
\text{deformation weight on the surface}
\xrightarrow{\;PMP\;}
\text{operator insertion in the discrete-series trace}.
}
\tag{0.5}
\]

---

# Part I. Why Toeplitz insertion is forced by the Bergman side

## 1. Weighted diagonal Bergman trace

On a compact surface, if \(K_q(x,y)\) is the Bergman kernel and \(B_q(x)=K_q(x,x)\) its diagonal density in the fixed convention, then

\[
\boxed{
\operatorname{Tr}(T_W^{(q)})
=
\int_X W(x)B_q(x)\,dA(x).
}
\tag{1.1}
\]

Indeed \(P_q^2=P_q\), so cyclicity of the finite-dimensional trace gives

\[
\operatorname{Tr}(P_qM_WP_q)
=
\operatorname{Tr}(M_WP_q),
\]

and the diagonal kernel of \(M_WP_q\) is \(W(x)K_q(x,x)\).

Thus whenever the Fisher/Kodaira--Spencer curvature produces a weighted Bergman density, its operator-theoretic meaning is already Toeplitz.

No representation-theory guess is needed for this statement.

## 2. Insert a deck/group action

Let \(U_g^{(q)}\) denote the unitary action of a hyperbolic group element \(g\) on the holomorphic \(q\)-differential Hilbert space. Whenever the product is trace class (automatically on the compact finite-dimensional quotient),

\[
\boxed{
\operatorname{Tr}\!\left(T_W^{(q)}U_g^{(q)}\right)
=
\operatorname{Tr}\!\left(M_WP_qU_g^{(q)}P_q\right).
}
\tag{1.2}
\]

The right-hand side is the integral of the diagonal of the **transported Bergman kernel**, multiplied by \(W\). In local coordinates it has the schematic form

\[
\boxed{
\operatorname{Tr}\!\left(T_W^{(q)}U_g^{(q)}\right)
=
\int W(x)\,\mathcal K_q(g;x,x)\,dA(x),
}
\tag{1.3}
\]

where \(\mathcal K_q(g;x,x)\) includes the automorphy/Chern phase dictated by the chosen realization.

Equation (1.3) is the exact **type** of the Sun/FCIG weighted loop term.

The convention-dependent task is to prove that \(\mathcal K_q(g;x,x)\) is exactly the oriented kernel used in `systolic-bergman-orbital.md`, including all bundle factors.

---

# Part II. Cyclic quotient and the trace-class firewall

## 3. Why the full representation trace is dangerous

The holomorphic discrete series \(D_{2q-1}^{+}\) is infinite-dimensional. On its noncompact model, neither

\[
T_{W_q}^{(q)}
\quad\text{nor}\quad
T_{W_q}^{(q)}\pi_q(a_{L/2})
\]

is automatically trace class for an arbitrary lifted periodic weight.

Therefore the notation

\[
\operatorname{Tr}_{D_{2q-1}^{+}}
\left(T_{W_q}^{(q)}\pi_q(a_{L/2})\right)
\]

must be regarded as **provisional** until one chooses the correct relative/orbital trace functional.

The geometric calculation already tells us what that functional should reduce to: unfold by the centralizer of the primitive class and integrate one fundamental cylinder.

Thus the safer target is

\[
\boxed{
\operatorname{Tr}^{\rm orb}_{c,m}
\left(T_{W_q}^{(q)}\pi_q(a_{m\ell_c/2})\right)
:=
\text{centralizer-normalized cyclic-cylinder diagonal integral}.
}
\tag{2.1}
\]

This is a definition template, not yet an invariant construction.

## 4. Expected geometric reduction

With the conventions of the existing Sun--Selberg unfolding note, the desired identity is

\[
\boxed{
\operatorname{Tr}^{\rm orb}_{c,m}
\left(T_{W_q}^{(q)}\pi_q(a_{m\ell_c/2})\right)
\stackrel{?}{=}
\mathcal N_{c,m,q}\,
\mathcal J_{q,m\ell_c}[W_q],
}
\tag{2.2}
\]

where \(\mathcal N_{c,m,q}\) denotes the already-audited orientation/centralizer/prefactor normalization from the Sun unfolding.

No value for \(\mathcal N_{c,m,q}\) is asserted here; it must be imported from the exact unfolding convention rather than guessed.

Combining with Casimir transmutation gives

\[
\boxed{
\operatorname{Tr}^{\rm orb}_{c,m}
\left(T_{W_q}^{(q)}\pi_q(a_{m\ell_c/2})\right)
\stackrel{?}{=}
\mathcal N_{c,m,q}\,
\mathscr D_{q,L}
\mathcal J_{q,L}[f_\mu]
\big|_{L=m\ell_c}.
}
\tag{2.3}
\]

Equation (2.3) is a much more concrete OCC target than an unspecified inserted character.

---

# Part III. Relation to the cyclic Fourier modes

## 5. Toeplitz insertion sees the same mode data

The cylinder decomposition gives

\[
\overline f_\mu(u)
=
\sum_{n\in\mathbb Z}|b_{n,c}|^2F_{n,c}(u).
\tag{3.1}
\]

Therefore

\[
\mathcal J_{q,m\ell_c}[f_\mu]
=
\sum_n|b_{n,c}|^2\Lambda_{n,c}^{(q,m)}.
\tag{3.2}
\]

If (2.3) holds, the matrix of the Toeplitz insertion in the basis naturally adapted to the cyclic subgroup must have diagonal trace data satisfying

\[
\boxed{
\sum_n
\langle e_n,T_{f_\mu}^{(q)}\pi_q(a_{m\ell_c/2})e_n\rangle
\sim
\sum_n|b_{n,c}|^2\Lambda_{n,c}^{(q,m)},
}
\tag{3.3}
\]

where the left side is interpreted through the orbital/relative trace rather than an unjustified absolute trace.

This exposes the next calculation: compute the Toeplitz matrix elements in a standard disk/upper-half-plane realization of \(D_{2q-1}^{+}\) and compare them with the explicit \(F_{n,c}\) multipliers.

---

# Part IV. Why this improves the character conjecture

## 6. Ordinary character is recovered by the identity insertion

Formally, setting \(T_W=I\) in an inserted trace recovers the ordinary character:

\[
\operatorname{Tr}(I\,\pi_q(g))=\Theta_q(g).
\]

The Sun/FCIG unweighted orbital nevertheless vanishes after transverse orbital integration because that operation is not the same functional as evaluation of the character on \(g\). This remains consistent with the previous normalization firewall.

The weighted response replaces the identity insertion by a Toeplitz observable carrying \(\mu\).

Thus the Selberg denominator and the information response are related without being identified:

\[
\boxed{
\begin{array}{rcl}
\Theta_q(g)&:&\text{trace of group transport},\\
T_{W_q}&:&\text{quantized deformation observable},\\
\operatorname{Tr}^{\rm orb}(T_{W_q}\pi_q(g))&:&\text{candidate FCIG class response}.
\end{array}
}
\tag{4.1}
\]

## 7. Information-geometric meaning

This candidate is especially natural because the BLS track already interprets multiplication by a position observable and its Bergman compression as the ambient/compressed measurement pair. The same compression now appears in the nonperturbative orbital sector.

So the emerging operator slogan is

\[
\boxed{
\text{Born/Fisher observable}
\quad\text{and}\quad
\text{Selberg/Bergman orbital insertion}
\quad\text{are two uses of the same Toeplitz quantization map }W\mapsto P_qM_WP_q.
}
\tag{4.2}
\]

This is an FCIG structural synthesis. It does not imply equality of the corresponding global observables.

---

# Part V. New gates

## TOI-A — transported Bergman kernel crosswalk

**OPEN, exact target.** In a fixed \(D_{2q-1}^{+}\) realization, compute the diagonal kernel of

\[
P_q\pi_q(a_{L/2})P_q
\]

and prove that it reproduces the oriented Sun cylinder kernel

\[
\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}
\]

with the exact automorphy/Chern phase and measure convention.

## TOI-B — relative/orbital trace construction

**OPEN.** Define \(\operatorname{Tr}^{\rm orb}_{c,m}\) invariantly and prove that its centralizer normalization agrees with `sun-selberg-unfolding.md`.

## TOI-C — resolvent Toeplitz matrix elements

**OPEN / computational.** Compute the matrix elements of

\[
T_{f_\mu}^{(q)}=P_qM_{(1+\square_0)^{-1}|\mu|^2}P_q
\]

in the cyclic-mode basis and identify the exact relation to \(\Lambda_{n,c}^{(q,m)}\).

## TOI-D — descendant recurrence

**OPEN / falsifiable.** Test whether the resulting diagonal/orbital coefficients obey the \(\mathfrak{sl}_2\) raising/lowering recurrence required to produce the discrete-series descendant factor

\[
\frac{1}{1-e^{-L}}.
\]

---

## 8. Current best theorem target

The representation-theoretic frontier can now be stated without a free placeholder operator:

\[
\boxed{
\textbf{Toeplitz Orbital Closure:}\qquad
\mathcal J_{q,L}[W_q]
\text{ is the cyclic/orbital trace of }
P_qM_{W_q}P_q\,\pi_q(a_{L/2}),
}
\]

with all bundle phases, Haar measures, centralizer factors and trace regularizations explicitly fixed.

If true, the remaining finite-\(q\) FCIG information term is not merely “character-like.” It is a **deformation-inserted discrete-series orbital trace**.

That is now the sharpest nonperturbative target.
