from utils import *
inp = open("2015/input-16.txt", "r").read()

parsed_input = parser(inp, ["\n", r"Sue |: |, "])

sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for i in parsed_input:
    num, pairs = inp[0], zip(i[1::2], i[2::2])
    if all(map(lambda p: sue[p[0]] == p[1], pairs)):
        break
print(num)

for i in parsed_input:
    num, pairs = inp[0], zip(i[1::2], i[2::2])
    if all(map(lambda p: sue[p[0]] < p[1] if p[0] in ["cats", "trees"] else sue[p[0]] > p[1] if p[0] in ["pomeranians", "goldfish"] else sue[p[0]] == p[1], pairs)):
        break
print(num)