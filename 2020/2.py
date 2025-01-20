from utils import *
inp = input_file(2020, 2).strip()

parsed_input = parser(inp, ["\n", "-| |: "])

valid = lambda i: i[0] <= i[3].count(i[2]) <= i[1]
p1 = sum(map(valid, parsed_input))

valid = lambda i: (i[3][i[0] - 1] == i[2]) ^ (i[3][i[1] - 1] == i[2])
p2 = sum(map(valid, parsed_input))

output(p1, p2)