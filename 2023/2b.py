f = open("2023/input-2.txt", "r")
inp = f.read().split("\n")
s = 0
for ind, i in enumerate(inp[:-1]):
    sets = (i[i.index(":") + 2:]).split("; ")
    dic = {"red": 0, "green": 0,  "blue": 0}
    for bl in sets:
        for k in bl.split(", "):
            m  = k.split(" ")
            dic[m[1]] = max(dic[m[1]], int(m[0]))
    s += dic["red"] * dic["green"] * dic["blue"]
print(s)