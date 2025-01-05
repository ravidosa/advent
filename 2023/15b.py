f = open("2023/input-15.txt", "r")
inp = f.read()
box = {}
def hash(i):
    cur = 0
    for j in range(len(i)):
        cur += ord(i[j])
        cur *= 17
        cur %= 256
    return cur
for i in inp[:-1].split(","):
    if i[-1] == "-":
        ii = hash(i[:-1])
        b = box.get(ii, [])
        box[ii] = list(filter(lambda x: not x[0].startswith(i[:-1]), box.get(ii, [])))
    elif i[-2] == "=":
        ii = hash(i[:-2])
        b = box.get(ii, [])
        mat = list(filter(lambda x: x[1][0].startswith(i[:-2]), enumerate(b)))
        if len(mat) == 0:
            b.append((i[:-2], int(i[-1])))
        else:
            b[mat[0][0]] = (i[:-2], int(i[-1]))
        box[ii] = b
print(sum([sum([(b[0] + 1) * (ii + 1) * bb[1] for ii, bb in enumerate(b[1])]) * (len(b[1]) > 0) for b in box.items()]))