import re, operator, functools, itertools, collections, math, cmath, z3, networkx as nx, heapq as hq, requests, sys, os, pathlib, bs4, datetime
from env import SESSION

p1, p2 = None, None

# INPUT/OUTPUT

y, d = None, None

def input_file(year=datetime.datetime.now().year, day=datetime.datetime.now().day):
    global y, d
    y, d = year, day
    if "test" in sys.argv:
        if pathlib.Path("{0}/testinput-{1}.txt".format(year, day)).is_file():
            return open("{0}/testinput-{1}.txt".format(year, day), "r").read()
        url_html = requests.get("https://adventofcode.com/{0}/day/{1}".format(year, day), cookies={"session": SESSION}, headers={"User-Agent":"https://github.com/ravidosa/advent/blob/main/utils.py"})
        soup = bs4.BeautifulSoup(url_html.text, "lxml")
        prev_p = next(filter(lambda t: any(map(lambda s: re.search(r"(E|e)xample", s), t.stripped_strings)), soup.findAll("p")))
        if prev_p:
            test_text = prev_p.find_next_sibling().getText()
            f = open("{0}/testinput-{1}.txt".format(year, day), "w")
            f.write(test_text)
            f.close()
            return test_text
    else:
        if pathlib.Path("{0}/input-{1}.txt".format(year, day)).is_file():
            return open("{0}/input-{1}.txt".format(year, day), "r").read()
        url_file = requests.get("https://adventofcode.com/{0}/day/{1}/input".format(year, day), cookies={"session": SESSION}, headers={"User-Agent":"https://github.com/ravidosa/advent/blob/main/utils.py"})
        if url_file.text != "Puzzle inputs differ by user.  Please log in to get your puzzle input.\n":
            f = open("{0}/input-{1}.txt".format(year, day), "w")
            f.write(url_file.text)
            f.close()
            return url_file.text
        else:
            print("update session in env.py")

def output(*p):
    if "p1" in sys.argv or "p2" in sys.argv:
        res = requests.post("https://adventofcode.com/{0}/day/{1}/answer".format(y, d), cookies={"session": SESSION}, headers={"User-Agent":"https://github.com/ravidosa/advent/blob/main/utils.py"}, data={"level": 1 if "p1" in sys.argv else 2, "answer": p[0 if "p1" in sys.argv else 1]})
        if "That's not the right answer; your answer is too high." in res.text:
            print("too high")
        elif "That's not the right answer; your answer is too low." in res.text:
            print("too low")
        elif "That's not the right answer" in res.text:
            print("wrong")
        else:
            print("correct")
    for pp in p:
        if pp != None:
            print(pp)



# STRINGS/PARSING

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = letm = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
alph = lower + upper

fingerprint = lambda i: "".join(sorted(str(i)))

par_def = lambda i: int(i) if re.fullmatch(r"(\+|-)?[0-9]+", i) else str(i)

def parser(input, split, par=par_def, strip=True, flatten=True):
    if len(split) == 1:
        return [par(inp.strip() if strip else inp) for inp in re.split(split[0], input) if inp != ""] if re.search(split[0], input) else par(input.strip() if strip else input) if flatten else [par(input.strip() if strip else input)]
    else:
        return [parser(inp, split[1:], par, strip=strip, flatten=flatten) for inp in re.split(split[0], input) if inp != ""] if re.search(split[0], input) else parser(input, split[1:], par, strip=strip, flatten=flatten) if flatten else [parser(input, split[1:], par, strip=strip, flatten=flatten)]



# MAX/MIN

def maxval(iterable, key=lambda i: i):
    return key(max(iterable, key=key))
def minval(iterable, key=lambda i: i):
    return key(min(iterable, key=key))
def keyval(dic, val):
    return dic.keys()[dic.values().index(val)]
def argmax(iterable, key=lambda i: i):
    iterable = list(iterable)
    return max(range(len(iterable)), key=lambda ind: key(iterable[ind]))
def argmin(iterable, key=lambda i: i):
    iterable = list(iterable)
    return min(range(len(iterable)), key=lambda ind: key(iterable[ind]))
def cmp(a, b, key=lambda i: i):
    ka, kb = key(a), key(b)
    return (ka > kb) - (ka < kb)



# GRID

