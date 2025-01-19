from utils import *
inp = input_file(2018, 2).strip()

parsed_input = parser(inp, ["\n"])

exrep = lambda p, i: any(map(lambda g: p.count(g) == i, set(p)))
print(sum(map(lambda p: exrep(p, 2), parsed_input)) * sum(map(lambda p: exrep(p, 3), parsed_input)))

common = lambda pair: "".join(map(lambda i: pair[0][i] if pair[0][i] == pair[1][i] else "", range(len(pair[0]))))
print(max(map(common, itertools.combinations(parsed_input, 2)), key=len))