from utils import *
inp = input_file(2021, 1).strip()

parsed_input = parser(inp, ["\n"])

print(sum(map(lambda i: parsed_input[i - 1] < parsed_input[i], range(1, len(parsed_input)))))

print(sum(map(lambda i: sum(parsed_input[i - 3: i]) < sum(parsed_input[i - 2: i + 1]), range(3, len(parsed_input)))))