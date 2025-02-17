from utils import *
inp = input_file(2023, 6).strip()

parsed_input = parser(inp, "{{s}}: {{li\s}}")

time, dist = parsed_input[0][1], parsed_input[1][1]

p1 = prod(math.floor((t + (t ** 2 - 4 * d) ** 0.5) / 2) - math.ceil((t - (t ** 2 - 4 * d) ** 0.5) / 2) + 1 for t, d in zip(time, dist))

t, d = int("".join(map(str, time))), int("".join(map(str, dist)))
p2 = math.floor((t + (t ** 2 - 4 * d) ** 0.5) / 2) - math.ceil((t - (t ** 2 - 4 * d) ** 0.5) / 2) + 1

output(p1, p2)