from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_repository as checker  # noqa: E402
import run_tests as elenchus_runner  # noqa: E402


class RegistryTests(unittest.TestCase):
    def _registry_root(self, payload: object) -> tempfile.TemporaryDirectory:
        temporary = tempfile.TemporaryDirectory()
        evidence = Path(temporary.name) / "evidence"
        evidence.mkdir()
        text = payload if isinstance(payload, str) else json.dumps(payload)
        (evidence / "pins.json").write_text(text, encoding="utf-8")
        return temporary

    def test_exact_two_source_pins(self) -> None:
        registry = checker.load_registry(ROOT)
        self.assertEqual(registry["sources"], list(checker.EXPECTED_SOURCES))
        self.assertEqual(len(registry["sources"]), 2)

    def test_evidence_schema(self) -> None:
        registry = checker.load_registry(ROOT)
        self.assertEqual(registry["schema"], "shoggoth-vs-centaur.pins.v1")
        self.assertEqual(registry["target"]["visibility"], "private")
        self.assertEqual(registry["policy"]["source_repositories"], "read-only")
        self.assertEqual(registry["policy"]["integration"], "out-of-scope")

    def test_pin_mismatch_is_rejected(self) -> None:
        registry = checker.load_registry(ROOT)
        hostile = copy.deepcopy(registry)
        hostile["sources"][0]["commit"] = "0" * 40
        temporary = self._registry_root(hostile)
        self.addCleanup(temporary.cleanup)
        with self.assertRaisesRegex(checker.CheckError, "exact two source pins"):
            checker.load_registry(Path(temporary.name))

    def test_malformed_registry_is_rejected(self) -> None:
        temporary = self._registry_root("{not-json")
        self.addCleanup(temporary.cleanup)
        with self.assertRaisesRegex(checker.CheckError, "malformed"):
            checker.load_registry(Path(temporary.name))


