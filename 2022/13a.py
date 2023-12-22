f = open("2022/input-13.txt", "r")
inp = f.read().split("\n\n")
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
corr = 0    
for ind, i in enumerate(inp):
    i = i.split("\n")
    l, r = i[0], i[1]
    corr += (ind + 1) * int(compare(eval(l), eval(r)) == -1)
print(corr)