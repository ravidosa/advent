from utils import *
inp = open("2024/input-15.txt", "r").read().strip().split("\n\n")

moves = "".join(parser(inp[1], "\n"))

grid = Grid(inp[0])
currp = grid.find("@").pop(0)
boxes = grid.find("O")
for move in moves:
    r, c = currp
    dr, dc = dir_sym[move]["tup"]
    if 0 <= r + dr < grid.rows and 0 <= c + dc < grid.cols:
        if grid.grid[r + dr][c + dc] != "#":
            nextp = (r + dr, c + dc)
            if nextp not in boxes:
                currp = nextp
            else:
                move_box = set()
                next_box = set()
                next_box.add(nextp)
                while len(next_box) > 0:
                    move_box = move_box.union(next_box)
                    check_box = set()
                    for box in next_box:
                        br, bc = box
                        check = (br + dr, bc + dc)
                        if check in boxes:
                            check_box.add(check)
                        elif grid.grid[br + dr][bc + dc] == "#":
                            check_box = set()
                            move_box = set()
                            break
                    next_box = check_box
                if len(move_box) > 0:
                    temp_boxes = boxes.copy()
                    for box in move_box:
                        br, bc = box
                        temp_boxes[boxes.index(box)] = (br + dr, bc + dc)
                    currp = nextp
                    boxes = temp_boxes.copy()
print(sum(map(lambda box: 100 * box[0] + box[1], boxes)))

grid = Grid(inp[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
currp = grid.find("@").pop(0)
boxes = grid.find("[")
for move in moves:
    r, c = currp
    dr, dc = dir_sym[move]["tup"]
    if 0 <= r + dr < grid.rows and 0 <= c + dc < grid.cols:
        if grid.grid[r + dr][c + dc] != "#":
            nextp = (r + dr, c + dc)
            if nextp not in boxes and (r + dr, c + dc - 1) not in boxes:
                currp = nextp
            else:
                move_box = set()
                next_box = set()
                if nextp in boxes:
                    next_box.add(nextp)
                else:
                    next_box.add((r + dr, c + dc - 1))
                while len(next_box) > 0:
                    move_box = move_box.union(next_box)
                    check_box = set()
                    for box in next_box:
                        br, bc = box
                        check = (br + dr, bc + dc)
                        if dr == 0:
                            if (br, bc + 2 * dc) in boxes:
                                check_box.add((br, bc + 2 * dc))
                            if (dc == 1 and grid.grid[br][bc + 2] == "#") or (dc == -1 and grid.grid[br][bc - 1] == "#"):
                                check_box = set()
                                move_box = set()
                                break
                        if dc == 0:
                            if (br + dr, bc) in boxes:
                                check_box.add((br + dr, bc))
                            if (br + dr, bc - 1) in boxes:
                                check_box.add((br + dr, bc - 1))
                            if (br + dr, bc + 1) in boxes:
                                check_box.add((br + dr, bc + 1))
                            if grid.grid[br + dr][bc] == "#" or grid.grid[br + dr][bc + 1] == "#":
                                check_box = set()
                                move_box = set()
                                break
                    next_box = check_box
                if len(move_box) > 0:
                    temp_boxes = boxes.copy()
                    for box in move_box:
                        br, bc = box
                        temp_boxes[boxes.index(box)] = (br + dr, bc + dc)
                    currp = nextp
                    boxes = temp_boxes.copy()
print(sum(map(lambda box: 100 * box[0] + box[1], boxes)))