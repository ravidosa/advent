from utils import *
inp = open("2022/input-1.txt", "r").read()

parsed_input = parser(inp, ["\n\n", "\n"])

print(max(map(sum, parsed_input)))

print(sum(sorted(map(sum, parsed_input))[-3:]))