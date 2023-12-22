from collections import Counter
def val(hand):
    str = "23456789TJQKA"
    typs = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
    typ = sorted(list(Counter(hand).values()))
    return (typs.index(typ) * 16 ** 5 + str.index(hand[0]) * 16 ** 4 + str.index(hand[1]) * 16 ** 3 + str.index(hand[2]) * 16 ** 2 + str.index(hand[3]) * 16 ** 1 + str.index(hand[4]))

f = open("2023/input-7.txt", "r")
inp = f.read().split("\n")
print(sum([(x[0] + 1) * x[1][1] for x in enumerate(sorted([(i.split(" ")[0], int(i.split(" ")[1])) for i in inp[:-1]],  key = lambda x: val(x[0])))]))