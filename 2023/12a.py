import functools
f = open("2023/input-12.txt", "r")
inp = f.read().split("\n")
@functools.lru_cache(maxsize=None)
def possy(s, rn, rm):
    if len(s) == 0:
        return int(rn == 0 and len(rm) == 0) or (len(rm) == 1 and rn != 0 and rn == rm[0])
    else:
        if (rn != 0 and (len(s) - s.count(".") + rn < sum(rm) or len(rm) == 0)) or (s[0] == "." and rn != 0 and rn != rm[0]):
            return 0
        else:
            poss = 0
            if (s[0] == "." and rn != 0) or (s[0] == "?" and rn != 0 and rn == rm[0]):
                poss += possy(s[1:], 0, rm[1:])
            if (s[0] == "#" or s[0] == "?"):
                poss += possy(s[1:], rn + 1, rm)
            if (s[0] == "." or s[0] == "?") and rn == 0:
                poss += possy(s[1:], 0, rm)
            return poss
s = 0
for i in inp[:-1]:
    ii = i.split(" ")
    dam = tuple([int(x) for x in ii[1].split(",")])
    s += possy(ii[0], 0, dam)
print(s)