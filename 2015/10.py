from utils import *
inp = input_file(2015, 10).strip()

def look_and_say(seq):
    return "".join(str(len(list(g))) + d for d, g in itertools.groupby(seq))

seq = inp
for _ in range(40):
    seq = look_and_say(seq)
p1 = len(seq)

for _ in range(50 - 40):
    seq = look_and_say(seq)
p2 = len(seq)

output(p1, p2)