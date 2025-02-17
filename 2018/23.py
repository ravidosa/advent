from utils import *
inp = input_file(2018, 23).strip()

parsed_input = parser(inp, "pos=<{{i}},{{i}},{{i}}>, r={{i}}")

maxrob = max(parsed_input, key=lambda i: i[3])
p1 = sum(manhattan(r[:-1], maxrob[:-1]) <= maxrob[-1] for r in parsed_input)

output(p1)