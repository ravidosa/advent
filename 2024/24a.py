f = open("2024/input-24.txt", "r")
init, conn = f.read().split("\n\n")
init, conn = init.split("\n"), conn.split("\n")

valdic = {}
for ini in init:
    n, i = ini.split(": ")
    valdic[n] = int(i)

z = 0
for con in conn:
    i, n = con.split(" -> ")
    valdic[n] = i.split(" ")
    if n[0] == "z":
        z += 1

def val(wir):
    if type(valdic[wir]) == int:
        return valdic[wir]
    else:
        if valdic[wir][1] == "AND":
            valdic[wir] = val(valdic[wir][0]) & val(valdic[wir][2])
        elif valdic[wir][1] == "OR":
            valdic[wir] = val(valdic[wir][0]) | val(valdic[wir][2])
        elif valdic[wir][1] == "XOR":
            valdic[wir] = val(valdic[wir][0]) ^ val(valdic[wir][2])
        return valdic[wir]

num = ""
for i in range(z):
    num += str(val("z" + str(i).zfill(len(str(z)))))
print(int(num[::-1], 2))