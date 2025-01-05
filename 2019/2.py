from utils import *
inp = open("2019/input-2.txt", "r").read().strip()

parsed_input = parser(inp, [","])

program = parsed_input.copy()
program[1], program[2] = 12, 2
res = intcode(program)
print(res[0])

found = False
for noun in range(100):
    for verb in range(100):
        program = parsed_input.copy()
        program[1], program[2] = noun, verb
        res = intcode(program)
        if res and res[0] == 19690720:
            found = True
            break
    if found:
        break
print(100 * noun + verb)