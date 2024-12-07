import itertools

f = open("2024/input-7.txt", "r")
inp = f.read().split("\n")

s = 0

def evally(vals, ops):
    res = vals[0]
    for ind, op in enumerate(ops):
        if op == "+":
            res += vals[ind + 1]
        else:
            res *= vals[ind + 1]
    return res

for i in inp:
    test = int(i[:i.index(":")])
    vals = [int(ii) for ii in i[i.index(":") + 2:].split(" ")]

    val = False

    for j in range(2 ** (len(vals) - 1)):
        conf = format(j, "0" + str(len(vals) - 1) + 'b')
        ops = ["+" if pos == "0" else "*" for pos in conf]

        chk = evally(vals, ops)
        if chk == test:
            val = True
    
    if val == True:
        s += test

print(s)