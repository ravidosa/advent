from utils import *
inp = input_file(2024, 9).strip()

disk = []
for i, ch in enumerate(inp):
  if i % 2 == 0:
    disk.extend([i//2]*int(ch))
  else:
    disk.extend([None]*int(ch))
disky = []
dq = collections.deque(disk)
while dq:
    h = dq.popleft()
    while dq and h == None:
        h = dq.pop()
    if h != None:
        disky.append(h)
p1 = sum(map(lambda i: i[0] * i[1], enumerate(disky)))

files = {}
frees = []
pos = 0
for i in range(len(inp) // 2):
    files[i] = [pos, int(inp[2 * i])]
    pos += int(inp[2 * i])
    frees.append([pos, int(inp[2 * i + 1])])
    pos += int(inp[2 * i + 1])
files[i + 1] = [pos, int(inp[2 * (i + 1)])]
for i in range(len(files) - 1, 0, -1):
    for f in frees:
        if files[i][0] > f[0] and files[i][1] <= f[1]:
            files[i][0] = f[0]
            f[0] += files[i][1]
            f[1] -= files[i][1]
            break
p2 = sum(map(lambda f: (f * (2 * files[f][0] + files[f][1] - 1) * files[f][1]) // 2 , files))

output(p1, p2)