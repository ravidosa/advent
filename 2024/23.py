from utils import *
inp = input_file(2024, 23).strip()

parsed_input = parser(inp, "{{s}}-{{s}}")

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
p1 = s

p2 = ",".join(sorted(max(nx.find_cliques(G), key=len)))

output(p1, p2)