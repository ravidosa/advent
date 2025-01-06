from utils import *
inp = open("2022/input-7.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", " "])
path = []
dirs = {"/": {}}
for inp in parsed_input:
    if inp[1] == "cd":
        if inp[2] == "..":
            path.pop()
        else:
            path.append(inp[2])
    elif inp[0] == "dir":
        functools.reduce(operator.getitem, path, dirs)[inp[1]] = {}
    elif inp [1] == "ls":
        continue
    else:
        functools.reduce(operator.getitem, path, dirs)[inp[1]] = inp[0]
sizes = {}
def sizer(dir, path):
    if type(s := functools.reduce(operator.getitem, path, dirs)[dir]) is int:
        return s
    else:
        sizes[dir] = (s := sum(map(lambda k: sizer(k, path + [dir]), functools.reduce(operator.getitem, path, dirs)[dir].keys())))
        return s
sizer("/", [])

print(sum(filter(lambda s: s <= 100000, sizes.values())))

print(min(filter(lambda s: s >= (sizes["/"] - 40000000), sizes.values())))