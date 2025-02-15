from utils import *
inp = input_file(2017, 5).strip()

parsed_input = parser(inp)

instr = parsed_input.copy()
pos, steps = 0, 0
while 0 <= pos < len(instr):
    instr[pos] += 1
    pos += instr[pos] - 1
    steps += 1
p1 = steps

instr = parsed_input.copy()
pos, steps = 0, 0
while 0 <= pos < len(instr):
    instr[pos] += (inc := (-1 if instr[pos] >= 3 else 1))
    pos += instr[pos] - inc
    steps += 1
p2 = steps

output(p1, p2)