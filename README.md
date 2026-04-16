# EV Planner

A tool for planning optimal EV (Effort Value) training routes in Pokemon FireRed and LeafGreen.

## Goal

Minimize total operations needed to reach exact EV targets for a pokemon or team. Operations include moves, steps, healing, item management, and travel.

## Project Structure

```
docs/                   <- Project documentation
  ev_planner_spec_v3.md <- Current spec: rules, formulas, constraints
  sub_problems.md       <- Independent sub-problems and dependency graph
  roadmap.md            <- Development stages and deliverables
  thoughts.md           <- Scratch notes and future ideas
  archive/              <- Previous spec versions (v1, v2)
  pdfs/                 <- Generated PDF artifacts
references/             <- Optional local symlinks for dev-specific agent context
```

### `references/` (local context links)

`references/` is intended as a developer-managed directory for symbolic links to external files/folders that provide additional context for local agent workflows. Use it as needed on a per-developer basis; contents can vary by machine and working style.

## Status

Prototyping phase. Working through incremental development stages defined in [roadmap.md](docs/roadmap.md), starting with single-pokemon EV calculations and building toward full team optimization.

## Key Documents

- [Spec (v3)](docs/ev_planner_spec_v3.md) — What the system does
- [Sub-Problems](docs/sub_problems.md) — How to build it
- [Roadmap](docs/roadmap.md) — In what order
