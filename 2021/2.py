from utils import *
inp = open("2021/input-2.txt", "r").read()

parsed_input = parser(inp, ["\n", " "])

h, d = 0, 0
for i in parsed_input:
    h += i[1] * (i[0] == "forward")
    d += i[1] * ((i[0] == "down") - (i[0] == "up"))
print(h * d)

h, d, aim = 0, 0, 0
for i in parsed_input:
    h += i[1] * (i[0] == "forward")
    d += aim * i[1] * (i[0] == "forward")
    aim += i[1] * ((i[0] == "down") - (i[0] == "up"))
print(h * d)