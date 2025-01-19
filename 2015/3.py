from utils import *
inp = input_file(2015, 3).strip()

vis = set()
pos = 0+0j
vis.add(pos)
for i in inp:
    pos += dir_sym[i]["comp"]
    vis.add(pos)
p1 = len(vis)

SANTAS = 2
vis = set()
for j in range(SANTAS):
    pos = 0+0j
    vis.add(pos)
    for i in inp[j::SANTAS]:
        pos += dir_sym[i]["comp"]
        vis.add(pos)
p2 = len(vis)

output(p1, p2)