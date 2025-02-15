from utils import *
inp = input_file(2015, 5).strip()

parsed_input = parser(inp)

nice = lambda inp: len(re.findall(r'[aeiou]', inp)) >= 3 and len(re.findall(r'(.)\1', inp)) >= 1 and not re.findall(r'ab|cd|pq|xy', inp)
p1 = sum(map(nice, parsed_input))

nice = lambda inp: len(re.findall(r'(..).*\1', inp)) >= 1 and len(re.findall(r'(.).\1', inp)) >= 1
p2 = sum(map(nice, parsed_input))

output(p1, p2)