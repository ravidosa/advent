from utils import *
inp = input_file(2020, 6).strip()

parsed_input = parser(inp, ["\n\n"], lambda i: (i.replace("\n", ""), i.count("\n") + 1))

p1 = sum(len(set(i[0])) for i in parsed_input)

p2 = sum(len(list(g[1])) == i[1] for i in parsed_input for g in itertools.groupby(sorted(i[0])))

output(p1, p2)