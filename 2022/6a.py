f = open("2022/input-6.txt", "r")
inp = f.read()
for i in range(3, len(inp)):
    if len(set(inp[i-4:i])) == 4:
        print(i)
        break