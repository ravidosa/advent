f = open("2019/input-1.txt", "r")
inp = f.read().split("\n")

s = 0
for i in inp:
    i = int(i)
    while i // 3 - 2 > 0:
        i = i // 3 - 2
        s += i
print(s)