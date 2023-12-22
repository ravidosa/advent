f = open("2022/input-3.txt", "r")
inp = f.read().split("\n")
prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
prios = 0
for i in range((len(inp) - 1) // 3):
    r1 = set(list(inp[3 * i]))
    r2 = set(list(inp[3 * i + 1]))
    r3 = set(list(inp[3 * i + 2]))
    prios += (prio.index(list(r1.intersection(r2.intersection(r3)))[0]) + 1)
print(prios)