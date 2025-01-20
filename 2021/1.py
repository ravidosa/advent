from utils import *
inp = input_file(2021, 1).strip()

parsed_input = parser(inp, ["\n"])

p1 = sum(parsed_input[i - 1] < parsed_input[i] for i in range(1, len(parsed_input)))

p2 = sum(sum(parsed_input[i - 3: i]) < sum(parsed_input[i - 2: i + 1]) for i in range(3, len(parsed_input)))

output(p1, p2)