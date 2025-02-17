from utils import *
inp = input_file(2023, 15).strip()

parsed_input = parser(inp, "{{ls,}}")

hash = lambda string, curr=0: curr if len(string) == 0 else hash(string[1:], 17 * (curr + ord(string[0])) % 256)

p1 = sum(hash(i) for i in parsed_input)

boxes = {}
for i in parsed_input:
    if i[-1] == "-":
        h = hash(i[:-1])
        boxes[h] = [(l, f) for l, f in boxes.get(h, []) if l != i[:-1]]
    elif i[-2] == "=":
        h = hash(i[:-2])
        match = [ind for ind, (l, _) in enumerate(boxes.get(h, [])) if l == i[:-2]]
        if len(match) == 0:
            boxes[h] = boxes.get(h, []) + [(i[:-2], int(i[-1]))]
        else:
            boxes[h][match[0]] = (i[:-2], int(i[-1]))
p2 = sum((b + 1) * (ind + 1) * f for b in boxes for ind, (_, f) in enumerate(boxes[b]))

output(p1, p2)