# Development Workflow

Active development uses Python modules and unit tests. Notebooks are historical
artifacts only.

## Agent

1. Fill in the roadmap stage with concrete subsections.
   1. Base the stage on the current spec, sub-problems, and previous stage.
   2. Include formulas and expected numeric checkpoints where helpful.
2. Implement stable behavior in a small Python module.
   1. Compose existing helpers instead of rewriting them.
   2. Keep function inputs as simple dicts until a richer data model is needed.
   3. Maintain useful TODOs when the current stage intentionally defers work.
3. Add or update tests.
   1. Use `unittest` coverage for the module public API.
   2. Prefer adding new tests for new behavior; keep old tests as regression anchors.
4. Update docs.
   1. Keep roadmap stage status and deliverables accurate.
   2. Update the spec only when domain rules or terminology change.

## Human

1. Review the roadmap stage and checkpoint expectations.
2. Verify the module API reads cleanly.
3. Run the tests, then add comments or concerns as needed.

See also: [coding_style.md](coding_style.md)
