# Agent
1. Fill in roadmap stage with sub sections
  1. Base off of specification, sub-problems, and last stage
2. Stub out jupyter notebook with markdown cells
  1. Write out in English what each module should do
  2. Include math formulas and expected numeric checkpoints where helpful
# Human
3. Fill in with python code cells
  1. Prefer small cells that mirror the markdown checkpoints
4. Comment any thoughts / notes
# Agent
5. Refactor inside the notebook until checkpoints read cleanly
# Human
6. Verify refactor is clean and aligned with comments and thoughts
# Agent
6. Abstract into python files
  1. Move stable, reusable logic into a small module
  2. Keep notebooks as demos/spec surfaces; import from modules instead of redefining
  3. Maintian thoughts and TODOS if not resolved
# Human
8. Verify modules look good
# Agent
9. Add or update tests
  1. Add `unittest` (or `pytest`) coverage for the module public API
  2. Prefer adding new tests for new behavior; keep old tests as regression anchors
# Human
10. Verify tests look good, add comments/conerns if necessary
# Agent
11. Archive the stage notebook when its logic is fully represented by modules + tests
  1. Move the notebook under `archive/` (keep `.ipynb` in git for readable history)
  2. Optional: generate a `tar.gz` outside git for handoff bundles (avoid committing large binaries)

See also: [coding_style.md](coding_style.md)
