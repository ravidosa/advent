from utils import *
inp = input_file(2024, 8).strip()

grid = Grid(inp, par=str)
freqs = set(inp) - {".", "\n"}

nodes = set()
for freq in freqs:
    enna = grid.find(freq)
    for pair in itertools.combinations(enna, 2):
      en1, en2 = pair
      dr, dc = en1[0] - en2[0], en1[1] - en2[1]
      nodes.add((en1[0] + dr, en1[1] + dc))
      nodes.add((en2[0] - dr, en2[1] - dc))
p1 = sum(n in grid for n in nodes)

nodes = set()
for freq in freqs:
    enna = grid.find(freq)
    for pair in itertools.combinations(enna, 2):
      en1, en2 = pair
      dr, dc = en1[0] - en2[0], en1[1] - en2[1]
      steps = min(grid.cols // abs(dr), grid.rows // abs(dc))
      nodes.update((en1[0] + i * dr, en1[1] + i * dc) for i in range(-steps, steps))
p2 = sum(n in grid for n in nodes)

output(p1, p2)