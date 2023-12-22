shsc = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
osc = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}
f = open("2022/input-2.txt", "r")
inp = f.read().split("\n")
score = 0
for i in inp[:-1]:
    score += (shsc[i[2]] + osc[i])
print(score)