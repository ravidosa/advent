from utils import *
inp = input_file(2018, 7).strip()

parsed_input = parser(inp, ["\n", "Step | must be finished before step | can begin."])

G = nx.DiGraph()
G.add_edges_from(parsed_input)

p1 = "".join(nx.lexicographical_topological_sort(G))

tracker = {}
time = 0
while tracker or G:
    available = [t for t in G if t not in tracker and G.in_degree(t) == 0]
    if available and len(tracker.keys()) < 5:
        task = min(available)
        tracker[task] = ord(task) - 4
    else:
        mint = min(tracker.values())
        completed = [t for t in tracker.keys() if tracker[t] == mint]
        tracker = {t: tracker[t] - mint for t in filter(lambda tt: tracker[tt] > mint, tracker)}
        time += mint
        G.remove_nodes_from(completed)
p2 = time

output(p1, p2)