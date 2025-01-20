from utils import *
inp = input_file(2023, 21).strip()

grid = Grid(inp, wrap=True)
start = (65, 65)

reach = set()
reach.add(start)
for _ in range(65):
    reach = {tupadd(p, d) for d in grid.dirs for p in reach if grid.get_pos(tupadd(p, d)) != "#"}
p1 = len(reach)

n = 26501365 // 131
squares = []
reach = set()
reach.add(start)
for i in range(2 * 131 + 65 + 1):
    if i % 131 == 65:
        squares.append(len(reach))
    reach = {tupadd(p, d) for d in grid.dirs for p in reach if grid.get_pos(tupadd(p, d)) != "#"}
a, b, c = (squares[2] - 2 * squares[1] + squares[0]) // 2, (-squares[2] + 4 * squares[1] - 3 * squares[0]) // 2, squares[0]
p2 = a * n ** 2 + b * n + c

output(p1, p2)