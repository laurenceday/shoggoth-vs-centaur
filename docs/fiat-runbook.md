# Runbook: Shoggoth versus Centaur documentary comparison

This runbook derives from the receipted study at `.hexaemeron/study.md`. It builds a private, source-bound comparison repository. It does not copy either source, connect the systems, or design an integration.

## Step 1: Establish the evidence contract and repository scaffold

**Goal.** Create the smallest green repository that fixes the source pins, comparison method, rights boundary, Fiat record, offline validation contract, and read-only CI path before substantive claims are added.

**Entry.** The Fiat run branch `fiat/shoggoth-versus-centaur-purpose-capabilities-str` at signed bootstrap commit `db38e431561d473d2ee85a1bf4dfe8e94d135c13`, with the study and this runbook receipted and no product files present.

**Exit.** The repository contains a concise scaffold `README.md`; a proprietary rights notice; `.gitignore`; the authorised read-only Python CI workflow; the method, layer decision, evidence registry, and committed Fiat study/runbook; a standard-library repository checker; an Elenchus-compatible `unittest` runner; and focused scaffold tests. `python3 scripts/check_repository.py`, `python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-1.json`, and `python3 -m unittest discover -s tests` all exit zero, and the structured report has contract `elenchus.unittest.v1` with a complete passing run.

**Files.** Create `.github/workflows/verify.yml`, `.gitignore`, `LICENSE`, `README.md`, `docs/00-methodology.md`, `docs/decisions/ADR-001-layer-aware-comparison.md`, `docs/fiat-study.md`, `docs/fiat-runbook.md`, `evidence/pins.json`, `scripts/check_repository.py`, `scripts/run_tests.py`, `tests/__init__.py`, and `tests/test_repository.py`.

**Tests.** Add at least 10 standard-library tests for the exact two pins, evidence schema, required scaffold, rights notice, immutable source-link form, safe relative links, local-path and credential-marker rejection, CI commands, and `elenchus.unittest.v1` report shape. Elenchus command: `python3 scripts/run_tests.py --report {report}`. Report format: `elenchus.unittest.v1`. Report file: `.elenchus/shoggoth-vs-centaur-step-1.json`.

**Disciplines.** phylax: this step opens Markdown, JSON, filesystem-validation, CI, and GitHub-publication boundaries and closes them with bounded regular-file reads, offline checks, exact pins, no secret input, and private signed publication. ephoros: the checker and runner must emit file/pin diagnostics and one structured complete/incomplete test result. metron: none, no performance change or acceptance budget is authorised; the demo may record informational wall time only. elenchus: no failure is in hand at entry, but any defect found must gain a focused failing guard before its fix and use the declared runner. hypomnema: the layer model, claim statuses, source-pin policy, no-integration boundary, rights position, and human-authorship rule are expensive to reverse and live in the ADR, methodology, evidence registry, licence, and Fiat records.

## Step 2: Write the two source profiles and evidence ledger

**Goal.** Describe Shoggoth and Centaur symmetrically at their actual layers, with current capability, strength, weakness, security boundary, operating burden, residue, and negative space tied to the pinned evidence.

**Entry.** Step 1's signed green commit, with the offline evidence contract, source registry, methodology, and runner present and unchanged except where this step's new source claims require a focused test extension.

**Exit.** `docs/01-shoggoth.md`, `docs/02-centaur.md`, and `docs/SOURCES.md` exist; both profiles answer the same required questions; every current code claim uses the registered full-commit permalink; reported, planned, inferred, and unknown material is visibly distinct; source audits and issue evidence keep their stated boundaries; and no profile presents an absent out-of-scope layer as an automatic defect. `python3 scripts/check_repository.py`, `python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-2.json`, and `python3 -m unittest discover -s tests` all exit zero.

**Files.** Create `docs/01-shoggoth.md`, `docs/02-centaur.md`, and `docs/SOURCES.md`; extend `scripts/check_repository.py` and `tests/test_repository.py` only as needed to enforce the source-profile and claim-status contract; update scaffold navigation in `README.md` and `docs/00-methodology.md` without adding comparative conclusions.

**Tests.** Extend the suite to at least 18 tests covering the two symmetric profile inventories, exact pinned permalinks, required status labels, Skills audit-view attribution, Centaur audit-evidence absence, issue-report non-reproduction wording, security-control/residual adjacency, negative-space scope, source-ledger coverage, and absence of local source paths or copied code. Elenchus command: `python3 scripts/run_tests.py --report {report}`. Report format: `elenchus.unittest.v1`. Report file: `.elenchus/shoggoth-vs-centaur-step-2.json`.

**Disciplines.** phylax: public source, issue, audit, and negative-evidence boundaries can be widened by prose, so claims remain pinned, status-labelled, scoped to repository ownership, and free of credentials or local paths. ephoros: the checker must name the document and rule when profile shape, status, or pin coverage fails. metron: none, the step makes no speed, scale, cost, or adoption claim. elenchus: a broken source or status rule receives a focused fixture/test that fails on the parent state before correction. hypomnema: none, this step applies the receipted layer/status/pin decisions and must amend the study before changing one.

## Step 3: Publish the comparison, complement/competition analysis, and proving demo

**Goal.** Complete the reader-facing comparison without scores or a winner, separate conceptual complement from competitive overlap, and prove the full private repository from README through source ledger.

**Entry.** Step 2's signed green commit, with both source profiles and their ledger complete at the assigned pins.

**Exit.** The final `README.md`, comparison matrix, complement/competition analysis, and problem-to-layer decision guide form one navigable reader path; the matrix covers every study axis without aggregate ranking; complement stays conceptual and contains no adapter, migration, API map, copied implementation, or integration plan; competition is limited to responsibilities both projects address; all three local proof commands pass; informational timing is recorded without a budget claim; the remote identity/visibility and signature checks are ready for Fiat's push and integration gates. Run `python3 scripts/check_repository.py`, `python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-3.json`, and `python3 -m unittest discover -s tests`; each must exit zero and the report must show a complete passing run.

**Files.** Create `docs/03-comparison-matrix.md`, `docs/04-complement-and-competition.md`, and `docs/05-decision-guide.md`; complete `README.md`; extend `scripts/check_repository.py` and `tests/test_repository.py` for final navigation, axis, status, no-ranking, and no-integration checks; update `docs/SOURCES.md` only for evidence actually cited by the synthesis.

**Tests.** Extend the suite to at least 26 tests covering README navigation, all 13 required matrix axes, distinct complement and competition sections, no score/winner field, no implementation or migration plan, conceptual-complement boundary, problem-to-layer guide shape, full relative-link resolution, complete source/pin coverage, prohibited secret/local-path markers, and the exact final demo. Elenchus command: `python3 scripts/run_tests.py --report {report}`. Report format: `elenchus.unittest.v1`. Report file: `.elenchus/shoggoth-vs-centaur-step-3.json`.

**Disciplines.** phylax: synthesis can collapse layers, smuggle ranking, or widen complement into implementation, so the matrix names responsibilities, the two analyses remain separate, and explicit tests close those boundaries. ephoros: the final checker and runner answer whether navigation, axes, pins, prohibited shapes, and the entire suite passed; Fiat separately observes private remote identity and signature validity. metron: no optimisation is authorised; `/usr/bin/time -p` may record an informational final baseline only. elenchus: every discovered structural regression gets a focused parent-state failure and the declared report before its fix; a prose truth dispute remains a sourced Warden finding rather than a fabricated code failure. hypomnema: none, the existing ADR governs the final synthesis and any reversal requires a receipted amendment before code or prose changes.
