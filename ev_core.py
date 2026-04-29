"""Core EV math shared across demos and tests.

Stage 1 baseline only. New mechanics should add new concrete functions that
compose these helpers rather than rewriting them.
"""

import math


def ev_from_battle(opponents):
    """Return total EV yield from one battle against one or more opponents.

    opponents:
      - a single opponent dict, OR
      - an iterable (for example a list) of opponent dicts

    Each opponent dict is expected to include:
      - species (str)
      - ev_yield_stat (str)
      - ev_yield (int)

    Returns:
      int total EV yield from the battle
    """

    entries = [opponents] if isinstance(opponents, dict) else list(opponents)
    return sum(opp["ev_yield"] for opp in entries)


def battles_needed(trainee, opponents):
    """Return battles needed to reach target EVs for the trainee's current stat.

    trainee is expected to include:
      - target_evs (int)
      - current_evs (int)

    opponents follows the same shape rules as `ev_from_battle`.
    """

    remaining_evs_needed = trainee["target_evs"] - trainee["current_evs"]
    ev_gain = ev_from_battle(opponents)
    return math.ceil(remaining_evs_needed / ev_gain)
