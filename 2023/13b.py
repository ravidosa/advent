import numpy as np
f = open("2023/input-13.txt", "r")
inp = f.read().split("\n\n")
summy = 0
sm = 1
for i in inp[:-1]:
    pat = np.array([list(x) for x in i.split("\n")], dtype="str")
    for i in range(1, len(pat)):
        if np.sum(pat[max(0, 2 * i - len(pat)):i,:] != pat[min(len(pat) - 1, 2 * i - 1):i-1:-1,:]) == sm:
            summy += 100 * i
    for i in range(1, len(pat[0])):
        if np.sum(pat[:,max(0, 2 * i - len(pat[0])):i] != pat[:,min(len(pat[0]) - 1, 2 * i - 1):i-1:-1]) == sm:
            summy += i
print(summy)