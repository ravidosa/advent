from utils import *
inp = input_file(2015, 7).strip()

parsed_input = parser(inp, "`s (`s )?(`s )?-> `s")

def sig(tar):
    global wires
    if type(tar) is int:
        return tar
    ass = wires[tar]
    if type(ass) is int:
        return int(ass)
    elif len(ass) == 1 and (type(ass[0]) is int or ass[0].isdigit()):
        return int(ass[0])
    elif "AND" in ass:
        w1, _, w2 = ass
        wires[tar] = sig(w1) & sig(w2)
    elif "OR" in ass:
        w1, _, w2 = ass
        wires[tar] = sig(w1) | sig(w2)
    elif "NOT" in ass:
        _, w = ass
        wires[tar] = 2 ** 16 - 1 - sig(w)
    elif "LSHIFT" in ass:
        w, _, s = ass
        wires[tar] = (sig(w) << int(s)) % (2 ** 16)
    elif "RSHIFT" in ass:
        w, _, s = ass
        wires[tar] = sig(w) >> int(s)
    else:
        wires[tar] = sig(ass[0])
    return wires[tar]

wires = {i[-1]: i[:-1] for i in parsed_input}
override = sig("a")
p1 = override

wires = {i[-1]: i[:-1] for i in parsed_input}
wires["b"] = override
p2 = sig("a")

output(p1, p2)