from utils import *
inp = open("2022/input-3.txt", "r").read()

parsed_input = parser(inp, ["\n"])

print(sum(map(lambda inp: sum(map(lambda i: alph.index(i) + 1, set(inp[:len(inp) // 2]).intersection(set(inp[len(inp) // 2:])))), parsed_input)))

print(sum(map(lambda ind: sum(map(lambda i: alph.index(i) + 1, set(parsed_input[3 * ind]).intersection(parsed_input[3 * ind + 1]).intersection(parsed_input[3 * ind + 2]))), range(len(parsed_input) // 3))))