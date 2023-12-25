f = open("2023/input-19.txt", "r")
inp = f.read()[:-1]
wkfl, pt = inp.split("\n\n")
wkf = {"A": ["A"], "R": ["R"]}
for w in wkfl.split("\n"):
    wkf[w[:w.index("{")]] = [ww.split(":") for ww in w[w.index("{") + 1:-1].split(",")]
def splitty(r, rng):
    ch, inq, vally = r
    rng2 = []
    for rn in rng:
        rn = list(rn)
        if inq:
            rn[ch] = (max(rn[ch][0], vally + 1), rn[ch][1])
        else:
            rn[ch] = (rn[ch][0], min(rn[ch][1], vally - 1))
        if rn[ch][0] <= rn[ch][1]:
            rng2.append(tuple(rn))
    return rng2
def accy(r):
    if r[0] == "R":
        return []
    elif r[0] == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    elif len(r[0]) == 1:
        return accy(wkf[r[0][0]])
    else:
        yee = splitty(("xmas".index(r[0][0][0]), r[0][0][1] == ">", int(r[0][0][2:])), accy(wkf[r[0][1]]))
        nee = splitty(("xmas".index(r[0][0][0]), not r[0][0][1] == ">", int(r[0][0][2:]) + (1 if r[0][0][1] == ">" else -1)), accy(r[1:]))
        return yee + nee
tot = 0
rng = accy(wkf["in"])
for rn in rng:
    m = 1
    for r in rn:
        m *= (r[1] - r[0] + 1)
    tot += m
    print(m)
print(tot)