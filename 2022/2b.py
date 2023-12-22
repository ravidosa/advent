osc = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
shsc = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}
f = open("2022/input-2.txt", "r")
inp = f.read().split("\n")
score = 0
for i in inp[:-1]:
    score += (shsc[i] + osc[i[2]])
print(score)