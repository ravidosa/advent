from utils import *
inp = input_file(2023, 18).strip()

parsed_input = parser(inp, ["\n", r" |\(|\)"])

verts = []
bord = 0
pos = (0, 0)
for d, l, _ in parsed_input:
    mov = dir_letter[d]["tup"]
    pos = tupadd(pos, (l * mov[0], l * mov[1]))
    verts.append(pos)
    bord += l
a = shoelace(verts)
p1 = int(abs(a) + 1 + bord // 2)

dir_hex = {"3": (-1, 0), "0": (0, 1), "1": (1, 0), "2": (0, -1)}
verts = []
bord = 0
pos = (0, 0)
for _, _, h in parsed_input:
    mov, l = dir_hex[h[-1]], int(h[1:-1], 16)
    pos = tupadd(pos, (l * mov[0], l * mov[1]))
    verts.append(pos)
    bord += l
a = int(shoelace(verts))
p2 = abs(a) + 1 + bord // 2

output(p1, p2)