from utils import *
inp = open("2015/input-8.txt", "r").read()

parsed_input = parser(inp, ["\n"])

print(sum(map(lambda inp: len(inp) - len(eval(inp)), parsed_input)))

print(sum(map(lambda inp: 2 + (inp.count("\"") + inp.count("\\")), parsed_input)))