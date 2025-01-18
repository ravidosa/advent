from utils import *
inp = open("2015/input-10.txt", "r").read()

result = inp
for _ in range(40):
    result = "".join(map(lambda pair: str(len(list(pair[1]))) + pair[0], itertools.groupby(result)))
print(len(result))

for _ in range(50 - 40):
    result = "".join([str(len(list(g))) + d for d, g in itertools.groupby(result)])
print(len(result))