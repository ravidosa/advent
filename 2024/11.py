from utils import *
inp = open("2024/input-11.txt", "r").read()

parsed_input = parser(inp, [" "])

stone_ct = {i: parsed_input.count(i) for i in parsed_input}
stone = lambda i: [1] if i == 0 else divmod(i, 10 ** (dig // 2)) if ((dig := math.floor(math.log10(i)) + 1) % 2 == 0) else [2024 * i]

for _ in range(25):
    new_stone_ct = {}
    for num in stone_ct:
        for new_num in stone(num):
            new_stone_ct[new_num] = new_stone_ct.get(new_num, 0) + stone_ct[num]
    stone_ct = new_stone_ct
print(sum(stone_ct.values()))

for _ in range(75 - 25):
    new_stone_ct = {}
    for num in stone_ct:
        for new_num in stone(num):
            new_stone_ct[new_num] = new_stone_ct.get(new_num, 0) + stone_ct[num]
    stone_ct = new_stone_ct
print(sum(stone_ct.values()))