from utils import *
inp = input_file(2015, 25).strip()

parsed_input = parser(inp, [r"To continue, please consult the code grid in the manual\.  Enter the code at row |, column |\."])

r, c = parsed_input
n = r + c - 1
t_n = n * (n + 1) // 2
p1 = (20151125 * pow(252533, t_n - r, 33554393)) % 33554393

output(p1)