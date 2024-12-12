f = open("2024/input-11.txt", "r")
inp = [int(i) for i in f.read().split(" ")]

dic = {i: inp.count(i) for i in inp}

def rock(i):
    if i == 0:
        return [1]
    elif len(str(i)) % 2 == 0:
        n = len(str(i))
        return [int(str(i)[:n // 2]), int(str(i)[n // 2:])]
    else:
        return [2024 * i]

for j in range(25):
    dic_ = {}
    for k in dic:
        for kk in rock(k):
            dic_[kk] = dic_.get(kk, 0) + dic[k]
    dic = dic_
print(sum(dic.values()))