from utils import *
inp = input_file(2015, 2).strip()

parsed_input = parser(inp, ["\n", "x"])

surface_area = lambda box: 2 * (box[0] * box[1] + box[0] * box[2] + box[1] * box[2]) + min(box[0] * box[1], box[0] * box[2], box[1] * box[2])
print(sum(map(surface_area, parsed_input)))

ribbon = lambda box: 2 * min(box[0] + box[1], box[0] + box[2], box[1] + box[2]) + box[0] * box[1] * box[2]
print(sum(map(ribbon, parsed_input)))