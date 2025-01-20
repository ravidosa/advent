from utils import *
inp = input_file(2018, 25).strip()

parsed_input = parser(inp, ["\n", ","])

const = []
for i in parsed_input:
    con = [i]
    other = []
    for chcon in const:
        if any(manhattan(i, c) <= 3 for c in chcon):
            con += chcon
        else:
            other.append(chcon)
    const = other + [con]
p1 = len(const)

output(p1)