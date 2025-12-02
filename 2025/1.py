from utils import *
inp = input_file(2025, 1).strip()

parsed_input = parser(inp, "{{e}}")

dial = 50
zeros = 0
for turn in parsed_input:
    dire, dis = turn[0], int(turn[1:])
    dial = (dial + (-1 if dire == "L" else 1) * dis) % 100
    if dial == 0:
        zeros += 1
p1 = zeros

dial, prev_dial = 50, 50
zeros = 0
for turn in parsed_input:
    dire, dis = turn[0], int(turn[1:])
    zeros += (dis // 100)
    dis %= 100
    dial, prev_dial = dial + (-1 if turn[0] == "L" else 1) * dis, dial
    if dial >= 100 or dial < 0:
        dial %= 100
        if dial != 0 and prev_dial != 0:
            zeros += 1
    if dial == 0:
        zeros += 1
p2 = zeros

output(p1, p2)