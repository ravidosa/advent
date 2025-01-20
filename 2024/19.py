from utils import *
inp = input_file(2024, 19).strip().split("\n\n")

parsed_input = parser(inp[1], ["\n"])
patterns = parser(inp[0], [", "])

maxlen = maxval(patterns, key=len)
@functools.cache
def ways_match(design):
    w = 0
    for i in range(1, min(maxlen + 1, len(design))):
        if design[:i] in patterns:
            w += ways_match(design[i:])
    if design in patterns:
        w += 1
    return w
matches = [ways_match(design) for design in parsed_input]

p1 = sum(map(lambda i: i != 0, matches))

p2 = sum(matches)

output(p1, p2)