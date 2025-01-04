import re, itertools, cmath

lower = "abcdefghijklmnopqrstuvwxyz"
par = lambda i: int(i) if re.match(r"(\+|-)?[0-9]+", i) else str(i)

def parser(input, split):
    if len(split) == 1:
        return list(map(lambda inp: par(inp[1].strip()), enumerate(filter(None, re.split(split[0], input)))))
    else:
        return list(map(lambda inp: parser(inp, split[1:]), filter(None, re.split(split[0], input))))

# GRID
dir = {"^": 0+1j, ">": 1+0j, "v": 0-1j, "<": -1+0j}

class Grid:
    def __init__(self, input, par):
        self.grid = [[par(i) for i in inp] for inp in input.split("\n")]
        self.rows, self.cols = len(self.grid), len(self.grid[0])
    def __repr__(self):
        return "\n".join(map(lambda r: "".join(map(str, r)), self.grid))


def summer(iterable):
    if type(iterable) == int or type(iterable) == float:
        return iterable
    else:
        return sum(map(summer, iterable))
