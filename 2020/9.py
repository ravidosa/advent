from utils import *
inp = input_file(2020, 9).strip()

parsed_input = parser(inp)

i = 25
while parsed_input[i] in list(map(sum, itertools.combinations(parsed_input[i - 25: i], 2))):
    i += 1
invalid = parsed_input[i]
p1 = invalid

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
p2 = min(parsed_input[s:e + 1]) + max(parsed_input[s:e + 1])

output(p1, p2)