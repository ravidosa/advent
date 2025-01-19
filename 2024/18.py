from utils import *
inp = input_file(2024, 18).strip()

parsed_input = parser(inp, ["\n", ","])

grid = Grid((("." * 71 + "\n") * 71).strip())
for byte in parsed_input[:1024]:
    grid.set_pos(byte, "#")
print(grid.djkstra((0, 0), (70, 70), lambda currv, nextv: nextv != "#"))

low, high = 0, len(parsed_input) - 1
while low < high:
    mid = (low + high) // 2
    grid = Grid((("." * 71 + "\n") * 71).strip())
    for byte in parsed_input[:mid]:
        grid.set_pos(byte, "#")
    prev_poss = grid.djkstra((0, 0), (70, 70), lambda currv, nextv: nextv != "#") != math.inf
    grid.set_pos(parsed_input[mid], "#")
    curr_poss = grid.djkstra((0, 0), (70, 70), lambda currv, nextv: nextv != "#") != math.inf
    if prev_poss and curr_poss:
        low = mid
    elif not prev_poss and not curr_poss:
        high = mid
    else:
        break
print(str(parsed_input[mid][0]) + "," + str(parsed_input[mid][1]))