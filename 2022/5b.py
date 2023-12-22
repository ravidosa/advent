import re
f = open("2022/input-5.txt", "r")
inp = f.read().split("\n")
cr = (len(inp[0]) + 1) // 4
stack = [[] for _ in range(cr)]
i = 0
while (inp[i])[1] != "1":
    for j in range(cr):
        if (inp[i])[j * 4 + 1] != " ":
            stack[j].append((inp[i])[j * 4 + 1])
    i += 1
for k in range(i + 2, len(inp) - 1):
    instr = [int(x) for x in re.split('move | from | to ', inp[k])[1:]]
    stack[instr[2] - 1] = (stack[instr[1] - 1])[:instr[0]] + (stack[instr[2] - 1])
    stack[instr[1] - 1] = (stack[instr[1] - 1])[instr[0]:]
print("".join([s[0] if len(s) > 0 else " " for s in stack]))