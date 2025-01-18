from utils import *
inp = open("2015/input-3.txt", "r").read().strip()

vis = set()
pos = 0+0j
vis.add(pos)
for i in inp:
    pos += dir_sym[i]["comp"]
    vis.add(pos)
print(len(vis))

SANTAS = 2
vis = set()
for j in range(SANTAS):
    pos = 0+0j
    vis.add(pos)
    for i in inp[j::SANTAS]:
        pos += dir_sym[i]["comp"]
        vis.add(pos)
print(len(vis))