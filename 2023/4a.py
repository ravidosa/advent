f = open("2023/input-4.txt", "r")
inp = f.read().split("\n")
com = [len(set([int(x.strip()) for x in filter(lambda x: x != "", i[i.index("|") + 2:].split(" "))]).intersection(set([int(x.strip()) for x in filter(lambda x: x != "", i[i.index(":") + 2: i.index("|") - 1].split(" "))]))) for i in inp[:-1]]
print(sum([2 ** (c - 1) if c > 0 else 0 for c in com]))