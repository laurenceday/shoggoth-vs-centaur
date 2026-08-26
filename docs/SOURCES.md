# Source ledger

This ledger makes the two profiles reproducible without copying either source.
It records the edition pins, read mode, current and post-pin public records,
bounded absence searches, and what remains unknown.

## Edition pins and observation boundary

- Shoggoth / Skills uses
  `wildcat-finance/skills@58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff`.
  On 2026-08-26, local `HEAD`, `origin/main`, and the live `refs/heads/main`
  observation matched. Current code claims use the
  [registered full-commit base](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md).
- Centaur uses
  `paradigmxyz/centaur@36397534096bb89c065a52a9fcfebed34b995a00`.
  On 2026-08-26, local `HEAD`, `origin/main`, and the live `refs/heads/main`
  observation matched. Current code claims use the
  [registered full-commit base](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md).

The live-main observation proves only that each assigned pin was the public
tip when observed. It does not make `main` immutable and does not move this
edition when either source changes. Pull-request and issue state below was also
observed on 2026-08-26 and can change later.

The machine-readable authority is [`evidence/pins.json`](../evidence/pins.json).

## Read mode and status use

- Skills read mode covers canonical contracts, selected implementation and instruction
  surfaces, a whole-set-checked audit synopsis set, merged pull requests, open
  issues, and bounded repository searches.
- Centaur read mode covers architecture and security documentation, selected implementation
  and deployment files, merged pull requests, open issues, and bounded
  repository searches. No repository audit record was found.
- Current claims use immutable full-commit blob links from the registered
  repository only.
- Public records use durable pull-request or issue URLs, with status and the
  2026-08-26 observation date stated. A report is not independent reproduction.

