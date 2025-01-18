from utils import *
inp = open("2024/input-19.txt", "r").read().strip().split("\n\n")

patterns = parser(inp[0], [", "])
parsed_input = parser(inp[1], ["\n"])
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

print(sum(map(lambda i: i != 0, matches)))

print(sum(matches))