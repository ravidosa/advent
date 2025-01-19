from utils import *
inp = input_file(2024, 2).strip()

parsed_input = parser(inp, ["\n", " "])

safe = lambda i: all(x<=y and 1<=abs(x-y)<=3 for x, y in zip(i, i[1:])) or all(x>=y and 1<=abs(x-y)<=3 for x, y in zip(i, i[1:]))
print(sum(map(safe, parsed_input)))

safe = lambda i: any(map(lambda j: (ii := i[:j] + i[j+1:]) and (all(x<=y and 1<=abs(x-y)<=3 for x, y in zip(ii, ii[1:])) or all(x>=y and 1<=abs(x-y)<=3 for x, y in zip(ii, ii[1:]))), range(len(i))))
print(sum(map(safe, parsed_input)))