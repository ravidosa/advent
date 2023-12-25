f = open("2023/input-20.txt", "r")
inp = f.read().split("\n")
mods = {"button": {"typ": "butt", "to": ["broadcaster"]}, "output": {"typ": "out", "to": []}}
for i in inp[:-1]:
    if i[0] == "%":
        mods[i[1:i.index(" -> ")]] = {"typ": "flop", "to": i[i.index(" -> ") + 4:].split(", "), "stat": 0}
    elif i[0] == "&":
        mods[i[1:i.index(" -> ")]] = {"typ": "con", "to": i[i.index(" -> ") + 4:].split(", "), "inp": {}}
    else:
        mods["broadcaster"] = {"typ": "broad", "to": i[i.index(" -> ") + 4:].split(", ")}
for mod in mods:
    for s in mods[mod]["to"]:
        if s in mods and mods[s]["typ"] == "con":
            mods[s]["inp"][mod] = 0
lo = 0
hi = 0
def pulse(pul, m1, m2):
    global lo, hi
    lo += (pul == 0)
    hi += (pul == 1)
    if m1 in mods:
        if mods[m1]["typ"] == "broad":
            return [(pul, s, m1) for s in mods[m1]["to"]]
        if mods[m1]["typ"] == "flop" and pul == 0:
            mods[m1]["stat"] = int(not mods[m1]["stat"])
            return [(mods[m1]["stat"], s, m1) for s in mods[m1]["to"]]
        if mods[m1]["typ"] == "con":
            mods[m1]["inp"][m2] = pul
            if all(mods[m1]["inp"].values()):
                return [(0, s, m1) for s in mods[m1]["to"]]
            else:
                return [(1, s, m1) for s in mods[m1]["to"]]
    return []
q = []
for i in range(1000):
    q = q + [(0, "broadcaster", "button")]
    while len(q) > 0:
        p = q.pop(0)
        q = q + pulse(p[0], p[1], p[2])
print(lo * hi)