from utils import *
inp = input_file(2021, 7).strip()

parsed_input = parser(inp, [","])

mincrab, maxcrab = min(parsed_input), max(parsed_input)

p1 = min(map(lambda i: sum(map(lambda p: abs(p - i), parsed_input)), range(mincrab, maxcrab + 1)))

p2 = min(map(lambda i: sum(map(lambda p: (st := abs(p - i)) * (st + 1) // 2, parsed_input)), range(mincrab, maxcrab + 1)))

output(p1, p2)