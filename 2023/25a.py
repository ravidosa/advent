import networkx as nx
import functools
f = open("2023/input-25.txt", "r")
inp = f.read().split("\n")

g = nx.Graph()
qq = {}
ind = 0
for i in inp[:-1]:
    i = i.split(": ")
    for nn in i[1].split(" "):
        g.add_edge(i[0], nn)
rem = nx.minimum_edge_cut(g)
for a, b in rem:
	g.remove_edge(a, b)
answer = functools.reduce(lambda x, y: x * y, map(len, nx.connected_components(g)))
print(answer)