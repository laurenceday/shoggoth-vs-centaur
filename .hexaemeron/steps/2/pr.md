# Add pinned Shoggoth and Centaur source profiles

## Change

This step adds symmetric Shoggoth and Centaur profiles at the registered source
commits. Each profile covers purpose, architecture, capabilities, strengths,
limits, security boundaries, operating burden, open work, negative space and
evidence limits under the same headings and visible status labels.

The source ledger records exact pins, read modes, merged pull requests, open and
post-pin issues, Skills audit attribution, bounded absence searches, unknowns
and the update procedure. The checker and its tests enforce that evidence
contract before Step 3 writes any comparative synthesis.

## Audit

Both Step 2 rounds are recorded in
`audit/rounds/fiat-shoggoth-versus-centaur-purpose-capabilities-str.md`.
Round 1 found and folded three findings into this branch:

- `S2-R1-01` (medium) split adjacent status-labelled claims before checking
  each claim's pin or non-reproduction boundary.
- `S2-R1-02` (medium) expanded the source-copy inventory so upstream-language
  files and mirror directories reach the guard.
- `S2-R1-03` (low) corrected the README's description of the workflow commands
  and checkout credential handling.

Round 2 was clean. The audit fixes are folded into this step branch; this pull
request does not claim a separate stacked audit pull request.

## Proof

```bash
python3 scripts/check_repository.py
python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-2.json
python3 -m unittest discover -s tests
```

## Stack

The exact pull-request base is
`fiat/shoggoth-versus-centaur-purpose-capabilities-str-step-1-establish-the-evidence-contract`.
The exact head is
`fiat/shoggoth-versus-centaur-purpose-capabilities-str-step-2-write-the-two-source-profiles-an`.
The base branch is reviewed in [pull request #1](https://github.com/laurenceday/shoggoth-vs-centaur/pull/1).

## Provenance

The step commits are signed as
`Dr Laurence E. Day <laurence@wildcat.finance>` and retain the Shoggoth
co-author and `Wildcat-Origin: shoggoth` trailers.

## Boundary

This step copies no upstream source and proposes no adapter, migration,
embedding or integration. It records original, source-bound analysis only.

<!-- wildcat-origin: shoggoth -->
