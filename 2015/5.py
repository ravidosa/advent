from utils import *
inp = open("2015/input-5.txt", "r").read()

parsed_input = parser(inp, ["\n"])

nice = lambda inp: len(re.findall(r'[aeiou]', inp)) >= 3 and len(re.findall(r'(.)\1', inp)) >= 1 and not re.findall(r'ab|cd|pq|xy', inp)
print(sum(map(nice, parsed_input)))

nice = lambda inp: len(re.findall(r'(..).*\1', inp)) >= 1 and len(re.findall(r'(.).\1', inp)) >= 1
print(sum(map(nice, parsed_input)))