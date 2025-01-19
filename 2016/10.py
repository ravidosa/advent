from utils import *
inp = input_file(2016, 10).strip()

parsed_input = parser(inp, ["\n", r" goes to | gives low to | and high to | "])

bots = {}
outputs = {}
gives = {}
giving = []
for i in parsed_input:
    if i[0] == "value":
        bots[i[3]] = bots.get(i[3], []) + [i[1]]
        if len(bots[i[3]]) == 2:
            giving.append(i[3])
    else:
        gives[i[1]] = (i[2:4], i[4:6])
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

print(cmp_17_61)

print(outputs[0][0] * outputs[1][0] * outputs[2][0])