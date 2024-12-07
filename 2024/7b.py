import itertools

f = open("2024/input-7.txt", "r")
inp = f.read().split("\n")

s = 0

def evally(vals, ops):
    res = vals[0]
    for ind, op in enumerate(ops):
        if op == "+":
            res += vals[ind + 1]
        elif op == "*":
            res *= vals[ind + 1]
        else:
            res = int(str(res) + str(vals[ind + 1]))
    return res

def dec_to_tern(dec, N):
    if dec == 0:
        tern = "0"
    else:
        tern = ""
        while dec:
            dec, rem = divmod(dec, 3)
            tern = str(rem) + tern
    return tern.zfill(N)

for i in inp:
    test = int(i[:i.index(":")])
    vals = [int(ii) for ii in i[i.index(":") + 2:].split(" ")]

    val = False

    for j in range(3 ** (len(vals) - 1)):
        conf = dec_to_tern(j, len(vals) - 1)
        ops = ["+" if pos == "0" else "*" if pos == "1" else "||" for pos in conf]

        chk = evally(vals, ops)
        if chk == test:
            val = True
    
    if val == True:
        s += test

print(s)