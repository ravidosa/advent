import re

f = open("2024/input-4.txt", "r")
inp = f.read().split("\n")

s = 0

x = len(inp[0])
y = len(inp)

for i in range(y):
    for j in range(x):
        if inp[i][j] == "X":
            if j <= x - 4 and inp[i][j + 1] == "M" and inp[i][j + 2] == "A" and inp[i][j + 3] == "S":
                s += 1
            if j >= 3 and inp[i][j - 1] == "M" and inp[i][j - 2] == "A" and inp[i][j - 3] == "S":
                s += 1
            if i <= y - 4 and inp[i + 1][j] == "M" and inp[i + 2][j] == "A" and inp[i + 3][j] == "S":
                s += 1
            if i >= 3 and inp[i - 1][j] == "M" and inp[i - 2][j] == "A" and inp[i - 3][j] == "S":
                s += 1
            if j <= x - 4 and i <= y - 4 and inp[i + 1][j + 1] == "M" and inp[i + 2][j + 2] == "A" and inp[i + 3][j + 3] == "S":
                s += 1
            if j >= 3 and i >= 3 and inp[i - 1][j - 1] == "M" and inp[i - 2][j - 2] == "A" and inp[i - 3][j - 3] == "S":
                s += 1
            if j <= x - 4 and i >= 3 and inp[i - 1][j + 1] == "M" and inp[i - 2][j + 2] == "A" and inp[i - 3][j + 3] == "S":
                s += 1
            if j >= 3 and i <= y - 4 and inp[i + 1][j - 1] == "M" and inp[i + 2][j - 2] == "A" and inp[i + 3][j - 3] == "S":
                s += 1
print(s)