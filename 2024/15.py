from utils import *
inp = input_file(2024, 15).strip().split("\n\n")

parsed_input = "".join(parser(inp[1], "\n"))

def find_boxes(currp, move, double=False):
    global boxes
    nextp = tupadd(currp, dir_sym[move]["tup"])
    move_box = set()
    next_box = set()
    if nextp in boxes:
        next_box.add(nextp)
    elif double and tupadd(nextp, (0, -1)) in boxes:
        next_box.add(tupadd(nextp, (0, -1)))
    else:
        return set()
    while len(next_box) > 0:
        move_box = move_box.union(next_box)
        check_box = set()
        for box in next_box:
            br, bc = box
            dr, dc = dir_sym[move]["tup"]
            if dr == 0:
                if (br, bc + (2 if double else 1) * dc) in boxes:
                    check_box.add((br, bc + (2 if double else 1) * dc))
                if grid.get_pos((br, bc + ((2 if double else 1) if dc == 1 else -1))) == "#":
                    return set()
            if dc == 0:
                if (br + dr, bc) in boxes:
                    check_box.add((br + dr, bc))
                if double:
                    if (br + dr, bc - 1) in boxes:
                        check_box.add((br + dr, bc - 1))
                    if (br + dr, bc + 1) in boxes:
                        check_box.add((br + dr, bc + 1))
                if grid.get_pos((br + dr, bc))  == "#" or grid.get_pos((br + dr, bc + 1)) == "#":
                    return set()
        next_box = check_box
    return move_box
def update_boxes(move_boxes, move):
    temp_boxes = boxes.copy()
    for box in move_boxes:
        temp_boxes[boxes.index(box)] = tupadd(box, dir_sym[move]["tup"])
    return temp_boxes
def mover(currp, move, boxes, double=False):
    nextp = tupadd(currp, dir_sym[move]["tup"])
    if nextp in grid:
        if grid.get_pos(nextp) != "#":
            if nextp not in boxes and (tupadd(nextp, (0, -1)) not in boxes if double else True):
                return nextp, boxes
            else:
                move_boxes = find_boxes(currp, move, double)
                if len(move_boxes) > 0:
                    return nextp, update_boxes(move_boxes, move)
    return currp, boxes
gps = lambda boxes: sum(map(lambda box: 100 * box[0] + box[1], boxes))

grid = Grid(inp[0])
currp = grid.find("@")[0]
boxes = grid.find("O")
for move in parsed_input:
    currp, boxes = mover(currp, move, boxes)
p1 = gps(boxes)

grid = Grid(inp[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
currp = grid.find("@")[0]
boxes = grid.find("[")
for move in parsed_input:
    currp, boxes = mover(currp, move, boxes, True)
p2 = gps(boxes)

output(p1, p2)