from utils import *
inp = input_file(2023, 9).strip()

parsed_input = parser(inp, "{{li }}")

def extrap(seq):
    ex = seq[-1]
    while any(seq):
        seq = [b - a for a, b in zip(seq, seq[1:])]
        ex += seq[-1]
    return ex
p1 = sum(extrap(i) for i in parsed_input)

def extrap(seq):
    ex = seq[0]
    parity = len(seq) % 2
    while len(seq) > 1:
        seq = [b - a for a, b in zip(seq, seq[1:])]
        ex = seq[0] - ex
    return ex * (-1) ** (1 - parity)
p2 = sum(extrap(i) for i in parsed_input)

output(p1, p2)