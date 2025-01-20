from utils import *
inp = input_file(2016, 2).strip()

parsed_input = parser(inp, ["\n", ""])

def press(keypad):
    pos = 0+0j
    code = ""
    for i in parsed_input:
        for key in i:
            if (pos + dir_letter[key]["comp"] in keypad):
                pos += dir_letter[key]["comp"]
        code += str(keypad[pos])
    return code

keypad = {-1+1j: 1, 0+1j: 2, 1+1j: 3, -1+0j: 4, 0+0j: 5, 1+0j: 6, -1-1j: 7, 0-1j: 8, 1-1j: 9}
p1 = press(keypad)

keypad = {0+2j: 1, -1+1j: 2, 0+1j: 3, 1+1j: 4, -2+0j: 5, -1+0j: 6, 0+0j: 7, 1+0j: 8, 2+0j: 9, -1-1j: "A", 0-1j: "B", 1-1j: "C", 0-2j: "D"}
p2 = press(keypad)

output(p1, p2)