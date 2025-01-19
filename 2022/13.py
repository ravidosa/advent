from utils import *
inp = input_file(2022, 13).strip()

parsed_input = parser(inp, ["\n\n|\n"], eval)

def cmp(l, r):
    if type(l) is int and type(r) is int:
        return (l > r) - (l < r)
    elif type(l) is list and type(r) is list:
        if len(l) == 0 or len(r) == 0:
            return (len(l) > len(r)) - (len(l) < len(r))
        return first if (first := cmp(l[0], r[0])) else cmp(l[1:], r[1:])
    else:
        return cmp([l] if type(l) is int else l, [r] if type(r) is int else r)

print(sum(map(lambda i: (i + 1) * (cmp(parsed_input[2 * i], parsed_input[2 * i + 1]) == -1), range(len(parsed_input) // 2))))

d1 = sum(map(lambda i: cmp(i, [[2]]) == -1, parsed_input))
d2 = sum(map(lambda i: cmp(i, [[6]]) == -1, parsed_input))    
print((min(d1, d2) + 1) * (max(d1, d2) + 2))