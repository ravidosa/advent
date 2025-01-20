from utils import *
inp = input_file(2024, 25).strip()

parsed_input = parser(inp, ["\n\n", "\n"])

w, h = len(parsed_input[0][0]), len(parsed_input[0]) - 2
locks, keys = [], []
for i in parsed_input:
    pins = [sum(i[c][t] == "#" for c in range(1, h + 1)) for t in range(w)]
    if all(s == "#" for s in i[0]) and all(s == "." for s in i[-1]):
        locks.append(pins)
    if all(s == "." for s in i[0]) and all(s == "#" for s in i[-1]):
        keys.append(pins)

p1 = sum(all(l[t] + k[t] <= h for t in range(w)) for l, k in itertools.product(locks, keys))

output(p1)