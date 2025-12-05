from utils import *
inp = input_file(2025, 5).strip().split("\n\n")

fresh = parser(inp[0], "{{li-}}")
parsed_input = parser(inp[1], "{{i}}")

tot = 0
for i in parsed_input:
    for pair in fresh:
        l, r = pair
        if l <= i <= r:
            tot += 1
            break
p1 = tot

freshes = []
for l, r in sorted(fresh):
    if freshes and freshes[-1][1] >= l - 1:
        freshes[-1][1] = max(freshes[-1][1], r)
    else:
        freshes.append([l, r])
p2 = sum(rang[1] - rang[0] + 1 for rang in freshes)

output(p1, p2)