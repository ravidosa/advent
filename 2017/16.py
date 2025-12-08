from utils import *
inp = input_file(2017, 16).strip()

parsed_input = parser(inp, "{{le,}}")

ini = "abcdefghijklmnop"

def perm(progs):
    progs = list(progs)
    for i in parsed_input:
        if i[0] == "s":
            x = int(i[1:])
            progs = progs[-x:] + progs[:-x]
        if i[0] == "x":
            a, b = i[1:].split("/")
            a, b = int(a), int(b)
            progs[a], progs[b] = progs[b], progs[a]
        if i[0] == "p":
            a, b = i[1:].split("/")
            idx_a, idx_b = progs.index(a), progs.index(b)
            progs[idx_a], progs[idx_b] = b, a
    return "".join(progs)

p1 = perm(ini)

cyc = [ini]
p = ini
while (p_ := perm(p)) not in cyc:
    cyc.append(p_)
    p = p_
p2 = cyc[(1000000000 - cyc.index(p_)) % (len(cyc) - cyc.index(p_))]

output(p1, p2)