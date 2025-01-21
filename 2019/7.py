from utils import *
inp = input_file(2019, 7).strip()

parsed_input = parser(inp, [","])

max_out = -math.inf
for phase in itertools.permutations(range(5)):
    sig = 0
    for i in range(5):
        program = parsed_input.copy()
        _, out = intcode(program, [phase[i], sig])
        sig = out[0]
    max_out = max(max_out, sig)
p1 = max_out

output(p1, p2)