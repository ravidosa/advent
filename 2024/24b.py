from schemdraw.parsing import logicparse
f = open("2024/input-24.txt", "r")
init, conn = f.read().split("\n\n")
init, conn = init.split("\n"), conn.split("\n")

for ini in init:
    n, i = ini.split(": ")

z = len(init) // 2 + 1
xors = [None] * (z - 1)
ands = [None] * (z - 1)
cxors = [None] * (z - 1)
zees = [None] * z
cands = [None] * z
ors = [None] * z
for con in conn:
    i, n = con.split(" -> ")
    i = i.split(" ")
    if i[1] == "XOR" and ((i[0][0] == "x" and i[2][0] == "y") or (i[0][0] == "y" and i[2][0] == "x")):
        xors[int(i[0][1:])] = n
    if i[1] == "AND" and ((i[0][0] == "x" and i[2][0] == "y") or (i[0][0] == "y" and i[2][0] == "x")):
        ands[int(i[0][1:])] = n

for con in conn:
    i, n = con.split(" -> ")
    i = i.split(" ")
    if i[1] == "XOR" and (i[0] in xors or i[2] in xors):
        cxors[xors.index((i[0])) if i[0] in xors else xors.index(i[2])] = n
    if i[1] == "AND" and (i[0] in xors or i[2] in xors):
        cands[xors.index((i[0])) if i[0] in xors else xors.index(i[2])] = n
    if i[1] == "OR" and (i[0] in ands or i[2] in ands):
        ors[ands.index((i[0])) if i[0] in ands else ands.index(i[2])] = n

for i in range(z):
    print(i)
    if i != z - 1:
        print("s = " + str(cxors[i]) + " (" + str(xors[i]) + " xor c_in_" + str(i) + ")" )

print(xors)
print(ands)
print(ors)
print(cands)
print(cxors)

# and stare at it very hard