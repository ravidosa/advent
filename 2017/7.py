from utils import *
inp = input_file(2017, 7).strip()

parsed_input = parser(inp, "{{le \(|\)| -> |, }}")

G = nx.DiGraph()
G.add_edges_from((prog, p) for prog, _, *above in parsed_input for p in above)
root = [n for n, d in G.in_degree() if d==0][0]
p1 = root

weight = {i[0]: i[1] for i in parsed_input}
stacks = {i[0]: i[1] for i in parsed_input if len(i) == 2}
def balance(disc):
    w = weight[disc] + sum(balance(n) for n in G.neighbors(disc))
    stacks[disc] = w
    return w
balance(root)
wrong_node = root
next = sorted([(n, balance(n)) for n in G.neighbors(wrong_node)], key=lambda i: i[1])
while next[0][1] != next[-1][1]:
    if len(next) == 2:
        opt = sorted([(n, balance(n)) for n in G.neighbors(next[0][0])], key=lambda i: i[1])
        wrong_node = next[0][0] if opt[0][1] != opt[-1][1] else next[1][0]
        target = next[1][1] if opt[0][1] != opt[-1][1] else next[0][1]
    else:
        wrong_node = next[0][0] if next[0][1] != next[1][1] else next[-1][0]
        target = next[1][1]
    next = sorted([(n, balance(n)) for n in G.neighbors(wrong_node)], key=lambda i: i[1])
p2 = weight[wrong_node] + (target - stacks[wrong_node])

output(p1, p2)