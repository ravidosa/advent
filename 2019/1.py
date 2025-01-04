from utils import *
inp = open("2019/input-1.txt", "r").read()

parsed_input = parser(inp, ["\n"])

print(sum(map(lambda i: i // 3 - 2, parsed_input)))

s = 0
for i in parsed_input:
    while i // 3 - 2 > 0:
        i = i // 3 - 2
        s += i
print(s)