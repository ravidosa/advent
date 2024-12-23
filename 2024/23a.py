import networkx as nx
f = open("2024/input-23.txt", "r")
inp = f.read().split("\n")

G = nx.Graph()
for i in inp:
    u, v = i.split("-")
    G.add_edge(u, v)
s = 0
for clique in nx.enumerate_all_cliques(G):
    if len(clique) == 3:
        a, b, c = clique
        if a[0] == "t" or b[0] == "t" or c[0] == "t":
            s += 1
    elif len(clique) > 3:
        break
print(s)