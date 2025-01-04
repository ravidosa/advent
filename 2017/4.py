from utils import *
inp = open("2017/input-4.txt", "r").read()

parsed_input = parser(inp, ["\n", " "])
print(sum(map(lambda i: len(i) == len(set(i)), parsed_input)))

parsed_input = parser(inp, ["\n", " "], fingerprint)
print(sum(map(lambda i: len(i) == len(set(i)), parsed_input)))