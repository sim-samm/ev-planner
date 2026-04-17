# Development Roadmap

For domain rules and formulas see [ev_planner_spec_v3.md](ev_planner_spec_v3.md). For sub-problem breakdown and dependencies see [sub_problems.md](sub_problems.md).

**Rule:** Each stage must be usable on its own and prove the next stage's prerequisite. Do not start a stage until the previous stage's notebook cells run cleanly. After completing a stage, revisit the next stage's sketch and flesh it out before coding.

---

## Stage 1: One Pokemon, One Stat, One Opponent

**Deliverable:** `notebooks/01_ev_basics.ipynb`

Five micro-steps. Each is a notebook cell pair — markdown explanation above, code below.

### 1a — Define a trainee

Create a simple data structure for the pokemon being trained.

```python
trainee = {
    "species": "Magikarp",
    "target_stat": "speed",
    "current_evs": 0,
    "target_evs": 252,
}
```

**Proves:** We have a structure to hold pokemon state.

### 1b — Define an opponent

Create a separate data structure for the pokemon being fought.

```python
opponent = {
    "species": "Geodude",
    "ev_yield_stat": "defense",
    "ev_yield": 1,
}
```

**Proves:** Opponent data is separate from trainee data.

### 1c — Implement `ev_from_battle`

Simplest case — no items, no Exp. Share.

```python
def ev_from_battle(opponent_ev_yield):
    return opponent_ev_yield
```

**Proves:** The arithmetic engine exists and is testable.

### 1d — Calculate battles needed

First integration of data + math.

```python
import math

remaining = trainee["target_evs"] - trainee["current_evs"]
battles_needed = math.ceil(remaining / ev_from_battle(opponent["ev_yield"]))
```

**Proves:** The pipeline produces a usable answer (e.g. "KO 252 Geodude for 252 Def EVs").

### 1e — Add a second opponent, compare

Hardcode a second species and print both results side by side.

```python
opponent_b = {
    "species": "Graveler",
    "ev_yield_stat": "defense",
    "ev_yield": 2,
}
```

**Proves:** The framework generalizes beyond one opponent and seeds the comparison concept.

---

## Stage 2: Add Macho Brace

**Deliverable:** `held_items.ipynb`

Five micro-steps. Each is a notebook cell pair - markdown explanation above, code below.

### 2a - Define held-item state

Add simple held-item toggles and multipliers for the trainee.

```python
held_item_state = {
    "has_macho_brace": True,
    "macho_multiplier": 2,
}
```

**Proves:** Item state is explicit and can be passed into battle math.

### 2b - Extend `ev_from_battle` with item multiplier

Apply Macho Brace to the EV yield output while keeping base behavior available.

```python
def ev_from_battle(opponents, held_item_state=None):
    ...
```

**Proves:** EV arithmetic can incorporate held-item effects without breaking Stage 1 paths.

### 2c - Verify EV gain deltas

Run checkpoints that print EV gain with vs. without Macho Brace for the same opponent.

**Proves:** Item multiplier is active and numerically correct at the function level.

### 2d - Compare battles needed with vs. without item

Use the same trainee + opponent input and print both battle counts.

**Proves:** Item effect propagates from EV gain into planning output.

### 2e - Show side-by-side plan rows

Generate comparison rows for both states and print ordered output.

**Proves:** Stage 2 produces decision-ready output and sets up Stage 3 (vitamin layering).

---

## Stage 3: Add Vitamins (sketch)

**Deliverable:** Extend notebook

- Implement vitamin pre-loading: given a wallet, buy N vitamins first, battle the remainder.
- Enforce the 0–100 stat cap from Spec Section 5.
- **Proves:** Vitamin math is correct and reduces battles further.

---

## Stage 4: Full EV Spread for One Pokemon (sketch)

**Deliverable:** Extend notebook

- Target multiple stats (e.g. 252 Atk / 252 Spe / 4 HP).
- Different opponent per stat.
- Enforce per-stat (252) and total (508) caps.
- **Proves:** Constraints work together; this is a complete single-pokemon planner.

---

## Stage 5: Compare and Rank Battle Options (sketch)

**Deliverable:** Extend notebook, first touch of game data

- Introduce a small data set (5–10 opponents for one route).
- Rank by `ev_per_move`.
- **Proves:** The system can recommend "fight X instead of Y."

---

## Stage 6: Exp. Share + Sweeper (sketch)

**Deliverable:** Extend notebook

- Two pokemon: sweeper (battler) + trainee (Exp. Share holder).
- Implement `battle_is_useful` three-channel filter.
- **Proves:** Party dynamics and passive EV gain work.

---

## Future Stages

To be detailed after Stage 6 proves the foundation:

- Trainer battles + money / `ev_from_money`
- Full party of six
- OHKO heuristic
- `ev_per_operation` weighting
- Route optimization
- Experience tracking (see [thoughts.md](thoughts.md))
