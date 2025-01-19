from utils import *
inp = input_file(2015, 1).strip()

print(inp.count("(") - inp.count(")"))

floor, pos = 0, 0
while floor >= 0:
    floor += (1 if inp[pos] == "(" else -1)
    pos += 1
print(pos)