from utils import *
inp = open("2020/input-6.txt", "r").read()

parsed_input = parser(inp, ["\n\n"], lambda i: (i.replace("\n", ""), i.count("\n") + 1))

print(sum(map(lambda i: len(set(i[0])), parsed_input)))

print(sum(map(lambda i: sum(map(lambda g: len(list(g[1])) == i[1], itertools.groupby(sorted(i[0])))), parsed_input)))