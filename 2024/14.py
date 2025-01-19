from utils import *
inp = input_file(2024, 14).strip()

parsed_input = parser(inp, ["\n", " ", "p=|v=|,"])

W, H = 101, 103
def safety(t):
    quads = [0, 0, 0, 0]
    for i in parsed_input:
        p, v = i
        pxf, pyf = (p[0] + v[0] * t) % W, (p[1] + v[1] * t) % H
        if pxf != W // 2 and pyf != H // 2:
            quads[2 * (pxf > W // 2) + (pyf > H // 2)] += 1
    return prod(quads)

print(safety(100))

mint1, mint2 = sorted(range(max(W, H)), key=safety)[:2]
posst = [chi_rem([mint1, mint2], [W, H]), chi_rem([mint2, mint1], [W, H])]
print(min(posst, key=safety))