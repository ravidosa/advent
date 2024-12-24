f = open("2024/input-22.txt", "r")
inp = map(int, f.read().split("\n"))

s = 0
for i in inp:
    for _ in range(2000):
        i = (i ^ (i * 64)) % 16777216
        i = (i ^ (i // 32)) % 16777216
        i = (i ^ (i * 2048)) % 16777216
    s += i
print(s)