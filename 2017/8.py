from utils import *
inp = input_file(2017, 8).strip()

parsed_input = parser(inp, "{{s}} {{s}} {{i}} if {{s}} {{s}} {{s}}")

regm = []
reg = {}
for i in parsed_input:
    if eval(str(reg.get(i[3], 0)) + i[4] + str(i[5])):
        reg[i[0]] = reg.get(i[0], 0) + (i[2] if i[1] == "inc" else -i[2])
    regm.append(max(reg.values()))

p1 = regm[-1]

p2 = max(regm)

output(p1, p2)