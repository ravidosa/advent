from utils import *
inp = input_file(2024, 11).strip()

parsed_input = parser(inp, "{{li }}")

stone_ct = {i: parsed_input.count(i) for i in parsed_input}
stone = lambda i: [1] if i == 0 else divmod(i, 10 ** (dig // 2)) if ((dig := math.floor(math.log10(i)) + 1) % 2 == 0) else [2024 * i]
def next_stone_ct(stone_ct):
    new_stone_ct = {}
    for num in stone_ct:
        for new_num in stone(num):
            new_stone_ct[new_num] = new_stone_ct.get(new_num, 0) + stone_ct[num]
    return new_stone_ct


for _ in range(25):
    stone_ct = next_stone_ct(stone_ct)
p1 = sum(stone_ct.values())

for _ in range(75 - 25):
    stone_ct = next_stone_ct(stone_ct)
p2 = sum(stone_ct.values())

output(p1, p2)