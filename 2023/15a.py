f = open("2023/input-15.txt", "r")
inp = f.read()
tot = 0
for i in inp[:-1].split(","):
    cur = 0
    for j in range(len(i)):
        cur += ord(i[j])
        cur *= 17
        cur %= 256
    tot += cur
print(tot)