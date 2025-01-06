from utils import *
inp = open("2020/input-7.txt", "r").read()

parsed_input = parser(inp, ["\n", r" bags contain | bags?, | bags?\.|no other"], lambda i: [int(i[:i.index(" ")]), i[i.index(" ") + 1:]] if i[0].isdigit() else i)
bag_dict = {i[0]: [] if len(i) == 1 else i[1:] for i in parsed_input}

col_contain = lambda col: set() if len(bag_dict[col]) == 0 else (cols := set(map(lambda pair: pair[1], bag_dict[col]))).union(functools.reduce(lambda a, b: a.union(b), map(col_contain, cols), set()))
print(sum(map(lambda col: "shiny gold" in col_contain(col), bag_dict.keys())))

bag_count = lambda col: 1 if len(bag_dict[col]) == 0 else 1 + sum(map(lambda pair: pair[0] * bag_count(pair[1]), bag_dict[col]))
print(bag_count("shiny gold") - 1)