from utils import *
inp = input_file(2023, 5).strip().split("\n\n")

parsed_input = parser(inp[0], "seeds: {{li }}")
maps = [parser(i[i.index("\n") + 1:], "{{li }}") for i in inp[1:]]

def range_divide(li, lf, ri, rl):
    if li < ri and lf >= ri and lf < ri + rl:
        return [(li, ri - 1)], [(ri, li)]
    elif li >= ri and lf < ri + rl:
        return [], [(li, lf)]
    elif li >= ri and lf >= ri + rl and li < ri + rl:
        return [(ri + rl, lf)], [(li, ri + rl - 1)]
    elif li < ri and lf >= ri + rl:
        return [(li, ri - 1), (ri + rl, lf)], [(ri, ri + rl - 1)]
    else:
        return [(li, lf)], []

locs = parsed_input
for i in range(7):
    mapped = []
    for di, ri, rl in maps[i]:
        locs, mapped = [l for l in locs if l < ri or l >= ri + rl], mapped + [di + l - ri for l in locs if l >= ri and l < ri + rl]
    locs.extend(mapped)
p1 = min(locs)

locs = [(parsed_input[2 * i], parsed_input[2 * i] + parsed_input[2 * i + 1]) for i in range(len(parsed_input) // 2)]
for i in range(7):
    mapped = []
    for di, ri, rl in maps[i]:
        locs, mapped = [d for li, lf in locs for d in range_divide(li, lf, ri, rl)[0]], mapped + [tupadd(d, (di - ri, di - ri)) for li, lf in locs for d in range_divide(li, lf, ri, rl)[1]]
    locs.extend(mapped)
p2 = minval(locs, key=lambda l: l[0])

output(p1, p2)