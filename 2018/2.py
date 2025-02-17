from utils import *
inp = input_file(2018, 2).strip()

parsed_input = parser(inp)

exrep = lambda p, i: any(p.count(g) == i for g in set(p))
p1 = sum(exrep(p, 2) for p in parsed_input) * sum(exrep(p, 3) for p in parsed_input)

common = lambda pair: "".join(pair[0][i] if pair[0][i] == pair[1][i] else "" for i in range(len(pair[0])))
p2 = max(map(common, itertools.combinations(parsed_input, 2)), key=len)

output(p1, p2)