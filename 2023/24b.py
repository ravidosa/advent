from sympy import solve
from sympy.abc import x, y, z, t, u, v, a, b, c
f = open("2023/input-24.txt", "r")
inp = f.read().split("\n")
hail = [[[int(x) for x in ii.split(", ")] for ii in i.split(" @ ")] for i in inp[:-1]]
h1_1 = -1 * (x - hail[0][0][0]) / (t - hail[0][1][0]) - a
h1_2 = -1 * (y - hail[0][0][1]) / (u - hail[0][1][1]) - a
h1_3 = -1 * (z - hail[0][0][2]) / (v - hail[0][1][2]) - a
h2_1 = -1 * (x - hail[1][0][0]) / (t - hail[1][1][0]) - b
h2_2 = -1 * (y - hail[1][0][1]) / (u - hail[1][1][1]) - b
h2_3 = -1 * (z - hail[1][0][2]) / (v - hail[1][1][2]) - b
h3_1 = -1 * (x - hail[2][0][0]) / (t - hail[2][1][0]) - c
h3_2 = -1 * (y - hail[2][0][1]) / (u - hail[2][1][1]) - c
h3_3 = -1 * (z - hail[2][0][2]) / (v - hail[2][1][2]) - c
print([h1_1, h1_2, h1_3, h2_1, h2_2, h2_3, h3_1, h3_2, h3_3])
sol = solve([h1_1, h1_2, h1_3, h2_1, h2_2, h2_3, h3_1, h3_2, h3_3], x, y, z, t, u, v, a, b, c, dict=True)
print(sol[0][x] + sol[0][y] + sol[0][z])
