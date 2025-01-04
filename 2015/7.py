from utils import *
inp = open("2015/input-7.txt", "r").read()

parsed_input = parser(inp, ["\n", r" -> | "], [str])
def sig(tar):
    global wires
    ass = wires[tar]
    if type(ass) == int:
        return int(ass)
    elif len(ass) == 1 and (type(ass[0]) == int or ass[0].isdigit()):
        return int(ass[0])
    elif "AND" in ass:
        w1, _, w2 = ass
        wires[tar] = (int(w1) if w1.isdigit() else sig(w1)) & (int(w2) if w2.isdigit() else sig(w2))
    elif "OR" in ass:
        w1, _, w2 = ass
        wires[tar] = (int(w1) if w1.isdigit() else sig(w1)) | (int(w2) if w2.isdigit() else sig(w2))
    elif "NOT" in ass:
        _, w = ass
        wires[tar] = 2 ** 16 - 1 - (int(w) if w.isdigit() else sig(w))
    elif "LSHIFT" in ass:
        w, _, s = ass
        wires[tar] = ((int(w) if w.isdigit() else sig(w)) << int(s)) % (2 ** 16)
    elif "RSHIFT" in ass:
        w, _, s = ass
        wires[tar] = (int(w) if w.isdigit() else sig(w)) >> int(s)
    else:
        wires[tar] = sig(ass[0])
    return wires[tar]

wires = {inp[-1]: inp[:-1] for inp in parsed_input}
override = sig("a")
print(override)

wires = {inp[-1]: inp[:-1] for inp in parsed_input}
wires["b"] = override
print(sig("a"))