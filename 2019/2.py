from utils import *
from intcode import *
inp = input_file(2019, 2).strip()

parsed_input = parser(inp, "{{li,}}")

program = parsed_input.copy()
program[1], program[2] = 12, 2
intc = Computer(program)
all(intc.run())
p1 = intc[0]

for noun, verb in itertools.product(range(100), repeat = 2):
    program = parsed_input.copy()
    program[1], program[2] = noun, verb
    intc = Computer(program)
    all(intc.run())
    if intc[0] == 19690720:
        break
p2 = 100 * noun + verb

output(p1, p2)