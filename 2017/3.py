from utils import *
import math
inp = open("2017/input-3.txt", "r").read()

target = int(inp)
ring = (((minsq := math.ceil(math.sqrt(target))) + (minsq % 2 == 0)) - 1) // 2
mids = [(minsq + (minsq % 2 == 0)) ** 2 - (2 * i + 1) * ring for i in range(4)]
print(ring + abs(min(mids, key=lambda m: abs(m - target)) - target))

squares = {0+0j: 1, 1+0j: 1}
pos, dir = 1+0j, 1+0j
i, ring = 2, 1
while squares[pos] <= target:
    if math.sqrt(i).is_integer() and i % 2 == 1:
        ring += 1
    else:
        if (maxsq := (2 * ring + 1) ** 2 - i) % (2 * ring) == 0 or math.sqrt(i - 1).is_integer() and (i - 1) % 2 == 1:
            dir *= (0+1j)
    i += 1
    pos += dir
    squares[pos] = sum(map(lambda d: squares.get(pos + d, 0), diag_neighbors))
print(squares[pos])