from utils import *
inp = input_file(2022, 1).strip()

parsed_input = parser(inp, ["\n\n", "\n"])

print(max(map(sum, parsed_input)))

print(sum(sorted(map(sum, parsed_input))[-3:]))