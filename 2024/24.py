from utils import *
inp = open("2024/input-24.txt", "r").read().strip().split("\n\n")

parsed_input = parser(inp[0], ["\n", ": "])
connections = parser(inp[1], ["\n", " -> | "])
wire_dict = {i[0]: i[1] for i in parsed_input} | {c[-1]: c[:-1] for c in connections}
z = sum(map(lambda c: c[-1][0] == "z", connections))
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

print(int("".join(map(lambda i: str(val("z" + str(i).zfill(len(str(z))))), range(z)))[::-1], 2))

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
print(",".join(sorted(swapped)))