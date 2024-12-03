import re

f = open("2015/input-5.txt", "r")
inp = f.read().split("\n")

n = 0
for i in inp:
    if len(re.findall(r'(..).*\1', i)) >= 1:
        if len(re.findall(r'(.).\1', i)) >= 1:
            n += 1
print(n)