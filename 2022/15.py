from utils import *
inp = input_file(2022, 15).strip()

parsed_input = parser(inp, ["\n", ": ", "Sensor at x=|, y=|closest beacon is at x="])

y = 2000000
no_beacon = set()
for i in parsed_input:
    sensor, beacon = i
    d = manhattan(sensor, beacon)
    no_beacon.update(range(sensor[0] - (d - abs(sensor[1] - y)), sensor[0] + (d - abs(sensor[1] - y)) + 1))
    if beacon[1] == y:
        no_beacon.remove(beacon[0])
    if sensor[1] == y:
        no_beacon.add(sensor)
p1 = len(no_beacon)

m = 4000000
pdiag = []
ndiag = []
for i in parsed_input:
    sensor, beacon = i
    d = manhattan(sensor, beacon) + 1
    pdiag.extend([sensor[1] - (sensor[0] + d), sensor[1] - (sensor[0] - d)])
    ndiag.extend([sensor[1] + (sensor[0] + d), sensor[1] + (sensor[0] - d)])
for p, n in itertools.product(pdiag, ndiag):
    if (p - n) % 2 == 0:
        distress = ((n - p) // 2, (n + p) // 2)
        if all(map(lambda i: manhattan(i[0], i[1]) < manhattan(i[0], distress), parsed_input)):
            if 0 <= distress[0] <= m and 0 <= distress[1] <= m:
                break
p2 = 4000000 * distress[0] + distress[1]

output(p1, p2)