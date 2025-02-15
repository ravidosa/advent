from utils import *
inp = input_file(2016, 10).strip()

parsed_input = parser(inp, "{{le goes to | gives low to | and high to | }}")

bots = {}
outputs = {}
gives = {}
giving = []
for i in parsed_input:
    com = i[0]
    if com[0] == "value":
        bots[com[3]] = bots.get(com[3], []) + [com[1]]
        if len(bots[com[3]]) == 2:
            giving.append(com[3])
    else:
        gives[com[1]] = (com[2:4], com[4:6])
cmp_17_61 = None
while len(giving) > 0:
    bot = giving.pop(0)
    low, high = min(bots[bot]), max(bots[bot])
    if low == 17 and high == 61:
       cmp_17_61 = bot
    bots[bot].remove(low)
    bots[bot].remove(high)
    tyl, tyh = bots if gives[bot][0][0] == "bot" else outputs, bots if gives[bot][1][0] == "bot" else outputs
    tyl[gives[bot][0][1]] = tyl.get(gives[bot][0][1], []) + [low]
    if tyl == bots and len(bots[gives[bot][0][1]]) == 2:
        giving.append(gives[bot][0][1])
    tyh[gives[bot][1][1]] = tyh.get(gives[bot][1][1], []) + [high]
    if tyh == bots and len(bots[gives[bot][1][1]]) == 2:
        giving.append(gives[bot][1][1])

p1 = cmp_17_61

p2 = outputs[0][0] * outputs[1][0] * outputs[2][0]

output(p1, p2)