from utils import *
inp = open("2020/input-9.txt", "r").read()

parsed_input = parser(inp, ["\n"])

i = 25
while parsed_input[i] in list(map(sum, itertools.combinations(parsed_input[i - 25: i], 2))):
    i += 1
invalid = parsed_input[i]
print(invalid)

s, e = 0, 0
curr = 0
for i in range(len(parsed_input)):
    curr += parsed_input[i]
    if curr >= invalid:
        e = i
        while curr > invalid and s < e:
            curr -= parsed_input[s]
            s += 1
        if curr == invalid:
            break
print(min(parsed_input[s:e + 1]) + max(parsed_input[s:e + 1]))