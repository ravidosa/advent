from utils import *
inp = input_file(2017, 2).strip()

parsed_input = parser(inp, "{{li\t}}")

p1 = sum(max(i[0]) - min(i[0]) for i in parsed_input)

p2 = sum(max(pair) // min(pair) for i in parsed_input for pair in itertools.combinations(i[0], 2) if max(pair) % min(pair) == 0)

output(p1, p2)
