f = open("2015/input-8.txt", "r")
inp = f.read().split("\n")

tot = 0

for i in inp:
    tot += 2 + (i.count("\"") + i.count("\\"))
print(tot)