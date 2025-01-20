from utils import *
inp = input_file(2017, 1).strip()

parsed_input = parser(inp, [""])

p1 = sum(map(lambda i: parsed_input[i] * (parsed_input[i] == parsed_input[(i + 1) % len(parsed_input)]), range(len(parsed_input))))

p2 = sum(map(lambda i: parsed_input[i] * (parsed_input[i] == parsed_input[(i + len(parsed_input) // 2) % len(parsed_input)]), range(len(parsed_input))))

output(p1, p2)