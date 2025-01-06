from utils import *
inp = open("2019/input-4.txt", "r").read().strip()

parsed_input = parser(inp, "-")

valid = lambda p: p is int(fingerprint(p)) and any(map(lambda g: len(list(g[1])) >= 2, itertools.groupby(str(p))))
print(sum(map(valid, range(parsed_input[0], parsed_input[1] + 1))))

valid = lambda p: p is int(fingerprint(p)) and any(map(lambda g: len(list(g[1])) == 2, itertools.groupby(str(p))))
print(sum(map(valid, range(parsed_input[0], parsed_input[1] + 1))))