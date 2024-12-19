from functools import cache

f = open("2024/input-19.txt", "r")
inp = f.read().split("\n\n")

patterns, designs = inp[0].split(", "), inp[1].split("\n")
maxlen = len(max(patterns, key=len))

@cache
def ways_match(design):
    w = 0
    for i in range(1, min(maxlen + 1, len(design))):
        if design[:i] in patterns:
            w += ways_match(design[i:])
    if design in patterns:
        w += 1
    return w

ways = 0
for design in designs:
    ww = ways_match(design)
    ways += (ww != 0)
print(ways)