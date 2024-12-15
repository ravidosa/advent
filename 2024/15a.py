f = open("input.txt", "r")
inp = f.read().split("\n\n")

grid, mov = inp

grid = [list(g) for g in grid.split("\n")]
mov = "".join(mov.split("\n"))

x, y = "".join(["".join(g) for g in grid]).index("@") % len(grid[0]), "".join(["".join(g) for g in grid]).index("@") // len(grid[0])

dir = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}

boxes = [(x, y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == "O"]

for m in mov:
    dx, dy = dir[m]
    if 0 <= x + dx <= len(grid[0]) - 1 and 0 <= y + dy <= len(grid) - 1 and grid[y + dy][x + dx] != "#":
        if (x + dx, y + dy) not in boxes:
            x, y = x + dx, y + dy
        else:
            mbox = set()
            nbox = set()
            b = (x + dx, y + dy)
            nbox.add(b)
            while len(nbox) > 0:
                mbox = mbox.union(nbox)
                nnbox = set()
                for box in nbox:
                    bx, by = box
                    if (bx + dx, by + dy) in boxes:
                        nnbox.add((bx + dx, by + dy))
                    if grid[by + dy][bx + dx] == "#":
                        nnbox = set()
                        mbox = set()
                        break
                nbox = nnbox
            if len(mbox) > 0:
                for box in mbox:
                    bx, by = box
                    boxes[boxes.index(box)] = (bx + dx, by + dy)
                x, y = x + dx, y + dy
print(sum([100 * y + x for (x, y) in boxes]))