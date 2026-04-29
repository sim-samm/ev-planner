"""Held-item EV math that composes the Stage 1 core helpers."""

import math

from ev_core import ev_from_battle


def ev_from_battle_with_held_item(opponents, held_item):
    """Return battle EV yield after applying the held item's EV multiplier.

    held_item is expected to include:
      - ev_multiplier (int)

    Other item metadata, such as speed_multiplier, is intentionally ignored by
    EV math and can be used later by operation-cost planning.
    """

    return ev_from_battle(opponents) * held_item["ev_multiplier"]


def battles_needed_with_held_item(trainee, opponents, held_item):
    """Return battles needed when the trainee's held item modifies EV yield."""

    remaining_evs_needed = trainee["target_evs"] - trainee["current_evs"]
    ev_gain = ev_from_battle_with_held_item(opponents, held_item)
    return math.ceil(remaining_evs_needed / ev_gain)
