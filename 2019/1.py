from utils import *
inp = input_file(2019, 1).strip()

parsed_input = parser(inp)

p1 = sum(i // 3 - 2 for i in parsed_input)

s = 0
for i in parsed_input:
    while i // 3 - 2 > 0:
        i = i // 3 - 2
        s += i
p2 = s

output(p1, p2)