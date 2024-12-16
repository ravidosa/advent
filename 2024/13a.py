f = open("2024/input-13.txt", "r")
inp = f.read().split("\n\n")

tok = 0

for i in inp:
    isp = i.split("\n")
    a = (int(isp[0][isp[0].index("X") + 2:isp[0].index(",")]), int(isp[0][isp[0].index("Y") + 2:]))
    b = (int(isp[1][isp[1].index("X") + 2:isp[1].index(",")]), int(isp[1][isp[1].index("Y") + 2:]))
    p = (int(isp[2][isp[2].index("X") + 2:isp[2].index(",")]), int(isp[2][isp[2].index("Y") + 2:]))
    if a[0] * b[1] - b[0] * a[1] != 0:
        a_press = (p[0] * b[1] - b[0] * p[1]) / (a[0] * b[1] - b[0] * a[1])
        b_press = (p[1] * a[0] - a[1] * p[0]) / (a[0] * b[1] - b[0] * a[1])
    if a_press == int(a_press) and b_press == int(b_press):
        tok += int(a_press * 3 + b_press)
print(tok)