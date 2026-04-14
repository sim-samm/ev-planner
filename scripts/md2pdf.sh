#!/usr/bin/env bash
set -euo pipefail

# Convert Markdown to PDF with repo defaults.
# Works when run from anywhere inside this repo.
#
# Defaults:
#   - Input directory: docs/
#   - Output directory: docs/
#   - Output filename: same basename as input, with .pdf extension
#
# Examples:
#   scripts/md2pdf.sh spec_v3
#     -> docs/spec_v3.md to docs/spec_v3.pdf
#
#   scripts/md2pdf.sh sub_problems.md
#     -> docs/sub_problems.pdf
#
#   scripts/md2pdf.sh docs/spec_v3.md out/spec.pdf
#     -> explicit output path

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
DEFAULT_DOCS_DIR="${REPO_ROOT}/docs"
PAGEBREAK_HEADER="${SCRIPT_DIR}/pandoc-pagebreak-header.tex"

usage() {
  cat <<'EOF'
Usage:
  md2pdf.sh [input_md_or_basename] [output_pdf]

Behavior:
  - No args: fail with usage.
  - Basename input (no slash, no .md): uses docs/<name>.md
  - Path input: uses that exact markdown path.
  - No output arg: output path defaults to docs/<input-basename>.pdf.

Examples:
  scripts/md2pdf.sh spec_v3
  scripts/md2pdf.sh sub_problems.md
  scripts/md2pdf.sh docs/spec_v3.md build/spec_v3.pdf
EOF
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc not found in PATH." >&2
  exit 1
fi

if [[ "$1" == *"/"* || "$1" == *.md ]]; then
  INPUT_MD="$1"
  # If relative path was provided, resolve from current directory.
  if [[ "${INPUT_MD}" != /* ]]; then
    INPUT_MD="$(cd -- "${PWD}" && pwd)/${INPUT_MD}"
  fi
else
  INPUT_MD="${DEFAULT_DOCS_DIR}/$1.md"
fi

if [[ ! -f "${INPUT_MD}" ]]; then
  echo "Error: input markdown not found: ${INPUT_MD}" >&2
  exit 1
fi

if [[ $# -eq 2 ]]; then
  OUTPUT_PDF="$2"
  if [[ "${OUTPUT_PDF}" != /* ]]; then
    OUTPUT_PDF="$(cd -- "${PWD}" && pwd)/${OUTPUT_PDF}"
  fi
else
  INPUT_BASENAME="$(basename -- "${INPUT_MD}")"
  OUTPUT_PDF="${DEFAULT_DOCS_DIR}/${INPUT_BASENAME%.md}.pdf"
fi

OUTPUT_DIR="$(dirname -- "${OUTPUT_PDF}")"
mkdir -p "${OUTPUT_DIR}"

if [[ -f "${PAGEBREAK_HEADER}" ]]; then
  pandoc "${INPUT_MD}" \
    -o "${OUTPUT_PDF}" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V linestretch=1.15 \
    -V monofont="Menlo" \
    -H "${PAGEBREAK_HEADER}"
else
  pandoc "${INPUT_MD}" \
    -o "${OUTPUT_PDF}" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V linestretch=1.15 \
    -V monofont="Menlo"
fi

echo "Wrote: ${OUTPUT_PDF}"
