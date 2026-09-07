# FCIG Research Repository Policy

**Status:** active repository policy  
**Effective:** 2026-09-08

This directory is the public research workspace for **Fibered Cohomological Information Geometry (FCIG)**. The goal is not to maximize the number of speculative claims. The goal is to make every step inspectable: what is standard mathematics, what is calculated here, what is interpretation, and what remains open.

## 1. Role of `main`

`main` is always a readable, public-facing research state.

Material may be merged to `main` only when:

- notation is internally consistent;
- standard claims have a reference or are elementary enough to be proved in place;
- calculations specific to FCIG are marked **Derived here**;
- speculative statements are marked **FCIG interpretation**, **conjecture**, or **open problem**;
- numerical claims have reproducible code when a numerical check is material;
- no claim of novelty is made solely because a calculation was produced in this repository.

Exploratory work belongs on a topic branch and reaches `main` through a pull request.

## 2. Claim classes

Every substantial claim should fit one of these classes.

| Tag | Meaning | Required support |
| --- | --- | --- |
| **Established** | Standard or previously published mathematics | Citation to an appropriate source |
| **Derived here** | Calculation/proposition proved in an FCIG note | Derivation or proof in the note; code when useful |
| **FCIG interpretation** | New terminology or physical reading of established mathematics | Must not be presented as a cited theorem |
| **Conjecture** | A proposed mathematical/physical statement not yet proved | Explicit hypotheses and a falsification route where possible |
| **Open problem** | A question that structures the research program | Clear success/failure criterion |

A source may be cited only for what it actually supports. In particular, a general theorem is not a citation for a normalization-dependent FCIG coefficient unless that coefficient is explicitly contained in the source.

## 3. Citation policy

`fcig/references.bib` is the canonical bibliography.

The citation audit rules are:

1. prefer primary papers or standard monographs;
2. distinguish general background from an exact formula derived in this repository;
3. keep convention-sensitive identities visibly tied to the conventions used in the note;
4. do not write “new”, “first”, or “novel” without a dedicated literature search;
5. when the literature only motivates an analogy, label the analogy as interpretation rather than attribution.

`citation-map.md` and `cited-synthesis.md` remain provenance aids; the original notes should also contain inline citations.

## 4. Reproducibility policy

Exact symbolic derivations are preferred whenever available. Numerical code is used to:

- verify convention-sensitive formulas;
- catch sign, phase, or normalization errors;
- probe conjectures before a proof is attempted;
- test degeneration and scaling regimes.

A verifier should state its truncation/cutoff, tolerance, and the identity being checked. Numerical agreement is evidence, not proof.

## 5. Branch and PR policy

Use one conceptual unit per branch. Recommended names:

- `fcig-<model>-<topic>-YYYY-MM-DD`
- `fcig-citation-<topic>-YYYY-MM-DD`
- `fcig-infra-<topic>-YYYY-MM-DD`

A pull request should state:

- **Established background** used;
- **Derived here** results introduced;
- **Interpretive/conjectural** statements introduced;
- tests or numerical checks performed;
- unresolved caveats.

Prefer a merge commit when the PR represents a research milestone whose development history is useful; use squash only for mechanical cleanup.

## 6. Stable public paths

Existing public pages under `/fcig/` are stable and should not be moved casually.

In particular:

- `research-note.md` — general architecture;
- `elliptic-model.md` — Explicit Model I;
- `modular-holonomy.md` — Explicit Model II;
- future `*-model.md` files — explicit mathematical laboratories;
- `references.bib` — canonical bibliography;
- `ROADMAP.md` — active research order and gates.

HTML pages are publication views. Markdown files are the source research records.

## 7. Research order

FCIG will generalize by increasing mathematical difficulty while preserving exact checks as long as possible:

\[
\boxed{
\text{elliptic curves}
\to
\text{higher-dimensional abelian varieties}
\to
\text{genus }g\ge2\text{ curves}
\to
\text{Quillen/analytic-torsion refinement}
\to
\text{Lorentzian closure}.
}
\]

The gravitational closure is deliberately last. A failure of the geometric mechanisms in the intermediate stages is scientifically useful and should be recorded as a no-go result rather than hidden.

## 8. AI-assisted research rule

AI tools may assist with drafting, algebraic manipulation, code, literature triage, and counterexample search. They are not treated as an authority.

Before a mathematical claim is promoted to `main`, the repository must contain enough derivation, citation, or reproducible verification for a human reader to check it independently.

## 9. Versioning

Milestone tags should correspond to mathematical states, not calendar frequency. Proposed sequence:

- **v0.1** — fibered architecture and citation-audited synthesis;
- **v0.2** — completed elliptic local/global anomaly model;
- **v0.3** — higher-dimensional abelian generalization;
- **v0.4** — curved genus-\(g\ge2\) test;
- **v0.5** — Quillen/analytic-torsion refinement;
- **v1.0 candidate** — only after a precise Gravity Closure Conjecture survives the preceding tests.

The version numbers describe research maturity, not a claim that the physical theory is complete.
