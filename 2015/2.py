from utils import *
inp = open("2015/input-2.txt", "r").read()

parsed_input = parser(inp, ["\n", "x"], [int])

surface_area = lambda box: 2 * (box[0] * box[1] + box[0] * box[2] + box[1] * box[2]) + min(box[0] * box[1], box[0] * box[2], box[1] * box[2])
print(sum(map(surface_area, parsed_input)))

ribbon = lambda box: 2 * min(box[0] + box[1], box[0] + box[2], box[1] + box[2]) + box[0] * box[1] * box[2]
print(sum(map(ribbon, parsed_input)))