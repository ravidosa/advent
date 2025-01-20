from utils import *
inp = input_file(2020, 5).strip()

parsed_input = parser(inp, ["\n"])

halver = lambda s, l, u: (l if s in "FL" else u) if len(s) == 1 else halver(s[1:], l + (u - l + 1) // 2 if s[0] in "BR" else l, u - (u - l + 1) // 2 if s[0] in "FL" else u)
p1 = maxval(parsed_input, key=lambda s: halver(s[:-3], 0, 127) * 8 + halver(s[-3:], 0, 7))

seats = set(range(1024))
empty = seats.difference(map(lambda s: halver(s[:-3], 0, 127) * 8 + halver(s[-3:], 0, 7), parsed_input))
p2 = next(filter(lambda s: s - 1 not in empty and s + 1 not in empty, empty))

output(p1, p2)