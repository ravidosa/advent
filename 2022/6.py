from utils import *
inp = open("2022/input-6.txt", "r").read().strip()

i = 4
while i < len(inp) and len(set(inp[i - 4:i])) != 4:
    i += 1
print(i)

i = 14
while i < len(inp) and len(set(inp[i - 14:i])) != 14:
    i += 1
print(i)