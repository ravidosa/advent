from utils import *
import itertools
inp = open("2015/input-10.txt", "r").read()

result = inp
for _ in range(40):
    result = "".join([str(len(list(g))) + d for d, g in itertools.groupby(result)])
print(len(result))

result = inp
for _ in range(50):
    result = "".join([str(len(list(g))) + d for d, g in itertools.groupby(result)])
print(len(result))