dir_tup = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_diag_tup = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
dir_sym = {"^": {"comp": 0+1j, "tup": (-1, 0)}, ">": {"comp": 1+0j, "tup": (0, 1)}, "v": {"comp": 0-1j, "tup": (1, 0)}, "<": {"comp": -1+0j, "tup": (0, -1)}}
dir_letter = {"U": {"comp": 0+1j, "tup": (-1, 0)}, "R": {"comp": 1+0j, "tup": (0, 1)}, "D": {"comp": 0-1j, "tup": (1, 0)}, "L": {"comp": -1+0j, "tup": (0, -1)}}
neighbors = [1+0j, 0+1j, -1+0j, 0-1j]
diag_neighbors = [1+0j, 1+1j, 0+1j, -1+1j, -1+0j, -1-1j, 0-1j, 1-1j]

corner_tup = [[(-1, 0), (0, -1)], [(1, 0), (0, -1)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(-1, 0), (0, -1), (-1, -1)], [(1, 0), (0, -1), (1, -1)], [(-1, 0), (0, 1), (-1, 1)], [(1, 0), (0, 1), (1, 1)]]
area = lambda cells: len(cells)
peri = lambda cells: sum(tupadd(p, d) not in cells for d in dir_tup for p in cells)
sides = lambda cells: sum(all(tupadd(p, d) not in cells for d in c) if len(c) == 2 else all(tupadd(p, d) in cells for d in c[:2]) and tupadd(p, c[2]) not in cells for c in corner_tup for p in cells)

def tupadd(tuple1, tuple2):
    return tuple(p1 + p2 for p1, p2 in zip(tuple1, tuple2))

class Grid:
    def __init__(self, input, par=par_def, dirs=dir_tup, wrap=False):
        self.grid = [[par(i) for i in inp] for inp in input.split("\n")]
        self.rows, self.cols = len(self.grid), len(self.grid[0])
        self.dirs = dirs
        self.wrap = wrap
    def __repr__(self):
        return "\n".join("".join(map(str, r)) for r in self.grid)
    def __contains__(self, p):
        return 0 <= p[0] < self.rows and 0 <= p[1] < self.cols
    def find(self, loc):
        return [pos for pos in itertools.product(range(self.rows), range(self.cols)) if self.get_pos(pos) == loc]
    def get_pos(self, p):
        if p in self or self.wrap:
            return self.grid[p[0] % self.rows][p[1] % self.cols]
        return None
    def set_pos(self, p, s):
        if p in self or self.wrap:
            self.grid[p[0] % self.rows][p[1] % self.cols] = s
    def cells(self):
        return itertools.product(range(self.rows), range(self.cols))
    def row(self, pos, len=math.inf):
        r, c = pos
        return [self.get_pos((r, c + i)) for i in range(0, min(self.cols - c, len))]
    def col(self, pos, len=math.inf):
        r, c = pos
        return [self.get_pos((r + i, c)) for i in range(0, min(self.rows - r, len))]
    def pdiag(self, pos, len=math.inf):
        r, c = pos
        return [self.get_pos((r + i, c - i)) for i in range(0, min(self.rows - r, c + 1, len))]
    def ndiag(self, pos, len=math.inf):
        r, c = pos
        return [self.get_pos((r + i, c + i)) for i in range(0, min(self.rows - r, self.cols - c, len))]
    def bfs(self, start, move=lambda currv, nextv: True, fil=lambda v: True):
        vis, next = set(), set()
        next.add(start)
        while len(next) > 0:
            currp = next.pop()
            vis.add(currp)
            for d in self.dirs:
                nextp = tupadd(currp, d)
                if nextp in self:
                    if move(self.get_pos(currp), self.get_pos(nextp)) and nextp not in vis:
                        next.add(nextp)
        return {p for p in vis if fil(self.get_pos(p))}
    def dfs(self, currp, visited, move=lambda currv, nextv: True, fil=lambda v: True):
        r, c = currp
        if fil(self.get_pos(currp)):
            yield currp
        else:
            for d in self.dirs:
                nextp = tupadd(currp, d)
                if nextp in self:
                    if move(self.get_pos(currp), self.get_pos(nextp)) and nextp not in visited:
                        for p in self.dfs(nextp, visited + [currp], move, fil):
                            yield p
    def djkstra(self, start, end=lambda v: True, move=lambda currv, nextv: True, weight=lambda currp, nextp: 1):
        dist = [[math.inf for _ in range(self.cols)] for __ in range(self.rows)]
        processed = [[False for _ in range(self.cols)] for __ in range(self.rows)]
        dist[start[0]][start[1]] = 0
        queue = [(0, start)]
        while len(queue) > 0:
            currd, currp = hq.heappop(queue)
            r, c = currp
            if end and ((type(end) == tuple and currp == end) or (callable(end) and end(self.get_pos(currp)))):
                return dist[r][c]
            if not processed[r][c]:
                processed[r][c] = True
                for d in self.dirs:
                    dr, dc = d
                    nextp = tupadd(currp, d)
                    if nextp in self:
                        if move(self.get_pos(currp), self.get_pos(nextp)):
                            dist[r + dr][c + dc] = min(dist[r + dr][c + dc], dist[r][c] + weight(currp, nextp))
                            if nextp not in queue and not processed[r + dr][c + dc]:
                                hq.heappush(queue, (dist[r + dr][c + dc], nextp))
        return math.inf if end else dist

