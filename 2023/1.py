from utils import *
inp = input_file(2023, 1).strip()

parsed_input = parser(inp, ["\n"], str)

def calibration(i):
    d1, d2 = None, None
    while (d1 == None or d2 == None) and len(i) > 0:
        d1 = int(i[0]) if d1 == None and i[0].isdigit() else d1
        d2 = int(i[-1]) if d2 == None and i[-1].isdigit() else d2
        i = i[d1 == None:len(i) - (d2 == None)]
    return 10 * d1 + d2
p1 = sum(map(calibration, parsed_input))

def calibration(i):
    d1, d2 = None, None
    while (d1 == None or d2 == None) and len(i) > 0:
        for card, dig in digits.items():
            d1 = dig if d1 == None and i.startswith(card) or i.startswith(str(dig)) else d1
            d2 = dig if d2 == None and i.endswith(card) or i.endswith(str(dig)) else d2
        i = i[d1 == None:len(i) - (d2 == None)]
    return 10 * d1 + d2
p2 = sum(map(calibration, parsed_input))

output(p1, p2)