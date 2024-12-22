import itertools
f = open("2024/input-22.txt", "r")
inp = map(int, f.read().split("\n"))

maxbanana = 0
bananadic = []
for i in inp:
    banandic = {}
    pc = [None, None, None, None]
    for _ in range(2000):
        i_ = (i ^ (i * 64)) % 16777216
        i_ = (i_ ^ (i_ // 32)) % 16777216
        i_ = (i_ ^ (i_ * 2048)) % 16777216
        pc[:3] = pc[1:]
        pc[3] = i_ % 10 - i % 10
        i = i_
        if None not in pc and tuple(pc) not in banandic:
            banandic[tuple(pc)] = i % 10
    bananadic.append(banandic)
for chang in itertools.product(range(-9, 10), repeat=4):
    maxbanana = max(maxbanana, sum(map(lambda i: i.get(chang, 0), bananadic)))
print(maxbanana)