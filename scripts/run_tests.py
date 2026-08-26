#!/usr/bin/env python3
"""Run the actual unittest suite and emit one atomic Elenchus report."""

from __future__ import annotations

import argparse
import json
import os
import stat
import sys
import tempfile
import time
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "elenchus.unittest.v1"


def build_report(result: unittest.TestResult, duration_seconds: float) -> dict:
    failures = len(result.failures)
    errors = len(result.errors)
    tests_run = result.testsRun
    skips = len(getattr(result, "skipped", ()))
    complete = bool(getattr(result, "complete", True))
    passed = complete and tests_run > 0 and failures == 0 and errors == 0
    return {
        "contract": CONTRACT,
        "tests_run": tests_run,
        "failures": failures,
        "errors": errors,
        "skips": skips,
        "complete": complete,
        "exit_status": 0 if passed else 1,
        "duration_seconds": round(duration_seconds, 6),
    }


def safe_report_path(raw: str, root: Path = ROOT) -> Path:
    root = root.resolve()
    relative = Path(raw)
    if not raw or relative.is_absolute() or ".." in relative.parts:
        raise ValueError("report path must stay relative to the repository")
    if relative.suffix != ".json":
        raise ValueError("report path must end in .json")

    parent = root
    for part in relative.parent.parts:
        parent = parent / part
        if parent.exists() and parent.is_symlink():
            raise ValueError("report parent must not contain a symlink")
        parent.mkdir(exist_ok=True)
        resolved_parent = parent.resolve()
        try:
            resolved_parent.relative_to(root)
        except ValueError as exc:
            raise ValueError("report parent escapes the repository") from exc
        if not stat.S_ISDIR(resolved_parent.stat().st_mode):
            raise ValueError("report parent must be a directory")

    destination = root / relative
    if destination.exists() and (
        destination.is_symlink()
        or not stat.S_ISREG(destination.stat().st_mode)
    ):
        raise ValueError("report destination must be a regular file")
    return destination


def write_report(destination: Path, report: dict) -> None:
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=destination.parent,
            prefix=".elenchus-",
            suffix=".json.tmp",
            delete=False,
        ) as handle:
            temporary = handle.name
            json.dump(report, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
        temporary = None
    finally:
        if temporary is not None:
            Path(temporary).unlink(missing_ok=True)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True, metavar="PATH")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        destination = safe_report_path(args.report)
    except (OSError, ValueError) as exc:
        print(f"report path rejected: {exc}", file=sys.stderr)
        return 2

    started = time.perf_counter()
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    runner = unittest.TextTestRunner(stream=sys.stderr, verbosity=2)
    result = runner.run(suite)
    report = build_report(result, time.perf_counter() - started)
    write_report(destination, report)
    print(json.dumps(report, sort_keys=True))
    return report["exit_status"]


if __name__ == "__main__":
    raise SystemExit(main())
