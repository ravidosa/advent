from utils import *
inp = open("2019/input-6.txt", "r").read().strip()

parsed_input = parser(inp, ["\n", "\)"], str)

dir_orbit = {}
for i in parsed_input:
    dir_orbit[i[1]] = i[0]

ind_orbit = lambda p: 0 if p == "COM" else 1 + ind_orbit(dir_orbit[p])
print(sum(map(ind_orbit, dir_orbit)))

path_you = ["YOU"]
while path_you[0] != "COM":
    path_you = [dir_orbit[path_you[0]]] + path_you
path_san = ["SAN"]
while path_san[0] != "COM":
    path_san = [dir_orbit[path_san[0]]] + path_san
i = 0
while path_you[i] == path_san[i]:
    i += 1
print(len(path_you) + len(path_san) - 2 * (i + 1))