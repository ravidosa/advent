from utils import *
inp = open("2018/input-5.txt", "r").read().strip()

units = "|".join(map(lambda i: upper[i] + lower[i], range(26))) + "|" + "|".join(map(lambda i: lower[i] + upper[i], range(26)))
polymer = inp
while re.findall(units, polymer):
    polymer = re.sub(units, "", polymer)
print(len(polymer))

minl = len(inp)
for i in range(26):
    polymer = re.sub(lower[i] + "|" + upper[i], "", inp)
    while re.findall(units, polymer):
        polymer = re.sub(units, "", polymer)
    minl = min(minl, len(polymer))
print(minl)