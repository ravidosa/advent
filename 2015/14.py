from utils import *
inp = open("2015/input-14.txt", "r").read()

parsed_input = parser(inp, ["\n", r" can fly | km/s for | seconds, but then must rest for | seconds\."])

SECONDS = 2503
maxd = 0
for i in parsed_input:
    _, speed, time, rest = i
    d = SECONDS // (time + rest) * time * speed + min(SECONDS % (time + rest), time) * speed
    maxd = max(maxd, d)
print(maxd)

points = {}
for t in range(1, SECONDS + 1):
    maxd, maxr = 0, []
    for i in parsed_input:
        name, speed, time, rest = i
        d = t // (time + rest) * time * speed + min(t % (time + rest), time) * speed
        maxd, maxr = max(maxd, d), [name] if d > maxd else maxr + [name] if d == maxd else maxr
    for r in maxr:
        points[r] = points.get(r, 0) + 1
print(max(points.values()))