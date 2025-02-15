from utils import *
inp = input_file(2015, 23).strip()

parsed_input = parser(inp, "{{le\s|,}}")

def execute(reg):
    i = 0
    while 0 <= i < len(parsed_input):
        comm = parsed_input[i][0]
        if comm[0] == "hlf":
            reg[comm[1]] //= 2
            i += 1
        if comm[0] == "tpl":
            reg[comm[1]] *= 3
            i += 1
        if comm[0] == "inc":
            reg[comm[1]] += 1
            i += 1
        if comm[0] == "jmp":
            i += comm[1]
        if comm[0] == "jie":
            if reg[comm[1]] % 2 == 0:
                i += comm[2]
            else:
                i += 1
        if comm[0] == "jio":
            if reg[comm[1]] == 1:
                i += comm[2]
            else:
                i += 1
    return reg

p1 = execute({"a": 0, "b": 0})["b"]

p2 = execute({"a": 1, "b": 0})["b"]

output(p1, p2)