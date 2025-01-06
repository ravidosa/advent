from utils import *
inp = open("2017/input-2.txt", "r").read()

parsed_input = parser(inp, ["\n", "\t"])

print(sum(map(lambda i: max(i) - min(i), parsed_input)))

print(sum(map(lambda i: sum(map((lambda pair: int(max(pair) / min(pair)) * (max(pair) % min(pair) == 0)), itertools.combinations(i, 2))), parsed_input)))
