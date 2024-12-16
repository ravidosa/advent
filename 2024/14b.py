f = open("2024/input-14.txt", "r")
inp = f.read().split("\n")

W = 101
H = 103

mx = W // 2
my = H // 2

quads = [0, 0, 0, 0]

f = open("output.txt", "w")

for t in range(77, W * H, W):
    pfs = set()
    for i in inp:
        p, v = i.split(" ")
        px, py = int(p[p.index("p=") + 2: p.index(",")]), int(p[p.index(",") + 1:])
        vx, vy = int(v[v.index("v=") + 2: v.index(",")]), int(v[v.index(",") + 1:])

        pxf, pyf = (px + vx * t) % W, (py + vy * t) % H
        pfs.add((pxf, pyf))
    f.write("t=" + str(t) + "\n")
    f.write("\n".join(["".join(["x" if (x, y) in pfs else "." for x in range(W)]) for y in range(H)]) + "\n")

f.close()