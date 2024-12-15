f = open("2015/input-7.txt", "r")
inp = f.read().split("\n")

wdic = {i.split(" -> ")[1]: i.split(" -> ")[0] for i in inp}

def sig(tar):
    if type(tar) == int or tar.isdigit():
        return int(tar)
    if "AND" in tar:
        w1, w2 = tar.split(" AND ")
        wdic[tar] = (int(w1) if w1.isdigit() else sig(w1)) & (int(w2) if w2.isdigit() else sig(w2))
    if "OR" in tar:
        w1, w2 = tar.split(" OR ")
        wdic[tar] = (int(w1) if w1.isdigit() else sig(w1)) | (int(w2) if w2.isdigit() else sig(w2))
    if "NOT" in tar:
        w = tar[4:]
        wdic[tar] = 2 ** 16 - 1 - (int(w) if w.isdigit() else sig(w))
    if "LSHIFT" in tar:
        w, s = tar.split(" LSHIFT ")
        wdic[tar] = ((int(w) if w.isdigit() else sig(w)) << int(s)) % (2 ** 16)
    if "RSHIFT" in tar:
        w, s = tar.split(" RSHIFT ")
        wdic[tar] = (int(w) if w.isdigit() else sig(w)) >> int(s)
    else:
        wdic[tar] = sig(wdic[tar])
    return wdic[tar]

print(sig("a"))