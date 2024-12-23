import itertools
import networkx as nx
f = open("2024/input-23.txt", "r")
inp = f.read().split("\n")

G = nx.Graph()
for i in inp:
    u, v = i.split("-")
    G.add_edge(u, v)
cliques = nx.find_cliques(G)
max_cl = max(nx.find_cliques(G), key=len)
print(",".join(sorted(max_cl)))