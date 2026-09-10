# FCIG: Exact Disk Transport of the Bergman Kernel

**Status:** exact disk-model calculation; closes TOI-A up to the declared orientation convention  
**Date:** 2026-09-10  
**Depends on:** [`toeplitz-orbital-insertion.md`](toeplitz-orbital-insertion.md), [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md), [`sun-selberg-unfolding.md`](sun-selberg-unfolding.md).

> **Claim firewall.** The disk Bergman kernel and the canonical action of `SU(1,1)` are standard. The algebraic crosswalk below is derived explicitly in the stated convention. Orientation reversal complex-conjugates the final kernel. This note does **not** yet construct the invariant cyclic relative trace; that remains TOI-B.

---

## 0. Result

Put the curvature `-1` Poincare metric on the unit disk,

\[
 ds^2=\frac{4|dz|^2}{(1-|z|^2)^2},
 \qquad
 dA=\frac{4\,d^2z}{(1-|z|^2)^2}.
\]

For holomorphic `q`-differentials `f(z)(dz)^q`, the induced Hilbert norm is

\[
 \|f(dz)^q\|^2
 =2^{2-2q}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^{2q-2}d^2z.
\tag{0.1}
\]

Hence the coefficient Bergman kernel is

\[
 K_q(z,w)
 =\frac{(2q-1)2^{2q-2}}{\pi}(1-z\bar w)^{-2q}.
\tag{0.2}
\]

After passing to unitary fiber frames, its scalar coherent overlap is

\[
 \boxed{
 \mathcal C_q(z,w)
 =C_q
 \left[
 \frac{\sqrt{(1-|z|^2)(1-|w|^2)}}{1-z\bar w}
 \right]^{2q},
 \qquad
 C_q=\frac{2q-1}{4\pi}.
 }
\tag{0.3}
\]

Now let

\[
 g_L(z)=\frac{Cz+S}{Sz+C},
 \qquad
 C=\cosh\frac L2,
 \quad
 S=\sinh\frac L2.
\tag{0.4}
\]

This is the positive hyperbolic translation of length `L` along the real diameter. On the normal geodesic choose

\[
 z=ix,
 \qquad
 x=\tanh\frac r2,
 \qquad
 u=\sinh r=\frac{2x}{1-x^2}.
\tag{0.5}
\]

Define the unit-modulus automorphy phase

\[
 \rho_L(x)
 :=\frac{|C+iSx|}{C-iSx}.
\tag{0.6}
\]

Then the exact identity is

\[
 \boxed{
 \rho_L(x)^{2q}\,\mathcal C_q\bigl(ix,g_L(ix)\bigr)
 =C_q\left(C-iSu\right)^{-2q}.
 }
\tag{0.7}
\]

Therefore, in the orientation for which the canonical unitary transport contributes `rho_L^{2q}`, the transported disk Bergman kernel is exactly Sun's oriented cylinder kernel:

\[
 \boxed{
 C_q^{-1}\,\mathcal K_q(g_L;u)
 =\kappa_{q,L}(u)
 =\left(\cosh\frac L2-i\sinh\frac L2\,u\right)^{-2q}.
 }
\tag{0.8}
\]

The opposite orientation gives the complex conjugate.

This closes the kernel-shape part of **TOI-A** without asymptotics or fitting.

---

# Part I. Normalization of the disk Bergman kernel

## 1. Canonical metric

For

\[
 ds^2=\lambda^2|dz|^2,
 \qquad
 \lambda=\frac{2}{1-|z|^2},
\]

the cotangent norm is

\[
 |dz|^2=\lambda^{-2}=\left(\frac{1-|z|^2}{2}\right)^2.
\]

Thus

\[
 |(dz)^q|^2
 =\left(\frac{1-|z|^2}{2}\right)^{2q}.
\]

Multiplying by hyperbolic area gives (0.1).

For the standard weighted Bergman measure

\[
 (1-|z|^2)^{\alpha}d^2z,
 \qquad \alpha>-1,
\]

the reproducing kernel is

\[
 \frac{\alpha+1}{\pi}(1-z\bar w)^{-\alpha-2}.
\]

Taking `alpha=2q-2` and compensating for the constant `2^{2-2q}` in the norm gives (0.2).

Pairing the two fibers in unitary frames contributes

\[
 \left(
 \frac{(1-|z|^2)(1-|w|^2)}{4}
 \right)^q,
\]

so the numerical prefactor becomes

\[
 \frac{(2q-1)2^{2q-2}}{\pi}\,4^{-q}
 =\boxed{\frac{2q-1}{4\pi}}=C_q.
\tag{1.1}
\]

This is exactly the identity-orbital density used in the existing Sun--Selberg normalization.

---

# Part II. Hyperbolic translation

## 2. Basic `SU(1,1)` identities

For `z=ix`,

\[
 g_L(ix)=\frac{S+iCx}{C+iSx}.
\tag{2.1}
\]

The standard disk automorphism identity gives

\[
 1-|g_L(ix)|^2
 =\frac{1-x^2}{|C+iSx|^2}.
\tag{2.2}
\]

A direct calculation also gives

\[
 1-ix\,\overline{g_L(ix)}
 =\frac{C(1-x^2)-2iSx}{C-iSx}.
\tag{2.3}
\]

Consequently

\[
 \frac{\sqrt{(1-x^2)(1-|g_L(ix)|^2)}}
 {1-ix\,\overline{g_L(ix)}}
 =
 \frac{C-iSx}{|C+iSx|}
 \frac{1-x^2}{C(1-x^2)-2iSx}.
\tag{2.4}
\]

Multiplying by `rho_L(x)` cancels the first pure phase:

