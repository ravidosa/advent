from utils import *
inp = input_file(2024, 25).strip()

parsed_input = parser(inp, ["\n\n", "\n"])

w, h = len(parsed_input[0][0]), len(parsed_input[0]) - 2
locks, keys = [], []
for i in parsed_input:
    pins = [sum(map(lambda h: i[h][t] == "#", range(1, h + 1))) for t in range(w)]
    if all(map(lambda s: s == "#", i[0])) and all(map(lambda s: s == ".", i[-1])):
        locks.append(pins)
    if all(map(lambda s: s == ".", i[0])) and all(map(lambda s: s == "#", i[-1])):
        keys.append(pins)

p1 = sum(map(lambda pair: all(map(lambda t: pair[0][t] + pair[1][t] <= h, range(w))), itertools.product(locks, keys)))

output(p1)