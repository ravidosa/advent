f = open("2023/input-1.txt", "r")
inp = f.read().split("\n")
s = 0
letm = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0,}
for i in inp[:-1]:
    d1, d2 = None, None
    while (d1 == None or d2 == None) and len(i) > 0:
        for key, value in letm.items():
            if d1 == None and (i.startswith(key) or i.startswith(str(value))):
                d1 = value
            if d2 == None and (i.endswith(key) or i.endswith(str(value))):
                d2 = value
        i = i[int(d1 == None):len(i)-int(d2 == None)]
    s += (10 * d1 + d2)        
print(s)