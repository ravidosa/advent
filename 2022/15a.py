f = open("2022/input-15.txt", "r")
inp = f.read().split("\n")
def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
y = 2000000
nb = set()
sbs = [[tuple([int(x[2:]) for x in i.split(": ")[0][10:].split(", ")]), tuple([int(x[2:]) for x in i.split(": ")[1][21:].split(", ")])] for i in inp[:-1]]
for sb in sbs:
    d = dist(sb[0], sb[1])
    nb.update(list(range(sb[0][0] - (d - abs(sb[0][1] - y)), sb[0][0] + (d - abs(sb[0][1] - y) + 1))))
    if sb[1][1] == y:
        nb.remove(sb[1][0])
    if sb[0][1] == y:
        nb.add(sb[0][0])
print(len(nb))