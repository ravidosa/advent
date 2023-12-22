f = open("2023/input-4.txt", "r")
inp = f.read().split("\n")
cop = [1 for _ in range(len(inp) - 1)]
com = [len(set([int(x.strip()) for x in filter(lambda x: x != "", i[i.index("|") + 2:].split(" "))]).intersection(set([int(x.strip()) for x in filter(lambda x: x != "", i[i.index(":") + 2: i.index("|") - 1].split(" "))]))) for i in inp[:-1]]
for ind, c in filter(lambda x: x[1] > 0, enumerate(com)):
    cop[ind + 1:ind + 1 + c] = [v + cop[ind] for v in cop[ind + 1:ind + 1 + c]]
print(sum(cop))