# Study: Shoggoth and Centaur, at the layers they actually occupy

Assuming, unless corrected:

1. “Shoggoth” means the Wildcat Labs agent-and-skill collective distributed by `wildcat-finance/skills`, including the Promise Machine and Hexaemeron/Fiat. It does not mean a foundation model, the host application, or Paradigm's Centaur.
2. “Centaur” means `paradigmxyz/centaur`, the self-hosted team agent platform. It does not mean a model family or another project with the same name.
3. The comparison is reconnaissance for engineers and technical decision-makers. It is not a procurement score, a winner selection, or a claim that the two projects are interchangeable.
4. Complementarity is a responsibility-level observation only. The deliverable will not specify, prototype, recommend, or estimate an adapter, port, migration, embedding, shared plugin, or integration.
5. Source claims are frozen to the two assigned commits. Later changes are outside this edition until the evidence registry and affected prose are reviewed together.
6. A capability documented and implemented at the pin may be described as current. A proposal, open issue, or planned programme must remain labelled as such. An issue report is evidence that a report is open, not independent proof that every deployment reproduces it.
7. The target remains private. It will contain original analysis, short identifiers, and links; it will not copy either project's code or long passages of its prose.
8. The target begins at signed commit `db38e431561d473d2ee85a1bf4dfe8e94d135c13` on `main`. There are no target product files, merged pull requests, or audit records before this run.
9. Python 3 and its standard library are available. No package dependency, build system, hosted database, JavaScript toolchain, Kubernetes cluster, or running instance of either project is needed for the documentary prototype.
10. The human contributor remains the author and signer. Host or model names do not become Git authors, co-authors, pull-request bylines, or generated-by footers.

These readings follow the user's explicit boundary and the pinned source. No open ambiguity changes the chosen design.

## 1. Problem statement, user, working-prototype meaning, and proving demo path

The target will be a private, source-bound comparison repository. Its job is to explain what Shoggoth and Centaur are for, what each currently does, where each is strong, where each stops or has known residue, where their responsibilities overlap, and where the two responsibilities could sit beside one another without proposing that either project absorb the other.

The primary reader is an engineer deciding which kind of system a problem calls for. A second reader is a technical operator who needs to know which claims came from current source, which came from an open issue, and which are deductions from the difference in layer. The repository must let either reader challenge a sentence without cloning either source.

The comparison starts with this responsibility split:

| Subject | Primary layer | Unit of work | State it owns |
| --- | --- | --- | --- |
| Shoggoth | Governed specialist instructions and repository delivery | One bounded skill operation or one receipted delivery step | Evidence contracts, study/runbook artefacts, controller state, audit records, Git branches and pull requests |
| Centaur | Shared agent service and execution control | One durable session, execution, tool call, or workflow run | Postgres session/workflow state, sandbox assignment, event streams, principals, proxy configuration and delivery state |

That split is a starting proposition, not a verdict. The product documents must test it against source and retain the overlaps: both distribute skills, standardise agent behaviour, coordinate more than one agent turn, expose tools, and preserve records about work.

A working prototype contains:

- `README.md`, with a concise conclusion and a complete navigation path;
- `docs/00-methodology.md`, defining source status, comparison method, exclusions, and update procedure;
- `docs/01-shoggoth.md` and `docs/02-centaur.md`, each covering purpose, architecture, capabilities, strengths, weaknesses, current residue, and explicit negative space;
- `docs/03-comparison-matrix.md`, comparing the same named axes without scores, ranks, or a winner column;
- `docs/04-complement-and-competition.md`, separating conceptual complement from direct competitive overlap and repeating the no-integration boundary;
- `docs/05-decision-guide.md`, phrased as problem-to-layer questions rather than a recommendation for one project;
- `docs/SOURCES.md`, with pinned permalinks, pull requests, issues, audit read modes, observations, and unknowns;
- `docs/fiat-study.md` and `docs/fiat-runbook.md`, committed copies of the accepted planning record;
- `docs/decisions/ADR-001-layer-aware-comparison.md`, recording why a layer-aware comparison replaced a flat feature contest;
- `evidence/pins.json`, the machine-readable source registry;
- `scripts/check_repository.py`, `scripts/run_tests.py`, and `tests/`, using only the Python standard library; and
- `.github/workflows/verify.yml`, a read-only first-edition CI stub that runs the same standard-library checker and tests without secrets; and
- a proprietary `LICENSE` or rights notice, because privacy is not permission to republish and the user has not licensed this new analysis for redistribution.

The local proof path is:

```bash
python3 scripts/check_repository.py
python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur.json
python3 -m unittest discover -s tests
```

The publication proof path is:

```bash
gh repo view laurenceday/shoggoth-vs-centaur --json nameWithOwner,visibility,defaultBranchRef
git log --show-signature --format=fuller main --max-count=20
```

The prototype is successful only when all of these criteria hold:

