import re

f = open("2024/input-5.txt", "r")
inp1, inp2 = [i.split("\n") for i in f.read().split("\n\n")]

ordy = {}
for i in inp1:
    b, a = i.split("|")
    ordy[b] = ordy.get(b, []) + [a]

reg = re.compile("|".join([("((" + "|".join(ordy[k]) + ").*" + k + ")") for k in ordy.keys()]))

s = 0
for u in inp2:
    f = re.findall(reg, u)
    if len(f) != 0:
        while len(f) != 0:
            ff = [fff for fff in f[0] if len(fff) > 2]
            ind = u.index(ff[0])
            u = u[:ind] + ff[0][-2:] + ff[0][2:-2] + ff[0][:2] + u[ind + len(ff[0]):]
            f = re.findall(reg, u)
        ul = u.split(",")
        s += int(ul[(len(ul) - 1) // 2])
print(s)