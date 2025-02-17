from utils import *
inp = input_file(2017, 6).strip()

parsed_input = parser(inp, "{{li\s}}")

config = parsed_input.copy()
vis = []
cycle = 0
while tuple(config) not in vis:
    vis.append(tuple(config))
    maxbank = argmax(config)
    blocks = config[maxbank]
    config[maxbank] = 0
    for i in range(1, blocks + 1):
        config[(maxbank + i) % len(config)] += 1
    cycle += 1
p1 = cycle

p2 = cycle - vis.index(tuple(config))

output(p1, p2)