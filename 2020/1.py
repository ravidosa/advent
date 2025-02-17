from utils import *
inp = input_file(2020, 1).strip()

parsed_input = parser(inp)

for pair in itertools.combinations(parsed_input, 2):
    if sum(pair) == 2020:
        break
p1 = prod(pair)

for trio in itertools.combinations(parsed_input, 3):
    if sum(trio) == 2020:
        break
p2 = prod(trio)

output(p1, p2)