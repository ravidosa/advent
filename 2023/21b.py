f = open("2023/input-21.txt", "r")
inp = f.read().split("\n")
m, n = len(inp[:-1]), len(inp[0])
S = "".join(inp[:-1]).index("S")
S = (S % n, S // n)
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
vis = set([S])
rem = []
for i in range(3 * 131):
    if i % 131 == 65:
        rem.append(len(vis))
    vis = {((pos[0] + d[0]), (pos[1] + d[1])) for d in dir for pos in vis if inp[(pos[1] + d[1]) % n][(pos[0] + d[0]) % m] != "#"}
nn = 26501365 // 131
print(rem[0] + nn * (rem[1] - rem[0] + (nn - 1) * (rem[2] - rem[1] - rem[1] + rem[0]) // 2))