from utils import *
inp = input_file(2025, 6).strip()

parsed_input = parser(inp, "{{le }}")

tot = 0
for i in range(len(parsed_input[0])):
    par_tot = 0 if parsed_input[-1][i] == "+" else 1
    for j in range(len(parsed_input) - 1):
        if parsed_input[-1][i] == "+":
            par_tot += parsed_input[j][i]
        else:
            par_tot *= parsed_input[j][i]
    tot += par_tot
p1 = tot

parsed_input = transpose(make_rectangular(inp)).split("\n")

equations = []
for i in parsed_input:
    if i[-1] in ["+", "*"]:
        equations.append([i[-1]])
    if equations:
        row = re.sub(r"\+|\*| ", "", i)
        if len(row) > 0:
            equations[-1].append(int(row))
p2 = sum(functools.reduce(operator.mul if eqn[0] == "*" else operator.add, eqn[1:]) for eqn in equations)

output(p1, p2)