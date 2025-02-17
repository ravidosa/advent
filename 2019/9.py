from utils import *
from intcode import *
inp = input_file(2019, 9).strip()

parsed_input = parser(inp, "{{li,}}")

program = parsed_input.copy()
intc = Computer(program, [1])
all(intc.run())
p1 = intc.pop_out()[0]

program = parsed_input.copy()
intc = Computer(program, [2])
all(intc.run())
p2 = intc.pop_out()[0]

output(p1, p2)