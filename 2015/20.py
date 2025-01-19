from utils import *
inp = input_file(2015, 20).strip()

target = math.ceil(int(inp) / 10)
presents = {}
found = False
for i in range(1, target + 1):
    for j in range(1, target // i + 1):
        presents[i * j] = presents.get(i * j, 0) + i
        if i == 1 and presents[i * j] >= target:
            found = True
            break
    if found:
        break
p1 = min(presents, key=lambda i: i if presents[i] >= target else target)

target = math.ceil(int(inp) / 11)
presents = {}
found = False
for i in range(1, target + 1):
    for j in range(1, min(51, target // i + 1)):
        presents[i * j] = presents.get(i * j, 0) + i
        if i == 1 and presents[i * j] >= target:
            found = True
            break
    if found:
        break
p2 = min(presents, key=lambda i: i if presents[i] >= target else target)

output(p1, p2)