from utils import *
inp = open("2024/input-8.txt", "r").read().strip()

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
print(sum(map(lambda n: int(n in grid), nodes)))

nodes = set()
for freq in freqs:
    enna = grid.find(freq)
    for pair in itertools.combinations(enna, 2):
      en1, en2 = pair
      dr, dc = en1[0] - en2[0], en1[1] - en2[1]
      steps = min(grid.cols // abs(dr), grid.rows // abs(dc))
      nodes.update(map(lambda i: (en1[0] + i * dr, en1[1] + i * dc), range(-steps, steps)))
print(sum(map(lambda n: int(n in grid), nodes)))