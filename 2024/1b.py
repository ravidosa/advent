f = open("2024/input-1.txt", "r")
inp = list(map(int, f.read().split()))

l1 = sorted(inp[::2])
l2 = sorted(inp[1::2])
print(sum(map(lambda a: a * l2.count(a), l1)))