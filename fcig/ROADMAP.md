# FCIG Research Roadmap

**Current target:** v0.11 — target-structure / nonabelian bridge audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are kept as explicit no-go results.

---

## v0.3–v0.6 — geometry, determinants and differential characters — COMPLETE

The completed flat and curved laboratories establish:

- exact theta/state-count models and global lattice corrections;
- a curved hyperbolic local/global Bergman split;
- Quillen versus \(L^2\) determinant metrics and analytic torsion;
- degree-two differential characters as the correct package for line topology, curvature and holonomy.

---

## v0.7 — response / transgression — COMPLETE

Loop transgression is a genuine standard response operation,

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z),
\]

while positive-dimensional pushforward lowers degree.

---

## v0.8 — factorized pushforward — COMPLETE WITH NO-GO

For a smooth proper oriented real \(d\)-dimensional family \(p:Z\to M\),

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=
n\widehat{\mathcal A}
}
\]

on each connected component. Factorized degree restoration cannot generate an independent degree-two response direction.

---

## v0.9 — non-factorized \(\widehat\kappa_1\) / Quillen comparison — COMPLETE

For a smooth family of curves, \(\omega=K_{X/B}\),

\[
\widehat\kappa_1
:=
\pi_!\bigl(\widehat c_1(\omega)^2\bigr).
\]

GRR and the Quillen local-index theorem give

\[
I(\widehat\kappa_1)=12I(\widehat\lambda_Q),
\qquad
R(\widehat\kappa_1)=12R(\widehat\lambda_Q).
\]

Thus the only possible discrepancy at this stage is a topologically trivial flat character.

---

## v0.10 — global metrized Deligne--Riemann--Roch closure — COMPLETE

### Gate AA — Deligne-pairing realization — PASS

Fix the standard geometric realization

\[
\boxed{
\pi_!\left(
\widehat c_1(L)\cup\widehat c_1(M)
\right)
=
\widehat c_1(\langle L,M\rangle_\pi,\nabla^{\mathrm{Del}})
}
\]

under the canonical equivalence of differential-cohomology models. The product/fiber-integration structure is standard; the Hermitian Deligne cup-product is realized by the metrized Deligne pairing.

### Gate AB — metrized Deligne--RR — PASS

For a family of curves, Deligne's determinant isomorphism gives

\[
\det R\pi_*L^{\otimes12}
\simeq
\langle\omega,\omega\rangle_\pi
\otimes
\langle L,L\otimes\omega^{-1}\rangle_\pi^{\otimes6}.
\]

At \(L=\omega\), the second pairing is canonically trivial, so

\[
\boxed{
\lambda^{\otimes12}
\simeq
\langle\omega,\omega\rangle_\pi.
}
\]

With Quillen and Deligne metrics, the established theorem is an isometry up to an overall topological/base-independent constant. Such a constant does not change the Chern connection.

### Gate AC — global holonomy — PASS

Consequently the isomorphism is connection-preserving and

\[
\boxed{
\widehat\kappa_1
=
12\widehat\lambda_Q
}
\]

globally in the fixed convention. Hence for every loop \(\gamma\),

\[
\boxed{
\operatorname{Hol}_{\widehat\kappa_1}(\gamma)
=
\operatorname{Hol}_{\widehat\lambda_Q}(\gamma)^{12}.
}
\]

The flat residual of v0.9 therefore vanishes once the full metrized Deligne--RR identification is included.

Sources:

- `global-deligne-rr.md`
- Deligne (1987)
- Freixas i Montplet--Wentworth (2020)
- Aldrovandi (2005)
- Bär--Becker (2014)
- Bismut--Freed / Dai--Freed for determinant holonomy context

### v0.10 conclusion

\[
\boxed{
\text{MMM/Deligne self-intersection differential character}
=
12\times
\text{Quillen determinant differential character}
}
\]

at topology, curvature **and global holonomy** levels.

This closes the canonical smooth curve-family determinant/intersection sector.

---

## v0.11 — target-structure / nonabelian bridge audit — ACTIVE

The next problem cannot be solved by another identity in \(\widehat H^2(-;\mathbf Z)\). A proposed physical/geometric response must name an actual target bundle and structure group.

### Gate AD — explicit target geometry

Specify

\[
P\to M,
\qquad
G=\operatorname{StructureGroup}(P),
\]

before comparing any determinant curvature with a target curvature.

### Gate AE — base-space map/correspondence

Give an explicit map or correspondence relating the parameter/moduli base carrying the determinant character to the target base \(M\). No identification \(B=M\) by analogy is allowed.

### Gate AF — structure-group map

If a fixed homomorphism

\[
\varphi:U(1)\to G
\]

is proposed, audit the image of its Lie algebra map. A one-dimensional abelian source can only produce curvature in a one-dimensional abelian subalgebra of \(\mathfrak g\); it cannot by itself determine a generic nonabelian connection.

### Gate AG — Lorentzian/causal data

If the target is a spacetime frame bundle, separately specify the Lorentzian metric/causal structure. A \(U(1)\) differential character contains no such data by itself.

**Pass condition:** either an explicit additional geometric structure is supplied, or the attempted bridge is recorded as a no-go.

---

## Gravity Closure gate — NOT ACTIVE

The determinant sector is no longer the bottleneck. A future gravitational closure would still need:

1. an actual physical spacetime/base object;
2. a map/correspondence from the FCIG parameter geometry;
3. structure-group and tensor-type matching;
4. Lorentzian causal structure;
5. a horizon/thermodynamic entropy functional;
6. an established or testable dynamical limit;
7. a falsification route.
