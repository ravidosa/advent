f = open("2022/input-13.txt", "r")
inp = f.read().split("\n")
while "" in inp:
    inp.remove("")
def compare(l, r):
    if type(l) is int and type(r) is int:
        return (l > r) - (l < r)
    elif type(l) is list and type(r) is list:
        if len(l) == 0 or len(r) == 0:
            return (len(l) > len(r)) - (len(l) < len(r))
        elif compare(l[0], r[0]) == 0:
            return compare(l[1:], r[1:])
        else:
            return compare(l[0], r[0])
    else:
        l, r = ([l] if type(l) is int else l), ([r] if type(r) is int else r)
        return compare(l, r)
d1 = 0 
d2 = 0    
for i in inp:
    d1 += int(compare([[2]], eval(i)) == 1)
    d2 += int(compare([[6]], eval(i)) == 1)
print((min(d1, d2) + 1) * (max(d1, d2) + 2))