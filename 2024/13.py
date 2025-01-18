from utils import *
inp = open("2024/input-13.txt", "r").read().strip()

parsed_input = parser(inp, ["\n\n", "\n", "Button A: X|Button B: X|, Y=?|Prize: X="])

tok = 0
for i in parsed_input:
    a, b, p = i
    if a[0] * b[1] - b[0] * a[1] != 0:
        a_press = (p[0] * b[1] - b[0] * p[1]) / (a[0] * b[1] - b[0] * a[1])
        b_press = (p[1] * a[0] - a[1] * p[0]) / (a[0] * b[1] - b[0] * a[1])
    tok += int(a_press * 3 + b_press) * (a_press.is_integer() and b_press.is_integer())
print(tok)

tok = 0
for i in parsed_input:
    a, b, p = i
    p[0] += 10000000000000
    p[1] += 10000000000000
    if a[0] * b[1] - b[0] * a[1] != 0:
        a_press = (p[0] * b[1] - b[0] * p[1]) / (a[0] * b[1] - b[0] * a[1])
        b_press = (p[1] * a[0] - a[1] * p[0]) / (a[0] * b[1] - b[0] * a[1])
    tok += int(a_press * 3 + b_press) * (a_press.is_integer() and b_press.is_integer())
print(tok)