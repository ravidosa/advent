f = open("2023/input-8.txt", "r")
inp = f.read().split("\n")
lrdict = {}
iii = list(inp[0])
for i in inp[2:-1]:
    ii = i.split(" = ")
    lrdict[ii[0]] = ii[1][1:-1].split(", ")
loc = "AAA"
j = 0
while loc != "ZZZ":
    loc = lrdict[loc][0 if iii[j % len(iii)] == "L" else 1]
    j += 1
print(j)