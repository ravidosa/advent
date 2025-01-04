from utils import *
inp = open("2016/input-3.txt", "r").read()

parsed_input = parser(inp, ["\n", " "])

possible = lambda tri: tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0]
print(sum(map(possible, parsed_input)))

for i in range(len(parsed_input) // 3):
    parsed_input[3 * i][1], parsed_input[3 * i + 1][0] = parsed_input[3 * i + 1][0], parsed_input[3 * i][1]
    parsed_input[3 * i][2], parsed_input[3 * i + 2][0] = parsed_input[3 * i + 2][0], parsed_input[3 * i][2]
    parsed_input[3 * i + 1][2], parsed_input[3 * i + 2][1] = parsed_input[3 * i + 2][1], parsed_input[3 * i + 1][2]
print(sum(map(possible, parsed_input)))