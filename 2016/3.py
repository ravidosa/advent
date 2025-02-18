from utils import *
inp = input_file(2016, 3).strip()

parsed_input = parser(inp, "{{li }}")

possible = lambda tri: tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0]
p1 = sum(map(possible, parsed_input))

for i in range(len(parsed_input) // 3):
    parsed_input[3 * i][1], parsed_input[3 * i + 1][0] = parsed_input[3 * i + 1][0], parsed_input[3 * i][1]
    parsed_input[3 * i][2], parsed_input[3 * i + 2][0] = parsed_input[3 * i + 2][0], parsed_input[3 * i][2]
    parsed_input[3 * i + 1][2], parsed_input[3 * i + 2][1] = parsed_input[3 * i + 2][1], parsed_input[3 * i + 1][2]
p2 = sum(map(possible, parsed_input))

output(p1, p2)