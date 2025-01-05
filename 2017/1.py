from utils import *
inp = open("2017/input-1.txt", "r").read()

parsed_input = parser(inp, [""])

print(sum(map(lambda i: parsed_input[i] * (parsed_input[i] == parsed_input[(i + 1) % len(parsed_input)]), range(len(parsed_input)))))

print(sum(map(lambda i: parsed_input[i] * (parsed_input[i] == parsed_input[(i + len(parsed_input) // 2) % len(parsed_input)]), range(len(parsed_input)))))