from utils import *
inp = open("2022/input-12.txt", "r").read().strip()

grid = Grid(inp)
start = grid.find("S")[0]
end = grid.find("E")[0]
grid.set_pos(start, "a")
grid.set_pos(end, "z")

print(grid.djkstra(start, end, lambda currv, nextv: ord(nextv) - ord(currv) <= 1))

print(grid.djkstra(end, lambda v: v == "a", lambda currv, nextv: ord(currv) - ord(nextv) <= 1))