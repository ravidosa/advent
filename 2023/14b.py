import functools
f = open("2023/input-14.txt", "r")
inp = f.read()
load = 0
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
pat = inp[:-1]
m, n = len(pat.split("\n")[0]), len(pat.split("\n"))
def arrayer(strr):
    return [list(x) for x in strr.split("\n")]
def dearrayer(pat):
    return "\n".join(["".join(p) for p in pat])
@functools.lru_cache(maxsize=None)
def tilt(pat, d):
    mov = True
    pat = arrayer(pat)
    while mov:
        mov = False
        for y in range(0, n):
            if y + d[1] >= 0 and y + d[1] < n:
                for x in range(m):
                    if x + d[0] >= 0 and x + d[0] < m:
                        if pat[y][x] == "O" and pat[y + d[1]][x + d[0]] == ".":
                            mov = True
                            pat[y + d[1]][x + d[0]], pat[y][x] = "O", "."
    return dearrayer(pat)

@functools.lru_cache(maxsize=None)
def cycle(pat):
    return tilt(tilt(tilt(tilt(pat, dir[1]), dir[3]), dir[0]), dir[2])
cyc = []
cyced = False
for i in range(1000000000):
    pat = cycle(pat)
    load = sum([sum([n - y if arrayer(pat)[y][x] == "O" else 0 for x in range(m)]) for y in range(n)])
    if load in cyc:
        for j in range(len(cyc) // 2, 2, -1):
            if cyc[len(cyc)-j:] == cyc[len(cyc)-2 * j:len(cyc)-j]:
                cyced = True
                break
        if cyced:
            break
        cyc.append(load)
    else:
        cyc.append(load)
if cyced:
    print(cyc[(1000000000 - (len(cyc) - 2 * j) - 1) % j + (len(cyc) - 2 * j)])
else:
    print(cyc[-1])