f = open("2024/input-10.txt", "r")
inp = f.read().split("\n")

head = [(i % len(inp[0]), i // len(inp[0])) for i in range(len("".join(inp))) if "".join(inp)[i] == "0"]

inp = [[int(ii) for ii in i]for i in inp]

score = 0

for h in head:
    vis = set()
    t = set()
    vis.add(h)
    while len(vis) > 0:
        pos = vis.pop()
        x, y = pos
        if inp[y][x] == 9:
            if (y, x) not in t:
                score += 1
                t.add((y, x))
        if x > 0 and inp[y][x - 1] - inp[y][x] == 1:
            vis.add((x - 1, y))
        if x < len(inp[0]) - 1 and inp[y][x + 1] - inp[y][x] == 1:
            vis.add((x + 1, y))
        if y > 0 and inp[y - 1][x] - inp[y][x] == 1:
            vis.add((x, y - 1))
        if y < len(inp) - 1 and inp[y + 1][x] - inp[y][x] == 1:
            vis.add((x, y + 1))
print(score)