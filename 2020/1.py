from utils import *
inp = open("2020/input-1.txt", "r").read()

parsed_input = parser(inp, ["\n"])

for pair in itertools.combinations(parsed_input, 2):
    if sum(pair) == 2020:
        break
print(pair[0] * pair[1])

for trio in itertools.combinations(parsed_input, 3):
    if sum(trio) == 2020:
        break
print(trio[0] * trio[1] * trio[2])