class ScaffoldTests(unittest.TestCase):
    def test_required_scaffold_is_regular(self) -> None:
        for relative in checker.REQUIRED_FILES:
            with self.subTest(relative=relative):
                self.assertTrue(checker.regular_path(ROOT, relative).is_file())

    def test_fiat_records_are_exact_receipted_bytes(self) -> None:
        for relative, expected in checker.FIAT_DIGESTS.items():
            with self.subTest(relative=relative):
                actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
                self.assertEqual(actual, expected)

    def test_rights_notice_preserves_private_proprietary_status(self) -> None:
        notice = (ROOT / "LICENSE").read_text(encoding="utf-8")
        normalised = " ".join(notice.split())
        self.assertIn("private and proprietary", normalised)
        self.assertIn("No licence", normalised)
        self.assertIn("not legal advice", normalised)

    def test_ci_contains_exact_offline_commands(self) -> None:
        workflow = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("persist-credentials: false", workflow)
        for command in checker.WORKFLOW_COMMANDS:
            with self.subTest(command=command):
                self.assertIn(command, workflow)

    def test_readme_exposes_complete_step_three_reader_path(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "This edition contains the symmetric profiles, comparison matrix, "
            "conceptual complement and competitive-overlap analysis, decision guide, "
            "and source ledger.",
            " ".join(readme.split()),
        )

    def test_final_demo_commands_are_exposed(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        methodology = (ROOT / "docs/00-methodology.md").read_text(encoding="utf-8")
        for command in checker.STEP_COMMANDS:
            with self.subTest(command=command):
                self.assertIn(command, readme)
                self.assertIn(command, methodology)


class ProfileContractTests(unittest.TestCase):
    def _profile(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_profiles_have_exact_symmetric_heading_inventory(self) -> None:
        observed = []
        for relative in checker.PROFILE_FILES:
            text = self._profile(relative)
            headings = tuple(checker.H2_HEADING.findall(text))
            observed.append(headings)
            self.assertEqual(headings, checker.PROFILE_HEADINGS)
        self.assertEqual(observed[0], observed[1])

    def test_profiles_carry_all_five_visible_status_labels(self) -> None:
        for relative in checker.PROFILE_FILES:
            text = self._profile(relative)
            with self.subTest(relative=relative):
                for label in checker.STATUS_LABELS:
                    self.assertIn(label, text)

    def test_every_current_profile_block_has_its_registered_pin(self) -> None:
        for relative in checker.PROFILE_FILES:
            errors = checker.check_profile_document(relative, self._profile(relative))
            current_errors = [error for error in errors if "current-claim-pin" in error]
            with self.subTest(relative=relative):
                self.assertEqual(current_errors, [])

    def test_each_adjacent_current_claim_requires_its_own_pin(self) -> None:
        relative = "docs/01-shoggoth.md"
        hostile = self._profile(relative).replace(
            "([Domain inventory](https://github.com/wildcat-finance/skills/blob/"
            "58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/README.md#L129-L172))",
            "(source citation removed)",
            1,
        )
        errors = checker.check_profile_document(relative, hostile)
        self.assertTrue(any("current-claim-pin rule" in error for error in errors))

    def test_mutable_current_claim_link_is_rejected_with_named_rule(self) -> None:
        relative = "docs/01-shoggoth.md"
        source = checker.EXPECTED_SOURCES[0]
        hostile = self._profile(relative).replace(source["permalink_base"], "https://github.com/wildcat-finance/skills/blob/main/", 1)
        errors = checker.check_profile_document(relative, hostile)
        self.assertTrue(any("current-claim-pin rule" in error for error in errors))

    def test_reported_issue_without_non_reproduction_is_rejected(self) -> None:
        relative = "docs/02-centaur.md"
        text = self._profile(relative)
        hostile = text.replace(
            "This study verified that configuration split in source but did not\nindependently reproduce a deployed bypass.",
            "This study treats the report as deployed behaviour.",
        )
        errors = checker.check_profile_document(relative, hostile)
        self.assertTrue(any("issue-reproduction rule" in error for error in errors))

    def test_each_adjacent_reported_issue_needs_non_reproduction_boundary(self) -> None:
        relative = "docs/02-centaur.md"
        hostile = self._profile(relative).replace(
            "This study did not independently reproduce the report.",
            "The report remains open.",
            1,
        )
        errors = checker.check_profile_document(relative, hostile)
        self.assertTrue(any("issue-reproduction rule" in error for error in errors))

    def test_shoggoth_security_control_and_residual_are_adjacent(self) -> None:
        text = checker.section_text(
            self._profile("docs/01-shoggoth.md"), "Security and trust boundaries"
        ).lower()
        self.assertIn("fails closed", text)
        self.assertIn("does not make", text)
        self.assertIn("dedicated local worktree", text)

    def test_centaur_security_controls_and_residuals_are_adjacent(self) -> None:
        text = checker.section_text(
            self._profile("docs/02-centaur.md"), "Security and trust boundaries"
        ).lower()
        for marker in (
            "default-deny",
            "legitimate capabilities",
            "placeholders",
            "permissive by default",
            "issues/1385",
            "direct postgres",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_shoggoth_negative_space_is_repository_scoped(self) -> None:
        text = checker.section_text(
            self._profile("docs/01-shoggoth.md"), "Negative space"
        )
        self.assertIn("source-wide bounded search", text)
        self.assertIn("does not own or", text)
        self.assertIn("external\nShoggoth host", text)
        self.assertIn("not automatic defects", text)

    def test_centaur_negative_space_preserves_different_audit_record(self) -> None:
        text = checker.section_text(
            self._profile("docs/02-centaur.md"), "Negative space"
        )
        self.assertIn("source-wide bounded search", text)
        self.assertIn("different audit record", text)
        self.assertIn("no auditability", text)
        self.assertIn("not an\nautomatic platform defect", text)

    def test_profile_contract_errors_name_document_and_rule(self) -> None:
        relative = "docs/01-shoggoth.md"
        hostile = self._profile(relative).replace("## Purpose", "## Mission", 1)
        errors = checker.check_profile_document(relative, hostile)
        self.assertTrue(any(error.startswith(relative) for error in errors))
        self.assertTrue(any("profile-heading-order rule" in error for error in errors))

    def test_step_two_profile_rejects_comparative_ranking_language(self) -> None:
        relative = "docs/01-shoggoth.md"
        hostile = self._profile(relative) + "\nShoggoth is better than the other subject.\n"
        errors = checker.check_profile_document(relative, hostile)
        self.assertTrue(any("step-2-synthesis rule" in error for error in errors))


class SourceLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = (ROOT / "docs/SOURCES.md").read_text(encoding="utf-8")

    def test_ledger_contains_exact_pins_and_observation_date(self) -> None:
        self.assertIn("2026-08-26", self.ledger)
        for source in checker.EXPECTED_SOURCES:
            with self.subTest(subject=source["subject"]):
                self.assertIn(source["commit"], self.ledger)
                self.assertIn(source["permalink_base"], self.ledger)

    def test_ledger_covers_last_and_capability_pull_requests(self) -> None:
        for url in checker.LEDGER_PULL_REQUESTS:
            with self.subTest(url=url):
                self.assertIn(url, self.ledger)

    def test_ledger_covers_current_and_post_pin_issues(self) -> None:
        for url in checker.LEDGER_ISSUES:
            with self.subTest(url=url):
                self.assertIn(url, self.ledger)
        self.assertIn("post-pin context", self.ledger)

    def test_skills_audit_views_have_whole_set_attribution(self) -> None:
        self.assertIn("audit_synopsis.py --check .", self.ledger)
        self.assertIn("whole-set currency", self.ledger)
        for path in (
            "plugins/hexaemeron/audit/AUDIT_SYNOPSIS.md",
            "audit/rounds/fiat-608-bind-the-integrate-gate-to-the-sync-receipt.synopsis.md",
            "audit/rounds/fiat-510-reuse-source-bound-x-ray-analysis-across-fia.synopsis.md",
        ):
            with self.subTest(path=path):
                self.assertIn(path, self.ledger)

    def test_centaur_audit_absence_is_an_evidence_boundary(self) -> None:
        self.assertIn("evidence absence", self.ledger)
        self.assertIn("not a claim that Centaur", self.ledger)
        self.assertIn("does not assign an audit verdict", self.ledger)

    def test_issue_reports_are_not_presented_as_reproduced(self) -> None:
        self.assertIn("None was independently\nreproduced", self.ledger)
        self.assertIn("not\n  independently reproduced", self.ledger)

    def test_negative_evidence_searches_are_bounded(self) -> None:
        self.assertIn("## Negative-evidence searches", self.ledger)
        self.assertIn("does not own or claim Centaur's service responsibilities", self.ledger)
        self.assertIn("different operational\nrecord", self.ledger)
        self.assertIn("nothing universal about external hosts", self.ledger)

    def test_ledger_records_unknowns_and_update_procedure(self) -> None:
        self.assertIn("## Unknowns", self.ledger)
        self.assertIn("## Update procedure", self.ledger)
        self.assertIn("Update both profiles and this ledger in the same change", self.ledger)

    def test_source_ledger_checker_is_clean(self) -> None:
        self.assertEqual(checker.check_source_ledger(self.ledger), [])


class SynthesisContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.matrix = (ROOT / checker.MATRIX_FILE).read_text(encoding="utf-8")
        cls.complement = (ROOT / checker.COMPLEMENT_FILE).read_text(encoding="utf-8")
        cls.decision = (ROOT / checker.DECISION_FILE).read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.methodology = (ROOT / "docs/00-methodology.md").read_text(encoding="utf-8")
        cls.workflow = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")

    def test_all_three_synthesis_contracts_are_clean(self) -> None:
        self.assertEqual(checker.check_matrix_document(self.matrix), [])
        self.assertEqual(checker.check_complement_document(self.complement), [])
        self.assertEqual(checker.check_decision_document(self.decision), [])

    def test_matrix_has_exact_thirteen_axis_inventory(self) -> None:
        rows = checker.matrix_rows(self.matrix)
        self.assertEqual(len(rows), 13)
        self.assertEqual(tuple(row[0] for row in rows), checker.MATRIX_AXES)

    def test_missing_matrix_axis_is_rejected(self) -> None:
        row = next(
            line for line in self.matrix.splitlines() if line.startswith("| Intended user |")
        )
        hostile = self.matrix.replace(row + "\n", "", 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-axis rule" in error for error in errors))

    def test_changed_matrix_field_inventory_is_rejected(self) -> None:
        hostile = self.matrix.replace(
            "| Responsibility axis | Shoggoth | Centaur | Responsibility difference |",
            "| Responsibility axis | Shoggoth | Centaur | Overall |",
            1,
        )
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-field rule" in error for error in errors))

    def test_unlabelled_matrix_claim_is_rejected(self) -> None:
        hostile = self.matrix.replace("[Current] An operator", "An operator", 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-status rule" in error for error in errors))

    def test_matrix_subject_without_profile_source_is_rejected(self) -> None:
        hostile = self.matrix.replace("01-shoggoth.md#purpose", "missing-profile", 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-source-limit rule" in error for error in errors))

    def test_each_current_matrix_subject_cell_needs_its_direct_pin(self) -> None:
        source = checker.EXPECTED_SOURCES[0]
        hostile = self.matrix.replace(
            source["permalink_base"] + "README.md#L5-L17",
            "https://example.invalid/unpinned-source",
            1,
        )
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-current-pin rule" in error for error in errors))

    def test_matrix_subject_without_visible_limit_is_rejected(self) -> None:
        hostile = self.matrix.replace("Limit:", "Boundary:", 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-source-limit rule" in error for error in errors))

    def test_matrix_limit_needs_its_own_status(self) -> None:
        hostile = self.matrix.replace(
            "[Inferred] Limit: the Skills source",
            "Limit: the Skills source",
            1,
        )
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-limit-status rule" in error for error in errors))

    def test_matrix_difference_needs_both_profiles(self) -> None:
        row = next(
            line for line in self.matrix.splitlines() if line.startswith("| Intended user |")
        )
        hostile_row = row.rsplit("[Centaur context]", 1)[0] + "Centaur context removed |"
        hostile = self.matrix.replace(row, hostile_row, 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-difference-source rule" in error for error in errors))

    def test_centaur_security_residuals_must_remain_adjacent(self) -> None:
        hostile = self.matrix.replace("permissive egress", "bounded egress", 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("Centaur-security-adjacency rule" in error for error in errors))

    def test_matrix_rejects_aggregate_result_language(self) -> None:
        hostile = self.matrix + "\nOverall winner: one subject.\n"
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("non-scored-matrix rule" in error for error in errors))

    def test_matrix_rejects_each_quantified_or_procurement_shape(self) -> None:
        for snippet in (
            "Score: 9",
            "Overall rating: high",
            "Rank: 1",
            "5 stars",
            "10 points",
            "Procurement recommendation: adopt one subject",
        ):
            with self.subTest(snippet=snippet):
                errors = checker.check_matrix_document(self.matrix + "\n" + snippet + "\n")
                self.assertTrue(
                    any("non-scored-matrix rule" in error for error in errors)
                )

    def test_matrix_requires_ledger_and_pin_registry(self) -> None:
        hostile = self.matrix.replace("../evidence/pins.json", "pin-registry-removed", 1)
        errors = checker.check_matrix_document(hostile)
        self.assertTrue(any("matrix-evidence rule" in error for error in errors))

    def test_complement_and_competition_have_distinct_sections(self) -> None:
        self.assertEqual(
            tuple(checker.H2_HEADING.findall(self.complement)),
            checker.COMPLEMENT_HEADINGS,
        )

    def test_collapsed_complement_section_is_rejected(self) -> None:
        hostile = self.complement.replace(
            "## Competitive overlap", "## Conceptual complement", 1
        )
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("analysis-heading-order rule" in error for error in errors))

    def test_competition_is_limited_to_exact_six_responsibilities(self) -> None:
        competition = checker.section_text(self.complement, "Competitive overlap")
        self.assertEqual(
            tuple(checker.H3_HEADING.findall(competition)),
            checker.COMPETITION_HEADINGS,
        )

    def test_extra_competitive_responsibility_is_rejected(self) -> None:
        hostile = self.complement.replace(
            "## No-integration boundary",
            "### Runtime hosting\n\nNot in the accepted overlap.\n\n## No-integration boundary",
            1,
        )
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("competitive-overlap-axis rule" in error for error in errors))

    def test_each_competitive_axis_needs_consequences(self) -> None:
        hostile = self.complement.replace("**Shared consequence.**", "**Shared note.**", 1)
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("competitive-consequence rule" in error for error in errors))

    def test_conceptual_complement_keeps_vertical_responsibility_words(self) -> None:
        hostile = self.complement.replace(
            "what bounded agent\n  job, evidence, and delivery is authorised",
            "what work exists",
            1,
        )
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("conceptual-complement rule" in error for error in errors))

    def test_hard_no_integration_inventory_is_required(self) -> None:
        hostile = self.complement.replace("no adapter", "no connector", 1)
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("no-integration boundary" in error for error in errors))

    def test_actionable_adapter_heading_is_rejected(self) -> None:
        hostile = self.complement + "\n## Adapter design\n\nImplementation detail.\n"
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("no-integration rule" in error for error in errors))

    def test_actionable_api_route_is_rejected(self) -> None:
        hostile = self.complement + "\nPOST /bridge/session\n"
        errors = checker.check_complement_document(hostile)
        self.assertTrue(any("no-integration rule" in error for error in errors))

    def test_decision_guide_has_exact_problem_routes(self) -> None:
        self.assertEqual(
            tuple(checker.H2_HEADING.findall(self.decision)),
            checker.DECISION_HEADINGS,
        )

    def test_missing_decision_route_is_rejected(self) -> None:
        hostile = self.decision.replace(
            "## Does neither pin prove the answer?",
            "## Is another question open?",
            1,
        )
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("decision-heading-order rule" in error for error in errors))

    def test_decision_route_needs_question_inspection_and_unknown(self) -> None:
        hostile = self.decision.replace("**Inspect next.**", "**Read.**", 1)
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("decision-route-shape rule" in error for error in errors))

    def test_decision_route_needs_visible_unknown_status(self) -> None:
        hostile = self.decision.replace("[Unknown]", "[Unresolved]", 1)
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("decision-unknown rule" in error for error in errors))

    def test_decision_route_needs_evidence_link(self) -> None:
        heading = checker.DECISION_HEADINGS[0]
        body = checker.heading_section(self.decision, 2, heading)
        without_links = re.sub(r"\[[^\]]+\]\([^)]+\)", "evidence removed", body)
        hostile = self.decision.replace(body, without_links, 1)
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("decision-evidence rule" in error for error in errors))

    def test_product_choice_verdict_is_rejected(self) -> None:
        hostile = self.decision + "\nChoose Shoggoth for this work.\n"
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("no-product-verdict rule" in error for error in errors))

    def test_decision_guide_requires_ledger_and_pin_registry(self) -> None:
        hostile = self.decision.replace("../evidence/pins.json", "pin-removed", 1)
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("decision-evidence rule" in error for error in errors))

    def test_all_synthesis_relative_links_resolve(self) -> None:
        for relative in checker.SYNTHESIS_FILES:
            text = (ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(relative=relative):
                self.assertEqual(checker.check_relative_links(ROOT, relative, text), [])

    def test_broken_synthesis_relative_link_is_rejected(self) -> None:
        hostile = self.decision.replace("01-shoggoth.md#purpose", "missing.md", 1)
        errors = checker.check_relative_links(ROOT, checker.DECISION_FILE, hostile)
        self.assertTrue(any("unresolved Markdown link" in error for error in errors))

    def test_final_entrypoints_and_demo_are_clean(self) -> None:
        self.assertEqual(
            checker.check_final_entrypoints(
                self.readme, self.methodology, self.workflow
            ),
            [],
        )

    def test_missing_final_navigation_entry_is_rejected(self) -> None:
        hostile = self.readme.replace(checker.MATRIX_FILE, "matrix-link-removed", 1)
        errors = checker.check_final_entrypoints(
            hostile, self.methodology, self.workflow
        )
        self.assertTrue(any("navigation rule" in error for error in errors))

    def test_reordered_final_navigation_is_rejected(self) -> None:
        first, second = checker.README_NAVIGATION[1:3]
        hostile = self.readme.replace(first, "NAVIGATION_SWAP", 1)
        hostile = hostile.replace(second, first, 1).replace("NAVIGATION_SWAP", second, 1)
        errors = checker.check_final_entrypoints(
            hostile, self.methodology, self.workflow
        )
        self.assertTrue(any("navigation-order rule" in error for error in errors))

    def test_old_report_path_is_rejected_by_final_demo_contract(self) -> None:
        hostile = self.readme.replace(
            "shoggoth-vs-centaur-step-3.json", "shoggoth-vs-centaur-step-2.json", 1
        )
        errors = checker.check_final_entrypoints(
            hostile, self.methodology, self.workflow
        )
        self.assertTrue(any("missing verification command" in error for error in errors))

    def test_synthesis_inventory_has_no_actionable_cross_system_shape(self) -> None:
        for relative in checker.SYNTHESIS_FILES:
            text = (ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(relative=relative):
                self.assertEqual(checker.check_actionable_integration(relative, text), [])

    def test_numbered_cross_system_phase_is_rejected(self) -> None:
        hostile = self.decision + "\nPhase 1: connect the systems.\n"
        errors = checker.check_decision_document(hostile)
        self.assertTrue(any("no-integration rule" in error for error in errors))


class SourceCopyGuardTests(unittest.TestCase):
    def test_current_inventory_contains_no_upstream_source_copy_shape(self) -> None:
        inventory = checker.iter_text(ROOT)
        self.assertEqual(checker.check_source_copy_inventory(inventory), [])

    def test_upstream_language_file_is_rejected(self) -> None:
        errors = checker.check_source_copy_inventory([("vendor/session.rs", "fn main() {}")])
        self.assertTrue(any("source-copying rule" in error for error in errors))

    def test_repository_inventory_exposes_upstream_language_files_to_guard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "session.rs").write_text("fn main() {}\n", encoding="utf-8")
            errors = checker.check_source_copy_inventory(checker.iter_text(root))
        self.assertTrue(any("source-copying rule" in error for error in errors))

    def test_repository_inventory_exposes_source_mirror_files_to_guard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            mirror = root / "upstream"
            mirror.mkdir()
            (mirror / "snapshot.txt").write_text("copied source\n", encoding="utf-8")
            errors = checker.check_source_copy_inventory(checker.iter_text(root))
        self.assertTrue(any("source-copying rule" in error for error in errors))

    def test_source_named_parent_outside_repository_is_not_a_mirror(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "sources" / "analysis"
            root.mkdir(parents=True)
            (root / "README.md").write_text("original analysis\n", encoding="utf-8")
            errors = checker.check_source_copy_inventory(checker.iter_text(root))
        self.assertEqual(errors, [])

    def test_source_mirror_directory_is_rejected(self) -> None:
        errors = checker.check_source_copy_inventory([("upstream/README.md", "copy")])
        self.assertTrue(any("source-copying rule" in error for error in errors))


class HostileInputTests(unittest.TestCase):
    def test_immutable_source_links_accept_registered_full_pins(self) -> None:
        text = "\n".join(item["permalink_base"] + "README.md" for item in checker.EXPECTED_SOURCES)
        errors, subjects = checker.check_blob_links("fixture.md", text)
        self.assertEqual(errors, [])
        self.assertEqual(subjects, {"shoggoth", "centaur"})

    def test_mutable_or_mismatched_blob_link_is_rejected(self) -> None:
        bad = "https://github.com/wildcat-finance/skills/blob/main/README.md"
        errors, subjects = checker.check_blob_links("fixture.md", bad)
        self.assertEqual(subjects, set())
        self.assertEqual(len(errors), 1)
        self.assertIn("not pinned", errors[0])

    def test_every_document_blob_link_uses_a_registered_full_pin(self) -> None:
        for relative, text in checker.iter_text(ROOT):
            if not relative.endswith(".md"):
                continue
            errors, _ = checker.check_blob_links(relative, text)
            with self.subTest(relative=relative):
                self.assertEqual(errors, [])

    def test_relative_link_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "fixture.md").write_text("fixture", encoding="utf-8")
            outside = root.parent / "outside-fixture.md"
            outside.write_text("outside", encoding="utf-8")
            self.addCleanup(outside.unlink, missing_ok=True)
            errors = checker.check_relative_links(
                root, "docs/fixture.md", "[escape](../../outside-fixture.md)"
            )
            self.assertEqual(len(errors), 1)
            self.assertIn("escapes repository", errors[0])

    def test_safe_relative_link_resolves(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (root / "README.md").write_text("root", encoding="utf-8")
            (docs / "fixture.md").write_text("fixture", encoding="utf-8")
            errors = checker.check_relative_links(
                root, "docs/fixture.md", "[root](../README.md)"
            )
            self.assertEqual(errors, [])

    def test_absolute_local_path_marker_is_detected(self) -> None:
        hostile = "/" + "Users/" + "alice/source"
        self.assertTrue(any(pattern.search(hostile) for pattern in checker.LOCAL_PATHS))

    def test_credential_shaped_marker_is_detected(self) -> None:
        hostile = "-----BEGIN " + "PRIVATE KEY-----"
        self.assertTrue(any(pattern.search(hostile) for pattern in checker.CREDENTIALS))

    def test_inventory_ignores_controller_and_report_trees(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("visible", encoding="utf-8")
            for name in (".git", ".hexaemeron", ".elenchus"):
                hidden = root / name
                hidden.mkdir()
                (hidden / "hidden.md").write_text("hidden", encoding="utf-8")
            inventory = checker.iter_text(root)
            self.assertEqual(inventory, [("README.md", "visible")])


class ElenchusReportTests(unittest.TestCase):
    def test_passing_report_shape(self) -> None:
        result = unittest.TestResult()
        result.testsRun = 3
        result.skipped = [("case", "reason")]
        report = elenchus_runner.build_report(result)
        self.assertEqual(
            set(report),
            {
                "schema",
                "testsRun",
                "failures",
                "errors",
                "skipped",
                "complete",
                "expectedFailures",
                "unexpectedSuccesses",
            },
        )
        self.assertEqual(report["schema"], "elenchus.unittest.v1")
        self.assertTrue(report["complete"])
        self.assertEqual(elenchus_runner.report_exit_status(report), 0)

    def test_zero_test_report_is_not_a_pass(self) -> None:
        report = elenchus_runner.build_report(unittest.TestResult())
        self.assertEqual(report["testsRun"], 0)
        self.assertEqual(elenchus_runner.report_exit_status(report), 1)

    def test_incomplete_report_is_not_a_pass(self) -> None:
        result = unittest.TestResult()
        result.testsRun = 1
        result.complete = False
        report = elenchus_runner.build_report(result)
        self.assertFalse(report["complete"])
        self.assertEqual(elenchus_runner.report_exit_status(report), 1)

    def test_unexpected_success_is_not_a_pass(self) -> None:
        result = unittest.TestResult()
        result.testsRun = 1
        result.unexpectedSuccesses = ["case"]
        report = elenchus_runner.build_report(result)
        self.assertEqual(report["unexpectedSuccesses"], 1)
        self.assertEqual(elenchus_runner.report_exit_status(report), 1)

    def test_report_path_escape_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "stay inside"):
            elenchus_runner.safe_report_path("../outside.json")

    def test_absolute_report_path_inside_repository_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = root / ".elenchus" / "report.json"
            observed = elenchus_runner.safe_report_path(str(expected), root)
            self.assertEqual(observed, expected.resolve(strict=False))

    def test_absolute_report_path_outside_repository_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repository"
            root.mkdir()
            outside = Path(directory) / "outside.json"
            with self.assertRaisesRegex(ValueError, "stay inside"):
                elenchus_runner.safe_report_path(str(outside), root)


class WholeRepositoryTests(unittest.TestCase):
    def test_checker_is_green(self) -> None:
        errors, diagnostics = checker.inspect_repository(ROOT)
        self.assertEqual(errors, [], "\n".join(errors))
        self.assertTrue(any(line.startswith("PIN shoggoth:") for line in diagnostics))
        self.assertTrue(any(line.startswith("PIN centaur:") for line in diagnostics))


if __name__ == "__main__":
    unittest.main()
