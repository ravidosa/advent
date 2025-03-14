from utils import *
inp = input_file(2024, 16).strip()

grid = Grid(inp)
start = grid.find("S")[0]
end = grid.find("E")[0]

queue = [(0, start, 0)]
dist = {(start, 0): 0}
prev = {(start, 0): []}
while len(queue) > 0:
    currdist, currp, currd = hq.heappop(queue)
    r, c = currp
    prevdr, prevdc = dir_tup[currd]
    if currp == end:
        break
    if currdist <= dist.get((currp, currd), math.inf):
        for nextd in range(4):
            dr, dc = dir_tup[nextd]
            if dr != -prevdr or dc != -prevdc:
                nextp = tupadd(currp, dir_tup[nextd])
                cost = 1 + 1000 * (dr != prevdr or dc != prevdc)
                if nextp in grid:
                    if grid.get_pos(nextp) != "#":
                        if currdist + cost < dist.get((nextp, nextd), math.inf):
                            dist[(nextp, nextd)] = currdist + cost
                            prev[(nextp, nextd)] = [(currp, currd)]
                            hq.heappush(queue, (currdist + cost, nextp, nextd))
                        elif currdist + cost == dist.get((nextp, nextd), math.inf):
                            prev[(nextp, nextd)] += [(currp, currd)]
p1 = minval(range(4), key=lambda i: dist.get((end, i), math.inf))

spots = set()
spots.add((end, min(range(4), key=lambda i: dist.get((end, i), math.inf))))
while True:
    pspots = set(pspot for spot in spots for pspot in prev[spot])
    if pspots.issubset(spots):
        break
    spots.update(pspots)
p2 = len(set([spot[0] for spot in spots]))

output(p1, p2)