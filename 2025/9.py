from utils import *
inp = input_file(2025, 9).strip()

parsed_input = parser(inp, "{{li,}}")

area = 0
for i in range(len(parsed_input)):
    for j in range(i + 1, len(parsed_input)):
        xi, yi = parsed_input[i]
        xj, yj = parsed_input[j]
        xi, xj = min(xi, xj), max(xi, xj)
        yi, yj = min(yi, yj), max(yi, yj)
        area = max((xj - xi + 1) * (yj - yi + 1), area)
p1 = area

polygon = shapely.Polygon(parsed_input)
area = 0
for i in range(len(parsed_input)):
    for j in range(i + 1, len(parsed_input)):
        xi, yi = parsed_input[i]
        xj, yj = parsed_input[j]
        xi, xj = min(xi, xj), max(xi, xj)
        yi, yj = min(yi, yj), max(yi, yj)
        if polygon.contains(shapely.Polygon([(xi, yi), (xj, yi), (xj, yj), (xi, yj)])):
            area = max((xj - xi + 1) * (yj - yi + 1), area)
p2 = area

output(p1, p2)