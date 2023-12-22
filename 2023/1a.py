f = open("2023/input-1.txt", "r")
inp = f.read().split("\n")
s = 0
for i in inp[:-1]:
    d1, d2 = None, None
    while (d1 == None or d2 == None) and len(i) > 0:
        if d1 == None and i[0].isdigit():
            d1 = int(i[0])
        if d2 == None and i[-1].isdigit():
            d2 = int(i[-1])
        i = i[int(d1 == None):len(i)-int(d2 == None)]
    s += (10 * d1 + d2)        
print(s)