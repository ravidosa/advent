from utils import *
inp = input_file(2017, 4).strip()

parsed_input = parser(inp, ["\n", " "])
print(sum(map(lambda i: len(i) == len(set(i)), parsed_input)))

parsed_input = parser(inp, ["\n", " "], fingerprint)
print(sum(map(lambda i: len(i) == len(set(i)), parsed_input)))