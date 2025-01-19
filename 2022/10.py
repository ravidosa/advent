from utils import *
inp = input_file(2022, 10).strip()

parsed_input = parser(inp, ["\n", " "])

sigs = [1]
for i in parsed_input:
    sigs += [sigs[-1]]
    if i[0] == "addx":
        sigs += [sigs[-1] + i[1]]
print(sum(map(lambda i: (i + 1) * sigs[i], range(19, 220, 40))))

for i in range(len(sigs)):
    if abs(sigs[i] - (i % 40)) <= 1:
        print("##", end="")
    else:
        print("  ", end="")
    if i % 40 == 39:
        print("")