from utils import *
inp = input_file(2022, 7).strip()

parsed_input = parser(inp, ["\n", " "])

path = []
dirs = {"/": {}}
for i in parsed_input:
    if i[1] == "cd":
        if i[2] == "..":
            path.pop()
        else:
            path.append(i[2])
    elif i[0] == "dir":
        functools.reduce(operator.getitem, path, dirs)[i[1]] = {}
    elif i[1] == "ls":
        continue
    else:
        functools.reduce(operator.getitem, path, dirs)[i[1]] = i[0]
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