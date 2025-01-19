from utils import *
inp = open("2015/input-9.txt", "r").read()

parsed_input = parser(inp, ["\n", " to | = "])

matrix = {}
locations = set()
for i in parsed_input:
    l1, l2, cost = i
    matrix[(l1, l2)], matrix[(l2, l1)] = cost, cost
    locations.update([l1, l2])

mind = sum(matrix.values())
for route in itertools.permutations(locations):
    d = sum(map(lambda i: matrix[(route[i], route[i + 1])], range(len(locations) - 1)))
    mind = min(mind, d)
print(mind)

maxd = 0
for route in itertools.permutations(locations):
    d = sum(map(lambda i: matrix[(route[i], route[i + 1])], range(len(locations) - 1)))
    maxd = max(maxd, d)
print(maxd)