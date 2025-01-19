from utils import *
inp = input_file(2015, 13).strip()

parsed_input = parser(inp, ["\n", r" would | happiness units by sitting next to | |\."])

matrix = {}
names = set()
for i in parsed_input:
    n1, gl, change, n2 = i
    matrix[(n1, n2)] = change * (1 if gl == "gain" else -1)
    names.update([n1, n2])
change = lambda seating: sum(map(lambda i: matrix.get((seating[i], seating[(i + 1) % len(names)]), 0) + matrix.get((seating[(i + 1) % len(names)], seating[i]), 0), range(len(seating))))

p1 = max(itertools.permutations(names), key=change)

names.add("me")
p2 = max(itertools.permutations(names), key=change)

output(p1, p2)