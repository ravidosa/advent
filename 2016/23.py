from utils import *
inp = input_file(2016, 23).strip()

parsed_input = parser(inp, "{{le }}")

offset = parsed_input[19][1] * parsed_input[20][1]

p1 = math.factorial(7) + offset

p2 = math.factorial(12) + offset

output(p1, p2)