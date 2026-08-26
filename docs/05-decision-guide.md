# Problem-to-layer decision guide

This guide maps a problem to the layer and evidence that can answer it. It is
not a product verdict. Read it against the exact [pin registry](../evidence/pins.json)
and the qualifications in the [source ledger](SOURCES.md).

## Is the primary problem evidence-bounded agent work and repository delivery?

**Question.** [Inferred] Does the unresolved problem concern which specialist
job is authorised, what evidence supports it, where its authority stops, or how
a repository change passes study, audit, prose, signature, and publication
gates? Those are the responsibilities described by the
[Shoggoth profile](01-shoggoth.md#purpose).

**Inspect next.** Read the [architecture and owned state](01-shoggoth.md#architecture-and-owned-state),
the [security boundary](01-shoggoth.md#security-and-trust-boundaries), and the
[Skills evidence inventory](SOURCES.md#shoggoth-skills-evidence). Confirm that
the exact skill and Fiat promises cover the proposed job, including their
refusals and recovery paths.

**Keep unknown.** [Unknown] The pin does not establish process isolation,
cluster networking, hosted credential substitution, production throughput, or
the behaviour of an external Shoggoth host. Preserve those as separate
questions under the [recorded unknowns](SOURCES.md#unknowns).

## Is the primary problem shared operated sessions, isolation, state, and credentials?

**Question.** [Inferred] Does the unresolved problem concern team ingress,
durable sessions, per-thread execution, workflow recovery, principals, granted
tools, or credential substitution and egress? Those are the responsibilities
described by the [Centaur profile](02-centaur.md#purpose).

**Inspect next.** Read the [owned service state](02-centaur.md#architecture-and-owned-state),
the [security controls and residuals](02-centaur.md#security-and-trust-boundaries),
and the [Centaur evidence inventory](SOURCES.md#centaur-evidence). Keep
default-deny pod policy and placeholder substitution beside permissive egress,
legitimate-capability misuse, and the wider workflow-host Postgres and HTTPS
boundary.

**Keep unknown.** [Unknown] The pin does not prove production recovery,
correct grants, constrained managed-mode egress, cost, uptime, or issue
reproduction. The [open-record boundary](SOURCES.md#open-and-post-pin-records)
must remain attached to those questions.

## Is the primary problem an overlap responsibility?

**Question.** [Inferred] Is the decision specifically about skill and
instruction distribution, workflow conventions, multi-agent coordination,
extension mechanisms, the audit story, or behavioural standardisation? Those
are the shared responsibilities isolated in the
[competitive-overlap analysis](04-complement-and-competition.md#competitive-overlap).

**Inspect next.** Use the corresponding row in the
[responsibility matrix](03-comparison-matrix.md#responsibility-matrix), then
read both linked profile sections. Compare the consequence of evidence-promise
governance with the consequence of operated deployment controls without
converting layer scope into product value.

**Keep unknown.** [Unknown] The pins do not supply a common workload trial,
operator study, cost model, or independent semantic evaluation. The
[methodology](00-methodology.md#comparison-rules) therefore supports no
cross-layer efficiency conclusion.

## Do both layers need separate evaluation?

**Question.** [Inferred] Does the work need both a governed answer to what an
agent job may do and a separate answer to where a team session runs and
recovers? Treat that as two responsibility questions, as set out in the
[conceptual-complement section](04-complement-and-competition.md#conceptual-complement),
not as one adoption decision.

**Inspect next.** Evaluate the [Shoggoth evidence boundary](01-shoggoth.md#evidence-limits)
and [Centaur trust boundary](02-centaur.md#security-and-trust-boundaries)
independently. Record an owner, evidence requirement, stopping point, and
unresolved risk for each layer before comparing any overlap.

**Keep unknown.** [Unknown] Conceptual adjacency proves no interoperability,
fit, dependency, or deployment result. The
[no-integration boundary](04-complement-and-competition.md#no-integration-boundary)
remains controlling.

## Does neither pin prove the answer?

**Question.** [Unknown] Is the actual question about runtime correctness,
production scale, latency, uptime, cost, model quality, adoption, private
overlays, external hosts, or universal reproduction of an issue? The
[source ledger](SOURCES.md#unknowns) says neither repository pin proves those
outcomes in this edition.

**Inspect next.** Define the missing evidence before treating either source as
an answer: a representative workload, direct deployment exercise, recovery or
security test, measured operating record, independent audit, or documented
user study. Keep that new corpus separate from the current
[read modes](SOURCES.md#read-mode-and-status-use) until it is pinned and
reviewed.

**Keep unknown.** [Unknown] Until that evidence exists, retain the question as
unresolved. Repository architecture and public issue state are not substitutes
for measurements or independent reproduction.
