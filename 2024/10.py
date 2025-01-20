from utils import *
inp = input_file(2024, 10).strip()

grid = Grid(inp)
heads = grid.find(0)

p1 = sum(map(lambda head: len(list((grid.bfs(head, lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))), heads))

p2 = sum(map(lambda head: len(list((grid.dfs(head, [], lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))), heads))

output(p1, p2)