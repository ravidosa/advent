from utils import *
inp = input_file(2016, 20).strip()

parsed_input = parser(inp, "{{i}}-{{i}}")

MAX = 2 ** 32

blocked = sorted(parsed_input)
ip, ind = 0, 0
free = MAX
tot = 0
while ip < MAX:
    lower, upper = blocked[ind]
    if ip >= lower:
        if ip <= upper:
            ip = upper + 1
            continue
        ind += 1
    else:
        free = min(ip, free)
        tot += 1
        ip += 1

p1 = free

p2 = tot

output(p1, p2)