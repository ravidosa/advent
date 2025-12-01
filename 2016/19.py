from utils import *
inp = input_file(2016, 19).strip()

n = int(inp)
L = n - 2 ** (n.bit_length() - 1)

p1 = 2 * L + 1

tern = 3 ** (len(dec_to_tern(n, 0)) - 1)
p2 = n - tern if n <= 2 * tern else tern + 2 * (n - 2 * tern)

output(p1, p2)