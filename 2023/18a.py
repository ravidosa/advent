f = open("2023/input-18.txt", "r")
inp = f.read().split("\n")
vers = []
pts = 0
dir = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
pos = (0, 0)
for i in inp[:-1]:
    ii = i.split(" ")
    d = dir[ii[0]]
    pos = (pos[0] + int(ii[1]) * d[0], pos[1] + int(ii[1]) * d[1])
    vers.append(pos)
    pts += int(ii[1])
n = len(vers)
area = 0.0
for i in range(n):
    j = (i + 1) % n
    area += vers[i][0] * vers[j][1]
    area -= vers[j][0] * vers[i][1]
area = abs(area) / 2.0
print(area + 1 - pts // 2 + pts)