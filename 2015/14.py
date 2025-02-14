from utils import *
inp = input_file(2015, 14).strip()

parsed_input = parser(inp, ["\n", r" can fly | km/s for | seconds, but then must rest for | seconds\."])

dist = lambda t, speed, time, rest: t // (time + rest) * time * speed + min(t % (time + rest), time) * speed

p1 = maxval(parsed_input, key=lambda i: dist(2503, *i[1:]))

points = {}
for t in range(1, 2504):
    maxd, maxr = 0, []
    for i in parsed_input:
        name, speed, time, rest = i
        d = dist(t, speed, time, rest)
        maxd, maxr = max(maxd, d), [name] if d > maxd else maxr + [name] if d == maxd else maxr
    for r in maxr:
        points[r] = points.get(r, 0) + 1
p2 = max(points.values())

output(p1, p2)