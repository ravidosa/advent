import re, operator, functools, itertools, collections, math, cmath, z3, networkx as nx, heapq as hq, requests, sys, os, pathlib, bs4, datetime, copy, shapely
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
        if "You don't seem to be solving the right level." in res.text:
            print("wrong day")
        elif "That's not the right answer; your answer is too high." in res.text:
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
digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
alph = lower + upper

fingerprint = lambda i: "".join(sorted(str(i)))

def par_nest(i, ty, spl):
    if len(spl) == 1:
        return [int(ii) if ty == "nli" else (int(ii.strip()) if re.fullmatch(r"(\+|-)?[0-9]+" if ty == "nle" else ii, ii.strip()) else ii) for ii in re.split(spl[0], i)]
    else:
        return [par_nest(ii, ty, spl[1:]) for ii in re.split(spl[0], i)]
    
def par_def(i, fmt):
    if fmt == "i":
        return int(i.strip())
    if fmt == "s" or fmt == "p":
        return i
    if fmt == "e":
        return int(i.strip()) if re.fullmatch(r"(?:\+|-)?[0-9]+", i.strip()) else i
    if fmt.startswith("li"):
        return [int(ii.strip()) for ii in re.split(fmt[2:], i) if ii != ""]
    if fmt.startswith("ls") or fmt.startswith("lp"):
        return [ii for ii in re.split(fmt[2:], i) if ii != ""]
    if fmt.startswith("le"):
        return [int(ii.strip()) if re.fullmatch(r"(?:\+|-)?[0-9]+", ii.strip()) else ii for ii in re.split(fmt[2:], i) if ii != ""]
    if fmt.startswith("nl"):
        return par_nest(i, fmt[:3], fmt[3:].split("|"))

def fmt_regex(fmt):
    if fmt == "i":
        return r"(\s*(?:\+|-)?[0-9]+\s*)"
    if fmt == "s" or fmt == "e":
        return r"(\S+)"
    if fmt == "p":
        return r"(.+)"
    if fmt.startswith("li"):
        return r"((?:(?:" + fmt[2:] + r")*\s*(?:\+|-)?[0-9]+\s*)*)(?:" + fmt[2:] + r")*"
    if fmt.startswith("ls") or fmt.startswith("le"):
        return r"((?:(?:" + fmt[2:] + r")*\S+)*)(?:" + fmt[2:] + r")*"
    if fmt.startswith("lp"):
        return r"((?:(?:" + fmt[2:] + r")*.+)*)(?:" + fmt[2:] + r")*"
    if fmt.startswith("nli"):
        return r"((?:(?:" + fmt[3:] + r")*\s*(?:\+|-)?[0-9]+\s*)*)(?:" + fmt[3:] + r")*"
    if fmt.startswith("nls") or fmt.startswith("nle"):
        return r"((?:(?:" + fmt[3:] + r")*\S+)*)(?:" + fmt[3:] + r")*"
    if fmt.startswith("nlp"):
        return r"((?:(?:" + fmt[3:] + r")*.+)*)(?:" + fmt[3:] + r")*"

def parser(input, format=None, split=None, strip=False):
    split = "\n" in input if split == None else split
    if format:
        cleaned = format
        for special in ".+*?^$([])":
            cleaned = re.sub("\\" + special + "(?![^{]*\})", "\\\\" + special, cleaned)
        cleaned = re.sub("(?<![{])({)(?![{])", "\\{", cleaned)
        cleaned = re.sub("(?<![}])(})(?![}])", "\\}", cleaned)
        formats = re.findall("{{(i|s|e|p|li[^}]*|ls[^}]*|le[^}]*|lp[^}]*|nli[^}]*|nls[^}]*|nle[^}]*|nlp[^}]*)}}", format)
        for fmt in formats:
            cleaned = cleaned.replace("{{" + fmt + "}}", fmt_regex(fmt))
        if split:
            if len(formats) == 1:
                return [par_def(re.fullmatch(cleaned, i).groups()[0], formats[0]) for i in input.split("\n")]
            else:
                return [[par_def(ii, formats[min(ind, len(formats) - 1)]) for ind, ii in enumerate(re.fullmatch(cleaned, i).groups())] for i in input.split("\n")]
        else:
            if len(formats) == 1:
                return par_def(re.fullmatch(cleaned, input).groups()[0], formats[0])
            else:
                return [par_def(ii, formats[min(ind, len(formats) - 1)]) for ind, ii in enumerate(re.fullmatch(cleaned, input).groups())]
    else:
        return [par_def(i, "e") for i in input.split("\n")] if split else input

# MAX/MIN

def maxval(iterable, key=lambda i: i):
    return key(max(iterable, key=key))
def minval(iterable, key=lambda i: i):
    return key(min(iterable, key=key))
def keyval(dic, val):
    return [k for k in dic if dic[k] == val]
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

transpose = lambda matrix : [list(row) for row in zip(*matrix)]

class Grid:
    def __init__(self, input, par=lambda i: par_def(i, "e"), dirs=dir_tup, wrap=False):
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


# TEXT

def make_rectangular(string):
    maxlen = max(len(line) for line in string.splitlines())
    return "\n".join(line.ljust(maxlen) for line in string.splitlines())

def transpose(string):
    return "\n".join(''.join(chars) for chars in zip(*string.splitlines()))

# LISTS

def copy(lst):
    return [copy(item) if isinstance(item, list) else item for item in lst]