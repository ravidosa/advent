from utils import *
inp = input_file(2024, 10).strip()

grid = Grid(inp)
heads = grid.find(0)

p1 = sum(len(list((grid.bfs(head, lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))) for head in heads)

p2 = sum(len(list((grid.dfs(head, [], lambda currv, nextv: nextv - currv == 1, lambda v: v == 9)))) for head in heads)

output(p1, p2)