from __future__ import annotations

import os
import sys
import unittest


# Allow `import ev_items` when running tests from any working directory.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from ev_items import (  # noqa: E402
    battles_needed_with_held_item,
    ev_from_battle_with_held_item,
)


class TestEvItems(unittest.TestCase):
    def test_macho_brace_doubles_single_opponent_ev_gain(self) -> None:
        opp = {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1}
        held_item = {"item": "Macho Brace", "ev_multiplier": 2}
        self.assertEqual(ev_from_battle_with_held_item(opp, held_item), 2)

    def test_macho_brace_doubles_multiple_opponent_ev_gain(self) -> None:
        opps = [
            {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1},
            {"species": "Graveler", "ev_yield_stat": "defense", "ev_yield": 2},
        ]
        held_item = {"item": "Macho Brace", "ev_multiplier": 2}
        self.assertEqual(ev_from_battle_with_held_item(opps, held_item), 6)

    def test_battles_needed_uses_boosted_ev_gain(self) -> None:
        trainee = {
            "species": "Magikarp",
            "target_stat": "speed",
            "current_evs": 0,
            "target_evs": 252,
        }
        opps = [
            {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1},
            {"species": "Graveler", "ev_yield_stat": "defense", "ev_yield": 2},
        ]
        held_item = {"item": "Macho Brace", "ev_multiplier": 2}
        self.assertEqual(battles_needed_with_held_item(trainee, opps, held_item), 42)

    def test_speed_multiplier_does_not_affect_ev_battle_count(self) -> None:
        trainee = {
            "species": "Magikarp",
            "target_stat": "speed",
            "current_evs": 0,
            "target_evs": 252,
        }
        opps = [
            {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1},
            {"species": "Graveler", "ev_yield_stat": "defense", "ev_yield": 2},
        ]
        held_item = {
            "item": "Macho Brace",
            "ev_multiplier": 2,
            "speed_multiplier": 0.5,
        }
        self.assertEqual(battles_needed_with_held_item(trainee, opps, held_item), 42)


if __name__ == "__main__":
    unittest.main()
