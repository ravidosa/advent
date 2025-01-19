from utils import *
inp = input_file(2015, 23).strip()

parsed_input = parser(inp, ["\n", ", | "])

reg = {"a": 0, "b": 0}
i = 0
while 0 <= i < len(parsed_input):
    inp = parsed_input[i]
    if inp[0] == "hlf":
        reg[inp[1]] //= 2
        i += 1
    if inp[0] == "tpl":
        reg[inp[1]] *= 3
        i += 1
    if inp[0] == "inc":
        reg[inp[1]] += 1
        i += 1
    if inp[0] == "jmp":
        i += inp[1]
    if inp[0] == "jie":
        if reg[inp[1]] % 2 == 0:
            i += inp[2]
        else:
            i += 1
    if inp[0] == "jio":
        if reg[inp[1]] == 1:
            i += inp[2]
        else:
            i += 1
p1 = reg["b"]

reg = {"a": 1, "b": 0}
i = 0
while 0 <= i < len(parsed_input):
    inp = parsed_input[i]
    if inp[0] == "hlf":
        reg[inp[1]] //= 2
        i += 1
    if inp[0] == "tpl":
        reg[inp[1]] *= 3
        i += 1
    if inp[0] == "inc":
        reg[inp[1]] += 1
        i += 1
    if inp[0] == "jmp":
        i += inp[1]
    if inp[0] == "jie":
        if reg[inp[1]] % 2 == 0:
            i += inp[2]
        else:
            i += 1
    if inp[0] == "jio":
        if reg[inp[1]] == 1:
            i += inp[2]
        else:
            i += 1
p2 = reg["b"]

output(p1, p2)