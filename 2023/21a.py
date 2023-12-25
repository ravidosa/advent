f = open("2023/input-21.txt", "r")
inp = f.read().split("\n")
m, n = len(inp[:-1]), len(inp[0])
S = "".join(inp[:-1]).index("S")
S = (S % n, S // n)
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
vis = set([S])
for i in range(64):
    vis = {((pos[0] + d[0]) % m, (pos[1] + d[1]) % n) for d in dir for pos in vis if inp[(pos[1] + d[1]) % n][(pos[0] + d[0]) % m] != "#"}
print(len(vis))