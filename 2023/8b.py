from math import gcd
f = open("2023/input-8.txt", "r")
inp = f.read().split("\n")
lrdict = {}
iii = list(inp[0])
for i in inp[2:-1]:
    ii = i.split(" = ")
    lrdict[ii[0]] = ii[1][1:-1].split(", ")
loc = list(filter(lambda x: x[-1] == "A", lrdict.keys()))
lcm = 1
j = 0
while len(loc) > 0:
    loc = [lrdict[l][0 if iii[j % len(iii)] == "L" else 1] for l in loc]
    j += 1
    if "Z" in [l[-1] for l in loc]:
        lcm = lcm*j//gcd(lcm, j)
    loc = list(filter(lambda x: x[-1] != "Z", loc))
print(lcm)