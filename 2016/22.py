from utils import *
inp = input_file(2016, 22).strip()

parsed_input = parser(inp, "{{le/dev/grid/node-x|-y|T|%| }}")[2:]

tot = 0
for nodeA in parsed_input:
    for nodeB in parsed_input:
        if nodeA != nodeB:
            if nodeA[3] != 0:
                if nodeA[3] <= nodeB[4]:
                    tot += 1
p1 = tot

output(p1, p2)