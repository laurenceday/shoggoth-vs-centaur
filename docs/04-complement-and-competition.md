# Complement and competition by responsibility

This analysis follows the [responsibility matrix](03-comparison-matrix.md) and
uses the status and evidence rules in the [source ledger](SOURCES.md). It keeps
vertical conceptual complement separate from the responsibilities both
repositories address.

## Conceptual complement

- [Inferred] At the responsibility level, Shoggoth governs what bounded agent
  job, evidence, and delivery is authorised. It is centred on promise
  boundaries and receipted repository change, with the limits stated in the
  [Shoggoth profile](01-shoggoth.md#purpose).
- [Inferred] Centaur operates where team sessions run, persist, receive
  capabilities, and recover. It is centred on service, execution, state,
  credential, and workflow controls, with the residuals stated in the
  [Centaur profile](02-centaur.md#purpose).
- [Inferred] The analytical relationship is vertical: one source describes
  governance of a bounded job and its delivery while the other describes the
  operated place in which team sessions execute. That responsibility-level
  adjacency follows the [two owned-state descriptions](01-shoggoth.md#architecture-and-owned-state)
  and the [Centaur service planes](02-centaur.md#architecture-and-owned-state).

These statements identify different owned responsibilities. They do not add a
deployment claim to either pinned repository.

## Competitive overlap

The overlap is confined to the six responsibilities below. Each consequence
describes what a team would have to govern under that approach; none supplies
a universal product verdict.

### Skill and instruction distribution

[Inferred] **Shoggoth consequence.** A portable router, canonical skills, and
promise boundaries make the owned job and stopping point explicit; the suite's
versions and generated contracts require maintenance. [Shoggoth evidence](01-shoggoth.md#architecture-and-owned-state)

[Inferred] **Centaur consequence.** Ordered overlays can add or shadow skills,
prompts, and personas for a deployment; precedence and pin selection remain
operator responsibilities. [Centaur evidence](02-centaur.md#current-capabilities)

[Inferred] **Shared consequence.** Both standardise instructions, but one does
so around evidence promises and the other around deployed content assembly.
[Shoggoth boundary](01-shoggoth.md#weaknesses-and-limits), [Centaur boundary](02-centaur.md#strengths)

### Workflow conventions

[Inferred] **Shoggoth consequence.** Fiat fixes a delivery sequence of study,
runbook, implementation, audit, prose, publication, and integration receipts;
it is deliberately specialised for repository change. [Shoggoth evidence](01-shoggoth.md#current-capabilities)

[Inferred] **Centaur consequence.** Durable handlers coordinate side effects,
waits, schedules, tools, and agent turns; trusted workflow code carries the
wider host boundary described by the source. [Centaur evidence](02-centaur.md#current-capabilities)

[Inferred] **Shared consequence.** Both constrain how work proceeds, but their
workflow state answers different questions: delivery authorisation versus
service execution and recovery. [Shoggoth state](01-shoggoth.md#architecture-and-owned-state), [Centaur state](02-centaur.md#architecture-and-owned-state)

### Multi-agent coordination

[Inferred] **Shoggoth consequence.** Surveyor, Mason, Warden, and Scribe have
separate authority packets, so review roles remain visible; the unfinished run
stays tied to one local worktree. [Shoggoth evidence](01-shoggoth.md#architecture-and-owned-state)

[Inferred] **Centaur consequence.** Workflow primitives dispatch child and
bounded concurrent agent turns under a principal; reported event-stream and
host-loop behaviour remains unproved here. [Centaur evidence](02-centaur.md#residual-and-open-work)

[Inferred] **Shared consequence.** Both coordinate more than one agent role or
turn. One emphasises separation of delivery authority, while the other
emphasises scheduling within a durable runtime. [Shoggoth limit](01-shoggoth.md#weaknesses-and-limits), [Centaur limit](02-centaur.md#evidence-limits)

### Extension mechanisms

[Inferred] **Shoggoth consequence.** New bounded operations join a marketplace
whose router and sibling boundaries control selection and hand-off; broad
suite governance grows with the catalogue. [Shoggoth evidence](01-shoggoth.md#architecture-and-owned-state)

[Inferred] **Centaur consequence.** Organisation overlays extend tools,
workflows, skills, personas, prompts, and sandbox files without changing the
base source; source order can shadow names. [Centaur evidence](02-centaur.md#current-capabilities)

[Inferred] **Shared consequence.** Both separate common behaviour from a single
task, but Shoggoth extends governed operations and Centaur extends deployment
content and capabilities. [Shoggoth surface](01-shoggoth.md#current-capabilities), [Centaur surface](02-centaur.md#current-capabilities)

### Audit story

[Inferred] **Shoggoth consequence.** Evidence classes, receipts, audit rounds,
and synopsis checks make the authority for a transition reviewable; their own
contracts refuse broader proof. [Shoggoth evidence](01-shoggoth.md#evidence-limits)

[Inferred] **Centaur consequence.** Persisted events, proxy logs, principals,
grants, and telemetry support operational reconstruction; the public pin has
no discovered audit-report tree and receives no audit verdict here. [Centaur evidence](02-centaur.md#evidence-limits)

[Inferred] **Shared consequence.** Both preserve records about work, but those
records answer different questions and cannot be relabelled without losing
their stated boundaries. [Shoggoth record](01-shoggoth.md#evidence-limits), [Centaur record](02-centaur.md#negative-space)

### Behavioural standardisation

[Inferred] **Shoggoth consequence.** Canonical skill contracts specify
evidence, refusal, recovery, and stopping points; semantic truth still depends
on sources and execution. [Shoggoth evidence](01-shoggoth.md#security-and-trust-boundaries)

[Inferred] **Centaur consequence.** Harness adapters, tools, workflow
primitives, principals, policies, and overlays standardise how sessions receive
and exercise capabilities; granted capability does not guarantee safe intent.
[Centaur evidence](02-centaur.md#security-and-trust-boundaries)

[Inferred] **Shared consequence.** Both reduce ad hoc agent behaviour, one by
governing the operation and the other by governing the execution environment.
[Shoggoth boundary](01-shoggoth.md#security-and-trust-boundaries), [Centaur boundary](02-centaur.md#security-and-trust-boundaries)

## No-integration boundary

This repository specifies no adapter, API or interface map, combined
architecture, dependency, migration phase, implementation steps, or embedding.
It does not claim that using the two together is recommended. Conceptual
adjacency is not an instruction to connect, port, adopt, or alter either
source. The [methodology](00-methodology.md#comparison-rules) and
[layer decision](decisions/ADR-001-layer-aware-comparison.md) hold that line.

## Evidence limits

- [Current] The analysis covers repository-owned behaviour at the exact
  [registered pins](SOURCES.md#edition-pins-and-observation-boundary).
- [Reported] Open issues remain dated, non-reproduced records in the
  [source ledger](SOURCES.md#open-and-post-pin-records); they do not enlarge the
  competitive overlap.
- [Planned] Shoggoth checkpoint proposals remain outside current capability in
  the [Shoggoth profile](01-shoggoth.md#residual-and-open-work).
- [Unknown] Runtime correctness, scale, cost, model quality, adoption, private
  overlays, and external hosts remain outside the [evidence read here](SOURCES.md#unknowns).
