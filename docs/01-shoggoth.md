# Shoggoth profile

This profile describes the surface owned by `wildcat-finance/skills` at the
registered commit. It does not extend the claim to a model host, the external
Shoggoth Interceptor, or any private deployment.

## Purpose

[Current] Shoggoth is the Wildcat Labs agent-and-skill collective: narrow
members own named jobs, state what their evidence supports, and stop at sibling
boundaries. The pinned distribution contains 14 plugins, 23 first-party skills,
four Fiat workers, a portable router, and five unchanged vendored security
skills. Its stated work includes evidence handling, protocol and credit tasks,
prose shaping, and receipted repository delivery. ([Skills README](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L5-L17))

[Inferred] Its primary purpose in this comparison is to decide what bounded
agent operation is authorised by available evidence and, through Fiat, carry
repository work through a reviewable delivery sequence. That reading joins the
collective definition to the stated delivery composition; it does not turn
Shoggoth into a general runtime platform. ([Collective definition](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L5-L17), [delivery composition](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L245-L254))

## Architecture and owned state

[Current] The suite has a portable router, one canonical skill for each owned
operation, fourteen plugin packages, and explicit hand-offs between domain and
phase skills. The router chooses a canonical surface but establishes no domain
result itself. ([Router contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/.agents/skills/promise-machine/SKILL.md#L6-L24), [Promise Machine scope](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L26-L35))

[Current] The Promise Machine is the common evidence law. It gives each promise
a stable identity, evidence, boundary, authorised transition, refusal, and
recovery. Evidence can be narrowed or supplemented in a hand-off; it cannot be
silently strengthened. ([Governing principle](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L15-L24), [composition](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L110-L135))

[Current] Fiat owns delivery state in a dedicated run worktree. Its controller
emits the next directive from durable state and advances through study,
runbook, implementation, audit, prose, push, and integration receipts. Mason,
Surveyor, Warden, and Scribe receive bounded packets and cannot advance the
controller. ([Fiat state boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L43-L50), [worktree contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L77-L107), [worker authority](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L174-L194))

## Current capabilities

- [Current] Domain skills preserve or transform bounded evidence, reconstruct credit records, capture chain state, evaluate grounded agents, check protocol boundaries, and measure one Solidity gas change at a time. Each listed skill also states where it stops. ([Domain inventory](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L129-L172))
- [Current] Phase skills govern study and runbook completeness, off-chain controls, observability, performance changes, failure reduction, durable decisions, and prose. ([Phase inventory](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L196-L225))
- [Current] Fiat creates stacked step branches, requires per-step audit and prose work, and carries signed commits through an integration path. ([Stacked delivery](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L276-L300))
- [Current] The run-observation contract can validate a bounded JSONL record and can bind an accepted prefix to one Fiat receipt. Its own boundary says this does not prove capture completeness, event truth, or general delivery evidence. ([Validation promise](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L195-L219), [receipt-binding boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L130-L135))

## Strengths

- [Inferred] Claim boundaries are inspectable because the same contract names what a check establishes, what it leaves open, and which transition stops on insufficient evidence. The strength is traceability of the claim, not automatic truth. ([Evidence classes](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L51-L68), [refusal and recovery](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L137-L145))
- [Inferred] Repository delivery is broken into roles and durable gates, reducing reliance on a single chat transcript or an agent's memory. The controller still depends on the configured host, signer, and GitHub environment. ([Durable directive rule](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L43-L50), [dedicated worktree](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L77-L107))
- [Inferred] The source-review surface is directly inspectable as contracts, skills, scripts, tests, and records. This states its repository shape and makes no speed, cost, or adoption measurement. ([Repository purpose and inventory](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L99-L127))

## Weaknesses and limits

- [Current] Promise checks prove only their named relation. The root contract expressly refuses to turn a passing check into proof of general skill correctness, input truth, or a neighbouring claim. ([Promise boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L15-L24))
- [Current] A live Fiat run stays in one local worktree, and current contributor guidance says not to move an unfinished run between machines. That limits portable multi-contributor continuation today. ([Contributor warning](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L44-L56))
- [Inferred] The broad governed surface creates maintenance work across skill versions, generated Promise Machine copies, package manifests, evidence coverage, workers, and vendored boundaries. The portable router narrows selection; it does not remove that suite-wide upkeep. ([Collective topology](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L99-L113), [installation copies](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L235-L245))
- [Current] Some legacy Hexaemeron audit rounds predate the modern audit fields. The verified synopsis preserves `Audit schema`, `Covered`, `Not checked`, and `Elenchus verdict` as missing rather than reconstructing them. ([Hexaemeron audit synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/audit/AUDIT_SYNOPSIS.md))

## Security and trust boundaries

[Current] The Promise Machine fails closed on missing, stale, malformed, or
mismatched evidence for the dependent transition while leaving inspection,
repair, rerun, rollback, and safe exit available. This control limits what a
result may authorise; it does not make source data true or an agent's conclusion
semantically correct. ([Refusal and recovery](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L137-L145), [conformance boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L165-L177))

[Current] Fiat binds work to a dedicated local worktree, hash-linked controller
state, bounded worker authority, signed commits, and GitHub receipts. Those
controls govern delivery provenance. The repository does not claim that they
isolate agent processes, hold third-party credentials outside a sandbox, or
enforce a cluster network boundary. ([Fiat worktree](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L77-L107), [receipted-delivery contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L643-L652), [worker authority](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L174-L194))

## Operating burden

[Inferred] An operator needs a compatible agent host, the selected skill
package, a Git checkout, the target's own toolchain, and signing and GitHub
identity when Fiat publishes. The skills repository does not ask that operator
to run its own Postgres or Kubernetes service merely to invoke a skill. This is
a statement about the repository-owned surface, not every possible host.
([Contributor path](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L44-L79), [requirements](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L259-L270))

[Unknown] This study did not measure contributor time, maintenance cost,
production throughput, or failure rate. No operating-efficiency conclusion is
authorised.

## Residual and open work

- [Reported] [Issue #508](https://github.com/wildcat-finance/skills/issues/508) was open when observed on 2026-08-26. It reports remaining audit-carryover, delegated-write, and executable runbook-gate work. This study did not independently reproduce each gap.
- [Planned] [Issue #558](https://github.com/wildcat-finance/skills/issues/558) was open when observed on 2026-08-26. It proposes a programme for portable receipted transitions and expressly separates any service repository into a separately authorised decision. The programme is not current capability.
- [Planned] [Issue #560](https://github.com/wildcat-finance/skills/issues/560) was open when observed on 2026-08-26. It proposes immutable base and checkpoint identity after predecessor decisions. The checkpoint contract is not shipped at this pin.

## Negative space

[Inferred] A source-wide bounded search at the pin found no first-party
`services/` control-plane tree and found service terms only in checkpoint
proposals and studies, audit or evaluation specimens, or generic boundary
guidance. The Skills repository therefore does not own or
claim a shared multi-user session service, Postgres event store, Kubernetes
sandbox scheduler, central principal service, or credential-injecting egress
proxy. This is scoped repository negative evidence, not a claim that an external
Shoggoth host could never provide those layers. ([Repository tree and owned surface](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L99-L127))

[Inferred] Those absences are not automatic defects. They keep this repository
focused on governed agent operations and delivery, while leaving service
operation and process isolation to the host or target environment. ([Skill boundaries](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L129-L172))

## Evidence limits

[Current] Before using audit summaries, the study ran the repository's
whole-set audit-synopsis currency check and received zero exit. The three views
used here are the [Hexaemeron plugin synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/audit/AUDIT_SYNOPSIS.md), the [Fiat #608 synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/audit/rounds/fiat-608-bind-the-integrate-gate-to-the-sync-receipt.synopsis.md), and the [Fiat #510 synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/audit/rounds/fiat-510-reuse-source-bound-x-ray-analysis-across-fia.synopsis.md). Currency means each synopsis matched its source rendering; it does not mean every domain skill was semantically audited or that the whole collective is secure.

[Reported] Pull requests [#539](https://github.com/wildcat-finance/skills/pull/539)
and [#579](https://github.com/wildcat-finance/skills/pull/579) record bounded
run-observation capture and later receipt binding. Their own limits remain in
the current Promise Machine contract; this profile does not promote those
records into proof of complete run capture.

[Unknown] Neither the collective nor its hosts were run in this study. Runtime
correctness, production scale, model quality, the semantic correctness of every
domain skill, and private Interceptor behaviour remain unknown.
