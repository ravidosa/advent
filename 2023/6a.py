from functools import reduce
from math import floor, ceil
f = open("2023/input-6.txt", "r")
inp = f.read().split("\n")
t = [int(x) for x in list(filter(lambda x: x != "", inp[0][inp[0].index(":") + 1:].split(" ")))]
d = [int(x) for x in list(filter(lambda x: x != "", inp[1][inp[1].index(":") + 1:].split(" ")))]
print(reduce(lambda x, y: x * y, [floor((tt + (tt ** 2 - 4 * dd) ** 0.5) / 2) - ceil((tt - (tt ** 2 - 4 * dd) ** 0.5) / 2) + 1 for tt, dd in zip(t, d)]))