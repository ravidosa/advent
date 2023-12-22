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
s1 = [(int(ii[2 * x]), int(ii[2 * x]) + int(ii[2 * x + 1]) - 1) for x in range(len(ii) // 2)]
for arr in ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]:
    s2 = []
    for s in mapd[arr]:
        s3 = []
        while len(s1) > 0:
            r = s1.pop(0)
            if r[0] < s[1] and r[1] >= s[1] and r[1] < s[1] + s[2]:
                s3.append((r[0], s[1] - 1))
                s2.append((s[0], s[0] + r[1] - s[1]))
            elif r[0] >= s[1] and r[1] < s[1] + s[2]:
                s2.append((s[0] + r[0] - s[1], s[0] + r[1] - s[1]))
            elif r[0] >= s[1] and r[1] >= s[1] + s[2] and r[0] < s[1] + s[2]:
                s2.append((s[0] + r[0] - s[1], s[0] + s[2] - 1))
                s3.append((s[1] + s[2], r[1]))
            else:
                s3.append(r)
        s1.extend(s3)
    s1.extend(s2)
print(min([r[0] for r in s1]))