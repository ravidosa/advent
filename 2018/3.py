from utils import *
inp = open("2018/input-3.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", "#| @ |,|: |x"])
fabric_dict = {}

for i in parsed_input:
    _, x, y, w, h = i
    for c in range(x, x + w):
        for r in range(y, y + h):
            fabric_dict[c + r * 1j] = fabric_dict.get(c + r * 1j, 0) + 1
print(sum(map(lambda f: f >= 2, fabric_dict.values())))

for i in parsed_input:
    id, x, y, w, h = i
    if all(map(lambda pair: fabric_dict[pair[0] + pair[1] * 1j] == 1, itertools.product(range(x, x + w), range(y, y + h)))):
        break
print(id)