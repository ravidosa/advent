from utils import *
inp = open("2015/input-7.txt", "r").read()

parsed_input = parser(inp, ["\n", r" -> | "])
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

wires = {inp[-1]: inp[:-1] for inp in parsed_input}
override = sig("a")
print(override)

wires = {inp[-1]: inp[:-1] for inp in parsed_input}
wires["b"] = override
print(sig("a"))