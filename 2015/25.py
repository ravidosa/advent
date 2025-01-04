from utils import *
inp = open("2015/input-25.txt", "r").read()

parsed_input = parser(inp, [r"To continue, please consult the code grid in the manual\.  Enter the code at row |, column |\."])

r, c = 1, 1
code = 20151125
while r != parsed_input[0] or c != parsed_input[1]:
    if r == 1:
        r, c = c + 1, 1
    else:
        r, c = r - 1, c + 1
    code = (code * 252533) % 33554393
print(code)