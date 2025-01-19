from utils import *
inp = input_file(2016, 4).strip()

parsed_input = parser(inp, ["\n", r"-|\[|\]"])

real = lambda room: room[-2] * ("".join(sorted(lower, key=lambda l: -("".join(room[:-2]).count(l))))[:5] == room[-1])
print(sum(map(real, parsed_input)))

for i in parsed_input:
    if "north" in "".join(map(lambda l: lower[(lower.index(l) + i[-2]) % 26] if l != " " else l, " ".join(inp[:-2]))):
        print(i[-2])