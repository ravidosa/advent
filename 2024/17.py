from utils import *
inp = input_file(2024, 17).strip().split("\n\n")

parsed_input = parser(inp[1], ["Program: |,"])
a, b, c = parser(inp[0], ["Register A: |Register B: |Register C: "])

i = 0
ct = 0
output = []
while i < len(parsed_input) and ct < 100:
    ct += 1
    opcode = parsed_input[i]
    operand = parsed_input[i + 1]

    literal = operand
    combo = operand if 0 <= operand <= 3 else a if operand == 4 else b if operand == 5 else c

    if opcode == 0:
        a = a // (2 ** combo)
        i += 2
    if opcode == 1:
        b = b ^ literal
        i += 2
    if opcode == 2:
        b = combo % 8
        i += 2
    if opcode == 3:
        if a != 0:
            i = literal
        else:
            i += 2
    if opcode == 4:
        b = b ^ c
        i += 2
    if opcode == 5:
        output.append(combo % 8)
        i += 2
    if opcode == 6:
        b = a // (2 ** combo)
        i += 2
    if opcode == 7:
        c = a // (2 ** combo)
        i += 2
p1 = ",".join(map(str, output))

x = z3.BitVec('x', 3 * len(parsed_input) + 1)
opt = z3.Optimize()
for i in range(len(parsed_input)):
    opt.add_soft(((((x >> (3 * i)) & 7) ^ 5) ^ 6 ^ ((x >> (3 * i)) >> (((x >> (3 * i)) & 7) ^ 5))) & 7 == parsed_input[i])
h = opt.minimize(x)
opt.check()
p2 = h.value()

output(p1, p2)