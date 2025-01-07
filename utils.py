import re, operator, functools, itertools, math, cmath, z3

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph = lower + upper

par_def = lambda i: int(i) if re.fullmatch(r"(\+|-)?[0-9]+", i) else str(i)

def parser(input, split, par=par_def, strip=True):
    if len(split) == 1:
        return list(map(lambda inp: par(inp[1].strip() if strip else inp[1]), enumerate(filter(None, re.split(split[0], input)))))
    else:
        return list(map(lambda inp: parser(inp, split[1:], par), filter(None, re.split(split[0], input))))

def maxval(iterable, key=lambda i: i):
    return key(max(iterable, key=key))
def minval(iterable, key=lambda i: i):
    return key(min(iterable, key=key))
def keyval(dic, val):
    return dic.keys()[dic.values().index(val)]

# GRID
dir_arr = {"^": 0+1j, ">": 1+0j, "v": 0-1j, "<": -1+0j}
dir_letter = {"U": 0+1j, "R": 1+0j, "D": 0-1j, "L": -1+0j}
neighbors = [1+0j, 0+1j, -1+0j, 0-1j]
diag_neighbors = [1+0j, 1+1j, 0+1j, -1+1j, -1+0j, -1-1j, 0-1j, 1-1j]

class Grid:
    def __init__(self, input, par=par_def):
        self.grid = [[par(i) for i in inp] for inp in input.split("\n")]
        self.rows, self.cols = len(self.grid), len(self.grid[0])
    def __repr__(self):
        return "\n".join(map(lambda r: "".join(map(str, r)), self.grid))


def summer(iterable):
    if type(iterable) is int or type(iterable) == float or type(iterable) == bool:
        return iterable
    else:
        return sum(map(summer, iterable))

fingerprint = lambda i: "".join(sorted(str(i)))

### INTCODE

def intcode(int_list, inp=None):
    i = 0
    while int_list[i] != 99:
        if int_list[i] == 1:
            if i < len(int_list) - 3 and all(map(lambda j: int_list[i + j] < len(int_list), range(1, 4))):
                int_list[int_list[i + 3]] = int_list[int_list[i + 1]] + int_list[int_list[i + 2]]
                i += 4
            else:
                return None
        elif int_list[i] == 2:
            if i < len(int_list) - 3 and all(map(lambda j: int_list[i + j] < len(int_list), range(1, 4))):
                int_list[int_list[i + 3]] = int_list[int_list[i + 1]] * int_list[int_list[i + 2]]
                i += 4
            else:
                return None
        elif int_list[i] == 3:
            if i < len(int_list) - 3 and all(map(lambda j: int_list[i + j] < len(int_list), range(1, 2))):
                int_list[int_list[i + 3]] = int_list[int_list[i + 1]] * int_list[int_list[i + 2]]
                i += 4
            else:
                return None
        if i >= len(int_list):
            return None
    return int_list