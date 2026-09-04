#!/usr/bin/env python3
"""Content-integrity checks for the George Orwell skill.

This repository ships no application code: it is an agent skill made of
Markdown and YAML. "Building" it means proving the content is well formed and
internally consistent, so this script is the closest thing the repo has to a
test suite.

Checks performed:
  1. Required top-level and reference files exist.
  2. SKILL.md front matter parses and declares name/version/license/description.
  3. Every disputed-quote YAML record parses, carries the required fields, and
     is classified `secondary` (the rule stated in references/attribution/README.md).
  4. Each disputed-quote record's quotation is present in the SKILL.md
     misattribution blacklist, and the counts on both sides match.
  5. Every references/... path mentioned in SKILL.md resolves to a real file.

Exit code is 0 when everything passes and 1 otherwise.
"""

from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "references/catalog.md",
    "references/plain-style.md",
    "references/attribution/README.md",
    "references/research/01-writings.md",
    "references/research/02-conversations.md",
    "references/research/03-expression-dna.md",
    "references/research/04-external-views.md",
    "references/research/05-decisions.md",
    "references/research/06-timeline.md",
]

REQUIRED_YAML_FIELDS = [
    "id",
    "classification",
    "quote",
    "normalized_quote",
    "attributed_to",
    "status",
    "confidence",
    "last_checked",
]

errors: list[str] = []
passes: list[str] = []
warnings: list[str] = []


def ok(msg: str) -> None:
    passes.append(msg)


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def best_window_ratio(needle: str, haystack: str) -> float:
    """Highest similarity of `needle` against any equal-length window of text."""
    n = len(needle)
    if n == 0 or n > len(haystack):
        return difflib.SequenceMatcher(None, needle, haystack).ratio()
    matcher = difflib.SequenceMatcher(None, needle, "")
    best = 0.0
    step = max(1, n // 8)
    for start in range(0, len(haystack) - n + 1, step):
        matcher.set_seq2(haystack[start : start + n])
        best = max(best, matcher.ratio())
        if best == 1.0:
            break
    return best


def normalize(text: str) -> str:
    """Collapse whitespace and unify quote/dash glyphs for robust matching."""
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", text).strip()


def check_required_files() -> None:
    for rel in REQUIRED_FILES:
        if (REPO / rel).is_file():
            ok(f"exists: {rel}")
        else:
            fail(f"missing required file: {rel}")


def parse_front_matter(md_text: str) -> dict | None:
    if not md_text.startswith("---"):
        return None
    end = md_text.find("\n---", 3)
    if end == -1:
        return None
    block = md_text[3:end]
    try:
        return yaml.safe_load(block)
    except yaml.YAMLError as exc:  # pragma: no cover - defensive
        fail(f"SKILL.md front matter is not valid YAML: {exc}")
        return None


def check_skill_front_matter() -> str:
    skill_path = REPO / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    fm = parse_front_matter(text)
    if fm is None:
        fail("SKILL.md is missing a YAML front-matter block")
        return text
    for key in ("name", "version", "license", "description"):
        if fm.get(key):
            ok(f"SKILL.md front matter has '{key}'")
        else:
            fail(f"SKILL.md front matter missing '{key}'")
    if fm.get("name") == "george-orwell-skill":
        ok("SKILL.md name is 'george-orwell-skill'")
    else:
        fail(f"unexpected SKILL.md name: {fm.get('name')!r}")
    return text


def check_yaml_records() -> list[dict]:
    yaml_dir = REPO / "references/attribution/disputed-quotes"
    records: list[dict] = []
    yaml_files = sorted(yaml_dir.glob("*.yaml"))
    if not yaml_files:
        fail(f"no YAML records found in {yaml_dir}")
        return records
    for path in yaml_files:
        rel = path.relative_to(REPO)
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            fail(f"{rel}: YAML parse error: {exc}")
            continue
        if not isinstance(data, dict):
            fail(f"{rel}: top-level YAML is not a mapping")
            continue
        missing = [f for f in REQUIRED_YAML_FIELDS if not data.get(f)]
        if missing:
            fail(f"{rel}: missing fields: {', '.join(missing)}")
        else:
            ok(f"{rel}: all required fields present")
        if data.get("classification") == "secondary":
            ok(f"{rel}: classification is 'secondary'")
        else:
            fail(f"{rel}: classification must be 'secondary', got {data.get('classification')!r}")
        records.append(data)
    return records


def check_blacklist_consistency(skill_text: str, records: list[dict]) -> None:
    marker = "Misattribution blacklist"
    idx = skill_text.find(marker)
    if idx == -1:
        fail("SKILL.md has no 'Misattribution blacklist' section")
        return
    blacklist = normalize(skill_text[idx:])
    for rec in records:
        quote = normalize(str(rec.get("quote", "")))
        rid = rec.get("id", "<unknown>")
        if not quote:
            fail(f"record '{rid}' has an empty quote")
            continue
        if quote in blacklist:
            ok(f"blacklist contains quote for '{rid}'")
            continue
        ratio = best_window_ratio(quote, blacklist)
        if ratio >= 0.9:
            warn(
                f"blacklist quote for '{rid}' differs slightly from the YAML "
                f"record (similarity {ratio:.2f}); wording drift worth reconciling"
            )
        else:
            fail(
                f"blacklist has no matching quote for '{rid}' "
                f"(best similarity {ratio:.2f})"
            )

    numbered = re.findall(r"\n\s*\d+\.\s", skill_text[idx:])
    if len(numbered) == len(records):
        ok(f"blacklist item count matches YAML record count ({len(records)})")
    else:
        fail(
            f"blacklist item count ({len(numbered)}) != YAML record count ({len(records)})"
        )


def check_internal_references(skill_text: str) -> None:
    refs = sorted(set(re.findall(r"references/[A-Za-z0-9_./-]+\.(?:md|yaml)", skill_text)))
    for rel in refs:
        if (REPO / rel).is_file():
            ok(f"reference resolves: {rel}")
        else:
            fail(f"SKILL.md references a missing file: {rel}")


def main() -> int:
    check_required_files()
    skill_text = check_skill_front_matter()
    records = check_yaml_records()
    check_blacklist_consistency(skill_text, records)
    check_internal_references(skill_text)

    print(f"PASS: {len(passes)} check(s)")
    for msg in passes:
        print(f"  \u2713 {msg}")
    if warnings:
        print(f"\nWARN: {len(warnings)} advisory(ies)")
        for msg in warnings:
            print(f"  ! {msg}")
    if errors:
        print(f"\nFAIL: {len(errors)} problem(s)")
        for msg in errors:
            print(f"  \u2717 {msg}")
        return 1
    print("\nAll content-integrity checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
