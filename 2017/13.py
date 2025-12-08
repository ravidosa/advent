from utils import *
inp = input_file(2017, 13).strip()

parsed_input = parser(inp, "{{i}}: {{i}}")

p1 = sum((i[0] % (i[1] * 2 - 2) == 0) * i[0] * i[1] for i in parsed_input)

p2 = next(t for t in itertools.count() if all(((i[0] + t) % (i[1] * 2 - 2) != 0) for i in parsed_input))

output(p1, p2)