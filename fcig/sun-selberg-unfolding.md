# FCIG: Exact Sun–Selberg Unfolding and Orbital Normalization

**Status:** exact derived theorem + normalization closure  
**Date:** 2026-09-10  
**Scope:** compact torsion-free hyperbolic surfaces, Sun's oriented based-loop Bergman formula, absolute convergence, conjugacy-class unfolding, centralizer length, orientation counting, and the zero cyclic Fourier mode.  
**Depends on:** [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md), [`casimir-orbital-transmutation.md`](casimir-orbital-transmutation.md), [`cyclic-fourier-profile.md`](cyclic-fourier-profile.md), [`cyclic-mode-asymptotics.md`](cyclic-mode-asymptotics.md).

> **Claim policy.** Sun's exact loop formula and standard Selberg centralizer/unfolding machinery are established inputs. The convergence estimate, its application to Sun's kernel, and the resulting normalization formula below are **Derived here**. The Riemann--Roch dimension itself is classical.

---

## 1. Setup

Let

\[
X=\Gamma\backslash\mathbb H
\]

be compact, torsion-free, genus \(g\ge2\), and let \(q\ge2\). In complex dimension one Sun's formula is

\[
\boxed{
B_q(p)=C_q\left(1+\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2q}\!\frac{\ell(\gamma)}2
\cos(2\pi q\alpha_\gamma)\right),
\qquad
C_q=\frac{2q-1}{4\pi}.
}
\tag{1.1}
\]

The loops in \(\mathfrak G_p\) are **oriented**. Choosing a lift \(z\in\mathbb H\) identifies them with nonidentity deck transformations \(\gamma\in\Gamma\), the oriented geodesic segment from \(z\) to \(\gamma z\) projecting to the based loop.

For a real bounded \(\Gamma\)-invariant weight \(W\), define

\[
\mathcal B_q[W]
:=\int_XW(B_q-C_q)dA.
\tag{1.2}
\]

---

## 2. Absolute convergence

### Theorem A — uniform absolute convergence on a compact quotient

For every \(q\ge2\),

\[
\sum_{\gamma\ne1}
\cosh^{-2q}\!\frac{d(z,\gamma z)}2
\tag{2.1}
\]

converges uniformly for \(z\) in a compact fundamental domain. Consequently Sun's real loop series may be integrated termwise against every bounded weight \(W\), and it may be rearranged by conjugacy classes.

**Proof.** On a cocompact Fuchsian group there are constants \(A,B>0\), uniform for \(z\) in a fixed compact fundamental domain, such that

\[
N_z(R):=\#\{\gamma\in\Gamma:d(z,\gamma z)\le R\}\le Ae^{R}+B.
\tag{2.2}
\]

For \(r\ge1\),

\[
\cosh^{-2q}(r/2)\le C_q' e^{-qr}.
\tag{2.3}
\]

Splitting the orbit into unit shells gives

\[
\sum_{n\ge1}
O(e^n)e^{-qn}
=
\sum_{n\ge1}O(e^{-(q-1)n}),
\tag{2.4}
\]

which converges for \(q>1\). Uniformity of the orbit-counting bound gives uniform convergence. Since \(|\cos(2\pi q\alpha)|\le1\), the same majorant applies to Sun's series. Dominated convergence/Tonelli for the absolute majorant then justify termwise integration and rearrangement. \(\square\)

---

## 3. Exact conjugacy-class unfolding

For a nontrivial hyperbolic element \(\gamma\), let \(\Gamma_\gamma\) denote its centralizer. Standard hyperbolic-group/trace-formula theory gives a unique primitive element \(\delta\) and an integer \(m\ge1\) with

\[
\gamma=\delta^m,
\qquad
\Gamma_\gamma=\langle\delta\rangle.
\tag{3.1}
\]

The quotient \(\langle\delta\rangle\backslash\mathbb H\) is the cyclic hyperbolic cylinder whose longitudinal fundamental length is

\[
\boxed{\ell(\delta),\ \text{not }m\ell(\delta).}
\tag{3.2}
\]

The kernel parameter for the \(m\)-th power is nevertheless

\[
L=m\ell(\delta).
\tag{3.3}
\]

Let \(W_\delta(t,u)\) be the lift of \(W\) to this cylinder, with

