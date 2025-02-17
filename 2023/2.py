from utils import *
inp = input_file(2023, 2).strip()

parsed_input = parser(inp, "Game {{i}}: {{nle; |, | }}")

def cols(game):
    col_dict = {"r": 0, "g": 0, "b": 0}
    for set in game:
        for cube in set:
            col_dict[cube[1][0]] = max(col_dict[cube[1][0]], cube[0])
    return col_dict
def possible(game, r, g, b):
    col_dict = cols(game)
    return col_dict["r"] <= r and col_dict["g"] <= g and col_dict["b"] <= b

p1 = sum(g[0] * possible(g[1], 12, 13, 14) for g in parsed_input)

p2 = sum(prod(cols(g[1]).values()) for g in parsed_input)

output(p1, p2)