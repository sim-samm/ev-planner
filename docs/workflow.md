1. Fill in roadmap stage with sub sections
  1. Base off of specification, sub-problems, and last stage
2. Stub out jupyter notebook with markdown cells
  1. Write out in English what each module should do
  2. Include math formulas and expected numeric checkpoints where helpful
3. Fill in with python code cells
  1. Prefer small cells that mirror the markdown checkpoints
4. Comment any thoughts / notes
5. Refactor inside the notebook until checkpoints read cleanly
6. Abstract into python files
  1. Move stable, reusable logic into a small module (for example `ev_core.py`)
  2. Keep notebooks as demos/spec surfaces; import from modules instead of redefining
7. Add or update tests
  1. Add `unittest` (or `pytest`) coverage for the module public API
  2. Prefer adding new tests for new behavior; keep old tests as regression anchors
8. Archive the stage notebook when its logic is fully represented by modules + tests
  1. Move the notebook under `archive/` (keep `.ipynb` in git for readable history)
  2. Optional: generate a `tar.gz` outside git for handoff bundles (avoid committing large binaries)
9. Start the next stage notebook that imports the modules and repeats from step 2

See also: [coding_style.md](coding_style.md)