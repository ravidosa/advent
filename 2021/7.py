from utils import *
inp = open("2021/input-7.txt", "r").read()

parsed_input = parser(inp, [","])

mincrab, maxcrab = min(parsed_input), max(parsed_input)

print(min(map(lambda i: sum(map(lambda p: abs(p - i), parsed_input)), range(mincrab, maxcrab + 1))))

print(min(map(lambda i: sum(map(lambda p: (st := abs(p - i)) * (st + 1) // 2, parsed_input)), range(mincrab, maxcrab + 1))))