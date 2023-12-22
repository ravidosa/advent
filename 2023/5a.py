f = open("2023/input-5.txt", "r")
inp = f.read().split("\n")
ii = inp[0].split(" ")[1:]
mapd = {}
i = 1
while i < len(inp):
    if len(inp[i]) == 0:
        k = ""
    else:
        if inp[i][-1] == ":":
            k = inp[i][inp[i].index("-to-") + 4:inp[i].index(" ")]
            mapd[k] = []
        elif k != "":
            mapd[k].append([int(x) for x in inp[i].split(" ")])
    i += 1
s1 = [int(x) for x in ii]
for arr in ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]:
    s2 = []
    for s in mapd[arr]:
        s3 = []
        while len(s1) > 0:
            r = s1.pop(0)
            if r >= s[1] and r < s[1] + s[2]:
                s2.append(s[0] + r - s[1])
            else:
                s3.append(r)
        s1.extend(s3)
    s1.extend(s2)
print(min([r for r in s1]))