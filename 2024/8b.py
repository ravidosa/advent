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
        for i in range(1, min(len(inp[0]) // abs(dx), len(inp) // abs(dy))):
            nods.add((en1[0] + i * dx, en1[1] + i * dy))
            nods.add((en2[0] - i * dx, en2[1] - i * dy))
        nods.add(en1)
        nods.add(en2)

print(len([n for n in nods if 0 <= n[0] <= len(inp[0]) - 1 and 0 <= n[1] <= len(inp) - 1]))