def summer(iterable):
    if type(iterable) is int or type(iterable) == float or type(iterable) == bool:
        return iterable
    else:
        return sum(map(summer, iterable))



### INTCODE

def intcode(int_list, inp=None):
    inp_pos = 0
    out = []
    mode = lambda i, j: (int_list[i] // 10 ** (j + 1)) % 10
    pret = lambda i, j: int_list[int_list[i + j]] if mode(i, j) == 0 else int_list[i + j]
    valid = lambda i, pars: i < len(int_list) - pars and all(int_list[i + j] < len(int_list) if mode(i, j) == 0 else True for j in range(1, pars + 1))
    i = 0
    while int_list[i] != 99:
        if int_list[i] % 100 == 1 and valid(i, 3):
            int_list[int_list[i + 3]] = pret(i, 1) + pret(i, 2)
            i += 4
        elif int_list[i] % 100 == 2 and valid(i, 3):
            int_list[int_list[i + 3]] = pret(i, 1) * pret(i, 2)
            i += 4
        elif int_list[i] % 100 == 3 and valid(i, 1):
            int_list[int_list[i + 1]] = inp[inp_pos]
            inp_pos += 1
            i += 2
        elif int_list[i] % 100 == 4 and valid(i, 1):
            out.append(pret(i, 1))
            i += 2
        elif int_list[i] % 100 == 5 and valid(i, 2):
            if pret(i, 1) != 0:
                i = pret(i, 2)
            else:
                i += 3
        elif int_list[i] % 100 == 6 and valid(i, 2):
            if pret(i, 1) == 0:
                i = pret(i, 2)
            else:
                i += 3
        elif int_list[i] % 100 == 7 and valid(i, 3):
            if pret(i, 1) < pret(i, 2):
                int_list[int_list[i + 3]] = 1
            else:
                int_list[int_list[i + 3]] = 0
            i += 4
        elif int_list[i] % 100 == 8 and valid(i, 3):
            if pret(i, 1) == pret(i, 2):
                int_list[int_list[i + 3]] = 1
            else:
                int_list[int_list[i + 3]] = 0
            i += 4
        else:
            return None, None
        if i >= len(int_list):
            return None, None
    return int_list, out

# MATH

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

def manhattan(tuple1, tuple2):
    return sum(abs(p1 - p2) for p1, p2 in zip(tuple1, tuple2))

def shoelace(vertices):
    return sum(vertices[i][0] * vertices[(i + 1) % len(vertices)][1] - vertices[(i + 1) % len(vertices)][0] * vertices[i][1] for i in range(len(vertices))) / 2

def prod(iterable):
    return functools.reduce(operator.mul, iterable)

def bigcup(iterable):
    return functools.reduce(lambda a, b: a.union(b), iterable, set())

def bigcap(iterable):
    return functools.reduce(lambda a, b: a.intersection(b), iterable, set())

def increasing(n):
    return all(str(n)[i] >= str(n)[i - 1] for i in range(1, len(str(n))))

def decreasing(n):
    return all(str(n)[i] <= str(n)[i - 1] for i in range(1, len(str(n))))