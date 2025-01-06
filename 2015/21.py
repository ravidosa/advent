from utils import *
inp = open("2015/input-21.txt", "r").read().strip()

shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".split("\n\n")
weapons = parser(shop[0], ["Weapons:    Cost  Damage  Armor|\n", " "])
armors = parser(shop[1], ["Armor:      Cost  Damage  Armor|\n", " "])
rings = parser(shop[2], ["Rings:      Cost  Damage  Armor|\n", " "])
_, boss_hp, __, boss_damage, ___, boss_armor = parser(inp, ["\n|: "])
armors.append(["None", 0, 0, 0])

player_hp = 100
ming = math.inf
for combo in itertools.product(range(len(weapons)), range(len(armors)), itertools.combinations(range(len(rings)), 2)):
    w, a, ring = combo
    for r in [[], [ring[0]], [ring[1]], ring]:
        player_damage = weapons[w][2] + sum(map(lambda rr: rings[rr][3], r))
        player_armor = (0 if a == len(armors) else armors[a][3]) + sum(map(lambda rr: rings[rr][4], r))
        if math.ceil(player_hp / max(1, boss_damage - player_armor)) >= math.ceil(boss_hp / max(1, player_damage - boss_armor)):
            ming = min(ming, weapons[w][1] + (0 if a == len(armors) else armors[a][1]) + sum(map(lambda rr: rings[rr][2], r)))
print(ming)

maxg = 0
for combo in itertools.product(range(len(weapons)), range(len(armors)), itertools.combinations(range(len(rings)), 2)):
    w, a, ring = combo
    for r in [[], [ring[0]], [ring[1]], ring]:
        player_damage = weapons[w][2] + sum(map(lambda rr: rings[rr][3], r))
        player_armor = (0 if a == len(armors) else armors[a][3]) + sum(map(lambda rr: rings[rr][4], r))
        if math.ceil(player_hp / max(1, boss_damage - player_armor)) < math.ceil(boss_hp / max(1, player_damage - boss_armor)):
            maxg = max(maxg, weapons[w][1] + (0 if a == len(armors) else armors[a][1]) + sum(map(lambda rr: rings[rr][2], r)))
print(maxg)