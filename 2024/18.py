from utils import *
inp = open("2024/input-18.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", ","])

grid = Grid((("." * 71 + "\n") * 71).strip())
for byte in parsed_input[:1024]:
    c, r = byte
    grid.grid[r][c] = "#"
print(grid.djkstra((0, 0), (70, 70), lambda currv, nextv: nextv != "#"))

grid = Grid((("." * 71 + "\n") * 71).strip())
for byte in parsed_input:
    c, r = byte
    grid.grid[r][c] = "#"
    if grid.djkstra((0, 0), (70, 70), lambda currv, nextv: nextv != "#") == math.inf:
        break
print(str(byte[0]) + "," + str(byte[1]))