from utils import *
inp = open("2016/input-4.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", r"-|\[|\]"])

real = lambda room: room[-2] * ("".join(sorted(lower, key=lambda l: -("".join(room[:-2]).count(l))))[:5] == room[-1])
print(sum(map(real, parsed_input)))

for inp in parsed_input:
    if "north" in "".join(map(lambda l: lower[(lower.index(l) + inp[-2]) % 26] if l != " " else l, " ".join(inp[:-2]))):
        print(inp[-2])