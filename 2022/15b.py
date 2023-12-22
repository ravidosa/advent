f = open("2022/input-15.txt", "r")
inp = f.read().split("\n")
def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
sbs = [[tuple([int(x[2:]) for x in i.split(": ")[0][10:].split(", ")]), tuple([int(x[2:]) for x in i.split(": ")[1][21:].split(", ")])] for i in inp[:-1]]
b = set()
m = 4000000
bc = None
fslash = []
bslash = []
for sb in sbs:
    d = dist(sb[0], sb[1]) + 1
    #y = (x - (sb1[0] + d1)) + sb[1] = x + sb[1] - (sb[0] + d1)
    #y = (x - (sb1[0] - d1)) + sb[1] = x + sb[1] - (sb[0] - d1)
    #y = -(x - (sb1[0] + d1)) + sb[1] = -x + sb[1] + (sb[0] + d1)
    #y = -(x - (sb1[0] - d1)) + sb[1] = -x + sb[1] + (sb[0] - d1)
    fslash.extend([sb[0][1] - (sb[0][0] + d), sb[0][1] - (sb[0][0] - d)])
    bslash.extend([sb[0][1] + (sb[0][0] + d), sb[0][1] + (sb[0][0] - d)])
for f in fslash:
    for b in bslash:
        p = ((b - f) // 2, (b + f) // 2)
        bc_f = True
        for sb in sbs:
            if dist(sb[0], sb[1]) >= dist(sb[0], p):
                bc_f = False
                break
        if bc_f and 0 <= p[0] and p[0] <= m and 0 <= p[1] and p[1] <= m:
            bc = p
            break
    if bc:
        break
print(4000000 * bc[0] + bc[1])