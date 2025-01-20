from utils import *
inp = input_file(2019, 4).strip()

parsed_input = parser(inp, "-")

valid = lambda p: p is int(fingerprint(p)) and any(len(list(g[1])) >= 2 for g in itertools.groupby(str(p)))
p1 = sum(map(valid, range(parsed_input[0], parsed_input[1] + 1)))

valid = lambda p: p is int(fingerprint(p)) and any(len(list(g[1])) == 2 for g in itertools.groupby(str(p)))
p2 = sum(map(valid, range(parsed_input[0], parsed_input[1] + 1)))

output(p1, p2)