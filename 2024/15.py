from utils import *
inp = input_file(2024, 15).strip().split("\n\n")

parsed_input = "".join(parser(inp[1], "\n"))

grid = Grid(inp[0])
currp = grid.find("@")[0]
boxes = grid.find("O")
for move in parsed_input:
    nextp = tupadd(currp, dir_sym[move]["tup"])
    if nextp in grid:
        if grid.get_pos(nextp) != "#":
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
                        check = tupadd(box, dir_sym[move]["tup"])
                        if check in boxes:
                            check_box.add(check)
                        elif grid.get_pos(check) == "#":
                            check_box = set()
                            move_box = set()
                            break
                    next_box = check_box
                if len(move_box) > 0:
                    temp_boxes = boxes.copy()
                    for box in move_box:
                        temp_boxes[boxes.index(box)] = tupadd(box, dir_sym[move]["tup"])
                    currp = nextp
                    boxes = temp_boxes.copy()
print(sum(map(lambda box: 100 * box[0] + box[1], boxes)))

grid = Grid(inp[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
currp = grid.find("@")[0]
boxes = grid.find("[")
for move in parsed_input:
    nextp = tupadd(currp, dir_sym[move]["tup"])
    if nextp in grid:
        if grid.get_pos(nextp) != "#":
            if nextp not in boxes and tupadd(nextp, (0, -1)) not in boxes:
                currp = nextp
            else:
                move_box = set()
                next_box = set()
                if nextp in boxes:
                    next_box.add(nextp)
                else:
                    next_box.add(tupadd(nextp, (0, -1)))
                while len(next_box) > 0:
                    move_box = move_box.union(next_box)
                    check_box = set()
                    for box in next_box:
                        check = tupadd(box, dir_sym[move]["tup"])
                        br, bc = box
                        dr, dc = dir_sym[move]["tup"]
                        if dr == 0:
                            if (br, bc + 2 * dc) in boxes:
                                check_box.add((br, bc + 2 * dc))
                            if (dc == 1 and grid.get_pos((br, bc + 2)) == "#") or (dc == -1 and grid.get_pos((br, bc - 1)) == "#"):
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
                            if grid.get_pos((br + dr, bc))  == "#" or grid.get_pos((br + dr, bc + 1)) == "#":
                                check_box = set()
                                move_box = set()
                                break
                    next_box = check_box
                if len(move_box) > 0:
                    temp_boxes = boxes.copy()
                    for box in move_box:
                        temp_boxes[boxes.index(box)] = tupadd(box, dir_sym[move]["tup"])
                    currp = nextp
                    boxes = temp_boxes.copy()
print(sum(map(lambda box: 100 * box[0] + box[1], boxes)))