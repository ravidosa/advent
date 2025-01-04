from utils import *
inp = open("2015/input-1.txt", "r").read().strip()

print(inp.count("(") - inp.count(")"))

floor, pos = 0, 0
while floor >= 0:
    floor += (1 if inp[pos] == "(" else -1)
    pos += 1
print(pos)