import re, operator, functools, itertools, collections, math, cmath, z3, networkx as nx, heapq as hq

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
dir_tup = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_diag_tup = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
dir_sym = {"^": {"comp": 0+1j, "tup": (-1, 0)}, ">": {"comp": 1+0j, "tup": (0, 1)}, "v": {"comp": 0-1j, "tup": (1, 0)}, "<": {"comp": -1+0j, "tup": (0, -1)}}
dir_letter = {"U": 0+1j, "R": 1+0j, "D": 0-1j, "L": -1+0j}
neighbors = [1+0j, 0+1j, -1+0j, 0-1j]
diag_neighbors = [1+0j, 1+1j, 0+1j, -1+1j, -1+0j, -1-1j, 0-1j, 1-1j]

corner_tup = [[(-1, 0), (0, -1)], [(1, 0), (0, -1)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(-1, 0), (0, -1), (-1, -1)], [(1, 0), (0, -1), (1, -1)], [(-1, 0), (0, 1), (-1, 1)], [(1, 0), (0, 1), (1, 1)]]
area = lambda cells: len(cells)
peri = lambda cells: sum(map(lambda p: sum(map(lambda d: (p[0] + d[0], p[1] + d[1]) not in cells, dir_tup)), cells))
sides = lambda cells: sum(map(lambda p: sum(map(lambda c: all(map(lambda d: (p[0] + d[0], p[1] + d[1]) not in cells, c)) if len(c) == 2 else all(map(lambda d: (p[0] + d[0], p[1] + d[1]) in cells, c[:2])) and (p[0] + c[2][0], p[1] + c[2][1]) not in cells, corner_tup)), cells))

class Grid:
    def __init__(self, input, par=par_def, dirs=dir_tup):
        self.grid = [[par(i) for i in inp] for inp in input.split("\n")]
        self.rows, self.cols = len(self.grid), len(self.grid[0])
        self.dirs = dirs
    def __repr__(self):
        return "\n".join(map(lambda r: "".join(map(str, r)), self.grid))
    def find(self, loc):
        return list(filter(lambda i: self.grid[i[0]][i[1]] == loc, itertools.product(range(self.rows), range(self.cols))))
    def bfs(self, start, move=lambda currv, nextv: True, fil=lambda v: True):
        vis, next = set(), set()
        next.add(start)
        while len(next) > 0:
            currp = next.pop()
            vis.add(currp)
            r, c = currp
            for d in self.dirs:
                dr, dc = d
                if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                    nextp = (r + dr, c + dc)
                    if move(self.grid[r][c], self.grid[r + dr][c + dc]) and nextp not in vis:
                        next.add(nextp)
        return filter(lambda p: fil(self.grid[p[0]][p[1]]), vis)
    def dfs(self, currp, visited, move=lambda currv, nextv: True, fil=lambda v: True):
        r, c = currp
        if fil(self.grid[r][c]):
            yield currp
        else:
            for d in self.dir:
                dr, dc = d
                if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                    nextp = (r + dr, c + dc)
                    if move(self.grid[r][c], self.grid[r + dr][c + dc]) and nextp not in visited:
                        for p in self.dfs(nextp, visited + [currp], move, fil):
                            yield p
    def djkstra(self, start, end, move=lambda currv, nextv: True, weight=lambda currp, nextp: 1):
        dist = [[math.inf for _ in range(self.cols)] for __ in range(self.rows)]
        processed = [[False for _ in range(self.cols)] for __ in range(self.rows)]
        dist[start[0]][start[1]] = 0
        queue = [(0, start)]
        while len(queue) > 0:
            currd, currp = hq.heappop(queue)
            r, c = currp
            if currp == end:
                return dist[r][c]
            if not processed[r][c]:
                processed[r][c] = True
                for d in self.dir:
                    dr, dc = d
                    if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                        nextp = (r + dr, c + dc)
                        if move(self.grid[r][c], self.grid[r + dr][c + dc]):
                            dist[r + dr][c + dc] = min(dist[r + dr][c + dc], dist[r][c] + weight(currp, nextp))
                            if nextp not in queue and not processed[r + dr][c + dc]:
                                hq.heappush(queue, (dist[r + dr][c + dc], nextp))
        return math.inf if end else dist

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

## MATH
def dec_to_tern(dec, N):
    if dec == 0:
        tern = "0"
    else:
        tern = ""
        while dec:
            dec, rem = divmod(dec, 3)
            tern = str(rem) + tern
    return tern.zfill(N)

def chi_rem(a, n):
    if len(a) == 1:
        return a[0]
    else:
        next_a = (a[0] * n[1] * pow(n[1], -1, n[0]) + a[1] * n[0] * pow(n[0], -1, n[1])) % (n[0] * n[1])
        next_n = n[0] * n[1]
        return chi_rem([next_a] + a[2:], [next_n] + n[2:])

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])