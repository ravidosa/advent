import re

f = open("2024/input-3.txt", "r")
inp = f.read()

mul = re.findall(r'mul\([0-9]+,[0-9]+\)', inp)
print(sum(map(lambda x: int(x[4:x.index(',')]) * int(x[x.index(',') + 1:-1]), mul)))