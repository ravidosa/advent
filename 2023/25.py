from utils import *
inp = input_file(2023, 25).strip()

parsed_input = parser(inp, ["\n", ": ", " "])

G = nx.Graph()
G.add_edges_from((comp[0], c) for comp, conn in parsed_input for c in conn)
G.remove_edges_from(nx.minimum_edge_cut(G))
p1 = prod(map(len, nx.connected_components(G)))

output(p1)