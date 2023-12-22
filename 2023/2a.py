f = open("2023/input-2.txt", "r")
inp = f.read().split("\n")
s = 0
for ind, i in enumerate(inp[:-1]):
    sets = (i[i.index(":") + 2:]).split("; ")
    good = True
    for bl in sets:
        dic = {"red": 0, "green": 0,  "blue": 0}
        for k in bl.split(", "):
            m  = k.split(" ")
            dic[m[1]] += int(m[0])
        if not (dic["red"] <= 12 and dic["green"] <= 13 and dic["blue"] <= 14):
            good = False
    s += int(good) * (ind + 1)
print(s)