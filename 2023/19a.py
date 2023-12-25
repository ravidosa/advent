f = open("2023/input-19.txt", "r")
inp = f.read()[:-1]
wkfl, pt = [l.split("\n") for l in inp.split("\n\n")]
wkf = {"A": ["A"], "R": ["R"]}
for w in wkfl:
    wkf[w[:w.index("{")]] = [ww.split(":") for ww in w[w.index("{") + 1:-1].split(",")]
rat = 0
for p in pt:
    x, m, a, s = [int(pp[pp.index("=") + 1:]) for pp in p[1:-1].split(",")]
    w = "in"
    while w != "A" and w != "R":
        for ch in wkf[w]:
            if len(ch) > 1 and eval(ch[0]):
                w = ch[-1]
                break
            if len(ch) == 1:
                w = ch[0]
    if w == "A":
        rat += (x + m + a + s)
print(rat)