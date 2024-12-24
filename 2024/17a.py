f = open("2024/input-17.txt", "r")
inp = f.read().split("\n")

a, b, c = [int(i[i.index(":") + 2:]) for i in inp[0:3]]

prog = inp[-1][inp[-1].index(":") + 2:].split(",")
i = 0
while i < len(prog):
    opcode = prog[i]
    operand = prog[i + 1]

    literal = int(operand)
    combo = int(operand) if operand in ["0", "1", "2", "3"] else a if operand == "4" else b if operand == "5" else c

    if opcode == "0":
        a = a // (2 ** combo)
        i += 2
    if opcode == "1":
        b = b ^ literal
        i += 2
    if opcode == "2":
        b = combo % 8
        i += 2
    if opcode == "3":
        if a != 0:
            i = literal
        else:
            i += 2
    if opcode == "4":
        b = b ^ c
        i += 2
    if opcode == "5":
        print(str(combo % 8) + ",", end="")
        i += 2
    if opcode == "6":
        b = a // (2 ** combo)
        i += 2
    if opcode == "7":
        c = a // (2 ** combo)
        i += 2
print("")