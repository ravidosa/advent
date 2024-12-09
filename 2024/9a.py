from collections import deque

f = open("2024/input-9.txt", "r")
inp = f.read()

disk = []

for i, ch in enumerate(inp):
  if i % 2 == 0:
    disk.extend([i//2]*int(ch))
  else:
    disk.extend([None]*int(ch))

disky = []
dq = deque(disk)
while dq:
    h = dq.popleft()
    if h == None:
        while dq and h == None:
            h = dq.pop()
    if h != None:
        disky.append(h)

print(sum([i * d for i, d in enumerate(disky)]))