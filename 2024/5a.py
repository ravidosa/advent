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
    if len(re.findall(reg, u)) == 0:
        ul = u.split(",")
        s += int(ul[(len(ul) - 1) // 2])
print(s)