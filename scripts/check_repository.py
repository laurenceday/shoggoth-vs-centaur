#!/usr/bin/env python3
"""Offline structural checks for the documentary comparison repository."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 1_048_576
MAX_TOTAL_BYTES = 8_388_608
SCHEMA = "shoggoth-vs-centaur.pins.v1"
EXCLUDED_DIRS = {".git", ".hexaemeron", ".elenchus", "__pycache__"}
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml"}
REQUIRED_FILES = (
    ".github/workflows/verify.yml",
    ".gitignore",
    "LICENSE",
    "README.md",
    "docs/00-methodology.md",
    "docs/decisions/ADR-001-layer-aware-comparison.md",
    "docs/fiat-study.md",
    "docs/fiat-runbook.md",
    "evidence/pins.json",
    "scripts/check_repository.py",
    "scripts/run_tests.py",
    "tests/__init__.py",
    "tests/test_repository.py",
)
COMMANDS = (
    "python3 scripts/check_repository.py",
    "python3 scripts/run_tests.py --report .elenchus/shoggoth-vs-centaur-step-1.json",
    "python3 -m unittest discover -s tests",
)
EXPECTED_SOURCES = (
    {
        "subject": "shoggoth",
        "repository": "wildcat-finance/skills",
        "commit": "58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff",
        "permalink_base": (
            "https://github.com/wildcat-finance/skills/blob/"
            "58b7dcd1004bf8e6b0cf517bbcc778789e2c43ff/"
        ),
    },
    {
        "subject": "centaur",
        "repository": "paradigmxyz/centaur",
        "commit": "36397534096bb89c065a52a9fcfebed34b995a00",
        "permalink_base": (
            "https://github.com/paradigmxyz/centaur/blob/"
            "36397534096bb89c065a52a9fcfebed34b995a00/"
        ),
    },
)
FIAT_DIGESTS = {
    "docs/fiat-study.md": (
        "a9c55bce2e2371f6ac308980d3c4ac39b4087894902d4b729132c9bda23363d7"
    ),
    "docs/fiat-runbook.md": (
        "07c7c50361d2ffb3da60e245932c49b09fcdb8825672122ed60e183141844113"
    ),
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)")
GITHUB_BLOB = re.compile(
    r"https://github\.com/([^/]+/[^/]+)/blob/([^/#?\s\"'<>]+)/[^\s)]+"
)
LOCAL_PATHS = (
    re.compile(r"(?<![A-Za-z0-9])/(?:Users|home)/[^\s`'\"<>]+"),
    re.compile(r"(?i)(?<![A-Za-z0-9])[A-Z]:\\Users\\[^\s`'\"<>]+"),
)
CREDENTIALS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
    re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"),
)


class CheckError(ValueError):
    """A bounded input failed validation."""


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def regular_path(root: Path, relative: str) -> Path:
    """Resolve one repository-relative regular file without following symlinks."""

    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise CheckError(f"unsafe relative path: {relative}")
    root = root.resolve()
    current = root
    for part in rel.parts:
        current = current / part
        if current.is_symlink():
            raise CheckError(f"symlink is not accepted: {relative}")
    resolved = current.resolve(strict=True)
    if not _inside(resolved, root):
        raise CheckError(f"path escapes repository: {relative}")
    mode = resolved.stat().st_mode
    if not stat.S_ISREG(mode):
        raise CheckError(f"not a regular file: {relative}")
    return resolved


def read_text(root: Path, relative: str) -> str:
    path = regular_path(root, relative)
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        raise CheckError(f"file exceeds {MAX_FILE_BYTES} bytes: {relative}")
    data = path.read_bytes()
    if len(data) != size:
        raise CheckError(f"file changed while being read: {relative}")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CheckError(f"file is not UTF-8: {relative}") from exc


def load_registry(root: Path) -> dict:
    raw = read_text(root, "evidence/pins.json")
    try:
        registry = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CheckError(f"malformed evidence/pins.json: {exc.msg}") from exc
    if not isinstance(registry, dict):
        raise CheckError("evidence registry must be an object")
    if registry.get("schema") != SCHEMA:
        raise CheckError(f"evidence schema must be {SCHEMA}")
    sources = registry.get("sources")
    if sources != list(EXPECTED_SOURCES):
        raise CheckError("evidence registry does not contain the exact two source pins")
    expected_target = {
        "repository": "laurenceday/shoggoth-vs-centaur",
        "bootstrap_commit": "db38e431561d473d2ee85a1bf4dfe8e94d135c13",
        "visibility": "private",
    }
    if registry.get("target") != expected_target:
        raise CheckError("target evidence does not match the private bootstrap")
    policy = registry.get("policy")
    if not isinstance(policy, dict):
        raise CheckError("evidence policy must be an object")
    if policy.get("source_repositories") != "read-only":
        raise CheckError("source repositories must remain read-only")
    if policy.get("integration") != "out-of-scope":
        raise CheckError("integration must remain out-of-scope")
    return registry


def iter_text(root: Path) -> list[tuple[str, str]]:
    """Read a bounded set of regular first-party text files without mutation."""

    root = root.resolve()
    found: list[tuple[str, str]] = []
    total = 0
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        directory = Path(dirpath)
        dirnames[:] = sorted(
            name
            for name in dirnames
            if name not in EXCLUDED_DIRS and not (directory / name).is_symlink()
        )
        for name in sorted(filenames):
            path = directory / name
            relative = path.relative_to(root).as_posix()
            if name != "LICENSE" and path.suffix not in TEXT_SUFFIXES:
                continue
            if path.is_symlink():
                raise CheckError(f"symlink is not accepted: {relative}")
            if not stat.S_ISREG(path.stat().st_mode):
                continue
            size = path.stat().st_size
            if size > MAX_FILE_BYTES:
                raise CheckError(f"file exceeds {MAX_FILE_BYTES} bytes: {relative}")
            total += size
            if total > MAX_TOTAL_BYTES:
                raise CheckError(f"text inventory exceeds {MAX_TOTAL_BYTES} bytes")
            found.append((relative, read_text(root, relative)))
    return found


def check_relative_links(root: Path, relative: str, text: str) -> list[str]:
    errors: list[str] = []
    for match in MARKDOWN_LINK.finditer(text):
        raw = match.group(1).strip("<>")
        parsed = urlsplit(raw)
        if parsed.scheme in {"http", "https", "mailto"}:
            continue
        if parsed.scheme or parsed.netloc or raw.startswith(("/", "~")):
            errors.append(f"{relative}: unsafe Markdown link {raw}")
            continue
        if raw.startswith("#"):
            continue
        link_path = unquote(parsed.path)
        if not link_path:
            continue
        if "\\" in link_path or "\x00" in link_path:
            errors.append(f"{relative}: unsafe Markdown link {raw}")
            continue
        candidate = (root / relative).parent / link_path
        try:
            resolved = candidate.resolve(strict=True)
        except FileNotFoundError:
            errors.append(f"{relative}: unresolved Markdown link {raw}")
            continue
        if not _inside(resolved, root.resolve()) or not resolved.is_file():
            errors.append(f"{relative}: Markdown link escapes repository {raw}")
    return errors


def check_blob_links(relative: str, text: str) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    subjects: set[str] = set()
    by_repo = {item["repository"]: item for item in EXPECTED_SOURCES}
    for match in GITHUB_BLOB.finditer(text):
        repository, revision = match.groups()
        source = by_repo.get(repository)
        if source is None:
            errors.append(f"{relative}: unregistered GitHub blob repository {repository}")
            continue
        if revision != source["commit"]:
            errors.append(
                f"{relative}: {repository} blob link is not pinned to {source['commit']}"
            )
            continue
        subjects.add(source["subject"])
    return errors, subjects


def inspect_repository(root: Path = ROOT) -> tuple[list[str], list[str]]:
    root = root.resolve()
    errors: list[str] = []
    diagnostics: list[str] = []

    for relative in REQUIRED_FILES:
        try:
            regular_path(root, relative)
        except (CheckError, FileNotFoundError) as exc:
            errors.append(f"required file {relative}: {exc}")
        else:
            diagnostics.append(f"FILE {relative}: ok")

    try:
        registry = load_registry(root)
    except (CheckError, FileNotFoundError) as exc:
        errors.append(str(exc))
        registry = None
    if registry is not None:
        for source in registry["sources"]:
            diagnostics.append(
                f"PIN {source['subject']}: {source['repository']}@{source['commit']}"
            )

    for relative, digest in FIAT_DIGESTS.items():
        try:
            actual = hashlib.sha256(regular_path(root, relative).read_bytes()).hexdigest()
        except (CheckError, FileNotFoundError) as exc:
            errors.append(f"{relative}: {exc}")
        else:
            if actual != digest:
                errors.append(f"{relative}: receipted byte digest mismatch")
            else:
                diagnostics.append(f"FIAT {relative}: {actual}")

    try:
        inventory = iter_text(root)
    except (CheckError, OSError) as exc:
        errors.append(str(exc))
        inventory = []

    linked_subjects: set[str] = set()
    for relative, text in inventory:
        if relative.endswith(".md"):
            errors.extend(check_relative_links(root, relative, text))
            blob_errors, subjects = check_blob_links(relative, text)
            errors.extend(blob_errors)
            linked_subjects.update(subjects)
        for pattern in LOCAL_PATHS:
            if pattern.search(text):
                errors.append(f"{relative}: absolute local path is prohibited")
                break
        for pattern in CREDENTIALS:
            if pattern.search(text):
                errors.append(f"{relative}: credential-shaped content is prohibited")
                break

    if linked_subjects != {"shoggoth", "centaur"}:
        errors.append("immutable full-commit links are required for both source subjects")

    try:
        licence = read_text(root, "LICENSE")
    except (CheckError, FileNotFoundError):
        licence = ""
    normalised_licence = " ".join(licence.split())
    for phrase in ("private and proprietary", "No licence", "not legal advice"):
        if phrase not in normalised_licence:
            errors.append(f"LICENSE: missing rights phrase {phrase!r}")

    try:
        readme = read_text(root, "README.md")
        workflow = read_text(root, ".github/workflows/verify.yml")
    except (CheckError, FileNotFoundError):
        readme = workflow = ""
    for command in COMMANDS:
        if command not in readme:
            errors.append(f"README.md: missing verification command {command}")
        if command not in workflow:
            errors.append(f"verify.yml: missing verification command {command}")
    normalised_readme = " ".join(readme.split())
    if "profiles and comparative conclusions are not written yet" not in normalised_readme:
        errors.append("README.md: scaffold must not claim profiles or synthesis are complete")

    diagnostics.append(f"INVENTORY regular UTF-8 files: {len(inventory)}")
    return errors, diagnostics


def main() -> int:
    errors, diagnostics = inspect_repository(ROOT)
    for line in diagnostics:
        print(line)
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print(f"RESULT fail: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("RESULT pass: evidence and scaffold contract satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
