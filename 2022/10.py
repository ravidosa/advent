from utils import *
inp = input_file(2022, 10).strip()

parsed_input = parser(inp, ["\n", " "])

sigs = [1]
for i in parsed_input:
    sigs += [sigs[-1]]
    if i[0] == "addx":
        sigs += [sigs[-1] + i[1]]
p1 = sum(map(lambda i: (i + 1) * sigs[i], range(19, 220, 40)))

disp = ""
for i in range(len(sigs)):
    if abs(sigs[i] - (i % 40)) <= 1:
        disp += "##"
    else:
        disp += "  "
    if i % 40 == 39:
        disp += "\n"
p2 = disp

output(p1, p2)