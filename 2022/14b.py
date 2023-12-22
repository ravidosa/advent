f = open("2022/input-14.txt", "r")
inp = f.read().split("\n")
instr = [[[int(x) for x in l.split(",")]for l in i.split(" -> ")] for i in inp[:-1]]
maxy = max([max([j[1] for j in i]) for i in instr]) + 2
maxx = 2 * maxy + 1
cav = [["." for _ in range(maxx)] for _ in range(maxy)]
cav.append(["#" for _ in range(maxx)])
for i in instr:
    for j in range(len(i) - 1):
        for k in range(min(i[j][0], i[j + 1][0]) - (500 - maxy), max(i[j][0], i[j + 1][0]) + 1 - (500 - maxy)):
            for l in range(min(i[j][1], i[j + 1][1]), max(i[j][1], i[j + 1][1]) + 1):
                cav[l][k] = "#"
s = 0
s_loc = [0, maxy]
while cav[0][maxy] != "#":
    if cav[s_loc[0] + 1][s_loc[1]] == "#":
        if cav[s_loc[0] + 1][s_loc[1] - 1] == "#":
            if cav[s_loc[0] + 1][s_loc[1] + 1] == "#":
                s += 1
                cav[s_loc[0]][s_loc[1]] = "#"
                s_loc = [0, maxy]
            else:
                s_loc = [s_loc[0] + 1, s_loc[1] + 1]
        else:
            s_loc = [s_loc[0] + 1, s_loc[1] - 1]
    else:
        s_loc = [s_loc[0] + 1, s_loc[1]]
print(s)