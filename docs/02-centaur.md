# Centaur profile

This profile describes the surface owned by `paradigmxyz/centaur` at the
registered commit. It does not extend the claim to private overlays or a
deployment that differs from the source.

## Purpose

[Current] Centaur presents itself as a self-hosted platform for teams to run
shared agents through Slack or an API, with isolated per-thread environments,
durable state, tools, workflows, credentials, and organisational extensions.
([Centaur README](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L18-L64))

[Inferred] Its primary purpose in this comparison is to operate where team
agent sessions run, persist, receive capabilities, and recover. This describes
the source-owned service layer; it does not claim that Centaur supplies every
possible evidence-governance contract an organisation may want. ([Architecture](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L16-L41))

## Architecture and owned state

[Current] Centaur names five planes: ingress, control, execution, capabilities,
and secrets and egress. `api-rs` and Postgres own durable sessions, messages,
executions, events, sandbox assignment, workflow state, recovery, and control
telemetry; Kubernetes pods provide the active execution path. ([Five planes](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L16-L24), [durable lifecycle](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L26-L41), [execution path](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L63-L78))

[Current] Ingress services validate and render platform traffic, the control
plane serialises and persists work, per-thread sandboxes run harnesses, and
tools and workflows supply agent capabilities. Per-sandbox `iron-proxy`
instances substitute granted credentials on outbound requests. ([Component map](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L66-L96), [credential substitution](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L101-L111))

## Current capabilities

- [Current] Session messages, execution state, and output events persist in Postgres. Clients can resume the event stream with `after_event_id`, and the documented failure model reloads state after client, API, pod, workflow-worker, or proxy interruption. ([Durable lifecycle](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L26-L41), [failure model](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L113-L122))
- [Current] One Kubernetes sandbox pod is assigned per thread; harness adapters normalise Amp, Claude Code, Codex, and pi-mono inputs for that execution path. ([Execution path](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L63-L78))
- [Current] Python tool plugins become local CLI shims, while workflow handlers can checkpoint side effects, schedule work, wait, call tools, start child work, and dispatch bounded concurrent agent turns. ([Tool and workflow layer](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L80-L99), [workflow primitives](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L53-L68), [agent turns](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L115-L161))
- [Current] Workflow principals bind workflow-host permissions to an existing or derived principal, and missing principal state can fail startup. ([Workflow principals](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L163-L195))
- [Current] Ordered overlay repositories can contribute tools, workflows, skills, personas, prompts, and sandbox files without forking Centaur. Later sources shadow earlier names, and a commit SHA can pin rollout content. ([Overlay purpose](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L8-L19), [pin and visibility](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L42-L68), [skill composition](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L107-L130))

## Strengths

- [Inferred] Durable session events give clients a first-party recovery contract instead of asking each ingress to reconstruct a run from process logs. The claim is architectural; no production recovery exercise was run here. ([Durable API lifecycle](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L26-L41))
- [Inferred] Per-thread pods, a default-deny namespace policy, and paired proxies give operators explicit process, network, and credential boundaries to inspect. Their documented residuals remain in the security section below. ([Sandbox controls](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L34-L57), [namespace policy](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L1-L35))
- [Inferred] Tools, workflows, principals, and ordered overlays let a deployment extend capabilities without putting organisation-specific behaviour into the base repository. Pinning still belongs to the operator. ([Overlay contract](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L8-L68), [workflow principals](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L163-L195))

## Weaknesses and limits

- [Inferred] The shared platform brings a fleet: Kubernetes, Postgres, API and ingress services, sandbox and proxy pods, workflow hosts, Console, repo cache, images, policies, and secrets configuration. Those components are the mechanism that supplies shared operation, and they are also the operator's maintenance surface. ([Component map](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L66-L96))
- [Current] Workflow-host compatibility can allow direct database access through `ctx._pool`; the documentation says this is not a hard isolation boundary and prefers tools or narrower helpers for new workflows. ([Database boundary](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L287-L295))
- [Current] The chart also grants trusted workflow-host code direct Postgres and outbound HTTPS paths. Those paths sit outside ordinary tool calls through the paired proxy and require workflow code and grants to be treated as a wider trust boundary. ([Workflow-host network policy](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L113-L147))
- [Unknown] This study did not measure deployment effort, cost, throughput, uptime, user count, or adoption. Fleet size alone supplies no performance or value conclusion.

## Security and trust boundaries

[Current] Each thread receives a restricted Kubernetes pod, and the chart starts
with namespace-wide default-deny ingress and egress. The same security document
says an agent can read and write its own sandbox, run shell commands, and use
any tool allowed by its token; containment is at the sandbox boundary, and
legitimate capabilities can still be misused. ([Sandbox and network controls](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L34-L57), [declared limits](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L132-L158), [default-deny policy](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L1-L35))

