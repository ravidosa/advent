from utils import *
inp = open("2024/input-23.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", "-"])

G = nx.Graph()
G.add_edges_from(parsed_input)

s = 0
for clique in nx.enumerate_all_cliques(G):
    if len(clique) == 3:
        a, b, c = clique
        if a[0] == "t" or b[0] == "t" or c[0] == "t":
            s += 1
    elif len(clique) > 3:
        break
print(s)

print(",".join(sorted(max(nx.find_cliques(G), key=len))))