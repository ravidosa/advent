from utils import *
inp = input_file(2019, 5).strip()

parsed_input = parser(inp, [","])

program = parsed_input.copy()
_, out = intcode(program, [1])
p1 = out[-1]

program = parsed_input.copy()
_, out = intcode(program, [5])
p2 = out[0]

output(p1, p2)