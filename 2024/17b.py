import z3

f = open("2024/input-17.txt", "r")
inp = f.read().split("\n")


prog = inp[-1][inp[-1].index(":") + 2:].split(",")
x = z3.BitVec('x', 3 * len(prog) + 1)
s = z3.Optimize()
for i in range(len(prog)):
    s.add_soft(((((x >> (3 * i)) & 7) ^ 5) ^ 6 ^ ((x >> (3 * i)) >> (((x >> (3 * i)) & 7) ^ 5))) & 7 is int(prog[i]))
h = s.minimize(x)
s.check()
print(h.value())