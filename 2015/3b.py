f = open("2015/input-3.txt", "r")
inp = f.read()

vis = set()
for j in range(2):
    x, y = 0, 0
    vis.add((x, y))
    for i in inp[j::2]:
        x += (1 if i == ">" else -1 if i == "<" else 0)
        y += (1 if i == "^" else -1 if i == "v" else 0)
        vis.add((x, y))
print(len(vis))