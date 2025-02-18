from utils import *
inp = input_file(2020, 7).strip()

parsed_input = parser(inp, "{{p}} bags contain {{lp bags?, | bags?\.|no other bags\.}}")

bag_dict = {i[0]: [] if len(i[1]) == 0 else [(int(ii[:ii.index(" ")]), ii[ii.index(" ") + 1:]) for ii in i[1]] for i in parsed_input}

col_contain = lambda col: set() if len(bag_dict[col]) == 0 else (cols := set(qty for _, qty in bag_dict[col])).union(functools.reduce(lambda a, b: a.union(b), map(col_contain, cols), set()))
p1 = sum("shiny gold" in col_contain(col) for col in bag_dict.keys())

bag_count = lambda col: 1 if len(bag_dict[col]) == 0 else 1 + sum(qty * bag_count(cont) for qty, cont in bag_dict[col])
p2 = bag_count("shiny gold") - 1

output(p1, p2)