\[
\overline W_\delta(u)
=\frac1{\ell(\delta)}\int_0^{\ell(\delta)}W_\delta(t,u)dt.
\tag{3.4}
\]

Using the oriented complex kernel

\[
\kappa_{q,L}(u)
=\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q},
\tag{3.5}
\]

define

\[
\mathcal J_{q,L}[W_\delta]
=\Re\int_{\mathbb R}\overline W_\delta(u)\kappa_{q,L}(u)du.
\tag{3.6}
\]

### Theorem B — exact Sun–Selberg unfolding

If \(\mathcal P_{\rm or}\) denotes primitive **oriented** conjugacy classes, then

\[
\boxed{
\mathcal B_q[W]
=
C_q
\sum_{[\delta]\in\mathcal P_{\rm or}}
\ell(\delta)
\sum_{m=1}^{\infty}
\mathcal J_{q,m\ell(\delta)}[W_\delta].
}
\tag{3.7}
\]

Equivalently, if \(\mathcal P\) denotes primitive **unoriented** closed geodesics and one chooses one orientation \(\delta_c\) for each \(c\in\mathcal P\), then orientation reversal complex-conjugates \(\kappa\) and leaves the real orbital unchanged, so

\[
\boxed{
\mathcal B_q[W]
=
2C_q
\sum_{c\in\mathcal P}
\ell_c
\sum_{m=1}^{\infty}
\mathcal J_{q,m\ell_c}[W_c].
}
\tag{3.8}
\]

**Derived here from standard Selberg unfolding.** The factor \(2\) in (3.8) is exactly the pair \(\delta_c^{m},\delta_c^{-m}\) present in Sun's oriented based-loop sum. The centralizer quotient is always by \(\langle\delta_c\rangle\), hence the longitudinal factor is the primitive length \(\ell_c\).

---

## 4. Orbital Riemann--Roch is now unconditional

For \(W\equiv1\), the Chern-holonomy moment theorem gives, for every \(L>0\),

\[
\mathcal J_{q,L}[1]
=\Re\int_{\mathbb R}\kappa_{q,L}(u)du=0.
\tag{4.1}
\]

Therefore every nonidentity hyperbolic conjugacy-class orbital in (3.8) vanishes and

\[
\boxed{
\int_XB_qdA=C_q\operatorname{Area}(X).
}
\tag{4.2}
\]

Gauss--Bonnet gives \(\operatorname{Area}(X)=4\pi(g-1)\), hence

\[
\boxed{
\dim H^0(X,K_X^q)
=(2q-1)(g-1),
\qquad q\ge2.
}
\tag{4.3}
\]

Thus the previous conditional orbital Riemann--Roch bridge is promoted to an exact theorem for compact torsion-free surfaces: the identity orbital is the complete unweighted index trace, while the Chern phase annihilates every nonidentity hyperbolic orbital.

---

## 5. Exact zero-mode class contribution

In the cyclic Fourier normalization used in [`cyclic-fourier-profile.md`](cyclic-fourier-profile.md), the longitudinal zero mode satisfies

\[
|b_0|^2=4|\partial_\mu\log\ell_c|^2.
\tag{5.1}
\]

For the power with \(L=m\ell_c\), the exact zero-mode calculation gives

\[
|b_0|^2\mathcal J_{q,L}[W_{q,0}]
=
2\pi(3q-1-qe^{-L})e^{-qL}
|\partial_\mu\log\ell_c|^2.
\tag{5.2}
\]

Combining (5.2) with the exact unoriented unfolding factor \(2C_q\ell_c\) yields the contribution of one primitive geodesic \(c\) and one power \(m\):

\[
\boxed{
\mathcal B^{(0)}_{q,c,m}
=
(2q-1)\ell_c
(3q-1-qe^{-m\ell_c})
e^{-qm\ell_c}
|\partial_\mu\log\ell_c|^2.
}
\tag{5.3}
\]

Summing all powers gives the exact zero-mode primitive-class contribution

\[
\boxed{
\begin{aligned}
\mathcal B^{(0)}_{q,c}
={}&(2q-1)\ell_c|\partial_\mu\log\ell_c|^2\\
&\times\left[
(3q-1)\frac{e^{-q\ell_c}}{1-e^{-q\ell_c}}
-q\frac{e^{-(q+1)\ell_c}}{1-e^{-(q+1)\ell_c}}
\right].
\end{aligned}
}
\tag{5.4}
\]

