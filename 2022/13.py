from utils import *
inp = input_file(2022, 13).strip().replace("\n\n", "\n")

parsed_input = parser(inp)

packets = [eval(i) for i in parsed_input]

def cmp(l, r):
    if type(l) is int and type(r) is int:
        return (l > r) - (l < r)
    elif type(l) is list and type(r) is list:
        if len(l) == 0 or len(r) == 0:
            return (len(l) > len(r)) - (len(l) < len(r))
        return first if (first := cmp(l[0], r[0])) else cmp(l[1:], r[1:])
    else:
        return cmp([l] if type(l) is int else l, [r] if type(r) is int else r)

p1 = sum((i + 1) * (cmp(packets[2 * i], packets[2 * i + 1]) == -1) for i in range(len(packets) // 2))

d1 = sum(cmp(i, [[2]]) == -1 for i in packets)
d2 = sum(cmp(i, [[6]]) == -1 for i in packets)    
p2 = (min(d1, d2) + 1) * (max(d1, d2) + 2)

output(p1, p2)