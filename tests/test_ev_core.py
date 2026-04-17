from __future__ import annotations

import os
import sys
import unittest


# Allow `import ev_core` when running tests from any working directory.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from ev_core import battles_needed, ev_from_battle  # noqa: E402

# TODO: create a fixture for data used in tests
class TestEvCore(unittest.TestCase):
    def test_ev_from_battle_single_opponent(self) -> None:
        opp = {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1}
        self.assertEqual(ev_from_battle(opp), 1)

    def test_ev_from_battle_multiple_opponents(self) -> None:
        opps = [
            {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1},
            {"species": "Graveler", "ev_yield_stat": "defense", "ev_yield": 2},
        ]
        self.assertEqual(ev_from_battle(opps), 3)

    def test_battles_needed_single_opponent(self) -> None:
        trainee = {
            "species": "Magikarp",
            "target_stat": "speed",
            "current_evs": 0,
            "target_evs": 252,
        }
        opp = {"species": "Geodude", "ev_yield_stat": "defense", "ev_yield": 1}
        self.assertEqual(battles_needed(trainee, opp), 252)

    def test_battles_needed_higher_yield(self) -> None:
        trainee = {
            "species": "Magikarp",
            "target_stat": "speed",
            "current_evs": 0,
            "target_evs": 252,
        }
        opp = {"species": "Graveler", "ev_yield_stat": "defense", "ev_yield": 2}
        self.assertEqual(battles_needed(trainee, opp), 126)


if __name__ == "__main__":
    unittest.main()
