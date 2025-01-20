from utils import *
inp = input_file(2018, 5).strip()

units = "|".join(upper[i] + lower[i] + "|" + lower[i] + upper[i] for i in range(26))
polymer = inp
while re.findall(units, polymer):
    polymer = re.sub(units, "", polymer)
p1 = len(polymer)

minl = len(inp)
for i in range(26):
    polymer = re.sub(lower[i] + "|" + upper[i], "", inp)
    while re.findall(units, polymer):
        polymer = re.sub(units, "", polymer)
    minl = min(minl, len(polymer))
p2 = minl

output(p1, p2)