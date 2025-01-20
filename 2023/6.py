from utils import *
inp = input_file(2023, 6).strip()

parsed_input = parser(inp, ["Time: *|Distance: *|\n", " "])

p1 = prod(math.floor((t + (t ** 2 - 4 * d) ** 0.5) / 2) - math.ceil((t - (t ** 2 - 4 * d) ** 0.5) / 2) + 1 for t, d in zip(parsed_input[0], parsed_input[1]))

t, d = int("".join(map(str, parsed_input[0]))), int("".join(map(str, parsed_input[1])))
p2 = math.floor((t + (t ** 2 - 4 * d) ** 0.5) / 2) - math.ceil((t - (t ** 2 - 4 * d) ** 0.5) / 2) + 1

output(p1, p2)