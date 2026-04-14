# Sub-Problems

Each sub-problem has a clear interface and can be owned independently. See [ev_planner_spec_v3.md](ev_planner_spec_v3.md) for the underlying rules, formulas, and constraints. See [roadmap.md](roadmap.md) for how these sub-problems map to development stages.

## Independent (no code dependencies — can start now)

**EV Arithmetic Engine:** Pure math. Implements `ev_from_battle`, `ev_from_money`, and `ev_per_move` from Spec Section 3. Takes item state and opponent yield as inputs, returns numbers. Testable with made-up inputs.

**OHKO Heuristic:** Given a battler's level, moves, and types plus an opponent's level and type, determines if a OHKO is expected. Outputs a bool.

**Vitamin Planner:** Given a party's current EV state and wallet, determines optimal vitamin purchases using the applicability and batching logic from Spec Section 5.

**Pokemon / Party Data Model:** Defines the shared data contract — a Pokemon (species, EV yield, level, types) and a PlayerParty (members, items held, current EVs per stat). Other sub-problems code against this interface.

**Game Data Layer:** Provides opponent EV yields, trainer rosters, money rewards, and encounter rates. Pure data entry — JSON/CSV against a defined schema. No math.

## Dependent (require one or more of the above)

**Battle Usefulness Filter:** Implements the three-channel logic from Spec Section 5 (`battle_is_useful`). Takes party state and opponent yield, returns which channels are active. *Depends on:* EV Arithmetic Engine.

**Battle Comparison / Ranking:** Given available battles (wild + trainer), ranks them by `ev_per_move` for a given party state. *Depends on:* EV Arithmetic Engine, Battle Usefulness Filter, Game Data Layer.

**Wild Encounter vs. VS Seeker Analysis:** Compares EV yield per step for wild encounters vs. trainer rematches. *Depends on:* EV Arithmetic Engine, Game Data Layer.

## Dependency Overview

```
EV Arithmetic ──┬──► Battle Usefulness Filter ──► Battle Ranking
                │                                      ▲
Data Model ─────┤                                      │
                │                                      │
Game Data ──────┼──► Wild vs VS Seeker Analysis        │
                └──────────────────────────────────────┘

OHKO Heuristic          (independent)
Vitamin Planner         (independent)
```

## Data sources / references

- **[pret/pokefirered](https://github.com/pret/pokefirered)** — Decompilation of Pokémon FireRed and LeafGreen. Game data lives under `data/` (and related C sources); strong primary reference for trainer parties, wild encounters, species base stats, EV yields, and other in-ROM facts when targeting FRLG.

- **[smogon/pokemon-showdown](https://github.com/smogon/pokemon-showdown)** — Pokémon battle simulator and data (`data/`, `sim/`). Handy for cross-generation dex data, move/type mechanics, and damage simulation; treat as a secondary check against the actual game when story-mode rules or generation-specific quirks differ from competitive sim defaults.
