from utils import *
inp = input_file(2015, 24).strip()

parsed_input = parser(inp, ["\n"])

def min_ideal(groups):
    for i in range(len(parsed_input)):
        if qes := [prod(c) for c in itertools.combinations(parsed_input, i) if sum(c) == sum(parsed_input) // groups]:
            return min(qes)
        
p1 = min_ideal(3)

p2 = min_ideal(4)

output(p1, p2)