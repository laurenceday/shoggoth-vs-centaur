# Shoggoth versus Centaur

This private repository is a source-bound comparison of the Shoggoth
agent-and-skill collective and Paradigm's Centaur team-agent platform. It asks
what each is for, what layer it occupies, and where their responsibilities may
complement or compete. It will not copy either project, choose a winner, or
design an integration.

This first Fiat step establishes the evidence contract and validation
scaffold. The two source profiles and comparative conclusions are not written
yet.

## Read now

- [Method and source policy](docs/00-methodology.md)
- [Layer-aware comparison decision](docs/decisions/ADR-001-layer-aware-comparison.md)
- [Fiat study](docs/fiat-study.md)
- [Fiat runbook](docs/fiat-runbook.md)
- [Machine-readable source pins](evidence/pins.json)

## Verify

The checks are offline and use only Python's standard library:

```bash
python3 scripts/check_repository.py
python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-1.json
python3 -m unittest discover -s tests
```

The GitHub workflow runs the same commands with read-only repository
permission and no secrets.

## Rights

The repository is private and proprietary. See [LICENSE](LICENSE).
