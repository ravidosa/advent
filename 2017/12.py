from utils import *
inp = input_file(2017, 12).strip()

parsed_input = parser(inp, "{{i}} <-> {{li, }}")

G = nx.Graph()
G.add_edges_from((comp, c) for comp, conn in parsed_input for c in conn)

p1 = len(nx.node_connected_component(G, 0))

p2 = nx.number_connected_components(G)

output(p1, p2)