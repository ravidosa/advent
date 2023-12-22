f = open("2022/input-1.txt", "r")
inp = f.read().split("\n\n")
maxi = 0
for i in inp[:-1]:
    maxi = max(maxi, sum([int(x) for x in i.split("\n")]))
print(maxi)