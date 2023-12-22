import re
f = open("2022/input-4.txt", "r")
inp = f.read().split("\n")
red = 0
for i in inp[:-1]:
    sec = [int(x) for x in re.split(',|-', i)]
    if (sec[0] <= sec[3] and sec[1] >= sec[2]) or (sec[0] >= sec[3] and sec[1] <= sec[2]):
        red += 1
print(red)