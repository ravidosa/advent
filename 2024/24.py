from utils import *
inp = input_file(2024, 24).strip().split("\n\n")

parsed_input = parser(inp[0], "{{s}}: {{i}}")
connections = parser(inp[1], "{{s}} {{s}} {{s}} -> {{s}}")

wire_dict = {i[0]: i[1] for i in parsed_input} | {c[-1]: c[:-1] for c in connections}
z = sum(c[-1][0] == "z" for c in connections)
def val(wir):
    if type(wire_dict[wir]) is int:
        return wire_dict[wir]
    else:
        if wire_dict[wir][1] == "AND":
            wire_dict[wir] = val(wire_dict[wir][0]) & val(wire_dict[wir][2])
        elif wire_dict[wir][1] == "OR":
            wire_dict[wir] = val(wire_dict[wir][0]) | val(wire_dict[wir][2])
        elif wire_dict[wir][1] == "XOR":
            wire_dict[wir] = val(wire_dict[wir][0]) ^ val(wire_dict[wir][2])
        return wire_dict[wir]

p1 = int("".join(str(val("z" + str(i).zfill(len(str(z))))) for i in range(z))[::-1], 2)

swapped = set()
for conn in connections:
    op1, op, op2, res = conn
    if res[0] == "z" and op != "XOR" and int(res[1:]) != z:
        swapped.add(res)
    if op == "XOR" and op1[0] not in "xyz" and op2[0] not in "xyz" and res[0] not in "xyz":
        swapped.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subconn in connections:
            subop1, subop, subop2, subres = subconn
            if (res == subop1 or res == subop2) and subop != "OR":
                swapped.add(res)
    if op == "XOR":
        for subconn in connections:
            subop1, subop, subop2, subres = subconn
            if (res == subop1 or res == subop2) and subop == "OR":
                swapped.add(res)
p2 = ",".join(sorted(swapped))

output(p1, p2)