from utils import *
inp = input_file(2024, 13).strip()

parsed_input = parser(inp, ["\n\n", "\n", "Button A: X|Button B: X|, Y=?|Prize: X="])

def press(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    det = ax * by - bx * ay
    if det != 0:
        a_press = (px * by - bx * py) / det
        b_press = (py * ax - ay * px) / det
        return int(a_press * 3 + b_press) * (a_press.is_integer() and b_press.is_integer())

p1 = sum(press(a, b, p) for a, b, p in parsed_input)

p2 = sum(press(a, b, [p[0] + 10000000000000, p[1] + 10000000000000]) for a, b, p in parsed_input)

output(p1, p2)