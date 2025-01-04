from utils import *
import itertools, math
inp = open("2015/input-21.txt", "r").read()
inpinp = inp.split("\n\n")

weapons = parser(inpinp[0], ["Weapons:    Cost  Damage  Armor|\n", " "], [str, int, int, int])
armors = parser(inpinp[1], ["Armor:      Cost  Damage  Armor|\n", " "], [str, int, int, int])
rings = parser(inpinp[2], ["Rings:      Cost  Damage  Armor|\n", " "], [str, int, int, int, int])
_, boss_hp, __, boss_damage, ___, boss_armor = parser(inpinp[3], ["\n|:"], [str, int, str, int, str, int])

player_hp = 100
ming = math.inf
for w in range(len(weapons)):
    for a in range(len(armors) + 1):
        for rc in range(2):
            for r in itertools.combinations(range(len(rings)), rc):
                player_damage = weapons[w][2] + sum(map(lambda rr: rings[rr][3], r))
                player_armor = (0 if a == len(armors) else armors[a][3]) + sum(map(lambda rr: rings[rr][4], r))
                if boss_damage - player_armor != 0 and player_damage - boss_armor != 0 and math.ceil(player_hp // (boss_damage - player_armor)) > math.ceil(boss_hp // (player_damage - boss_armor)):
                    ming = min(ming, weapons[w][1] + (0 if a == len(armors) else armors[a][1]) + sum(map(lambda rr: rings[rr][2], r)))
print(ming)