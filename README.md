# Shoggoth versus Centaur

This public repository is a source-bound comparison of the Shoggoth
agent-and-skill collective and Paradigm's Centaur team-agent platform. It asks
what each is for, what layer it occupies, and where their responsibilities may
complement or compete. It will not copy either project, choose a winner, or
design an integration.

The layer distinction is direct. Shoggoth governs what bounded agent
job, evidence, and repository delivery is authorised. Centaur operates where
shared team sessions run, persist, receive capabilities, and recover. They
overlap in instruction distribution, workflows, multi-agent coordination,
extensions, audit records, and behavioural conventions. That overlap does not
erase the different state and trust boundaries described by their pinned
sources.

This edition contains the symmetric profiles, comparison matrix, conceptual
complement and competitive-overlap analysis, decision guide, and source ledger.

## Read in order

- [Method and source policy](docs/00-methodology.md)
- [Shoggoth profile](docs/01-shoggoth.md)
- [Centaur profile](docs/02-centaur.md)
- [Responsibility matrix](docs/03-comparison-matrix.md)
- [Conceptual complement and competitive overlap](docs/04-complement-and-competition.md)
- [Problem-to-layer decision guide](docs/05-decision-guide.md)
- [Reproducible source ledger](docs/SOURCES.md)
- [Layer-aware comparison decision](docs/decisions/ADR-001-layer-aware-comparison.md)
- [Fiat study](docs/fiat-study.md)
- [Fiat runbook](docs/fiat-runbook.md)
- [Fiat audit synopsis](audit/rounds/fiat-shoggoth-versus-centaur-purpose-capabilities-str.synopsis.md)

The [machine-readable source pins](evidence/pins.json) freeze Skills at
`58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff` and Centaur at
`36397534096bb89c065a52a9fcfebed34b995a00`. Current claims use those editions;
reports, plans, inferences, and unknowns remain visibly distinct.

## Verify

The checks are offline and use only Python's standard library:

```bash
python3 scripts/check_repository.py
python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-3.json
python3 -m unittest discover -s tests
```

The GitHub workflow runs the same checker and test suite with read-only
repository permission and does not persist checkout credentials. The checker
fails closed on missing axes, broken navigation, mutable source links,
unlabelled synthesis, actionable cross-system design, copied-source shapes,
local paths, credential-shaped text, or a changed Fiat planning record.

## Rights

The repository is private and proprietary. See [LICENSE](LICENSE).
