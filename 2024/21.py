from utils import *
inp = input_file(2024, 21).strip()

parsed_input = parser(inp)

numeric = {"7": (0,0), "8": (1,0), "9": (2,0), "4": (0,1), "5": (1,1), "6": (2,1), "1": (0,2), "2": (1,2), "3": (2,2), "0": (1,3), "A": (2,3)}
directional = {"^": (1,0), "<": (0,1), "v": (1,1), ">": (2,1), "A": (2,0)}
@functools.cache
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
    path_up = "" if keypad == "n" else []
    for ind in range(len(path)):
        k1, k2 = pad[path[ind - 1]] if ind > 0 else pad["A"], pad[path[ind]]
        mp = min_press(k1, k2, keypad)
        path_up = path_up + (mp if keypad == "n" else [mp])
    return collections.Counter([path_up] if keypad == "n" else path_up)
def complexity(code, dir_robots):
    presses = route_press(code, "n")
    for _ in range(dir_robots):
        temp_presses = collections.Counter()
        for sub_route in presses:
            new_press = route_press(sub_route, "d")
            for press in new_press:
                new_press[press] *= presses[sub_route]
            temp_presses.update(new_press)
        presses = temp_presses
    return sum(len(p) * presses[p] for p in presses) * int(code[:-1])

p1 = sum(complexity(c, 2) for c in parsed_input)

p2 = sum(complexity(c, 25) for c in parsed_input)

output(p1, p2)