from utils import *
inp = input_file(2022, 3).strip()

parsed_input = parser(inp, ["\n"])

p1 = sum(map(lambda i: sum(map(lambda ii: alph.index(ii) + 1, set(i[:len(i) // 2]).intersection(set(i[len(i) // 2:])))), parsed_input))

p2 = sum(map(lambda ind: sum(map(lambda ii: alph.index(ii) + 1, set(parsed_input[3 * ind]).intersection(parsed_input[3 * ind + 1]).intersection(parsed_input[3 * ind + 2]))), range(len(parsed_input) // 3)))

output(p1, p2)