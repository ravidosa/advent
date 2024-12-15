import itertools

f = open("2015/input-9.txt", "r")
inp = f.read().split("\n")

gr = {}
locs = set()

for i in inp:
    ed, cost = i.split(" = ")
    l1, l2 = ed.split(" to ")
    gr[(l1, l2)] = int(cost)
    gr[(l2, l1)] = int(cost)
    locs.add(l1)
    locs.add(l2)

maxd = 0

for route in itertools.permutations(locs):
    d = 0
    for i in range(len(route) - 1):
        d += gr[(route[i], route[i + 1])]
    if d > maxd:
        maxd = d
print(maxd)