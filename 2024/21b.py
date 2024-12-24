from functools import cache
from collections import Counter
f = open("2024/input-21.txt", "r")
inp = f.read().split("\n")

numeric = {"7": (0,0), "8": (1,0), "9": (2,0), "4": (0,1), "5": (1,1), "6": (2,1), "1": (0,2), "2": (1,2), "3": (2,2), "0": (1,3), "A": (2,3)}
directional = {"^": (1,0), "<": (0,1), "v": (1,1), ">": (2,1), "A": (2,0)}

@cache
def min_press(k1, k2, keypad):
    if keypad == "n":
        pad = numeric
    else:
        pad = directional
    x, y = (k2[0] - k1[0], k2[1] - k1[1])
    if x > 0 and (k1[0], k2[1]) in pad.values():
        return abs(y) * ("v" if y > 0 else "^") + abs(x) * (">" if x > 0 else "<") + "A" 
    elif (k2[0], k1[1]) in pad.values():
        return abs(x) * (">" if x > 0 else "<") + abs(y) * ("v" if y > 0 else "^") + "A" 
    else:
        return abs(y) * ("v" if y > 0 else "^") + abs(x) * (">" if x > 0 else "<") + "A"

def route_press(path, keypad):
    if keypad == "n":
        pad = numeric
    else:
        pad = directional
    path_up = []
    for ind in range(len(path)):
        k1, k2 = pad[path[ind - 1]] if ind > 0 else pad["A"], pad[path[ind]]
        path_up.append(min_press(k1, k2, keypad))
    return Counter(path_up)
def route_length(route):
    return sum(map(lambda p: len(p[0]) * p[1], route.items()))
def route_press_1(path, keypad):
    if keypad == "n":
        pad = numeric
    else:
        pad = directional
    path_up = ""
    for ind in range(len(path)):
        k1, k2 = pad[path[ind - 1]] if ind > 0 else pad["A"], pad[path[ind]]
        path_up += min_press(k1, k2, keypad)
    return path_up
            
comp = 0
for i in inp:
    i_ = Counter([route_press_1(i, "n")])
    for j in range(25):
        next_route = Counter()
        for k, v in i_.items():
            count = route_press(k, "d")
            for k in count:
                count[k] *= v
            next_route.update(count)
        i_ = next_route
    comp += route_length(i_) * int(i[:-1])
print(comp)