from utils import *
inp = input_file(2016, 12).strip()

parsed_input = parser(inp, "{{le }}")

def execute(reg):
    i = 0
    def regmap(r):
        return r if type(r) == int else reg[r]
    while 0 <= i < len(parsed_input):
        comm = parsed_input[i]
        if comm[0] == "cpy":
            reg[comm[2]] = regmap(comm[1])
            i += 1
        if comm[0] == "inc":
            reg[comm[1]] += 1
            i += 1
        if comm[0] == "dec":
            reg[comm[1]] -= 1
            i += 1
        if comm[0] == "jnz":
            if regmap(comm[1]) != 0:
                i += regmap(comm[2])
            else:
                i += 1
    return reg

p1 = execute({"a": 0, "b": 0, "c": 0, "d": 0})["a"]

p2 = execute({"a": 0, "b": 0, "c": 1, "d": 0})["a"]

output(p1, p2)