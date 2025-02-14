from utils import *
inp = input_file(2015, 2).strip()

parsed_input = parser(inp, "`ix`ix`i")

surface_area = lambda box: 2 * (box[0] * box[1] + box[0] * box[2] + box[1] * box[2]) + min(box[0] * box[1], box[0] * box[2], box[1] * box[2])
p1 = sum(map(surface_area, parsed_input))

ribbon = lambda box: 2 * min(box[0] + box[1], box[0] + box[2], box[1] + box[2]) + box[0] * box[1] * box[2]
p2 = sum(map(ribbon, parsed_input))

output(p1, p2)