from utils import *
inp = input_file(2025, 8).strip()

parsed_input = parser(inp, "{{li,}}")

dist = []
for i in range(len(parsed_input)):
    for j in range(i + 1, len(parsed_input)):
        xi, yi, zi = parsed_input[i]
        xj, yj, zj = parsed_input[j]
        dist.append(((xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2, i, j))
dist.sort()
G = nx.Graph()
G.add_nodes_from([i for i in range(len(parsed_input))])

for e in dist[:1000]:
    _, i, j = e
    G.add_edge(i, j)
comps = list(map(len, nx.connected_components(G)))
comps.sort()
p1 = comps[-1] * comps[-2] * comps[-3]

for e in dist[1000:]:
    _, i, j = e
    G.add_edge(i, j)
    if max(map(len, nx.connected_components(G))) == len(parsed_input):
        break
p2 = parsed_input[i][0] * parsed_input[j][0]

output(p1, p2)