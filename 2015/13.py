from utils import *
inp = open("2015/input-13.txt", "r").read()

parsed_input = parser(inp, ["\n", r" would | happiness units by sitting next to | |\."])

matrix = {}
names = set()
for i in parsed_input:
    n1, gl, change, n2 = i
    matrix[(n1, n2)] = change * (1 if gl == "gain" else -1)
    names.update([n1, n2])

maxch = 0
for seating in itertools.permutations(names):
    d = sum(map(lambda i: matrix.get((seating[i], seating[(i + 1) % len(names)]), 0) + matrix.get((seating[(i + 1) % len(names)], seating[i]), 0), range(len(seating))))
    maxch = max(maxch, d)
print(maxch)

names.add("me")
maxch = 0
for seating in itertools.permutations(names):
    d = sum(map(lambda i: matrix.get((seating[i], seating[(i + 1) % len(names)]), 0) + matrix.get((seating[(i + 1) % len(names)], seating[i]), 0), range(len(seating))))
    maxch = max(maxch, d)
print(maxch)