For fixed \(c\),

\[
\boxed{
\mathcal B^{(0)}_{q,c}
=
2q^2\ell_c(3-e^{-\ell_c})
e^{-q\ell_c}
|\partial_\mu\log\ell_c|^2
+O(qe^{-q\ell_c})+O(q^2e^{-2q\ell_c}).
}
\tag{5.5}
\]

This is a **partial** class coefficient: nonzero cyclic Fourier modes contribute on the same \(q^2e^{-q\ell_c}\) scale and must be summed before comparison with the full FRZ coefficient.

---

## 6. Comparison with the Selberg coefficient

FRZ prove, for a systole direction with nonzero first variation,

\[
\bar\partial_\mu\partial_\mu\log Z(q)
\sim
-
\frac{q^2e^{-q\ell_0}}{1-e^{-\ell_0}}
\sum_{c\in S(X)}|\partial_\mu\ell_c|^2.
\tag{6.1}
\]

Equivalently, each primitive systole carries the scalar invariant

\[
|\partial_\mu\ell_c|^2
=\ell_c^2|\partial_\mu\log\ell_c|^2.
\tag{6.2}
\]

The zero Bergman mode (5.5) already has the same exponential and polynomial scale \(q^2e^{-q\ell_c}\), but it does **not** by itself reproduce the Selberg denominator \((1-e^{-\ell_c})^{-1}\). This is an important clue rather than a mismatch to be hidden.

The Selberg local factor is

\[
Z_c(q)=\prod_{k=0}^{\infty}(1-e^{-(q+k)\ell_c}),
\tag{6.3}
\]

so the denominator \((1-e^{-\ell_c})^{-1}\) comes from its infinite descendant tower in \(k\). On the Bergman/cyclic side the missing information is precisely the tower of nonzero Fourier modes. This motivates the representation-theoretic target

\[
\boxed{
\text{cyclic Fourier mode sum}
\stackrel{?}{=}
\text{holomorphic-discrete-series character/descendant denominator}.
}
\tag{6.4}
\]

For \(SL(2,\mathbb R)\), the Harish--Chandra character of an individual discrete-series representation on a regular hyperbolic element has the standard Weyl-denominator form

\[
\Theta_n(a_t)
\propto
\frac{e^{-n|t|}}{|e^t-e^{-t}|},
\tag{6.5}
\]

which is equivalently a geometric-series denominator after normalization of the hyperbolic parameter. Equation (6.5) is **established representation theory**; identifying the precise \(q\)-normalization of Sun's cyclic Bergman modes with this character is the next open crosswalk, not claimed here.

---

## 7. What is now closed and what remains

**Closed exactly:**

\[
\boxed{
\begin{gathered}
\text{absolute convergence for compact }X,\ q\ge2,\\
\text{Sun loop sum }\to\text{ conjugacy-class unfolding},\\
\text{primitive centralizer length }\ell_c,\\
\text{orientation factor }2,\\
\text{orbital Riemann--Roch},\\
\text{zero-mode primitive/power coefficient.}
\end{gathered}}
\]

**Remaining theorem target:** compute

\[
\sum_{n\in\mathbb Z}\mathcal B_{q,c,m}^{(n)}
\tag{7.1}
\]

in a closed representation-theoretic form and compare it term-by-term with the FRZ/Selberg local factor. The strongest clue is that the Selberg denominator and the hyperbolic discrete-series character denominator have the same descendant/Weyl structure.

---

## References used for the normalization

- Jingzhou Sun, *On the Bergman Kernel of complex hyperbolic manifolds*, arXiv:2511.16240v3 (2026), Theorem 1.1.
- H. P. McKean, *Selberg's Trace Formula as Applied to a Compact Riemann Surface*, Comm. Pure Appl. Math. 25 (1972), 225--246.
- D. Hejhal, *The Selberg Trace Formula for PSL(2,R), Vol. I*, LNM 548, Springer.
- K. Fedosova, J. Rowlett, G. Zhang, *Second Variation of Selberg Zeta Functions and Curvature Asymptotics*, Ann. Global Anal. Geom. 57 (2020), 23--60.
- Harish--Chandra, *Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters*, Acta Math. 116 (1966), 1--111.
