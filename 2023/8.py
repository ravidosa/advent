from utils import *
inp = input_file(2023, 8).strip().split("\n\n")

parsed_input = parser(inp[1], ["\n", r" = \(|\)", ", "])

path = {n: lr for n, lr in parsed_input}

steps = 0
currn = "AAA"
while currn != "ZZZ":
    currn = path[currn][0 if inp[0][steps % len(inp[0])] == "L" else 1]
    steps += 1
p1 = steps

lcm = 1
steps = 0
currn = [n for n in path if n[-1] == "A"]
while len(currn) > 0:
    currn = [path[c][0 if inp[0][steps % len(inp[0])] == "L" else 1] for c in currn]
    steps += 1
    if any(c[-1] == "Z" for c in currn):
        lcm = math.lcm(lcm, steps)
    currn = [c for c in currn if c[-1] != "Z"]
p2 = lcm

output(p1, p2)