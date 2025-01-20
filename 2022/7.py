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
        sizes[dir] = (s := sum(sizer(k, path + [dir]) for k in functools.reduce(operator.getitem, path, dirs)[dir].keys()))
        return s
sizer("/", [])

p1 = sum(s for s in sizes.values() if s <= 100000)

p2 = min(s for s in sizes.values() if s >= (sizes["/"] - 40000000))

output(p1, p2)