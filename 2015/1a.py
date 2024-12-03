f = open("2015/input-1.txt", "r")
inp = f.read()

print(inp.count("(") - inp.count(")"))