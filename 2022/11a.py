f = open("2022/input-11.txt", "r")
inp = f.read().split("\n")
m = {}
for i in range(len(inp) // 7):
    m[inp[7 * i][7]] = {
        "items": [int(it) for it in (inp[7 * i + 1][18:]).split(", ")],
        "op": inp[7 * i + 2][23:],
        "test": int(inp[7 * i + 3][21:]),
        "throw": [inp[7 * i + 4][29:], inp[7 * i + 5][30:]],
        "insp": 0
        }
for r in range(20):
    for key, value in m.items():
        value["items"] = [((it ** 2 if value["op"] == "* old" else (it + int(value["op"][2:]) if value["op"][0] == "+" else it * int(value["op"][2:])))) // 3 for it in value["items"]]
        value["insp"] += len(value["items"])
        while len(value["items"]) > 0:
            if value["items"][0] % value["test"] == 0:
                m[value["throw"][0]]["items"].append(value["items"].pop(0))
            else:
                m[value["throw"][1]]["items"].append(value["items"].pop(0))
insp = sorted([value["insp"] for value in m.values()])
print(insp[-1] * insp[-2])