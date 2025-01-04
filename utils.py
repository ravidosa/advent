import re, cmath

lower = "abcdefghijklmnopqrstuvwxyz"

def parser(input, split, par):
    if len(split) == 1:
        return list(map(lambda inp: par[min(inp[0], len(par) - 1)](inp[1]), enumerate(filter(None, re.split(split[0], input)))))
    else:
        return list(map(lambda inp: parser(inp, split[1:], par), filter(None, re.split(split[0], input))))

# GRID
dir = {"^": 0+1j, ">": 1+0j, "v": 0-1j, "<": -1+0j}

def summer(iterable):
    if type(iterable) == int or type(iterable) == float:
        return iterable
    else:
        return sum(map(summer, iterable))