[Current] Credential declarations use placeholders and bind substitution to
granted principals, hosts, and request locations, so raw values need not enter
the sandbox. The source also makes egress permissive by default: unmanaged
configuration uses `domains: ["*"]`, and managed proxies obtain their complete
configuration from the control plane rather than that local file. ([Credential properties](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L76-L121), [local default](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/iron-proxy/iron-proxy.yaml#L21-L25), [managed ownership](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/api-rs/crates/centaur-sandbox-agent-k8s/src/iron_proxy.rs#L197-L207))

[Reported] [Issue #1385](https://github.com/paradigmxyz/centaur/issues/1385)
was open when observed on 2026-08-26. It reports that the security page's local
hostname-allowlist edit is not delivered to managed Kubernetes proxies. At the
pin, Console assembles credential transforms without a general allowlist
transform. This study verified that configuration split in source but did not
independently reproduce a deployed bypass. ([Console transform assembly](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/console/app/models/principal_sync_config_snapshot.rb#L398-L407))

[Current] Workflow-host sandboxes can receive direct Postgres access and direct
outbound HTTPS. The workflow guide says `ctx._pool` is not a hard isolation
boundary, so trusted workflow code occupies a wider boundary than an ordinary
agent tool call through its paired proxy. ([Workflow-host network policy](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L113-L147), [database boundary](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L287-L295))

[Inferred] These controls reduce credential exposure and direct pod reach; they
do not establish safe agent intent, correct grants, or constrained managed-mode
egress. The security page itself leaves fully privileged host or cluster
attackers outside scope. ([Security scope](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L14-L32), [declared limits](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L132-L158))

## Operating burden

[Current] A supported deployment uses Kubernetes sandboxes, Helm policy and
configuration, Postgres, `api-rs`, ingress services, runtime images, proxy and
Console credential control, and repo-cache-backed extensions. Operators must
maintain principals, grants, default roles, capabilities, overlay refs, images,
policies, and durable-state recovery. ([Execution path](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L63-L78), [credential operator duties](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L132-L146), [overlay operation](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L42-L105))

[Unknown] No cluster was installed or operated for this study, so setup effort,
routine toil, incident load, and production recovery behaviour remain unknown.

## Residual and open work

- [Reported] [Issue #1475](https://github.com/paradigmxyz/centaur/issues/1475) was open when observed on 2026-08-26. It reports that workflow agent-turn event-stream opening can hang and that the Python-host RPC loop processes requests sequentially. The source shows an awaited per-request loop and event-stream open, but this study did not independently reproduce the reported startup race or starvation. ([Request loop](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/api-rs/crates/centaur-workflows/src/lib.rs#L2967-L3026), [event stream](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/api-rs/crates/centaur-workflows/src/lib.rs#L4258-L4329))
- [Reported] [Issue #1111](https://github.com/paradigmxyz/centaur/issues/1111) was open when observed on 2026-08-26 and reports missing usage records for workflow-tier agent turns. This study did not independently reproduce the report.
- [Reported] [Issue #1454](https://github.com/paradigmxyz/centaur/issues/1454) was open when observed on 2026-08-26 and reports that an OOM-killed sandbox can retain a generic `Created` status instead of the later Kubernetes cause. This study did not independently reproduce the report.
- [Reported] [Issue #1499](https://github.com/paradigmxyz/centaur/issues/1499) was filed after the registered source commit and was open when observed on 2026-08-26. It reports no sandbox `serviceAccountName` setting for cloud workload identity. It is post-pin context, not a property established by the pinned tree, and was not independently reproduced.

## Negative space

[Inferred] A source-wide bounded search at the pin returned no match for the
named `promise-machine`, `hexctl`, `hexaemeron`, `protasis`, Fiat-version,
`risk-register`, or hash-chained-receipt contracts. Centaur therefore does not
implement those named Shoggoth contracts in this repository. This is not an
automatic platform defect and does not rule out a private overlay or external
policy layer. ([Owned architecture](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L16-L24))

[Current] Centaur does have a different audit record: persisted messages,
executions and events, proxy request logs, principals, grants, and service
telemetry. The absence above must not be shortened to “no auditability.” These
records support operational reconstruction; the source does not claim they are
Fiat receipts or Promise Machine evidence. ([Audit trail](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L123-L130), [durable lifecycle](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L26-L41))

## Evidence limits

[Current] `SECURITY.md` is a reporting route, and a bounded repository search at
the pin found no audit report or audit-synopsis tree. That is an evidence
absence, not evidence that Centaur or a deployment has never been audited. This
profile therefore relies on pinned documentation and implementation plus
clearly labelled public issue and pull-request records. ([Security reporting file](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/SECURITY.md))

[Reported] Pull requests [#1394](https://github.com/paradigmxyz/centaur/pull/1394),
[#1439](https://github.com/paradigmxyz/centaur/pull/1439),
[#1450](https://github.com/paradigmxyz/centaur/pull/1450), and
[#1479](https://github.com/paradigmxyz/centaur/pull/1479) record capability,
principal, tool-catalogue, and scheduling changes included before the pin. They
are change records, not a fresh security assessment.

[Unknown] No Centaur service, workflow, sandbox, credential path, or recovery
path was executed here. Production correctness, scale, latency, cost, model
quality, private overlay behaviour, and independent issue reproduction remain
unknown.

[Planned] No Centaur roadmap item is promoted into the current inventory. Open
issue suggestions remain reported work unless a later pinned source edition
ships them.
