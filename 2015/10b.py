f = open("2015/input-10.txt", "r")
inp = f.read()
prev = inp

for _ in range(50):
    res = ""
    ct = 1
    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            ct += 1
        else:
            res += str(ct) + prev[i - 1]
            ct = 1
    res += str(ct) + prev[-1]
    prev = res
print(len(res))