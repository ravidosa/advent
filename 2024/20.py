from utils import *
inp = input_file(2024, 20).strip()

grid = Grid(inp)
start = grid.find("S")[0]
end = grid.find("E")[0]
dist = grid.djkstra(start, None, lambda currv, nextv: nextv != "#")
pos = list(filter(lambda p: dist[p[0]][p[1]] != math.inf, itertools.product(range(grid.rows), range(grid.cols))))

cheat_dict = {}
for pair in itertools.combinations(pos, 2):
    p1, p2 = pair
    if manhattan(p1, p2) <= 2:
        cheat = abs(dist[p1[0]][p1[1]] - dist[p2[0]][p2[1]]) - manhattan(p1, p2)
        if cheat >= 100:
            cheat_dict[cheat] = cheat_dict.get(cheat, 0) + 1
print(sum(cheat_dict.values()))

cheat_dict = {}
for pair in itertools.combinations(pos, 2):
    p1, p2 = pair
    if manhattan(p1, p2) <= 20:
        cheat = abs(dist[p1[0]][p1[1]] - dist[p2[0]][p2[1]]) - manhattan(p1, p2)
        if cheat >= 100:
            cheat_dict[cheat] = cheat_dict.get(cheat, 0) + 1
print(sum(cheat_dict.values()))