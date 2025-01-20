from utils import *
inp = input_file(2022, 12).strip()

grid = Grid(inp)
start = grid.find("S")[0]
end = grid.find("E")[0]
grid.set_pos(start, "a")
grid.set_pos(end, "z")

p1 = grid.djkstra(start, end, lambda currv, nextv: ord(nextv) - ord(currv) <= 1)

p2 = grid.djkstra(end, lambda v: v == "a", lambda currv, nextv: ord(currv) - ord(nextv) <= 1)

output(p1, p2)