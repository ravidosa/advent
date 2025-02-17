from utils import *
inp = input_file(2018, 9).strip()

parsed_input = parser(inp, "{{i}} players; last marble is worth {{i}} points", split=False)

players, marbles = parsed_input

score = [0] * players
circle = collections.deque([0])
for m in range(1, marbles + 1):
    if m % 23 != 0:
        circle.rotate(-1)
        circle.append(m)
    else:
        circle.rotate(7)
        score[m % players] += m + circle.pop()
        circle.rotate(-1)
p1 = max(score)

for m in range(marbles + 1, 100 * marbles + 1):
    if m % 23 != 0:
        circle.rotate(-1)
        circle.append(m)
    else:
        circle.rotate(7)
        score[m % players] += m + circle.pop()
        circle.rotate(-1)
p2 = max(score)

output(p1, p2)