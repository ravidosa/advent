from utils import *
inp = input_file(2024, 13).strip().replace("\n", " ").replace("  ", "\n")

parsed_input = parser(inp, "Button A: X+{{i}}, Y+{{i}} Button B: X+{{i}}, Y+{{i}} Prize: X={{i}}, Y={{i}}")

def press(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    det = ax * by - bx * ay
    if det != 0:
        a_press = (px * by - bx * py) / det
        b_press = (py * ax - ay * px) / det
        return int(a_press * 3 + b_press) * (a_press.is_integer() and b_press.is_integer())

p1 = sum(press(i[:2], i[2:4], i[4:]) for i in parsed_input)

p2 = sum(press(i[:2], i[2:4], [i[4] + 10000000000000, i[5] + 10000000000000]) for i in parsed_input)

output(p1, p2)