\[
 \rho_L(x)
 \frac{\sqrt{(1-x^2)(1-|g_L(ix)|^2)}}
 {1-ix\,\overline{g_L(ix)}}
 =
 \frac{1-x^2}{C(1-x^2)-2iSx}.
\tag{2.5}
\]

But from `u=2x/(1-x^2)`,

\[
 C(1-x^2)-2iSx
 =(1-x^2)(C-iSu).
\tag{2.6}
\]

Therefore

\[
 \boxed{
 \rho_L(x)
 \frac{\sqrt{(1-x^2)(1-|g_L(ix)|^2)}}
 {1-ix\,\overline{g_L(ix)}}
 =(C-iSu)^{-1}.
 }
\tag{2.7}
\]

Raising to `2q` and multiplying by `C_q` proves (0.7).

---

# Part III. Why the extra phase is the bundle transport

## 3. Unitary `q`-canonical automorphy

Write

\[
 j(g,z)=Sz+C,
 \qquad
 g'(z)=j(g,z)^{-2}.
\]

A holomorphic `q`-differential transforms by the factor `j(g,z)^{-2q}`. Passing from the holomorphic frame `(dz)^q` to the corresponding unitary frame multiplies this by the ratio of the fiber norms. Since

\[
 1-|gz|^2=\frac{1-|z|^2}{|j(g,z)|^2},
\]

the unitary action contributes a pure phase of the form

\[
 \left(\frac{|j(g,z)|}{j(g,z)}\right)^{2q}
\]

or its complex conjugate, depending on whether the group action is placed in the first or second kernel variable. On `z=ix`, these are precisely the two orientation choices associated with `C\pm iSx`.

Thus the phase in (0.6) is not an artificial correction. It is the canonical unitary automorphy/Chern transport needed to compare fibers before taking the off-diagonal Bergman pairing.

This also explains structurally why discarding the Chern phase destroys the exact moment cancellation in the existing orbital note.

---

# Part IV. Toeplitz insertion

## 4. Weighted transported diagonal

For any real lifted weight `W`, the diagonal kernel of the transported Toeplitz operator has, in this convention, the local scalar form

\[
 W(u)\,C_q\kappa_{q,L}(u).
\tag{4.1}
\]

On the cyclic cylinder, `dA=dt\,du`. Averaging in `t` and integrating one primitive centralizer period therefore gives

\[
 \boxed{
 \Re\int_0^{\ell_c}\!dt\int_{\mathbb R}
 W(t,u)\,C_q\kappa_{q,m\ell_c}(u)\,du
 =C_q\ell_c\,\mathcal J_{q,m\ell_c}[W].
 }
\tag{4.2}
\]

For one **oriented** conjugacy class this is exactly the local coefficient appearing in the existing Sun--Selberg unfolding formula. Pairing the inverse orientation doubles the real orbital and produces the unoriented factor `2C_q\ell_c`.

Hence the normalization candidate in the previous TOI notation is no longer free:

\[
 \boxed{
 \mathcal N_{c,m,q}=C_q\ell_c
 \quad\text{per oriented class},
 \qquad
 2C_q\ell_c
 \quad\text{per unoriented primitive geodesic}.
 }
\tag{4.3}
\]

This is a geometric cyclic-cylinder trace formula. Calling it an invariant `relative trace` on the abstract representation remains TOI-B.

---

# Part V. Gate update

## TOI-A — transported Bergman kernel crosswalk

**PASS in the explicit disk/cylinder realization.**

The unitary transported Bergman coherent overlap, including the canonical `q`-differential automorphy phase, is exactly

\[
 C_q\kappa_{q,L}(u).
\]

No semiclassical approximation is used.

## TOI-B — invariant orbital trace

**PARTIAL.** The geometric centralizer-normalized functional is now explicit and its normalization is fixed by (4.3). What remains is to package this cylinder integral invariantly as an orbital/relative trace on the `D^+_{2q-1}` realization and state its domain/regularization properties.

## TOI-C — resolvent Toeplitz matrix elements

**OPEN.** The next calculation is now clean: decompose `T_{f_\mu}^{(q)}` in the cyclic representation and compare its diagonal orbital coefficients with the existing `\Lambda_{n,c}^{(q,m)}`.

## TOI-D — descendant recurrence

**OPEN.** After TOI-C, test whether the cyclic-mode coefficients satisfy a ladder recurrence whose geometric sum is the character denominator `(1-e^{-L})^{-1}`.

---

## 5. Structural consequence

The nonperturbative kernel is no longer merely analogous to a discrete-series matrix coefficient. In a standard disk realization it is literally the gauge-corrected coherent-state Bergman matrix coefficient along a hyperbolic translation:

\[
 \boxed{
 \text{Sun cylinder kernel}
 =\text{Bergman coherent overlap}
 \times\text{canonical unitary transport phase}.
 }
\]

So the next FCIG question is not where the kernel comes from. That part is closed. The remaining question is how the **deformation Toeplitz symbol** decomposes under the cyclic subgroup and how that decomposition reorganizes into the Selberg descendant tower.

## Sources

- Jingzhou Sun, *On the Bergman Kernel of complex hyperbolic manifolds*, arXiv:2511.16240v3 (2026). Sun proves the exact loop formula and explicitly relates it to the universal-cover Bergman kernel summation.
- Standard weighted Bergman-space formula on the unit disk: for weight `(1-|z|^2)^\alpha`, the reproducing kernel is `(\alpha+1)/\pi\,(1-z\bar w)^{-\alpha-2}`.
- See also the project notes `systolic-bergman-orbital.md` and `sun-selberg-unfolding.md` for the cylinder Chern-holonomy and centralizer conventions.
