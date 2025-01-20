from utils import *
inp = input_file(2023, 24).strip()

parsed_input = parser(inp, ["\n", " @ |, "])

def intersect2d(h1, h2):
    px1, py1, _, vx1, vy1, _ = h1
    px2, py2, _, vx2, vy2, _ = h2
    det = vx1 * vy2 - vx2 * vy1
    if det != 0:
        t1, t2 = (vy2 * (px2 - px1) - vx2 * (py2 - py1)) / det, (vy1 * (px2 - px1) - vx1 * (py2 - py1)) / det
        if t1 >= 0 and t2 >= 0:
            return px1 + t1 * vx1, py1 + t1 * vy1
    return (math.inf, math.inf)
p1 = sum(all(200000000000000 <= coord <= 400000000000000 for coord in intersect2d(h1, h2)) for h1, h2 in itertools.combinations(parsed_input, 2))

p = z3.IntVector("p", 3)
v = z3.IntVector("v", 3)
t = z3.IntVector("t", 3)
sol = z3.Solver()
for h in range(3):
    for c in range(3):
        sol.add(p[c] - parsed_input[h][c] == t[h] * (v[c] - parsed_input[h][c + 3]))
sol.check()
p2 = sol.model().evaluate(sum(p))

output(p1, p2)