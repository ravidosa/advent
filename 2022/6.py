from utils import *
inp = input_file(2022, 6).strip()

def marker_ind(length):
    i = length
    while i < len(inp) and len(set(inp[i - length:i])) != length:
        i += 1
    return i

p1 = marker_ind(4)

p2 = marker_ind(14)

output(p1, p2)