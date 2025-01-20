from utils import *
inp = input_file(2017, 4).strip()

parsed_input = parser(inp, ["\n", " "])

valid = lambda password: len(list(password)) == len(set(password))

p1 = sum(map(valid, parsed_input))

p2 = sum(map(valid, map(lambda i: map(fingerprint, i), parsed_input)))

output(p1, p2)