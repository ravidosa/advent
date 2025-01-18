from utils import *
inp = open("2020/input-10.txt", "r").read()

parsed_input = parser(inp, ["\n"])

adapters = [0] + sorted(parsed_input)
diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))] + [3]
print(diffs.count(1) * diffs.count(3))

ways = lambda s, e: 1 if e - s == 0 else int(s in adapters and e in adapters) if e - s == 1 else (s in adapters and e in adapters) + (s in adapters and e in adapters and s + 1 in adapters) if e - s == 2 else (s in adapters and e in adapters) + (s in adapters and e in adapters and s + 1 in adapters) + (s in adapters and e in adapters and s + 2 in adapters) + (s in adapters and e in adapters and s + 1 in adapters and s + 2 in adapters) if e - s == 3 else ways(s, e - 1) * (e - 1 in adapters) + ways(s, e - 2) * (e - 2 in adapters) + ways(s, e - 3) * (e - 3 in adapters)
fixed = list(map(lambda t: adapters[t], filter(lambda i: adapters[i] - adapters[i - 1] == 3, range(1, len(adapters)))))
ranges = [(0, fixed[0] - 3)] + list(map(lambda i: (fixed[i - 1], fixed[i] - 3), range(1, len(fixed))))
print(prod(map(lambda r: ways(r[0], r[1]), ranges)))