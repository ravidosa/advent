from utils import *
inp = input_file(2024, 7).strip()

parsed_input = parser(inp, ["\n", ": | "])
def evally(vals, ops):
    res = vals[0]
    for ind, op in enumerate(ops):
        if op == "+":
            res += vals[ind + 1]
        elif op == "*":
            res *= vals[ind + 1]
        else:
            res = int(str(res) + str(vals[ind + 1]))
    return res

p1 = sum(map(lambda i: i[0] * any(map(lambda c: evally(i[1: ], c) == i[0], map(lambda j: map(lambda pos: "+" if pos == "0" else "*", format(j, "0" + str(len(i) - 2) + 'b')), range(2 ** (len(i) - 2))))), parsed_input))

p2 = sum(map(lambda i: i[0] * any(map(lambda c: evally(i[1: ], c) == i[0], map(lambda j: map(lambda pos: "+" if pos == "0" else "*" if pos == "1" else "||", dec_to_tern(j, len(i) - 2)), range(3 ** (len(i) - 2))))), parsed_input))

output(p1, p2)