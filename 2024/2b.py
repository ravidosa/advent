f = open("2024/input-2.txt", "r")
inp = [[int(fff) for fff in ff.split(" ")] for ff in f.read().split("\n")]

s = 0
for i in inp:
    for j in range(len(i)):
        ii = i[:j] + i[j+1:]
        if (all(x<=y and 1<=abs(x-y)<=3 for x, y in zip(ii, ii[1:])) or all(x>=y and 1<=abs(x-y)<=3 for x, y in zip(ii, ii[1:]))):
            s += 1
            break
print(s)