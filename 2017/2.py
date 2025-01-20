from utils import *
inp = input_file(2017, 2).strip()

parsed_input = parser(inp, ["\n", "\t"])

p1 = sum(max(i) - min(i) for i in parsed_input)

p2 = sum(int(max(pair) / min(pair)) * (max(pair) % min(pair) == 0)for i in parsed_input for pair in itertools.combinations(i, 2))

output(p1, p2)
