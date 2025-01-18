from utils import *
inp = open("2015/input-24.txt", "r").read()

parsed_input = parser(inp, ["\n"])

for i in range(len(parsed_input)):
    if qes := [prod(c) for c in itertools.combinations(parsed_input, i) if sum(c) == sum(parsed_input) // 3]:
        break
print(min(qes))

for i in range(len(parsed_input)):
    if qes := [prod(c) for c in itertools.combinations(parsed_input, i) if sum(c) == sum(parsed_input) // 4]:
        break
print(min(qes))