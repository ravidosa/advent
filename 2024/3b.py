import re

f = open("2024/input-3.txt", "r")
inp = f.read().split("do()")

s = 0
for i in inp:
    if i.find("don't()") != -1:
        i = i[:i.find("don't()")]
    mul = re.findall(r'mul\([0-9]+,[0-9]+\)', i)
    s += sum(map(lambda x: int(x[4:x.index(',')]) * int(x[x.index(',') + 1:-1]), mul))
print(s)