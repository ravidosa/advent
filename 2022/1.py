from utils import *
inp = input_file(2022, 1).strip().replace("\n", " ").replace("  ", "\n")

parsed_input = parser(inp, "{{li }}")

p1 = max(map(sum, parsed_input))

p2 = sum(sorted(map(sum, parsed_input))[-3:])

output(p1, p2)