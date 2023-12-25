f = open("2023/input-22.txt", "r")
inp = f.read()[:-1]
br = sorted([tuple([tuple([int(x) for x in bb.split(",")]) for bb in b.split("~")]) for b in inp.split("\n")], key=lambda b: b[0][2])
def cov(b):
    if b[0][0] < b[1][0]:
        return [ (x, b[0][1], b[0][2]) for x in range(b[0][0], b[1][0]+1)]
    elif b[0][1] < b[1][1]:
        return [ (b[0][0], y, b[0][2]) for y in range(b[0][1], b[1][1]+1)]
    elif b[0][2] < b[1][2]:
        return [ (b[0][0], b[0][1], z) for z in range(b[0][2], b[1][2]+1)]
    else:
        return [b[1]]
drbr = []
occ = set()
for b in br:
    bd = b
    while all(c not in occ for c in cov(((bd[0][0], bd[0][1], bd[0][2] - 1), (bd[1][0], bd[1][1], bd[1][2] - 1)))) and bd[0][2] >= 2:
        bd = ((bd[0][0], bd[0][1], bd[0][2] - 1), (bd[1][0], bd[1][1], bd[1][2] - 1))
    drbr.append(bd)
    for c in cov(bd):
        occ.add(c)
drbr = sorted(drbr, key=lambda b: b[0][2])
def suppy(b1, b2):
    c1, c2 = cov(b1), cov(b2)
    for c in c1:
        if (c[0], c[1], c[2] + 1) in c2:
            return True
    return False
supped = {}
for i1, b1 in enumerate(drbr):
    for i2, b2 in enumerate(drbr):
        if b2[0][2] > b1[1][2] + 1:
            break
        if i2 > i1 and suppy(b1, b2):
            supped[i2] = supped.get(i2, []) + [i1]
dis = {}
for i in range(len(drbr)):
    for j in range(len(drbr)):
        if supped.get(j, []) == [i]:
            dis[i] = dis.get(i, []) + [j]
print(sum([dis.get(i, []) == [] for i in range(len(drbr))]))