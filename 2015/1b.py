f = open("2015/input-1.txt", "r")
inp = f.read()

fl, i = 0, 0
while fl >= 0:
    fl += (1 if inp[i] == "(" else -1)
    i += 1
print(i)