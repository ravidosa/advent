f = open("2019/input-1.txt", "r")
inp = f.read().split("\n")

s = 0
for i in inp:
    s += int(i) // 3 - 2
print(s)