1. The three local commands exit zero; the structured runner reports `elenchus.unittest.v1`, `complete: true`, no failure, and no error.
2. `evidence/pins.json` names exactly `wildcat-finance/skills@58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff` and `paradigmxyz/centaur@36397534096bb89c065a52a9fcfebed34b995a00`, and every source-code link used to support a current claim contains the matching full commit.
3. Each system document has purpose, current capabilities, strengths, weaknesses or limits, trust/security boundaries, operational cost, and negative space. Each weakness is relative to the system's stated purpose rather than a generic absence list.
4. The matrix covers at least: intended user, deployment shape, unit of isolation, state and recovery, skill/instruction model, tools, workflows, multi-agent work, credentials, evidence/audit, release/delivery, extension model, and operating burden.
5. Current behavior, source-backed inference, planned work, issue-reported residue, and unknowns are visibly distinguishable.
6. Complement and competition are separate sections. Neither contains implementation steps, API mappings, adapter files, migration phases, copied source, or a claim that combining the projects is the recommended result.
7. No score, league table, single “better” verdict, fabricated benchmark, or adoption claim appears.
8. The repository contains no secret, credential-shaped value, absolute local path, long source quotation, or host/model authorship footer.
9. GitHub reports `PRIVATE`, `laurenceday/shoggoth-vs-centaur`, and default branch `main`; every delivery commit is locally signature-valid and GitHub verification is checked by Fiat before its receipt.

The proving demo is a fresh clone of the private target, the three local commands above, a read from `README.md` through the two system profiles and matrix to the source ledger, and the two publication checks. It does not start either source system.

## 2. Prior art in the repository, organisation, and outside both

### Target repository

The target has one signed, empty bootstrap commit and no earlier product pull request, audit record, study, runbook, or implementation. There are therefore no target findings or unfinished target changes to carry forward. The repository is a clean documentary start, not a revision of an earlier comparison.

### Shoggoth and Wildcat Labs source

The pinned Skills README defines Shoggoth as a collective rather than a single general assistant, lists 14 plugins, 23 first-party skills and four Fiat workers, and separates bounded domain jobs from the receipted delivery loop. The Promise Machine supplies the cross-skill evidence law. Fiat supplies the explicit delivery controller, durable state, per-step audit/prose/push loop and signed integration path.

The last two merged Skills pull requests at the pin were read:

