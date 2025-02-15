from utils import *
inp = input_file(2015, 9).strip()

parsed_input = parser(inp, "{{s}} to {{s}} = {{i}}")

matrix = {}
locations = set()
for i in parsed_input:
    l1, l2, cost = i
    matrix[(l1, l2)], matrix[(l2, l1)] = cost, cost
    locations.update([l1, l2])
dist = lambda route: sum(matrix[(route[i], route[i + 1])] for i in range(len(locations) - 1))

p1 = minval(itertools.permutations(locations), key=dist)

p2 = maxval(itertools.permutations(locations), key=dist)

output(p1, p2)