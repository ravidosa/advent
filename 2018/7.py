from utils import *
inp = input_file(2018, 7).strip()

parsed_input = parser(inp, ["\n", "Step | must be finished before step | can begin."])

G = nx.DiGraph()
G.add_edges_from(parsed_input)

p1 = "".join(nx.lexicographical_topological_sort(G))

tracker = {}
time = 0
while tracker or G:
    available = list(filter(lambda t: t not in tracker and G.in_degree(t) == 0, G))
    if available and len(tracker.keys()) < 5:
        task = min(available)
        tracker[task] = ord(task) - 4
    else:
        mint = min(tracker.values())
        completed = list(filter(lambda t: tracker[t] == mint, tracker.keys()))
        tracker = {t: tracker[t] - mint for t in filter(lambda tt: tracker[tt] > mint, tracker)}
        time += mint
        G.remove_nodes_from(completed)
p2 = time

output(p1, p2)