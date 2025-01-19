from utils import *
inp = input_file(2018, 23).strip()

parsed_input = parser(inp, ["\n", "pos=<|>, r=|,"])

maxrob = max(parsed_input, key=lambda i: i[3])
p1 = sum(map(lambda r: manhattan(r[:-1], maxrob[:-1]) <= maxrob[-1], parsed_input))

output(p1)