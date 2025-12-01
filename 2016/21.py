from utils import *
inp = input_file(2016, 21).strip()

parsed_input = parser(inp, "{{lewith position|with letter|steps|step|based on position of letter|positions|through|to position| }}")

password = "abcdefgh"
length = len(password)
for instr in parsed_input:
    if instr[0] == "swap":
        if instr[1] == "position":
            password = password.replace(password[instr[2]], "_").replace(password[instr[3]], password[instr[2]]).replace("_", password[instr[3]])
        if instr[1] == "letter":
            password = password.replace(instr[2], "_").replace(instr[3], instr[2]).replace("_", instr[3])
    if instr[0] == "rotate":
        if instr[1] == "left":
            rot = instr[2] % length
            password = password[rot:] + password[:rot]
        elif instr[1] == "right":
            rot = length - (instr[2] % length)
            password = password[rot:] + password[:rot]
        else:
            ind = password.index(instr[1])
            rot = length - ((ind + 1 + (ind >= 4)) % length)
            password = password[rot:] + password[:rot]
    if instr[0] == "reverse":
        password = password[:instr[1]] + password[instr[1]:instr[2] + 1][::-1] + (password[instr[2] + 1:] if instr[2] + 1 < length else "")
    if instr[0] == "move":
        rem = password[instr[2]]
        password = password[:instr[2]] + password[instr[2] + 1:]
        password = password[:instr[3]] + rem + password[instr[3]:]
p1 = password

password = "fbgdceah"
length = len(password)
for instr in parsed_input[::-1]:
    if instr[0] == "swap":
        if instr[1] == "position":
            password = password.replace(password[instr[2]], "_").replace(password[instr[3]], password[instr[2]]).replace("_", password[instr[3]])
        if instr[1] == "letter":
            password = password.replace(instr[2], "_").replace(instr[3], instr[2]).replace("_", instr[3])
    if instr[0] == "rotate":
        if instr[1] == "left":
            rot = length - (instr[2] % length)
            password = password[rot:] + password[:rot]
        elif instr[1] == "right":
            rot = instr[2] % length
            password = password[rot:] + password[:rot]
        else:
            ind = password.index(instr[1])
            rot = ind // 2 + (ind % 2 == 1 or (1 if ind == 0 else 5))
            password = password[rot:] + password[:rot]
    if instr[0] == "reverse":
        password = password[:instr[1]] + password[instr[1]:instr[2] + 1][::-1] + (password[instr[2] + 1:] if instr[2] + 1 < length else "")
    if instr[0] == "move":
        rem = password[instr[3]]
        password = password[:instr[3]] + password[instr[3] + 1:]
        password = password[:instr[2]] + rem + password[instr[2]:]
p2 = password

output(p1, p2)