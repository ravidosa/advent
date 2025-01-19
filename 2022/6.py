from utils import *
inp = input_file(2022, 6).strip()

i = 4
while i < len(inp) and len(set(inp[i - 4:i])) != 4:
    i += 1
print(i)

i = 14
while i < len(inp) and len(set(inp[i - 14:i])) != 14:
    i += 1
print(i)