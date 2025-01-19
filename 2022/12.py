from utils import *
inp = input_file(2022, 12).strip()

grid = Grid(inp)
start = grid.find("S")[0]
end = grid.find("E")[0]
grid.set_pos(start, "a")
grid.set_pos(end, "z")

print(grid.djkstra(start, end, lambda currv, nextv: ord(nextv) - ord(currv) <= 1))

print(grid.djkstra(end, lambda v: v == "a", lambda currv, nextv: ord(currv) - ord(nextv) <= 1))