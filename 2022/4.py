from utils import *
inp = input_file(2022, 4).strip()

parsed_input = parser(inp, ["\n", ",", "-"])

contain = lambda r1, r2: r1[0] <= r2[0] and r1[1] >= r2[1]
print(sum(map(lambda i: contain(i[0], i[1]) or contain(i[1], i[0]), parsed_input)))

overlap = lambda r1, r2: r1[1] >= r2[0] and r1[0] <= r2[1]
print(sum(map(lambda i: overlap(i[0], i[1]) or overlap(i[1], i[0]), parsed_input)))