from utils import *
inp = input_file(2024, 10).strip()

grid = Grid(inp)
heads = grid.find(0)

print(sum(map(lambda head: len(list((grid.bfs(head, lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))), heads)))

print(sum(map(lambda head: len(list((grid.dfs(head, [], lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))), heads)))