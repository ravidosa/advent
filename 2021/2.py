from utils import *
inp = input_file(2021, 2).strip()

parsed_input = parser(inp, ["\n", " "])

h, d = 0, 0
for i in parsed_input:
    h += i[1] * (i[0] == "forward")
    d += i[1] * ((i[0] == "down") - (i[0] == "up"))
p1 = h * d

h, d, aim = 0, 0, 0
for i in parsed_input:
    h += i[1] * (i[0] == "forward")
    d += aim * i[1] * (i[0] == "forward")
    aim += i[1] * ((i[0] == "down") - (i[0] == "up"))
p2 = h * d

output(p1, p2)