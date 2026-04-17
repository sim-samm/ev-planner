# What is an EV?
EV stands for "Effort Value" and they are used to increase a certain stat of a pokemon.
They allow a trainer to tune a pokemon for key battle situations, and make pokemon's strengths shine.

# Motivation
EV training is a time consuming process. It is worthwile to devote time
to minimize time spent training.

## Example with no Optimizations
- Each mokemon can at most earn 508 EVs
- Each pokemon defeated awards approximately 1-3 EVs
- To train one pokemon means 170 - 508 pokemon are defeated
- If training a new team of six this could mean 1020 - 3048 battles
TODO: follow this example in the worst case for all Optimizations
- maybe do code blocks throught to build up logic

# Methods of Obtaining EVs
1. Battling pokemon
2. Apply vitamins

## Battling pokemon
Each pokemon battled will yield some amount of EVs. They will be applied to one or more
stats of the pokemon who defeated them.

### Nuances
- Trainers may be battled again after 100 steps by using a VS. Seeker.
  - This can be used as a repeataple method for good source of EVs
  - However, a trainer may not always want to re-match
    - 100 steps is the minimum amount of steps, after which it would be a multiple of 100
- Wild pokemon are encountered in fewer stps, but thier encounter rate is normally not 100%
  - A repel trick with a fainted pokemon may be used to filter a pokemon encounter to 100%

## Vitamins
- Purchased for $9800
- Yield 10 EVs Each
- Only apply to the first 100 EVs of a pokemon's stat

# Increasing EV Yield with Items
The key items are the Macho Brace, Exp. Share, and Amulet Coin.

- Macho Brace: doubles the base EVs earned for the pokemon holding it in battle.
- Exp. Share: shares the base EVs the battler recieved (before any adjustments)
- Amulet Coin: doubles the money rewarded from battles (effectively doubles the amount of vitamins you can afford)

# Putting it All Together
Objective: Minimize the number of moves needed to reach an exact EV total.

- Explanation: Pokemon are defeated with a number of moves (which can be tracked easily in game). Exact EVs are important to reach, as every 4 equate to 1 stat point at level 100, if exact totals are missed, stat points will be missed (especially important for speed tie-breaks).

It is useful to use the ratio of EVs : Moves. This metric helps guide whether certain battles are worthwile compared to others. 

## Modeling All Battles as EVs per Move

### Receiving from one opponent
```python
# Opponent Yield - depend on lookups
opponent_ev_yield = 1 # use 1 as an example (for worst case)

# Pokemon in battle can hold combination of 5 different states
if sweeper_state:
  # sweepers (trained high-level pokemon for OHKOs)
  # can assume a OHKO, 1 move per pokemon
if trained_state:
  # Must check first as this overides amulet and macho states
  battler_factor = 0 
elif amulet_state or default :
  battler_factor = 1 # battler only recieves base EVs from opponent 
else:
  macho_state = 2 # battler recieves double the EVs from opponent

# Pokemon outside of battle can hold two states
if exp_shared_state:
  shared_evs = opponent_ev_yield # pokemon holding exp. share recieves base EVs from opponent
else: 
  shared_evs = 0 # pokemon not holding exp.share recieves no EVs

# Calculates EVs from Pokemon
evs_from_pokemon = (opponent_ev_yield * battler_factor) + shared_evs
```

### Recieving EVs from Money
```python
# TODO: work out a cohesive strategy for state varialbes
# either boolean or ints

vitamin_ev_yield = 10
vitamin_cost = 9800

# amulet was useful as a boolean above, but useful as an int here
evs_from_money = ((money_rewarded * amulet_state) / vitamin_cost) * vitamin_ev_yield
```

### Battle Types
#### Wild Pokemon Battles
```python
# TODO: prove that a OHKO sweeper gains at least as many EVs as 2HKO macho in the same amount of time
# measure in number of operations as a heuristic
# constants can be ignored (encounter rate, battle open, battle close)
# focus on variables (# of moves, healing, status, recovery)

moves_per_ko = 1 # assume a OHKO

# Formula
wild_battle_evs = evs_from_pokemon / moves_per_ko

# TODO: decide on a convetion for ev variables, either prefix or suffix
```

#### Trainer Pokemon Battles
```python
# Very much psuedo code, as it relies on a lot of undefined code in todos
# TODO: create a pokemon class that calculates EV yield

# Example Party
opponent_party = {nidorino, sandshrew}

def trainer_battle_evs():
  for pokemon in opponent_party:
    # TODO: create a class representing player's party (item holding, ev totals, etc.)
    # probably related to opponent_party in a hierarchy
    ev_sum += pokemon.evs_from_pokemon(player_party) + evs_from_money
  return ev_sum / len(opponent_party)
```

# Constraints
- If evs_from_pokemon do not correspond to a needed battler EV (remaining corresponding EVs are 0)
  - then we can only consider evs_from_money
    - and there must be other player_party members whos current EV levels are between 0 and 90
    - otherwise the evs_from_money cannot be considered (effectively 0)

# Known Assumptions
- All pokemons are consedered as OHKOs (one hit knock outs)
  - useful because 1 move will be used per pokemon
  - TODO: determin if a battler can sweep somehow
    - Heuristic:
      - if a battler knows a strong stab move that is super effecitve and is greater than or equal to opponent_level - 5
      - or if battler knows a strong stab move that hits neutrally and is greater than or equal to opponent_level + 10
  - if a pokemon cannot OHKO then a trained sweeper will be used

# When to apply EVs from Money
If wallet >= 9800 and EVs for any player_party member are 0 <= EVs <= 90

## Batching
When future funds will be a factor of 9800 and any player_party member EVs will be:

```python
vitamin_ev_limit = 100
# 0 <= EVs <= vitamin_ev_limit - (factor * vitamin_ev_yield)
```