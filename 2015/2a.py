f = open("2015/input-2.txt", "r")
inp = [sorted([int(fff) for fff in ff.split("x")]) for ff in f.read().split("\n")]

print(sum(map(lambda x: 2 * (x[0] * x[1] + x[0] * x[2] + x[1] * x[2]) + x[0] * x[1], inp)))