import itertools
import networkx as nx
f = open("2024/input-23.txt", "r")
inp = f.read().split("\n")

G = nx.Graph()
for i in inp:
    u, v = i.split("-")
    G.add_edge(u, v)
s = 0
cl = set()
for triple in itertools.combinations(G.nodes, 3):
    a, b, c = triple
    if (a, b) in G.edges and (b, c) in G.edges and (a, c) in G.edges:
        if a[0] == "t" or b[0] == "t" or c[0] == "t":
            s += 1
            cl.add(triple)
print(s)