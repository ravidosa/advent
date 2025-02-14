from utils import *
inp = input_file(2015, 8).strip()

parsed_input = parser(inp)

p1 = sum(len(i) - len(eval(i)) for i in parsed_input)

p2 = sum(2 + (i.count("\"") + i.count("\\")) for i in parsed_input)

output(p1, p2)