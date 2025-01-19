from utils import *
inp = open("2022/input-9.txt", "r").read()

parsed_input = parser(inp, ["\n", " "])

rope = [0+0j] * 2
vis = set()
vis.add(rope[-1])
for inp in parsed_input:
    for _ in range(inp[1]):
        rope[0] += dir_letter[inp[0]]["comp"]
        for seg in range(1, 2):
            if abs(rope[seg - 1] - rope[seg]) > math.sqrt(2):
                rope[seg] += cmp((rope[seg - 1] - rope[seg]).real, 0) + cmp((rope[seg - 1] - rope[seg]).imag, 0) * 1j
        vis.add(rope[-1])
print(len(vis))

rope = [0+0j] * 10
vis = set()
vis.add(rope[-1])
for inp in parsed_input:
    for _ in range(inp[1]):
        rope[0] += dir_letter[inp[0]]["comp"]
        for seg in range(1, 10):
            if abs(rope[seg - 1] - rope[seg]) > math.sqrt(2):
                rope[seg] += cmp((rope[seg - 1] - rope[seg]).real, 0) + cmp((rope[seg - 1] - rope[seg]).imag, 0) * 1j
        vis.add(rope[-1])
print(len(vis))