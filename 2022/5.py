from utils import *
inp = open("2022/input-5.txt", "r").read().split("\n\n")

parsed_input = parser(inp[0], ["\n"], str, False)
stack_count = len(parsed_input[-1].split())
initial_stacks = [[] for _ in range(stack_count)]
for r in parsed_input[:-1]:
    for ind, spot in enumerate(map(lambda i: r[4 * i: 4 * (i + 1)], range(stack_count))):
        if spot[1] != " ":
            initial_stacks[ind].append(spot[1])
parsed_input = parser(inp[1], ["\n", "move | from | to "])

stacks = [stack.copy() for stack in initial_stacks]
for instr in parsed_input:
    bct, s1, s2 = instr
    for _ in range(bct):
        stacks[s2 - 1].insert(0, stacks[s1 - 1].pop(0))
print("".join(map(lambda s: s[0], stacks)))

stacks = [stack.copy() for stack in initial_stacks]
for instr in parsed_input:
    bct, s1, s2 = instr
    stacks[s2 - 1] = stacks[s1 - 1][:bct] + stacks[s2 - 1]
    stacks[s1 - 1] = stacks[s1 - 1][bct:]
print("".join(map(lambda s: s[0], stacks)))