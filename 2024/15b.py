f = open("input.txt", "r")
inp = f.read().split("\n\n")

grid, mov = inp

grid = grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
grid = [list(g) for g in grid.split("\n")]
mov = "".join(mov.split("\n"))

x, y = "".join(["".join(g) for g in grid]).index("@") % len(grid[0]), "".join(["".join(g) for g in grid]).index("@") // len(grid[0])

dir = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}

boxes = [(x, y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == "["]
for m in mov:
    dx, dy = dir[m]
    if 0 <= x + dx <= len(grid[0]) - 1 and 0 <= y + dy <= len(grid) - 1 and grid[y + dy][x + dx] != "#":
        if (x + dx, y + dy) not in boxes and (x + dx - 1, y + dy) not in boxes:
            x, y = x + dx, y + dy
        else:
            mbox = set()
            nbox = set()
            if (x + dx, y + dy) in boxes:
                b = (x + dx, y + dy)
            else:
                b = (x + dx - 1, y + dy)
            nbox.add(b)
            while len(nbox) > 0:
                mbox = mbox.union(nbox)
                nnbox = set()
                for box in nbox:
                    bx, by = box
                    if dx == 0:
                        if (bx, by + dy) in boxes:
                            nnbox.add((bx, by + dy))
                        if (bx - 1, by + dy) in boxes:
                            nnbox.add((bx - 1, by + dy))
                        if (bx + 1, by + dy) in boxes:
                            nnbox.add((bx+ 1, by + dy))
                        if grid[by + dy][bx] == "#" or grid[by + dy][bx + 1] == "#":
                            nnbox = set()
                            mbox = set()
                            break
                    if dy == 0:
                        if (bx + 2 * dx, by) in boxes:
                            nnbox.add((bx + 2 * dx, by))
                        if (dx == 1 and grid[by][bx + 2] == "#") or (dx == -1 and grid[by][bx - 1] == "#"):
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