- [#648, “Bind Fiat integration to the sync receipt's recorded base head”](https://github.com/wildcat-finance/skills/pull/648), merged as `57accf1b219df1fafcfa460a8978d8e8586cf64d`, repaired a reader/writer receipt-key mismatch and carried two frozen-study prose/path inconsistencies forward rather than rewriting receipted bytes.
- [#649, “Reuse source-bound X-Ray preparation across Fiat audits”](https://github.com/wildcat-finance/skills/pull/649), merged as the assigned Skills pin, added bounded reuse while keeping global analysis and outputs fresh. Its own evidence explicitly does not prove model truth, semantic correctness, production speed, hostile-local-writer safety, or host installation.

Two earlier merged observation deliveries were also read because they define how much of a run record exists:

- [#539](https://github.com/wildcat-finance/skills/pull/539) shipped bounded pre-persistence run-observation capture and expressly left receipt binding and handover to successors.
- [#579](https://github.com/wildcat-finance/skills/pull/579) bound an accepted observation prefix to one Fiat receipt while leaving exhausted-audit carryover, delegated-write and runbook-gate work in #508.

Those records stop an easy overclaim: Shoggoth has a run-observation schema and optional receipt binding; it does not claim that every run is automatically, completely, or externally truthfully observed.

The Skills audit synopsis set was checked before any synopsis was used:

```bash
python3 plugins/hexaemeron/skills/fiat/scripts/audit_synopsis.py --check .
```

It exited zero at the assigned pin: every committed synopsis matched the current rendering of its named source. The directly relevant read views were:

- `plugins/hexaemeron/audit/AUDIT_SYNOPSIS.md`: F-01 through F-09 are fixed. F-10 accepts two fail-open hook escape hatches while retaining the workflow's explicit lint. Legacy `Audit schema`, `Covered`, `Not checked`, and `Elenchus verdict` fields are absent and remain unknown. The record also leaves cross-filesystem atomic replacement, concurrent controller calls, and ANSI in machine-facing JSON outside its rounds; the vendored Solidity suite was not applied to this Python plugin.
- `audit/rounds/fiat-608-bind-the-integrate-gate-to-the-sync-receipt.synopsis.md`: no product finding is open. Its first legacy round lacks the four modern audit fields and carries a Brevitas signal plus a frozen study/runbook path disagreement. Later rounds record the risk ids they covered, explicit Solidity waivers, null Elenchus verdicts, and the integration composition condition later resolved by the merged pull request.
- `audit/rounds/fiat-510-reuse-source-bound-x-ray-analysis-across-fia.synopsis.md`: findings in each fixing round are marked fixed or guarded, and final rounds have no finding. Persistent negative space remains: model-produced facts and final conclusions were not semantically proved, a hostile local writer can race selected filesystem state, fixed-order fixture timings support no production speed claim, and repository propagation is not proof of host activation.

The root audit log and plugin audit logs for Alexandria, Ariadne, Pandects, Probitas and Tabularium were discovered and their synopsis currency was checked. Their domain findings are not used to claim correctness of the collective and are outside this architecture comparison. The product must say that the capability inventory comes from canonical contracts, not that every capability received a fresh audit here.

Three open Skills issues are material negative space, not work for this target:

- [#508](https://github.com/wildcat-finance/skills/issues/508) is open and currently asks for the original lanes to be narrowed to residual audit-carryover, delegated-write and executable-command gaps.
- [#558](https://github.com/wildcat-finance/skills/issues/558) keeps portable contributor checkpoints as a programme, not an immediate build, and says a service repository requires separate authority.
- [#560](https://github.com/wildcat-finance/skills/issues/560) keeps immutable checkpoint identity blocked on predecessor decisions and current boundaries.

This comparison carries those facts as limits on cross-machine and multi-contributor portability. It does not turn their proposed checkpoint service into current Shoggoth capability.

### Centaur source

Centaur's current README describes a self-hosted team platform: Slack/API ingress, per-thread Kubernetes sandboxes, selectable harnesses, shared tools, durable workflows, credential boundaries, replayable state and organisation overlays. Its architecture page divides the system into ingress, control, execution, capability, and secrets/egress planes.

The two most recent merged Centaur pull requests at the pin were read:

- [#1497](https://github.com/paradigmxyz/centaur/pull/1497), merged as `3f4ce07095681033dd8245a418044ecc5c600f3c`, routes transient Google Docs network failures through an existing five-attempt retry policy. Its pull-request record says Rails tests were not run because Ruby and Docker were unavailable in that sandbox.
- [#1498](https://github.com/paradigmxyz/centaur/pull/1498), merged as the assigned Centaur pin, extends the Google Docs fetch read timeout from 5 seconds to 60 seconds and adds regression coverage.

These are current operations evidence for one Console sync lane, not proof of the core sandbox or workflow architecture. The following merged changes were read for the comparison axes they actually change:

- [#1394](https://github.com/paradigmxyz/centaur/pull/1394) added per-principal session-read, workflow-read and workflow-write capabilities to sandbox API JWTs and narrowed API NetworkPolicy ingress to proxy pods.
- [#1439](https://github.com/paradigmxyz/centaur/pull/1439) let workflows resolve existing principals by foreign id or `prn_` OID.
- [#1450](https://github.com/paradigmxyz/centaur/pull/1450) made the MCP tool catalogue obey the same allow/block lists as sandbox tool installation, removing tools that could only fail at call time.
- [#1479](https://github.com/paradigmxyz/centaur/pull/1479) guarded scheduled runs from recursively creating schedules when executable prompts contain cadence language.

`SECURITY.md` contains a reporting address, not an audit report. No repository audit or audit-synopsis tree was found at the Centaur pin. That is an evidence absence, not a claim that nobody has ever audited a deployment. The current security model and implementation were therefore read directly, together with current open reports:

- [#1385](https://github.com/paradigmxyz/centaur/issues/1385) reports that the documented hostname egress allowlist is not delivered to managed Kubernetes proxies. Current source corroborates the configuration split: the local YAML defaults to `domains: ["*"]`, managed proxies render no local config, and Console transform assembly emits credential transforms but no generic allowlist transform.
- [#1475](https://github.com/paradigmxyz/centaur/issues/1475) reports a workflow agent-turn event-stream-open hang and a sequential Python-host RPC loop that can starve sibling turns and the result message. The current Rust loop still awaits each `ctx.*` request inline, and `run_agent_session_turn` awaits stream creation without a surrounding timeout at that call site. The reported startup-race cause was not reproduced in this study.
- [#1111](https://github.com/paradigmxyz/centaur/issues/1111) reports no usage records for workflow-tier agent turns. This study did not run a workflow to reproduce it.
- [#1454](https://github.com/paradigmxyz/centaur/issues/1454) reports that an OOM-killed sandbox can persist a generic `Created` status instead of the later Kubernetes cause. This study did not reproduce the failure.
- [#1499](https://github.com/paradigmxyz/centaur/issues/1499) reports no sandbox `serviceAccountName` setting for cloud workload identity. It was filed after the assigned source pin and is labelled post-pin context, not a property established by the pin.

### Outside both repositories

The product uses ordinary Markdown, JSON, Git commit identities, immutable GitHub blob permalinks, Python 3 `unittest`, and the `networking.k8s.io/v1` NetworkPolicy identifier already present in Centaur. These are reference and verification mechanisms, not a third framework added to either subject. No market survey, popularity statistic, model benchmark, vendor pricing, or deployment benchmark enters the first edition because none is needed to answer the user's question and each would introduce another time-varying evidence set.

## 3. Constraints and non-goals, including the exact starting ref and toolchain

### Exact refs and affected versions

- Target start: `laurenceday/shoggoth-vs-centaur@db38e431561d473d2ee85a1bf4dfe8e94d135c13`, branch `main`.
- Shoggoth source: `wildcat-finance/skills@58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff`; its manifests record Hexaemeron `1.6.5`, and the canonical Fiat skill records `5.28.1`.
- Centaur source: `paradigmxyz/centaur@36397534096bb89c065a52a9fcfebed34b995a00`, described locally as `centaur-0.1.126-3-g36397534`.
- Controller for this run: Fiat `5.28.1` from Hexaemeron `1.6.5`. Its active Fiat skill, evolution ledger, controller script and two plugin manifests were byte-matched to the pinned Skills source before the run. Registry currency was unavailable and remains a recorded controller warning, not a claim of registry verification.

Both local source heads matched `git ls-remote origin refs/heads/main` during the study. That proves the assigned pins were the live remote tips at that observation time; it does not make `main` immutable.

### Toolchain

The product toolchain is Markdown, JSON, Git, GitHub CLI for publication checks, Python 3 standard library, `unittest`, and one read-only GitHub Actions verification stub. The workflow is authorised for this first edition only: it checks out the target and runs the same standard-library commands without a package install, secret, write permission, source-repository checkout, or network-dependent test. The checker must not install or import either source project. It must not require network access for its normal local verdict. It may validate URL shape and full commit pins without fetching them.

### Constraints

- The repository stays private and is published only to `laurenceday/shoggoth-vs-centaur`.
- All substantive work follows the current Fiat controller and its phase receipts.
- Commits and pull requests retain the human contributor's name, email, signature and GitHub account. Fiat's provenance can supplement that identity; a runtime host cannot replace it.
- Current claims use pinned source permalinks. Pull requests and issues use their durable GitHub URLs and state observed on 2026-08-26.
- A source document may describe an intention more strongly than current code supplies. The product must prefer the narrower intersection of documentation, implementation, test/PR evidence, and known residue.
- Strength and weakness are relational: a missing Kubernetes control plane is not a Shoggoth defect when Shoggoth does not claim to operate one; Centaur's lack of Fiat receipts is not a runtime failure when Centaur does not claim that evidence contract.
- Original prose should be concise enough to navigate but complete enough to preserve caveats. Tables may compress repeated axes; they may not compress away status or scope.

### Non-goals

- No adapter, plugin port, workflow port, shared schema, API map, proof of concept, integration backlog, migration, acquisition recommendation, or merged architecture.
- No copied implementation, vendored source, lifted prompt, rephrased manual, or long quotation.
- No deployment, penetration test, security audit, load test, model evaluation, cost model, adoption survey, or feature benchmark of either project.
- No claim about Paradigm's internal deployment, Wildcat's uncommitted roadmap, the separate Shoggoth Interceptor repository, or a host platform's capabilities beyond the pinned Skills distribution.
- No claim that a current open issue reproduces universally. Current-source corroboration and issue-reporter observation remain distinct.
- No release automation, website, rendered dashboard, database, generated diagrams, or hosted link checker in the first edition.
- No edit to either source repository and no issue or comment filed there.

### Fixed action boundaries

**Always:** run the repository checker and unit suite before each commit; run Imprimatur on every shipped Markdown file; keep current claims on full-commit permalinks; preserve status labels and unknowns; verify signatures locally before first push; verify GitHub commit status before each Fiat receipt.

**Ask first:** add a package dependency; expand or change CI beyond the authorised read-only standard-library workflow; change the licence; change the source pins; add an external evidence corpus; alter the layer model or comparison axes after the study; widen from analysis to integration; publish the private repository or any extract somewhere else.

**Never:** commit a credential, private key, token, absolute local path or host byline; edit the read-only source clones; execute source-repository setup commands; call an issue report a proved universal defect; turn proposed Skills checkpoint work into current capability; hide a Centaur security caveat; delete a failing test to obtain green output; claim a command ran when it did not; copy source code or design an integration.

## 4. Designs, their trades, and the chosen construction

### Option A: one long README

Put the full comparison, matrix and source notes in one file.

Trade: the shortest file tree and easiest first click, but changes to one claim create a large review surface, source qualifications drift away from their rows, and readers cannot enter through one system without scanning the other. It also encourages a flat feature contest because purpose, layer, implementation status and source inventory compete for one outline.

### Option B: modular, source-bound documentary repository

Keep a short README, two symmetric system profiles, one matrix, one complement/competition analysis, one decision guide, one source ledger, a small evidence registry, the Fiat planning record, and standard-library checks.

Trade: more files and internal links, but each claim has a stable home, the two systems receive the same questions, and status/pin rules can be tested. The file boundaries match how a reader challenges the work: method, one subject, cross-subject axis, implication, or evidence.

### Option C: JSON-first catalogue with generated Markdown

Represent every capability, strength, weakness and source in a schema, then render every document.

Trade: it could make status and source coverage exhaustive, but the generator and schema would become a second product. Natural-language conclusions, qualifications and responsibility boundaries do not reduce cleanly to fields. Review would spend time on generation mechanics instead of the comparison.

### Option D: a visual scorecard

Render features as marks, traffic lights, or numerical ratings.

Trade: rapid scanning at the cost of the main fact. The systems act at different layers, so a score converts purpose into an unexplained weighting. It would also breach the user's request to work out complement and competition rather than manufacture a winner.

### Choice

Choose Option B. It is the cheapest construction to comprehend that still keeps claims source-bound and exposes the layer mismatch. Option A is cheaper to build but not to audit. Option C adds machinery without increasing the truth of the source. Option D is rejected because it would encode a ranking the evidence cannot support.

The product's analysis must reach these bounded conclusions unless later evidence falsifies them:

#### Shoggoth: purpose and present strengths

- Purpose: compose narrow specialist skills and phase agents under an evidence law, then carry authorised repository work through a receipted delivery.
- Strength: the Promise Machine names what a check establishes and what it does not, controls evidence handoffs, and fails only the dependent transition when evidence is missing.
- Strength: Fiat separates study, runbook, implementation, audit, prose, push and integration; delegates bounded packets to workers; keeps one run in a dedicated worktree; and binds progress to durable controller state rather than chat memory.
- Strength: the suite has explicit domain boundaries. Its credit, chain-state, hook, gas, evidence, prose and delivery skills refuse adjacent jobs rather than presenting one agent as expert at everything.
- Strength: source review is cheap to reproduce. The distribution is mostly instruction, Python, schemas, tests and documentary contracts rather than a running service fleet.

#### Shoggoth: present weaknesses and limits

- The Skills repository does not own a shared multi-user service plane, durable session database, Kubernetes sandbox scheduler, central principal service, or credential-injecting egress proxy. That makes it light to apply to a repository but leaves those operational concerns to its host and target environment.
- Fiat's durable state is local to one run worktree. Current guidance warns against moving an unfinished run between machines; portable multi-contributor checkpoints remain an open programme (#558/#560).
- Receipt and observation machinery can prove named structural relations, not the semantic truth or completeness of an agent's conclusions. The Promise Machine says so explicitly, and recent X-Ray reuse work retains that limit.
- The governed surface is broad: 14 plugins, 23 first-party skills, phase disciplines, workers and vendored security skills. The portable router narrows selection, but maintainers still bear version, copy, evidence-coverage and boundary discipline across that suite.
- Historical audit records lack fields now required by the modern schema. Verified synopses preserve those fields as unknown rather than filling them in after the fact.

#### Centaur: purpose and present strengths

- Purpose: give a team shared agents through chat or API, with durable session state and real execution environments rather than isolated local agent setups.
- Strength: Postgres-backed messages, executions and events give clients a replay cursor and let service or client restarts recover state without reconstructing it from logs.
- Strength: per-thread Kubernetes sandboxes separate workspaces and processes; default-deny namespace policy limits direct pod reach; per-sandbox proxies keep raw third-party credentials out of agent environments.
- Strength: tools, workflows, skills, prompts and personas have deployment extension surfaces. Ordered overlays let an organisation add or shadow behaviour without forking the base repository, and pinned commits are supported for reproducible rollout.
- Strength: the workflow runtime supplies checkpoints, schedules, events, child work and bounded concurrent agent turns. Principals and route capabilities can scope what workflow hosts and agent turns may use.
- Strength: platform ingress, execution, capability and delivery responsibilities are explicit in the tree, which gives operators concrete state and logs to inspect.

#### Centaur: present weaknesses and limits

- The platform carries a substantial operating surface: Kubernetes, Postgres, Console, API, ingress services, sandbox images, repo cache, workflow hosts, per-sandbox proxy control and their network policies. A team gains shared operation by accepting that fleet.
- The security boundary contains rather than makes agents correct. Current security prose says agents can misuse legitimate capabilities and the containment boundary is outside the sandbox process, not inside its shell.
- Egress is permissive by default. More sharply, open #1385 and current source show that the documented local allowlist edit is not the configuration path used by managed Kubernetes proxies. The product must present this as a current documentation/managed-mode gap, not imply that credential host binding is absent; those are separate controls.
- Workflow-host sandboxes may receive direct database access and direct HTTPS, and the workflow documentation calls the database route not a hard isolation boundary. Trusted workflow code therefore has a wider boundary than an ordinary agent tool call through its paired proxy.
- Open reports identify workflow wait/liveness (#1475), workflow usage attribution (#1111), sandbox OOM diagnosis (#1454), and post-pin cloud workload identity (#1499) residue. The source supports parts of those paths, but this study did not operate a cluster and must not report independent reproduction.
- Centaur has its own repository skills and overlay skill distribution, but a source-wide search at the pin found no Promise Machine, Fiat, Hexaemeron, Protasis, risk-register or hash-chained receipt contract. It records service events and outbound activity; it does not thereby make the same evidence claim as Shoggoth.

#### Complement, without an integration design

The conceptual complement is vertical: Shoggoth answers “what bounded agent job is authorised and what evidence survives the handoff”; Centaur answers “where a team's agent session runs, persists, receives capabilities and recovers”. A team can value both responsibilities without either repository containing the other. This is an architectural observation only. The deliverable stops before deciding whether, how, or at what cost they could coexist in one deployment.

#### Competition, without a winner

The projects compete directly where a team chooses its common instruction/skill distribution, workflow conventions, multi-agent coordination model, extension mechanism, audit story, and behavioural standardisation. Shoggoth approaches those from evidence-bounded skills and repository delivery. Centaur approaches them from an operated platform with workflows, tools and overlays. The product should describe the consequence of each approach and leave the reader's operating problem to choose the relevant layer.

## 5. Risk register seed

Warden must review every id below and mark it reviewed or not applicable. The prose after the block supplies context; the ids remain the enumerable obligations.

```risk-register
source-drift | current claims against two moving upstream main branches | the registry pins full commits and every code permalink contains the matching pin
layer-conflation | a matrix row that treats skill governance and service operation as the same responsibility | every row names the responsibility and records absence as negative space rather than an automatic defect
status-collapse | current code, inference, proposal, issue report and unknown appearing in one voice | each non-current claim carries its status and sources never promote a report into independent reproduction
negative-evidence | claims about what a repository does not provide | searches are recorded with scope and the prose says repository-owned or claimed rather than universal
audit-overclaim | passing synopsis currency or historical audit findings | the study names the views read, preserves unknown legacy fields and does not call the collective or Centaur audited as a whole
security-caveat-loss | Centaur isolation and credential strengths beside permissive egress and legitimate-capability misuse | profile and matrix retain both the control and its documented or issue-reported residual in the same section
roadmap-promotion | Skills checkpoint issues or Centaur issue suggestions | planned and open work stays outside the current-capability inventory
issue-certainty | public issue reports used as if reproduced in this run | product marks reporter evidence, current-source corroboration and this study's non-reproduction separately
ranking-smuggle | prose or visual structure that implies a universal winner | checker and review reject scores, aggregate ratings and winner language while retaining responsibility-level differences
integration-creep | conceptual complement turning into an adapter or migration plan | no interface map, combined architecture, implementation step, dependency or copied source enters the product
source-copying | analysis repository receiving upstream code or long prose | inventory contains only original analysis, short identifiers and links; review compares suspicious files against source trees
private-path-leak | planning or generated reports exposing machine-specific paths | checker rejects absolute user paths and final review searches all tracked text
credential-leak | examples, GitHub output or copied configuration exposing a secret | fixtures use obvious placeholders and checks reject common token/private-key markers
pin-registry-mismatch | human-readable claims diverging from evidence/pins.json | one checker reads the registry and verifies every required document names the same full commits
broken-navigation | a modular repository whose internal links or required sections drift | the checker resolves every relative Markdown link and tests the required heading/file inventory
authorship-drift | a runtime host replacing the requested human contributor in commits or pull requests | local signature and author checks precede push and GitHub verification precedes each Fiat receipt
private-repo-drift | remote visibility or target identity changing during delivery | publication proof reads owner, name, visibility and default branch immediately before final receipt
```

No risk line asks Warden to audit either source project. The review subject is the comparison repository and the truth boundary of its claims.

## 6. Glossary seeds

**Shoggoth:** the Wildcat Labs agent-and-skill collective at the assigned Skills commit; singular conversational address may also refer to the active member.

**Shoggoth Interceptor:** the collective operating through an external problem-solving harness. It is acknowledged but not evaluated here.

**Skill:** one canonical instruction surface owning a narrow operation and its promise boundary.

**Phase agent:** a bounded worker or discipline used inside delivery; it does not gain the controller's authority.

**Promise Machine:** `promise-machine/v1`, the shared law that limits claims and downstream transitions to named evidence.

**Fiat:** the explicit Hexaemeron controller for study, runbook, step implementation, audit, prose, push and integration receipts.

**Receipt:** a controller record binding one completed transition to named evidence; it is not a general assertion that all work is correct.

**Run observation:** an optional bounded record of run events whose accepted prefix may be joined to one Fiat receipt; availability and external truth are not implied.

**Centaur:** Paradigm's self-hosted platform for shared team agents at the assigned commit.

**Ingress plane:** the chat or API boundary that verifies, normalises and forwards a user event.

**Control plane:** `api-rs` plus durable Postgres state for sessions, executions, recovery, workflows, auth and telemetry.

**Execution plane:** the Kubernetes sandbox and harness adapter in which one assigned agent session runs.

**Capability plane:** Centaur tools, workflows and overlays available to agents or workflow hosts.

**Sandbox:** a per-thread runtime pod with a workspace, shell, harness and approved local tool surfaces.

**Workflow:** a durable handler whose side effects, waits, tools and agent turns are coordinated by the Centaur workflow runtime.

**Overlay:** an ordered external repository that contributes tools, workflows, skills, prompts or personas without forking Centaur.

**Principal:** the Centaur identity to which roles, secrets and route capabilities are granted.

**Conceptual complement:** two responsibilities that can be useful in the same organisation; it is not a proposal to connect their implementations.

**Competitive overlap:** a responsibility both projects address, even if they address it from different layers.

**Current:** documented and supported by implementation or current repository contract at the pin.

**Reported:** present in an open issue or pull-request record but not independently reproduced in this study.

**Planned:** proposed work not supplied by the pinned implementation.

**Unknown:** not established by the selected evidence; no positive conclusion follows.

## 7. Sources and reproducible observations

### Pin and live-ref observation

| Subject | Assigned pin | Live observation on 2026-08-26 | Read mode |
| --- | --- | --- | --- |
| Shoggoth / Skills | `58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff` | local `HEAD`, `origin/main`, and `git ls-remote origin refs/heads/main` matched | canonical contracts, implementation excerpts, verified audit synopses, merged PRs and open issues |
| Centaur | `36397534096bb89c065a52a9fcfebed34b995a00` | local `HEAD`, `origin/main`, and `git ls-remote origin refs/heads/main` matched | documentation, implementation excerpts, merged PRs and open issues; no repository audit report found |
| Comparison repository | `db38e431561d473d2ee85a1bf4dfe8e94d135c13` | `main` and `origin/main` matched at Fiat init | empty signed bootstrap; no prior product PR or audit |

### Shoggoth primary sources

- [Collective definition and package inventory](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L5-L17).
- [Promise Machine behavior and boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L115-L127).
- [Domain skill capabilities and explicit stopping points](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L129-L172).
- [Fiat and worker authority split](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L174-L194).
- [Delivery composition](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L245-L254).
- [Promise Machine governing principle](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L15-L24), [evidence classes](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L51-L68), [consequence levels](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L94-L108), and [composition limits](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L110-L135).
- [Fiat activation and version](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L1-L20), [durable directive rule](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L43-L50), [dedicated worktree and state boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L77-L107), and [stacked branches](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L276-L300).
- [Collective and human authorship boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/SHOGGOTH.md#L37-L59).
- [Portable router selection rule](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/.agents/skills/promise-machine/SKILL.md#L6-L24).
- Verified audit views: [Hexaemeron plugin synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/audit/AUDIT_SYNOPSIS.md), [Fiat #608 synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/audit/rounds/fiat-608-bind-the-integrate-gate-to-the-sync-receipt.synopsis.md), and [Fiat #510 synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/audit/rounds/fiat-510-reuse-source-bound-x-ray-analysis-across-fia.synopsis.md).
- Recent merged records: [#648](https://github.com/wildcat-finance/skills/pull/648), [#649](https://github.com/wildcat-finance/skills/pull/649), [#539](https://github.com/wildcat-finance/skills/pull/539), and [#579](https://github.com/wildcat-finance/skills/pull/579).
- Planned/open negative space: [#508](https://github.com/wildcat-finance/skills/issues/508), [#558](https://github.com/wildcat-finance/skills/issues/558), and [#560](https://github.com/wildcat-finance/skills/issues/560).

Repository-relative negative-evidence observation:

```bash
git ls-tree -d --name-only 58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff
rg -l -i 'slack events api|postgres|kubernetes sandbox|networkpolicy|iron-proxy|credential proxy|session_events' \
  --glob '!docs/assets/**' --glob '!*.lock' --glob '!audit/**' .
```

The tree contains skills, schemas, scripts, tests, docs and audits, not a first-party `services/` control-plane tree. The few service terms found occur in proposed checkpoint-service decisions, a study, or boundary guidance. The product may therefore say that this repository does not own or claim Centaur's service responsibilities. It may not say no Shoggoth host or external harness could ever supply them.

### Centaur primary sources

- [Purpose and capability list](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L18-L27), [self-hosted team-platform statement](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L31-L64), and [component map](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L66-L96).
- [Five architecture planes](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L16-L24), [durable API lifecycle](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L26-L41), [execution path](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L63-L78), [tools and workflows](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L80-L99), and [credential substitution](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L101-L111).
- [Prompt-injection, dependency and credential-abuse threats](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L14-L32), [sandbox and network controls](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L34-L57), [credential properties](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L76-L121), [audit-trail claim](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L123-L130), and [declared limitations](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L132-L158).
- [Default-deny namespace policy](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L1-L35), [workflow-host direct Postgres and HTTPS egress](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L113-L147), and [proxy-only API path](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L195-L231).
- [Workflow ownership and durability](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L8-L26), [supported workflow primitives](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L53-L68), [checkpointed side effects](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L92-L109), [agent and multi-agent turns](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L115-L161), [workflow principals](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L163-L195), and [direct database boundary](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L287-L295).
- [Overlay purpose and precedence](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L8-L19), [pinning and visibility](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L42-L68), and [skill-directory composition](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L107-L130).
- [Permissive local allowlist default](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/iron-proxy/iron-proxy.yaml#L21-L25), [managed proxy config ownership](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/api-rs/crates/centaur-sandbox-agent-k8s/src/iron_proxy.rs#L197-L207), and [current Console transform assembly](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/console/app/models/principal_sync_config_snapshot.rb#L398-L407).
- [Sequential local workflow-host request handling](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/api-rs/crates/centaur-workflows/src/lib.rs#L2967-L3026) and [agent-turn event stream open](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/services/api-rs/crates/centaur-workflows/src/lib.rs#L4258-L4329).
- Recent merged records: [#1497](https://github.com/paradigmxyz/centaur/pull/1497), [#1498](https://github.com/paradigmxyz/centaur/pull/1498), [#1394](https://github.com/paradigmxyz/centaur/pull/1394), [#1439](https://github.com/paradigmxyz/centaur/pull/1439), [#1450](https://github.com/paradigmxyz/centaur/pull/1450), and [#1479](https://github.com/paradigmxyz/centaur/pull/1479).
- Current issue records: [#1385](https://github.com/paradigmxyz/centaur/issues/1385), [#1475](https://github.com/paradigmxyz/centaur/issues/1475), [#1111](https://github.com/paradigmxyz/centaur/issues/1111), [#1454](https://github.com/paradigmxyz/centaur/issues/1454), and post-pin [#1499](https://github.com/paradigmxyz/centaur/issues/1499).

Repository-relative negative-evidence observation:

```bash
rg -l -i 'promise-machine|promise machine|hexctl|hexaemeron|protasis|fiat-v[0-9]|risk-register|hash-chained receipt' \
  --glob '!pnpm-lock.yaml' --glob '!Cargo.lock' .
```

It returned no match at the assigned Centaur pin. The product may say Centaur does not implement those named Shoggoth contracts. It may not say Centaur has no auditability: its persisted events, proxy logs, principals and service telemetry are a different kind of record.

### Unknowns that remain

- Neither project was deployed or exercised by this study. Runtime behavior beyond source, tests and public records is unknown.
- No claim is made about production scale, uptime, cost, user count, model quality, latency or organisational adoption.
- Centaur issue reports were not independently reproduced. #1499 postdates the source pin.
- The semantic correctness of every Shoggoth domain skill and every Centaur tool/workflow is outside scope.
- The external Shoggoth Interceptor and any private Centaur overlays are outside the selected source.
- Remote visibility, branch state and open-issue state can change after observation and must be read again before final delivery.

## 8. On-call questions and signals

This deliverable creates no service, scheduled task, daemon or production on-call rotation. It therefore needs no runtime alert, request trace, service metric or incident dashboard. That absence is deliberate: the only executable surface is a bounded repository validator run by a contributor or the authorised read-only CI workflow.

The final demo still emits enough local signals to answer four maintenance questions:

1. **Did the evidence subject change?** `scripts/check_repository.py` reports the two parsed repository/commit pairs and refuses any mismatch between `evidence/pins.json`, required prose and pinned GitHub links.
2. **Is the documentary shape intact?** The checker reports required files, required system-profile headings, comparison axes, relative-link resolution and prohibited aggregate-ranking fields.
3. **Did a test stop early?** `scripts/run_tests.py --report <path>` records command identity, tests run, failures, errors, skips, `complete`, and exit status in `elenchus.unittest.v1` form.
4. **Was the published object still the requested private repository?** The final operator runs the `gh repo view` command from section 1 and Fiat records the exact GitHub evidence before integration completion.

These signal choices are governed by the pinned [Ephoros contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/ephoros/SKILL.md). The study cites that contract rather than copying its event rules.

## 9. Trust boundaries and controls

The relevant boundaries are documentary and publication boundaries, not the runtime boundaries of the two subjects:

| Capability opened | What is worth taking | Control that closes the boundary |
| --- | --- | --- |
| Read pinned source | Accurate current claims | Source clones remain read-only; full commits and repository-relative lines identify every current claim; no source setup or test command is executed |
| Read public PRs and issues | Change rationale and named residue | Record URL, state, merge commit/date where applicable, and distinguish reporter evidence from this study's observation |
| Read audit synopses | Compact view of prior findings and limits | Run whole-set currency check first; name the exact view; preserve unknown legacy fields and open negative space |
| Write target Markdown/JSON | An inspectable comparison | Writes stay under the Fiat worktree; checker rejects absolute local paths, unresolved relative links and mismatched pins |
| Run target validator/tests | Reproducible structural evidence | Python standard library only; repository-contained paths; no shell expansion, source import, network fetch or credential read |
| Publish through Git/GitHub | Private signed review history | Exact owner/repository/visibility check, human signing config, local signature verification, REST verification, controller receipts and step-scoped PRs |
| Cite source code | Challengeable claims without copied code | Short identifiers and immutable links only; no vendoring or long quotation |
| Discuss conceptual complement | Explain responsibility fit | A standing no-integration paragraph, no interface mapping or build steps, and a Warden review against `integration-creep` |

No secret is required by product code. Existing authenticated Git/GitHub tooling belongs to the publication environment and must not be printed, copied into fixtures, or read by the repository checker. The target validator treats all Markdown and JSON as untrusted bytes, caps file sizes, requires regular files below the repository root, and never evaluates embedded commands.

These controls are governed by the pinned [Phylax contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/phylax/SKILL.md). The study does not restate its capability inventory.

## 10. Performance budget and Metron command

There is no product performance claim. The output is a small static repository, and correctness, traceability and readable navigation dominate sub-second differences in a local validator. Setting a latency gate before a file tree exists would be an invented target.

The final demonstration records an informational baseline without turning it into acceptance authority:

```bash
/usr/bin/time -p python3 scripts/check_repository.py
/usr/bin/time -p python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur.json
```

If either command later becomes slow enough to obstruct normal review, a new study may set a budget against the then-current file count and machine. No optimisation is authorised by this run. This treatment is governed by the pinned [Metron contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/metron/SKILL.md).

## 11. Fail-closed posture and Elenchus guard convention

The repository checker stops with non-zero status when a required file or heading is missing, JSON is malformed, a pin is not a 40-character lowercase commit, a required current-claim link uses `main` instead of the registered commit, a relative link escapes or does not resolve, the same source has conflicting pins, a local absolute path appears, or the comparison shape admits a score/winner field. It reports the path and reason without rewriting the source.

The checker does not decide whether prose is true. Warden holds claims against the risk ids, source ledger and pinned pages. An unresolved source conflict, a status that cannot be classified, a changed pin without a complete review, an unverified signature, or a remote that is no longer the named private repository blocks only the dependent receipt or publication transition.

For a failure found during implementation or audit:

1. preserve the exact failing command and output;
2. reduce it to one cause;
3. add a focused `unittest` guard or fixture mutation that fails on the parent state;
4. fix the cause rather than the symptom;
5. run `python3 scripts/run_tests.py --report {report}` with report format `elenchus.unittest.v1` and step report path `.elenchus/shoggoth-vs-centaur-step-<n>.json`; and
6. rerun the full repository checker, tests and prose gates before any receipt.

A finding without a reproducible code path may be a prose/source correction rather than an Elenchus run; the audit record must say why. A truncated or missing report is not a pass. This convention is governed by the pinned [Elenchus contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/elenchus/SKILL.md).

## 12. Expensive-to-reverse decisions and their homes

The decisions likely to outlive one edit are:

| Decision | Why reversal is expensive | Durable home |
| --- | --- | --- |
| Compare by responsibility layer before feature | Every profile, matrix row and conclusion depends on it | `docs/decisions/ADR-001-layer-aware-comparison.md`, with a short pointer in `docs/00-methodology.md` |
| Freeze one edition to full source commits | Updating a pin may change every current claim and limitation | `evidence/pins.json` plus the update procedure in `docs/00-methodology.md` |
| Use five claim statuses: current, inferred, reported, planned, unknown | Changing vocabulary can silently reclassify issue reports or proposals | `docs/00-methodology.md` |
| Keep complement conceptual and forbid integration design | Reversing it changes the user's requested product and expands authority | this study, the ADR, and `docs/04-complement-and-competition.md` |
| Use symmetric profiles and a non-scored matrix | It controls whether the result remains a comparison or becomes advocacy | the ADR and `docs/03-comparison-matrix.md` |
| Keep checks offline and standard-library-only | Adding dependencies or network truth changes the trust and maintenance boundary | `docs/00-methodology.md`, `scripts/check_repository.py`, and tests |
| Retain private, unlicensed-for-redistribution analysis | A public licence or publication cannot be cleanly withdrawn from copies | `LICENSE` and repository visibility settings |
| Preserve human authorship and signed Fiat history | Rewriting published identity or signatures damages provenance | Git configuration, Fiat receipts and pull-request history; no model byline file |

The accepted study and runbook are committed as `docs/fiat-study.md` and `docs/fiat-runbook.md`; later planning changes append through the controller's amendment path rather than silently rewriting the accepted belief. Claim-level changes update the source ledger and the affected prose in the same pull request.

These records are governed by the pinned [Hypomnema contract](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/hypomnema/SKILL.md). The study names homes and leaves the contract's recording rules with their owner.

The study is ready to derive a runbook. It establishes a documentary repository and a layer-aware comparison method. It assumes the source pins and private target stated above. It does not establish either project's runtime correctness, a combined-system design, or a universal choice between them. The next action is to derive discrete Fiat steps whose first step scaffolds this exact evidence boundary and whose last step runs the demo path from section 1.
