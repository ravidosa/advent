from utils import *
inp = input_file(2022, 3).strip()

parsed_input = parser(inp, ["\n"])

p1 = sum(alph.index(ii) + 1 for i in parsed_input for ii in set(i[:len(i) // 2]).intersection(set(i[len(i) // 2:])))

p2 = sum(alph.index(ii) + 1 for ind in range(len(parsed_input) // 3) for ii in set(parsed_input[3 * ind]).intersection(parsed_input[3 * ind + 1]).intersection(parsed_input[3 * ind + 2]))

output(p1, p2)