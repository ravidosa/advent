from utils import *
inp = input_file(2021, 6).strip()

parsed_input = parser(inp, "{{li,}}")

fish_ct = {i: parsed_input.count(i) for i in parsed_input}
def next_fish_ct(fish_ct):
    new_fish_ct = {i: fish_ct.get(i + 1, 0) for i in range(8)}
    new_fish_ct[8] = fish_ct.get(0, 0)
    new_fish_ct[6] += fish_ct.get(0, 0)
    return new_fish_ct

for _ in range(80):
    fish_ct = next_fish_ct(fish_ct)
p1 = sum(fish_ct.values())

for _ in range(256 - 80):
    fish_ct = next_fish_ct(fish_ct)
p2 = sum(fish_ct.values())

output(p1, p2)