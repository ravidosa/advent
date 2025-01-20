f = open("2023/input-3.txt", "r")
inp = f.read().split("\n")
st = {}
for ind, i in enumerate(inp[:-1]):
    j = 0
    while j < len(i):
        l = 1
        while i[j:j+l].isdigit() and j + l <= len(i):
            l += 1
        if i[j:j+l-1].isdigit():
            for x in range(max(0, j - 1), min(len(i), j + l)):
                for y in range(max(0, ind - 1), min(ind + 2, len(inp) - 1)):
                    if inp[y][x] == "*":
                        st[(y, x)] = st.get((y, x), []) + [int(i[j:j+l-1])]
        j = j + l
print(sum([g[1][0] * g[1][1] for g in filter(lambda x: len(x[1]) == 2, st.items())]))