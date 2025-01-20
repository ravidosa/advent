from utils import *
inp = input_file(2015, 8).strip()

parsed_input = parser(inp, ["\n"])

p1 = sum(map(lambda i: len(i) - len(eval(i)), parsed_input))

p2 = sum(map(lambda i: 2 + (i.count("\"") + i.count("\\")), parsed_input))

output(p1, p2)