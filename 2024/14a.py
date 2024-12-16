f = open("2024/input-14.txt", "r")
inp = f.read().split("\n")

W = 101
H = 103
t = 100

mx = W // 2
my = H // 2

quads = [0, 0, 0, 0]

for i in inp:
    p, v = i.split(" ")
    px, py = int(p[p.index("p=") + 2: p.index(",")]), int(p[p.index(",") + 1:])
    vx, vy = int(v[v.index("v=") + 2: v.index(",")]), int(v[v.index(",") + 1:])

    pxf, pyf = (px + vx * t) % W, (py + vy * t) % H
    if pxf > mx and pyf > my:
        quads[0] += 1
    if pxf < mx and pyf > my:
        quads[1] += 1
    if pxf < mx and pyf < my:
        quads[2] += 1
    if pxf > mx and pyf < my:
        quads[3] += 1

print(quads[0] * quads[1] * quads[2] * quads[3])