f = open("2022/input-10.txt", "r")
inp = f.read().split("\n")
screen = list("###.....................................")
sigs = [1]
for i in inp[:-1]:
    if i[0:5] == "addx ":
        sigs.append(sigs[-1])
        sigs.append(sigs[-1] + int(i[5:]))
    elif i[0:4] == "noop":
        sigs.append(sigs[-1])
for i, sig in enumerate(sigs):
    if abs(sig - (i % 40)) <= 1:
        print("#", end="")
    else:
        print( ".", end="")
    if i % 40 == 39:
        print("")