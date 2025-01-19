from utils import *
inp = input_file(2019, 4).strip()

parsed_input = parser(inp, "-")

valid = lambda p: p is int(fingerprint(p)) and any(map(lambda g: len(list(g[1])) >= 2, itertools.groupby(str(p))))
print(sum(map(valid, range(parsed_input[0], parsed_input[1] + 1))))

valid = lambda p: p is int(fingerprint(p)) and any(map(lambda g: len(list(g[1])) == 2, itertools.groupby(str(p))))
print(sum(map(valid, range(parsed_input[0], parsed_input[1] + 1))))