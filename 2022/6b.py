f = open("2022/input-6.txt", "r")
inp = f.read()
for i in range(13, len(inp)):
    if len(set(inp[i-14:i])) == 14:
        print(i)
        break