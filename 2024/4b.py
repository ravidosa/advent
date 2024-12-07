import re

f = open("2024/input-4.txt", "r")
inp = f.read().split("\n")

s = 0

x = len(inp[0])
y = len(inp)

for i in range(1, y - 1):
    for j in range(1, x - 1):
        if i == 2 and j == 6:
            print(inp[i - 1][j - 1], inp[i + 1][j - 1], inp[i - 1][j + 1], inp[i + 1][j + 1])
        if inp[i][j] == "A":
            if inp[i - 1][j - 1] == "M" and inp[i + 1][j - 1] == "M" and inp[i - 1][j + 1] == "S" and inp[i + 1][j + 1] == "S":
                s += 1
            if inp[i - 1][j - 1] == "M" and inp[i + 1][j - 1] == "S" and inp[i - 1][j + 1] == "M" and inp[i + 1][j + 1] == "S":
                s += 1
            if inp[i - 1][j - 1] == "S" and inp[i + 1][j - 1] == "M" and inp[i - 1][j + 1] == "S" and inp[i + 1][j + 1] == "M":
                s += 1
            if inp[i - 1][j - 1] == "S" and inp[i + 1][j - 1] == "S" and inp[i - 1][j + 1] == "M" and inp[i + 1][j + 1] == "M":
                s += 1
print(s)