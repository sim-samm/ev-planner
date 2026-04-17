# Coding style (Python)

This repo prioritizes clarity and fast iteration over static typing machinery.

## Type hints

- Prefer **plain function signatures** without type annotations.
- Prefer **short docstrings** (or comments) that describe expected shapes for dict inputs, for example which keys exist and their meaning.
- Avoid `typing` imports unless there is a compelling reason.

Rationale: Python remains dynamically typed, and for this project the most valuable "contract" is usually a clear example plus tests.

## Tests

- Prefer `unittest` in `tests/` for small, explicit checks of module behavior.
- When behavior expands, add new tests rather than rewriting old ones, unless you are intentionally changing semantics.
