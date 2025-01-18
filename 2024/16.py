from utils import *
inp = open("2024/input-16.txt", "r").read().strip()

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
                cost = 1 + 1000 * (dr != prevdr or dc != prevdc)
                if 0 <= r + dr < grid.rows and 0 <= c + dc < grid.cols:
                    nextp = (r + dr, c + dc)
                    if grid.grid[r + dr][c + dc] != "#":
                        if currdist + cost < dist.get((nextp, nextd), math.inf):
                            dist[(nextp, nextd)] = currdist + cost
                            prev[(nextp, nextd)] = [(currp, currd)]
                            hq.heappush(queue, (currdist + cost, nextp, nextd))
                        elif currdist + cost == dist.get((nextp, nextd), math.inf):
                            prev[(nextp, nextd)] += [(currp, currd)]
print(minval(range(4), key=lambda i: dist.get((end, i), math.inf)))

spots = set()
spots.add((end, min(range(4), key=lambda i: dist.get((end, i), math.inf))))
while True:
    pspots = set(pspot for spot in spots for pspot in prev[spot])
    if pspots.issubset(spots):
        break
    spots.update(pspots)
print(len(set([spot[0] for spot in spots])))