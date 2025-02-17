from utils import *
inp = input_file(2021, 7).strip()

parsed_input = parser(inp, "{{li,}}")

mincrab, maxcrab = min(parsed_input), max(parsed_input)

p1 = min(sum(abs(p - i) for p in parsed_input) for i in range(mincrab, maxcrab + 1))

p2 = min(sum((st := abs(p - i)) * (st + 1) // 2 for p in parsed_input) for i in range(mincrab, maxcrab + 1))

output(p1, p2)