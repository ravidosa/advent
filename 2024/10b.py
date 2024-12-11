f = open("2024/input-10.txt", "r")
inp = f.read().split("\n")

head = [(i % len(inp[0]), i // len(inp[0])) for i in range(len("".join(inp))) if "".join(inp)[i] == "0"]

inp = [[int(ii) for ii in i]for i in inp]

score = 0

def dfs(node, visited):
    vis = visited.copy()
    global score
    x, y = node
    if inp[y][x] == 9:
        score += 1
    else:
        if node not in vis:
            vis.append(node)
            if x > 0 and inp[y][x - 1] - inp[y][x] == 1:
                dfs((x - 1, y), vis)
            if x < len(inp[0]) - 1 and inp[y][x + 1] - inp[y][x] == 1:
                dfs((x + 1, y), vis)
            if y > 0 and inp[y - 1][x] - inp[y][x] == 1:
                dfs((x, y - 1), vis)
            if y < len(inp) - 1 and inp[y + 1][x] - inp[y][x] == 1:
                dfs((x, y + 1), vis)
sscore = 0
for h in head:
    dfs(h, [])
print(score)
