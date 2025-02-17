from utils import *
inp = input_file(2017, 4).strip()

parsed_input = parser(inp, "{{ls }}")

valid = lambda password: len(list(password)) == len(set(password))

p1 = sum(map(valid, parsed_input))

p2 = sum(valid([fingerprint(ii) for ii in i]) for i in parsed_input)

output(p1, p2)