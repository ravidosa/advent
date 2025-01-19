from utils import *
inp = input_file(2020, 8).strip()

parsed_input = parser(inp, ["\n", " "])

acc, i = 0, 0
run = set()
while i not in run:
    run.add(i)
    if parsed_input[i][0] == "acc":
        acc += parsed_input[i][1]
        i += 1
    elif parsed_input[i][0] == "jmp":
        i += parsed_input[i][1]
    else:
        i += 1
print(acc)

for j in range(len(parsed_input)):
    modified = [i.copy() for i in parsed_input]
    if modified[j][0] != "acc":
        modified[j][0] = "nop" if modified[j][0] == "jmp" else "jmp"
        acc, i = 0, 0
        run = set()
        while i not in run and i < len(parsed_input):
            run.add(i)
            if modified[i][0] == "acc":
                acc += modified[i][1]
                i += 1
            elif modified[i][0] == "jmp":
                i += modified[i][1]
            else:
                i += 1
        if i == len(parsed_input):
            break
    else:
        continue
print(acc)