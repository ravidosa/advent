from utils import *
inp = input_file(2016, 9).strip()

def decompress(s, mode):
    if "(" not in s:
        return len(s)
    else:
        ret = 0
        while "(" in s:
            op = s.find("(")
            ret += op
            s = s[op:]
            x, cp = s.index("x"), s.index(")")
            l, rep = int(s[1:x]), int(s[x + 1:cp])
            s = s[cp + 1:]
            if mode == 1:
                ret += l * rep
            elif mode == 2:
                ret += decompress(s[:l], 2) * rep
            s = s[l:]
        ret += len(s)
        return ret

p1 = decompress(inp, 1)

p2 = decompress(inp, 2)

output(p1, p2)