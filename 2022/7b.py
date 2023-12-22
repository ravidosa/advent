from functools import reduce
from operator import getitem
sizes = []
def sizer(dirs):
    if type(dirs) is int:
        return dirs
    elif type(dirs) is dict:
        s = sum(sizer(value) for key, value in dirs.items())
        sizes.append(s)
        return s
f = open("2022/input-7.txt", "r")
inp = f.read().split("\n")
dirs = {"/": {}}
stack = []
for i in inp[:-1]:
    if i == "$ cd ..":
        stack.pop()
    elif i[:5] == "$ cd ":
        stack.append(i[5:])
    elif i[:4] == "dir ":
        reduce(getitem, stack, dirs)[i[4:]] = {}
    elif i == "$ ls":
        pass
    else:
        file = i.split(" ")
        reduce(getitem, stack, dirs)[file[1]] = int(file[0])
sizer(dirs["/"])
print(min([size if size >= max(sizes) - 40000000 else 70000000 for size in sizes]))