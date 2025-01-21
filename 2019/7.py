from utils import *
from intcode import *
inp = input_file(2019, 7).strip()

parsed_input = parser(inp, [","])

max_out = -math.inf
for phase in itertools.permutations(range(5)):
    intcs = [Computer(parsed_input.copy(), [p]) for p in phase]
    intcs[0].push_in([0])
    sysc = System(intcs)
    for i in range(4):
        sysc.connect(i, i + 1)
    sysc.connect(4, System.OUT)
    out = sysc.run()
    max_out = max(max_out, out[-1])
p1 = max_out

max_out = -math.inf
for phase in itertools.permutations(range(5, 10)):
    intcs = [Computer(parsed_input.copy(), [p]) for p in phase]
    intcs[0].push_in([0])
    sysc = System(intcs)
    for i in range(5):
        sysc.connect(i, (i + 1) % 5)
    sysc.connect(4, System.OUT)
    out = sysc.run()
    max_out = max(max_out, out[-1])
p2 = max_out

output(p1, p2)