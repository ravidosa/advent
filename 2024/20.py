from utils import *
inp = input_file(2024, 20).strip()

grid = Grid(inp)
start = grid.find("S")[0]
end = grid.find("E")[0]
dist = grid.djkstra(start, None, lambda currv, nextv: nextv != "#")
pos = grid.bfs(start, lambda currv, nextv: nextv != "#")
def cheat_ct(minch, chd):
    cheat_dict = {}
    for p1, p2 in itertools.combinations(pos, 2):
        if manhattan(p1, p2) <= chd:
            cheat = abs(dist[p1[0]][p1[1]] - dist[p2[0]][p2[1]]) - manhattan(p1, p2)
            if cheat >= minch:
                cheat_dict[cheat] = cheat_dict.get(cheat, 0) + 1
    return cheat_dict

p1 = sum(cheat_ct(100, 2).values())

p2 = sum(cheat_ct(100, 20).values())

output(p1, p2)