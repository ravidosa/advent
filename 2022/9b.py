f = open("2022/input-9.txt", "r")
inp = f.read().split("\n")
rope = [[0, 0] for i in range(10)]
vis = set([(0,0)])
def cmp(a, b):
    return (a > b) - (a < b) 
for i in inp[:-1]:
    instr = i.split(" ")
    for j in range(int(instr[1])):
        if instr[0] == "U":
            rope[0][1] = rope[0][1] + 1
        if instr[0] == "D":
            rope[0][1] = rope[0][1] - 1
        if instr[0] == "L":
            rope[0][0] = rope[0][0] - 1
        if instr[0] == "R":
            rope[0][0] = rope[0][0] + 1
        for k in range(1, 10):
            if abs(rope[k - 1][0] - rope[k][0]) > 1 or abs(rope[k - 1][1] - rope[k][1]) > 1:
                rope[k] = [rope[k][0] + cmp(rope[k - 1][0] - rope[k][0], 0), rope[k][1] + cmp(rope[k - 1][1] - rope[k][1], 0)]
                vis.add(tuple(rope[-1]))
print(len(vis))