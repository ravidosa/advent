from utils import *
inp = input_file(2022, 2).strip()

parsed_input = parser(inp, "{{s}} {{s}}")

score = lambda s1, s2: 3 * ((ord(s2) - ord(s1) - 1) % 3)
shape_score = lambda s: ord(s) - 87
p1 = sum(score(i[0], i[1]) + shape_score(i[1]) for i in parsed_input)

score = lambda s: 3 * (ord(s) - 88)
shape_score = lambda s1, s2: ((ord(s2) - 2 * ord(s1) - 64) % 3) + 1
p2 = sum(score(i[1]) + shape_score(i[0], i[1]) for i in parsed_input)

output(p1, p2)