from __future__ import annotations

import copy
import hashlib
import json
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
        for command in checker.COMMANDS:
            with self.subTest(command=command):
                self.assertIn(command, workflow)

    def test_readme_says_profiles_are_not_complete(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "profiles and comparative conclusions are not written yet",
            " ".join(readme.split()),
        )


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
        report = elenchus_runner.build_report(result, 0.125)
        self.assertEqual(
            set(report),
            {
                "contract",
                "tests_run",
                "failures",
                "errors",
                "skips",
                "complete",
                "exit_status",
                "duration_seconds",
            },
        )
        self.assertEqual(report["contract"], "elenchus.unittest.v1")
        self.assertTrue(report["complete"])
        self.assertEqual(report["exit_status"], 0)

    def test_zero_test_report_is_not_a_pass(self) -> None:
        report = elenchus_runner.build_report(unittest.TestResult(), 0.0)
        self.assertEqual(report["tests_run"], 0)
        self.assertEqual(report["exit_status"], 1)

    def test_incomplete_report_is_not_a_pass(self) -> None:
        result = unittest.TestResult()
        result.testsRun = 1
        result.complete = False
        report = elenchus_runner.build_report(result, 0.0)
        self.assertFalse(report["complete"])
        self.assertEqual(report["exit_status"], 1)

    def test_report_path_escape_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "stay relative"):
            elenchus_runner.safe_report_path("../outside.json")


class WholeRepositoryTests(unittest.TestCase):
    def test_checker_is_green(self) -> None:
        errors, diagnostics = checker.inspect_repository(ROOT)
        self.assertEqual(errors, [], "\n".join(errors))
        self.assertTrue(any(line.startswith("PIN shoggoth:") for line in diagnostics))
        self.assertTrue(any(line.startswith("PIN centaur:") for line in diagnostics))


if __name__ == "__main__":
    unittest.main()
