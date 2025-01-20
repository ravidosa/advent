from utils import *
inp = input_file(2021, 22).strip()

parsed_input = parser(inp, ["\n", r" x=|,y=|,z=|\.\."])

def cubes_on(fil=lambda ix, fx, iy, fy, iz, fz: True):
    cubes = collections.Counter()
    for i in parsed_input:
        instr, ix, fx, iy, fy, iz, fz = i
        sign = 1 if instr == "on" else 0
        if fil(ix, fx, iy, fy, iz, fz):
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
    return sum(map(lambda c: (c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1) * cubes[c], cubes))

p1 = cubes_on(lambda ix, fx, iy, fy, iz, fz: all(map(lambda i: -50 <= i <= 50, [ix, fx, iy, fy, iz, fz])))

p2 = cubes_on()

output(p1, p2)