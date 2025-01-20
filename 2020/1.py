from utils import *
inp = input_file(2020, 1).strip()

parsed_input = parser(inp, ["\n"])

for pair in itertools.combinations(parsed_input, 2):
    if sum(pair) == 2020:
        break
p1 = pair[0] * pair[1]

for trio in itertools.combinations(parsed_input, 3):
    if sum(trio) == 2020:
        break
p2 = trio[0] * trio[1] * trio[2]

output(p1, p2)