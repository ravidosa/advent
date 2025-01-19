from utils import *
inp = open("2021/input-22.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", r" x=|,y=|,z=|\.\."])

cubes = collections.Counter()
for i in parsed_input:
    instr, ix, fx, iy, fy, iz, fz = i
    sign = 1 if instr == "on" else 0
    if all(map(lambda i: -50 <= i <= 50, [ix, fx, iy, fy, iz, fz])):
        update = collections.Counter()
        for cube in cubes:
            cix, cfx, ciy, cfy, ciz, cfz = cube
            csign = cubes[cube]
            minx, maxx = max(ix, cix), min(fx, cfx)
            miny, maxy = max(iy, ciy), min(fy, cfy)
            minz, maxz = max(iz, ciz), min(fz, cfz)
            if minx <= maxx and miny <= maxy and minz <= maxz:
                update[(minx, maxx, miny, maxy, minz, maxz)] -= csign
        if sign > 0:
            update[(ix, fx, iy, fy, iz, fz)] += sign
        cubes.update(update)
print(sum(map(lambda c: (c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1) * cubes[c], cubes)))

cubes = collections.Counter()
for i in parsed_input:
    instr, ix, fx, iy, fy, iz, fz = i
    sign = 1 if instr == "on" else 0
    update = collections.Counter()
    for cube in cubes:
        cix, cfx, ciy, cfy, ciz, cfz = cube
        csign = cubes[cube]
        minx, maxx = max(ix, cix), min(fx, cfx)
        miny, maxy = max(iy, ciy), min(fy, cfy)
        minz, maxz = max(iz, ciz), min(fz, cfz)
        if minx <= maxx and miny <= maxy and minz <= maxz:
            update[(minx, maxx, miny, maxy, minz, maxz)] -= csign
    if sign > 0:
        update[(ix, fx, iy, fy, iz, fz)] += sign
    cubes.update(update)
print(sum(map(lambda c: (c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1) * cubes[c], cubes)))