from utils import *
inp = open("2024/input-10.txt", "r").read().strip()

grid = Grid(inp)
heads = grid.find(0)

print(sum(map(lambda head: len(list((grid.bfs(head, lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))), heads)))

print(sum(map(lambda head: len(list((grid.dfs(head, [], lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))), heads)))