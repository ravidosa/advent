from utils import *
inp = input_file(2020, 6).strip().replace("\n", " ").replace("  ", "\n")

parsed_input = parser(inp, "{{ls }}")

p1 = sum(len(set("".join(i))) for i in parsed_input)

p2 = sum(len(list(g)) == len(i) for i in parsed_input for _, g in itertools.groupby(sorted("".join(i))))

output(p1, p2)