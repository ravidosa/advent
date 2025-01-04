from utils import *
import itertools
inp = open("2015/input-9.txt", "r").read()

parsed_input = parser(inp, ["\n", " to | = "], [str, str, int])
gr = {}
locs = set()
for inp in parsed_input:
    l1, l2, cost = inp
    gr[(l1, l2)], gr[(l2, l1)] = cost, cost
    locs.update([l1, l2])

mind = sum(gr.values())
for route in itertools.permutations(locs):
    d = sum(map(lambda i: gr[(route[i], route[i + 1])], range(len(route) - 1)))
    mind = min(mind, d)
print(mind)

maxd = 0
for route in itertools.permutations(locs):
    d = sum(map(lambda i: gr[(route[i], route[i + 1])], range(len(route) - 1)))
    maxd = max(maxd, d)
print(maxd)