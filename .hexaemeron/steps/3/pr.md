# Publish the Shoggoth-Centaur comparison and decision guide

## Change

This step adds the 13-axis responsibility matrix, separates conceptual
complement from six competitive overlaps, and maps five kinds of reader
problem to the layer and evidence that can answer them. It finishes the
README, methodology, offline checker, test suite, and read-only workflow for
the complete documentary repository.

The comparison keeps every claim status and evidence qualification visible.
It supplies no score, winner, product recommendation, copied source, or
cross-system design.

## Audit

All three Step 3 rounds are recorded in
`audit/rounds/fiat-shoggoth-versus-centaur-purpose-capabilities-str.md`.
Round 1 found and fixed two medium findings:

- `S3-R1-01` expanded the no-ranking, product-verdict, and no-integration
  guards to ordinary positive prose across every reader-analysis file.
- `S3-R1-02` corrected two matrix statuses, narrowed one audit claim, and
  placed six direct source requirements beside the claims they support.

Round 2 found and fixed `S3-R2-01` (medium). The guard now accepts neutral
procedures and explicit denials while rejecting ordinary instructions to
pair, attach, or use the projects together. Round 3 was clean. The audit fixes
are folded into this step branch; this pull request does not claim a separate
stacked audit pull request.

## Proof

```bash
python3 scripts/check_repository.py
python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-3.json
python3 -m unittest discover -s tests
```

## Stack

The exact pull-request base is
`fiat/shoggoth-versus-centaur-purpose-capabilities-str-step-2-write-the-two-source-profiles-an`.
The exact head is
`fiat/shoggoth-versus-centaur-purpose-capabilities-str-step-3-publish-the-comparison-complemen`.
The base branch is reviewed in [pull request #2](https://github.com/laurenceday/shoggoth-vs-centaur/pull/2).

## Provenance

The step commits are signed as
`Dr Laurence E. Day <laurence@wildcat.finance>` and retain the Shoggoth
co-author and `Wildcat-Origin: shoggoth` trailers.

## Boundary

Neither source project was deployed. Runtime correctness, scale, latency,
cost, model quality, adoption, private overlays, and external hosts remain
outside the registered evidence. Open issues remain reported and
non-reproduced, and proposals remain planned.

<!-- wildcat-origin: shoggoth -->
