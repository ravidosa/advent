from utils import *
inp = input_file(2016, 25).strip()

parsed_input = parser(inp, "{{le }}")

offset = parsed_input[1][1] * parsed_input[2][1]

binn = 2
while binn < offset:
    binn = binn * 4 + 2

p1 = binn - offset

output(p1, p2)