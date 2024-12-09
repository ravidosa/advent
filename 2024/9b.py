from collections import deque

f = open("2024/input-9.txt", "r")
inp = f.read()

def checksum(disk):
    su = 0
    for i, n in enumerate(disk):
        if n != None:
            su += i * n
    return su

files = {}
frees = []
pos = 0
for i in range(len(inp) // 2):
    files[i] = [pos, int(inp[2 * i])]
    pos += int(inp[2 * i])
    frees.append([pos, int(inp[2 * i + 1])])
    pos += int(inp[2 * i + 1])
files[i + 1] = [pos, int(inp[2 * (i + 1)])]

for i in range(len(files) - 1, 0, -1):
    for f in frees:
        if files[i][0] > f[0] and files[i][1] <= f[1]:
            files[i][0] = f[0]
            f[0] += files[i][1]
            f[1] -= files[i][1]
            break

print(int(sum([(f * (2 * files[f][0] + files[f][1] - 1) / 2 * files[f][1]) for f in files])))