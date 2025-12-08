from utils import *
inp = input_file(2017, 15).strip()

parsed_input = parser(inp, "Generator {{s}} starts with {{i}}")

a, b = parsed_input[0][1], parsed_input[1][1]
tot = 0
for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    tot += (a % (2 ** 16) == b % (2 ** 16))
p1 = tot

def AG():
    x = parsed_input[0][1]
    while True:
        x = (x * 16807) % 2147483647
        if x % 4 == 0:
            yield x
def BG():
    x = parsed_input[1][1]
    while True:
        x = (x * 48271) % 2147483647
        if x % 8 == 0:
            yield x
ag = AG()
bg = BG()
tot = 0
for _ in range(5000000):
    a, b = next(ag), next(bg)
    tot += (a % (2 ** 16) == b % (2 ** 16))
p2 = tot

output(p1, p2)