The status vocabulary and its non-promotion rule live in
[the methodology](00-methodology.md#claim-statuses).

## Shoggoth / Skills evidence

### Canonical and current source

- [Collective definition and package inventory](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L5-L17)
- [Promise Machine behaviour and boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L115-L127)
- [Domain capabilities and stopping points](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L129-L172)
- [Fiat and worker authority](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L174-L194)
- [Promise Machine governing principle](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L15-L24), [evidence classes](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L51-L68), and [composition limits](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/PROMISE_MACHINE.md#L110-L145)
- [Fiat durable-state boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L43-L50), [worktree boundary](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L77-L107), and [stacked branches](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/skills/fiat/SKILL.md#L276-L300)
- [Portable router rule](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/.agents/skills/promise-machine/SKILL.md#L6-L24)

### Merged change records

The last two relevant merged pull requests at the pin were:

- [#648](https://github.com/wildcat-finance/skills/pull/648), merged on
  2026-08-26 as `57accf1b219df1fafcfa460a8978d8e8586cf64d`, bound Fiat
  integration to the sync receipt's recorded base head.
- [#649](https://github.com/wildcat-finance/skills/pull/649), merged on
  2026-08-26 as the registered Skills pin, shipped source-bound X-Ray
  preparation reuse while retaining explicit semantic and runtime limits.

Two earlier capability records bound the run-observation surface used in this
profile:

- [#539](https://github.com/wildcat-finance/skills/pull/539), merged on
  2026-08-24, added bounded pre-persistence capture.
- [#579](https://github.com/wildcat-finance/skills/pull/579), merged on
  2026-08-24, bound an accepted observation prefix to one Fiat receipt.

### Audit views and attribution

The study ran:

```bash
python3 plugins/hexaemeron/skills/fiat/scripts/audit_synopsis.py --check .
```

It exited zero across the committed synopsis set before any synopsis was used.
That check establishes rendering currency for the set; it does not establish
semantic correctness, whole-suite security, or fresh audit coverage. The exact
views read were:

- [Hexaemeron plugin synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/plugins/hexaemeron/audit/AUDIT_SYNOPSIS.md): F-01 through F-09 are fixed and F-10 is accepted with explicit hook escape hatches; legacy audit fields remain missing, and local-writer/concurrency/ANSI boundaries remain outside its rounds.
- [Fiat #608 synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/audit/rounds/fiat-608-bind-the-integrate-gate-to-the-sync-receipt.synopsis.md): no open product finding in the recorded rounds; the first legacy round preserves missing modern fields and frozen study/runbook inconsistencies.
- [Fiat #510 synopsis](https://github.com/wildcat-finance/skills/blob/58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/audit/rounds/fiat-510-reuse-source-bound-x-ray-analysis-across-fia.synopsis.md): fixed and guarded findings with continuing limits on semantic truth, model determinism, hostile local writers, production timing, and host installation.

Other plugin audit logs were discovered and included in the whole-set currency
check. They were not used to claim that every Shoggoth capability has received
a semantic audit.

### Open records

All three were open when observed on 2026-08-26:

- [#508](https://github.com/wildcat-finance/skills/issues/508): reported
  audit-carryover, delegated-write, and executable runbook-gate residue; not
  independently reproduced here.
- [#558](https://github.com/wildcat-finance/skills/issues/558): planned portable
  receipted-transition programme; not current capability.
- [#560](https://github.com/wildcat-finance/skills/issues/560): planned immutable
  base and checkpoint identity; not current capability.

## Centaur evidence

### Canonical and current source

- [Purpose and self-hosted team-platform statement](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/README.md#L18-L64)
- [Five architecture planes](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L16-L24), [durable lifecycle](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L26-L41), and [execution path](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L63-L78)
- [Tools and workflows](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L80-L99) and [credential substitution](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/architecture.mdx#L101-L111)
- [Threats and controls](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L14-L57), [credential properties](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L76-L121), [audit-trail claim](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L123-L130), and [declared limits](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/security.mdx#L132-L158)
- [Namespace default-deny and workflow-host routes](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/contrib/chart/templates/networkpolicy.yaml#L1-L147)
- [Workflow durability and primitives](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L8-L68), [agent turns and principals](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L115-L195), and [direct database boundary](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/workflows-v2.mdx#L287-L295)
- [Overlay precedence and pinning](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L8-L68) and [skill composition](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/docs/pages/extend/overlay.mdx#L107-L130)

### Merged change records

The last two merged pull requests at the pin were operational Console changes:

- [#1497](https://github.com/paradigmxyz/centaur/pull/1497), merged on
  2026-08-25 as `3f4ce07095681033dd8245a418044ecc5c600f3c`, added retries
  for Google Docs network failures.
- [#1498](https://github.com/paradigmxyz/centaur/pull/1498), merged on
  2026-08-26 as the registered Centaur pin, extended the Google Docs sync fetch
  timeout and added regression coverage.

The capability records used for profile context were merged before the pin:

- [#1394](https://github.com/paradigmxyz/centaur/pull/1394): per-principal
  session and workflow route capabilities plus a narrower proxy/API network
  path.
- [#1439](https://github.com/paradigmxyz/centaur/pull/1439): workflow principal
  resolution by foreign id or `prn_` OID.
- [#1450](https://github.com/paradigmxyz/centaur/pull/1450): MCP catalogue
  filtering by the sandbox tool allow/block policy.
- [#1479](https://github.com/paradigmxyz/centaur/pull/1479): a guard against
  recursive schedule creation from prompts containing cadence language.

### Audit-record boundary

A bounded repository search found a reporting `SECURITY.md` but no audit report,
audit directory, or audit-synopsis tree at the pin. This is evidence absence in
the public source, not a claim that Centaur or a private deployment has never
been audited. The profile therefore does not assign an audit verdict.
([Security reporting file](https://github.com/paradigmxyz/centaur/blob/36397534096bb89c065a52a9fcfebed34b995a00/SECURITY.md))

### Open and post-pin records

The following were open when observed on 2026-08-26. None was independently
reproduced in this study:

- [#1385](https://github.com/paradigmxyz/centaur/issues/1385): reported managed
  Kubernetes egress-allowlist configuration gap; pinned source was read for the
  local/managed configuration split.
- [#1475](https://github.com/paradigmxyz/centaur/issues/1475): reported workflow
  agent-turn event-stream hang and sequential host-loop starvation; the two
  pinned call sites were read.
- [#1111](https://github.com/paradigmxyz/centaur/issues/1111): reported missing
  usage records for workflow-tier agent turns.
- [#1454](https://github.com/paradigmxyz/centaur/issues/1454): reported loss of
  the later OOM-killed cause in sandbox status.
- [#1499](https://github.com/paradigmxyz/centaur/issues/1499): reported absent
  sandbox `serviceAccountName` configuration. It was filed after the registered
  commit and remains post-pin context, not a property established by the pin.

## Negative-evidence searches

The searches were repository-wide at each registered pin, excluded generated
lockfiles or binary/document assets where stated, and were interpreted only
against the repository-owned surface.

For Skills:

```bash
git ls-tree -d --name-only 58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff
git grep -li -E 'slack events api|postgres|kubernetes sandbox|networkpolicy|iron-proxy|credential proxy|session_events' 58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff -- ':!docs/assets/**' ':!audit/**'
```

The tree had no first-party service-control-plane directory. Matches described
checkpoint proposals and studies, audit or evaluation specimens, or generic
boundary guidance. The bounded conclusion is that Skills does not own or claim Centaur's service responsibilities; it says
nothing universal about external hosts.

For Centaur:

```bash
git grep -li -E 'promise-machine|promise machine|hexctl|hexaemeron|protasis|fiat-v[0-9]|risk-register|hash-chained receipt' 36397534096bb89c065a52a9fcfebed34b995a00 -- ':!pnpm-lock.yaml' ':!Cargo.lock'
```

The search returned no match. The bounded conclusion is that Centaur does not
implement those named Shoggoth contracts at the pin. Centaur's persisted events,
proxy logs, principals, grants, and telemetry remain a different operational
record, so “no auditability” would be false.

## Unknowns

- Neither source was deployed or exercised for this edition.
- Runtime correctness, scale, latency, uptime, cost, user count, adoption, and
  model quality are unknown.
- The semantic correctness of every Shoggoth skill and every Centaur tool or
  workflow is outside scope.
- Centaur issue reports were not independently reproduced; #1499 postdates the
  source pin.
- External Shoggoth harnesses and private Centaur overlays were not read.
- Issue state, live source tips, target visibility, and branch state can change
  after 2026-08-26.

## Update procedure

1. Choose new full commits and update [`evidence/pins.json`](../evidence/pins.json).
2. Record the new observation date and whether each live default branch matched
   the chosen commit.
3. Re-read every current claim, full-commit permalink, relevant merged change,
   audit view, open report, and negative-evidence search affected by either pin.
4. Keep reports and proposals status-labelled; do not promote them because a
   newer pin exists.
5. Update both profiles and this ledger in the same change.
6. Run the three offline commands in [the README](../README.md#verify).

Changing a link alone does not update the edition. The claim and its evidence
must still agree.
