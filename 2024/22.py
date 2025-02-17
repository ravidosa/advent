from utils import *
inp = input_file(2024, 22).strip()

parsed_input = parser(inp)

def next_secret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

s = 0
for i in parsed_input:
    secret = i
    for _ in range(2000):
        secret = next_secret(secret)
    s += secret
p1 = s

maxbanana_dict = {}
for i in parsed_input:
    seen = set()
    pc = [None, None, None, None]
    secret = i
    for _ in range(2000):
        secret, pc = next_secret(secret), pc[1:] + [next_secret(secret) % 10 - secret % 10]
        if None not in pc and tuple(pc) not in seen:
            seen.add(tuple(pc))
            maxbanana_dict[tuple(pc)] = maxbanana_dict.get(tuple(pc), 0) + (secret % 10)
p2 = max(maxbanana_dict.values())

output(p1, p2)