from utils import *
inp = input_file(2019, 1).strip()

parsed_input = parser(inp, ["\n"])

p1 = sum(map(lambda i: i // 3 - 2, parsed_input))

s = 0
for i in parsed_input:
    while i // 3 - 2 > 0:
        i = i // 3 - 2
        s += i
p2 = s

output(p1, p2)