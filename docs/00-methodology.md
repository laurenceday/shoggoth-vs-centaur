# Methodology

## Edition boundary

This edition is frozen to two public source repositories at exact commits:

- Shoggoth / Skills:
  `wildcat-finance/skills@58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff`
- Centaur:
  `paradigmxyz/centaur@36397534096bb89c065a52a9fcfebed34b995a00`

The machine-readable authority is [`evidence/pins.json`](../evidence/pins.json).
A current code claim must cite an immutable GitHub blob URL containing the
registered full commit. For example, the source definitions begin in the
[Skills README](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md)
and the
[Centaur README](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md).
Pull requests and issues may use their durable URLs because their status is
recorded separately from source-code claims.

## Layer model

The comparison starts with a responsibility distinction:

| Subject | Primary layer | Unit of work | State it owns |
| --- | --- | --- | --- |
| Shoggoth | Governed specialist instructions and repository delivery | A bounded skill operation or receipted delivery step | Evidence contracts, delivery records, branches, and pull requests |
| Centaur | Shared agent service and execution control | A durable session, execution, tool call, or workflow run | Service, workflow, sandbox, event, principal, and delivery state |

This is a method, not a verdict. Later documents must retain genuine overlap
and ask each system the same questions at the layer it claims.

## Claim statuses

- **Current** means documented and supported by implementation or a canonical
  repository contract at the registered pin.
- **Inferred** means a bounded conclusion drawn from named source evidence.
- **Reported** means present in an issue or pull-request record and not
  independently reproduced here.
- **Planned** means proposed work not supplied by the pinned implementation.
- **Unknown** means the selected evidence establishes no answer.

No status may silently become another. In particular, an issue report does not
prove universal reproduction, and absence from one repository is scoped to
what that repository owns or claims.

## Comparison rules

Strengths and weaknesses are relative to stated purpose. A missing service
control plane is not automatically a skill framework defect; a missing Fiat
receipt is not automatically a runtime-platform defect. The finished matrix
will name responsibilities and use no score, aggregate rating, or universal
winner.

Complementarity is conceptual only. This repository will not specify,
prototype, recommend, or estimate an adapter, port, migration, embedding,
shared plugin, or integration. It contains original analysis, short
identifiers, and links—not copied source or long upstream passages.

## Reproduction and update

The normal verdict is offline:

```bash
python3 scripts/check_repository.py
python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-1.json
python3 -m unittest discover -s tests
```

To update an upstream pin, change [the registry](../evidence/pins.json), review
every affected current claim and immutable permalink in the same change, and
rerun all three commands. A newer upstream `main` does not alter this edition
until that review completes.

## Authorship and rights

The human contributor remains the author and signer. Runtime or model names do
not become Git authors, pull-request bylines, or generated-by footers. The
private proprietary rights position is recorded in [LICENSE](../LICENSE).

At this scaffold stage, the source profiles and comparative synthesis remain
unwritten. The accepted [Fiat study](fiat-study.md) and
[runbook](fiat-runbook.md) define the later work.
