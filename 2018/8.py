from utils import *
inp = input_file(2018, 8).strip().split("\n")[0]

parsed_input = parser(inp, "{{li }}")

def meta_sum(data):
    children, meta, *data = data
    total = 0
    for _ in range(children):
        tot, data = meta_sum(data)
        total += tot
    total += sum(data[:meta])
    return total, data[meta:]
p1, _ = meta_sum(parsed_input)

def score(data):
    children, meta, *data = data
    scores = []
    for _ in range(children):
        sc, data = score(data)
        scores.append(sc)
    return sum(data[:meta]) if children == 0 else sum(scores[m - 1] if 0 < m <= len(scores) else 0 for m in data[:meta]), data[meta:]
p2, _ = score(parsed_input)

output(p1, p2)