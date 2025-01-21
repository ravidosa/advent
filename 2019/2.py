from utils import *
inp = input_file(2019, 2).strip()

parsed_input = parser(inp, [","])

program = parsed_input.copy()
program[1], program[2] = 12, 2
reg, _ = intcode(program)
p1 = reg[0]

found = False
for noun in range(100):
    for verb in range(100):
        program = parsed_input.copy()
        program[1], program[2] = noun, verb
        reg, _ = intcode(program)
        if reg and reg[0] == 19690720:
            found = True
            break
    if found:
        break
p2 = 100 * noun + verb

output(p1, p2)