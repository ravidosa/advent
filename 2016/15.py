from utils import *
inp = input_file(2016, 15).strip()

parsed_input = parser(inp, "Disc #{{i}} has {{i}} positions; at time=0, it is at position {{i}}.")

a1, n, a2 = transpose(parsed_input)
a = [-(a1_ + a2_) % n_ for a1_, a2_, n_ in zip(a1, a2, n)]

p1 = chi_rem(a, n)

p2 = chi_rem(a + [-(len(a) + 1) % 11], n + [11])

output(p1, p2)