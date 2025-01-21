from utils import *
inp = input_file(2021, 8).strip()

parsed_input = parser(inp, ["\n", r" \| ", " "])

digit_segs = {(0, 1, 2, 4, 5, 6): "0", (2, 5): "1", (0, 2, 3, 4, 6): "2", (0, 2, 3, 5, 6): "3", (1, 2, 3, 5): "4", (0, 1, 3, 5, 6): "5", (0, 1, 3, 4, 5, 6): "6", (0, 2, 5): "7", (0, 1, 2, 3, 4, 5, 6): "8", (0, 1, 2, 3, 5, 6): "9"}

p1 = sum((seg := list(map(len, i[1]))).count(2) + seg.count(4) + seg.count(3) + seg.count(7) for i in parsed_input)

res = 0
for i in parsed_input:
    patterns = sorted(map(set, i[0]), key=len)
    s = [None] * 7
    s[0] = patterns[1].difference(patterns[0]).pop()
    s13 = patterns[2].difference(patterns[0])
    s036 = patterns[3].intersection(patterns[4]).intersection(patterns[5])
    s[3] = s13.intersection(s036).pop()
    s[1] = s13.difference(s036).pop()
    s0156 = patterns[6].intersection(patterns[7]).intersection(patterns[8])
    s[5] = s0156.difference(s036).difference(s13).pop()
    s[2] = patterns[2].difference({s[1], s[3], s[5]}).pop()
    s[6] = s0156.difference({s[0], s[1], s[5]}).pop()
    s[4] = patterns[9].difference(s).pop()
    segmap = {s[seg]: seg for seg in range(7)}
    res += int("".join(digit_segs[tuple(sorted(map(lambda d: segmap[d], dig)))] for dig in i[1]))
p2 = res

output(p1, p2)