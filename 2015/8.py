from utils import *
inp = input_file(2015, 8).strip()

parsed_input = parser(inp, ["\n"])

p1 = sum(map(lambda inp: len(inp) - len(eval(inp)), parsed_input))

p2 = sum(map(lambda inp: 2 + (inp.count("\"") + inp.count("\\")), parsed_input))

output(p1, p2)