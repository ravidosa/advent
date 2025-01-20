from utils import *
inp = input_file(2020, 6).strip()

parsed_input = parser(inp, ["\n\n"], lambda i: (i.replace("\n", ""), i.count("\n") + 1))

p1 = sum(len(set(ans)) for ans, _ in parsed_input)

p2 = sum(len(list(g)) == per for ans, per in parsed_input for _, g in itertools.groupby(sorted(ans)))

output(p1, p2)