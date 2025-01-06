from utils import *
inp = open("2015/input-20.txt", "r").read().strip()

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
print(min(presents, key=lambda i: i if presents[i] >= target else target))

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
print(min(presents, key=lambda i: i if presents[i] >= target else target))