f = open("2022/input-1.txt", "r")
inp = f.read().split("\n\n")
max1 = 0
max2 = 0
max3 = 0
for i in inp[:-1]:
    el = sum([int(x) for x in i.split("\n")])
    max1, max2, max3 = max(max1, el), min(max1, max(max2, el)),  min(max2, max(max3, el))
print(max1 + max2 + max3)