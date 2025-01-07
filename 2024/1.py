from utils import *
inp = open("2024/input-1.txt", "r").read().strip()

parsed_input = parser(inp, ["\n| +"])
l1 = sorted(parsed_input[::2])
l2 = sorted(parsed_input[1::2])

print(sum(map(lambda a, b: abs(a - b), l1, l2)))

print(sum(map(lambda a: a * l2.count(a), l1)))