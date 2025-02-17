from utils import *
inp = input_file(2024, 14).strip()

parsed_input = parser(inp, "p={{i}},{{i}} v={{i}},{{i}}")

W, H = 101, 103
def safety(t):
    quads = [0, 0, 0, 0]
    for i in parsed_input:
        p, v = i[:2], i[2:]
        pxf, pyf = (p[0] + v[0] * t) % W, (p[1] + v[1] * t) % H
        if pxf != W // 2 and pyf != H // 2:
            quads[2 * (pxf > W // 2) + (pyf > H // 2)] += 1
    return prod(quads)

p1 = safety(100)

mint1, mint2 = sorted(range(max(W, H)), key=safety)[:2]
posst = [chi_rem([mint1, mint2], [W, H]), chi_rem([mint2, mint1], [W, H])]
p2 = min(posst, key=safety)

output(p1, p2)