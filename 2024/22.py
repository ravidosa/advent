from utils import *
inp = open("2024/input-22.txt", "r").read().strip()

parsed_input = parser(inp, ["\n"])

s = 0
for i in parsed_input:
    for _ in range(2000):
        i = (i ^ (i * 64)) % 16777216
        i = (i ^ (i // 32)) % 16777216
        i = (i ^ (i * 2048)) % 16777216
    s += i
print(s)

maxbanana_dict = {}
for i in parsed_input:
    seen = set()
    pc = [None, None, None, None]
    for _ in range(2000):
        i_ = (i ^ (i * 64)) % 16777216
        i_ = (i_ ^ (i_ // 32)) % 16777216
        i_ = (i_ ^ (i_ * 2048)) % 16777216
        pc[:3] = pc[1:]
        pc[3] = i_ % 10 - i % 10
        i = i_
        if None not in pc and tuple(pc) not in seen:
            seen.add(tuple(pc))
            maxbanana_dict[tuple(pc)] = maxbanana_dict.get(tuple(pc), 0) + (i % 10)
print(max(maxbanana_dict.values()))