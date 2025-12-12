from utils import *
inp = input_file(2025, 12).strip()

inp_ = inp.split("\n\n")
trees, inp_ = inp_[:-1], inp_[-1]
trees = [t.split(":\n")[1] for t in trees]
parsed_input = parser(inp_, "{{i}}x{{i}}: {{li }}")

p1 = sum([i[0] * i[1] >= sum(trees[ind].count("#") * ii for ind, ii in enumerate(i[2])) for i in parsed_input])

output(p1, p2)