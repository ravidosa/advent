import itertools
f = open("2024/input-8.txt", "r")
inp = f.read().split("\n")

typ = set("".join(inp)).difference(set("."))
print(typ)

nods = set()

for t in typ:
   print(t)
   enna = [(ind % len(inp[0]), ind // len(inp[0])) for ind, n in enumerate("".join(inp)) if n == t]
   print(enna)

   for pair in itertools.combinations(enna, 2):
      en1, en2 = pair
      dx, dy = en1[0] - en2[0], en1[1] - en2[1]
      nods.add((en1[0] + dx, en1[1] + dy))
      nods.add((en2[0] - dx, en2[1] - dy))

print(len([n for n in nods if 0 <= n[0] <= len(inp[0]) - 1 and 0 <= n[1] <= len(inp) - 1]))