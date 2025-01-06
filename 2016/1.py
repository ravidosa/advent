from utils import *
inp = open("2016/input-1.txt", "r").read().strip()

parsed_input = parser(inp, [", "], lambda i: [i[0], int(i[1:])])

pos, dir = 0+0j, 0+1j
for inp in parsed_input:
    dir *= (0+1j if inp[0] == "L" else 0-1j)
    pos += inp[1] * dir
print(abs(int(pos.real)) + abs(int(pos.imag)))

vis = set()
pos, dir = 0+0j, 0+1j
vis.add(pos)
for inp in parsed_input:
    dir *= (0+1j if inp[0] == "L" else 0-1j)
    rep = False
    for i in range(inp[1]):
        pos += dir
        if pos in vis:
            rep = True
            break
        else:
            vis.add(pos)
    if rep:
        break
print(abs(int(pos.real)) + abs(int(pos.imag)))