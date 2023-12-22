f = open("2022/input-3.txt", "r")
inp = f.read().split("\n")
prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
prios = 0
for i in inp[:-1]:
    r1 = set(list(i[:len(i) // 2]))
    r2 = set(list(i[len(i) // 2:]))
    prios += (prio.index(list(r1.intersection(r2))[0]) + 1)
print(prios)