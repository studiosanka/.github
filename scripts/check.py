#!/usr/bin/env python3
"""Checks this repository for mistakes GitHub would only show you after publishing.

    python scripts/check.py

- Every issue form in ISSUE_TEMPLATE/ is valid YAML with the fields GitHub requires.
- Every relative link in the Markdown files points at a file that exists.
- The profile README lists every repository whose folder sits next to this one (a reminder when a new one is added).
- Lists the TODOs that must be settled before this repository is made public.
Needs PyYAML.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors, notes = [], []

FIELD_TYPES = {"markdown", "textarea", "input", "dropdown", "checkboxes"}


def check_form(path):
    form = yaml.safe_load(path.read_text(encoding="utf-8"))
    for key in ("name", "description", "body"):
        if key not in form:
            errors.append(f"{path.name}: missing '{key}'")
    ids = set()
    for i, item in enumerate(form.get("body", [])):
        where = f"{path.name} body[{i}]"
        kind = item.get("type")
        if kind not in FIELD_TYPES:
            errors.append(f"{where}: unknown type {kind!r}")
            continue
        attrs = item.get("attributes", {})
        if kind == "markdown":
            if not attrs.get("value"):
                errors.append(f"{where}: markdown needs attributes.value")
            continue
        if not attrs.get("label"):
            errors.append(f"{where}: needs attributes.label")
        field_id = item.get("id")
        if field_id:
            if field_id in ids:
                errors.append(f"{where}: duplicate id {field_id}")
            ids.add(field_id)
            if not re.fullmatch(r"[A-Za-z0-9_-]+", field_id):
                errors.append(f"{where}: id {field_id!r} may only use letters, digits, - and _")
        if kind == "dropdown" and not attrs.get("options"):
            errors.append(f"{where}: dropdown needs options")
        if kind == "checkboxes" and not attrs.get("options"):
            errors.append(f"{where}: checkboxes needs options")
    if not any(b.get("type") != "markdown" for b in form.get("body", [])):
        errors.append(f"{path.name}: a form needs at least one input")


def check_config(path):
    cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    for link in cfg.get("contact_links", []):
        for key in ("name", "url", "about"):
            if key not in link:
                errors.append(f"config.yml: a contact link is missing '{key}'")


def check_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"(https?:|mailto:|#)", target):
                continue
            path = (md.parent / target.split("#")[0]).resolve()
            if not path.exists():
                errors.append(f"{md.relative_to(ROOT)}: link to missing file {target}")


def check_repo_list():
    profile = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
    for sibling in sorted(p.name for p in ROOT.parent.iterdir() if p.is_dir() and not p.name.startswith(".")):
        if sibling not in profile:
            notes.append(f"the folder '{sibling}' next to this repo is not in profile/README.md")


def todos():
    found = []
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if "TODO" in line or "coming soon" in line:
                found.append(f"{md.relative_to(ROOT)}:{n}")
    return found


def main():
    forms = sorted((ROOT / "ISSUE_TEMPLATE").glob("*.yml"))
    for f in forms:
        check_config(f) if f.name == "config.yml" else check_form(f)
    check_links()
    check_repo_list()
    print(f"Checked {len(forms)} issue template files.")
    for n in notes:
        print("NOTE:", n)
    for t in todos():
        print("TO SETTLE BEFORE PUBLISHING:", t)
    for e in errors:
        print("ERROR:", e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
