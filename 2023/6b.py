from math import floor, ceil
f = open("2023/input-6.txt", "r")
inp = f.read().split("\n")
t = int("".join(list(filter(lambda x: x != "", inp[0][inp[0].index(":") + 1:].split(" ")))))
d = int("".join(list(filter(lambda x: x != "", inp[1][inp[1].index(":") + 1:].split(" ")))))
print(floor((t + (t ** 2 - 4 * d) ** 0.5) / 2) - ceil((t - (t ** 2 - 4 * d) ** 0.5) / 2) + 1)