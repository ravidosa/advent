from utils import *
inp = input_file(2017, 4).strip()

parsed_input = parser(inp, "{{ls\s}}")

valid = lambda password: len(list(password[0])) == len(set(password[0]))

p1 = sum(map(valid, parsed_input))

p2 = sum(valid([fingerprint(ii) for ii in i[0]]) for i in parsed_input)

output(p1, p2)