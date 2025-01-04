from utils import *
inp = open("2017/input-5.txt", "r").read()

parsed_input = parser(inp, ["\n"])

pos, steps = 0, 0
while 0 <= pos < len(parsed_input):
    parsed_input[pos] += 1
    pos += parsed_input[pos] - 1
    steps += 1
print(steps)

parsed_input = parser(inp, ["\n"])
pos, steps = 0, 0
while 0 <= pos < len(parsed_input):
    parsed_input[pos] += (inc := (-1 if parsed_input[pos] >= 3 else 1))
    pos += parsed_input[pos] - inc
    steps += 1
print(steps)