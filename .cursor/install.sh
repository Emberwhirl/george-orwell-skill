#!/usr/bin/env bash
# Idempotent setup for the George Orwell skill repository.
#
# This repo ships no application code or dependencies: it is an agent skill
# made of Markdown and YAML. Setup therefore only (1) ensures the YAML parser
# the content validator needs is importable and (2) runs the validator as a
# smoke test that the content is well formed and internally consistent.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! python3 -c "import yaml" >/dev/null 2>&1; then
  echo "Installing PyYAML (needed by the content validator)…"
  pip3 install --quiet --user pyyaml
fi

echo "Running content-integrity checks…"
python3 scripts/validate_skill.py
