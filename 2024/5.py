from utils import *
inp = open("2024/input-5.txt", "r").read().split("\n\n")

parsed_input = parser(inp[1], ["\n"])
order = parser(inp[0], ["\n", "\|"], str)
ordy = {}
for o in order:
    ordy[o[0]] = ordy.get(o[0], []) + [o[1]]

ord_reg = "|".join([("((" + "|".join(ordy[k]) + ").*" + k + ")") for k in ordy.keys()])
print(sum(map(lambda i: (len(re.findall(ord_reg, i)) == 0) * int((ii := i.split(","))[(len(ii) - 1) // 2]), parsed_input)))

s = 0
for i in parsed_input:
    if len(f := re.findall(ord_reg, i)) != 0:
        while len(f) != 0:
            ff = [fff for fff in f[0] if len(fff) > 2]
            ind = i.index(ff[0])
            i = i[:ind] + ff[0][-2:] + ff[0][2:-2] + ff[0][:2] + i[ind + len(ff[0]):]
            f = re.findall(ord_reg, i)
        s +=  int((ii := i.split(","))[(len(ii) - 1) // 2])
print(s)