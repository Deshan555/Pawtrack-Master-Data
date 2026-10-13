#!/usr/bin/env python3
"""Validate manifest.json against every versioned JSON data file."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Cannot read valid manifest.json: {error}")

    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        fail("manifest.files must be a non-empty list")

    listed_paths: set[str] = set()
    for index, entry in enumerate(files):
        if not isinstance(entry, dict):
            fail(f"manifest.files[{index}] must be an object")

        relative_path = entry.get("path")
        expected_sha = entry.get("sha256")
        expected_bytes = entry.get("bytes")
        if not isinstance(relative_path, str) or not relative_path:
            fail(f"manifest.files[{index}].path must be a non-empty string")
        if relative_path in listed_paths:
            fail(f"Duplicate manifest path: {relative_path}")
        listed_paths.add(relative_path)
        if not isinstance(expected_sha, str) or len(expected_sha) != 64:
            fail(f"{relative_path}: sha256 must be a 64-character hexadecimal string")
        if not isinstance(expected_bytes, int) or expected_bytes < 0:
            fail(f"{relative_path}: bytes must be a non-negative integer")

        file_path = (ROOT / relative_path).resolve()
        if ROOT not in file_path.parents or not file_path.is_file():
            fail(f"{relative_path}: listed file does not exist inside the repository")

        content = file_path.read_bytes()
        actual_sha = hashlib.sha256(content).hexdigest()
        if actual_sha != expected_sha:
            fail(f"{relative_path}: checksum mismatch (expected {expected_sha}, got {actual_sha})")
        if len(content) != expected_bytes:
            fail(f"{relative_path}: byte count mismatch (expected {expected_bytes}, got {len(content)})")

        try:
            json.loads(content.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            fail(f"{relative_path}: invalid UTF-8 JSON: {error}")

    repository_json = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*.json")
        if ".git" not in path.parts and path.name != "manifest.json"
    }
    missing_from_manifest = sorted(repository_json - listed_paths)
    if missing_from_manifest:
        fail("JSON files missing from manifest: " + ", ".join(missing_from_manifest))

    print(f"Validated {len(files)} manifest entries and {len(repository_json)} data files.")


if __name__ == "__main__":
    main()
