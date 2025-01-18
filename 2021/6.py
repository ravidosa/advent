from utils import *
inp = open("2021/input-6.txt", "r").read()

parsed_input = parser(inp, [","])

fish_ct = {i: parsed_input.count(i) for i in parsed_input}

for _ in range(80):
    new_fish_ct = {i: fish_ct.get(i + 1, 0) for i in range(8)}
    new_fish_ct[8] = fish_ct.get(0, 0)
    new_fish_ct[6] += fish_ct.get(0, 0)
    fish_ct = new_fish_ct
print(sum(fish_ct.values()))

for _ in range(256 - 80):
    new_fish_ct = {i: fish_ct.get(i + 1, 0) for i in range(8)}
    new_fish_ct[8] = fish_ct.get(0, 0)
    new_fish_ct[6] += fish_ct.get(0, 0)
    fish_ct = new_fish_ct
print(sum(fish_ct.values()))